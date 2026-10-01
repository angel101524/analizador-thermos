
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from datetime import datetime

st.set_page_config(
    page_title="Analizador de Thermos",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ Analizador de Thermos")
st.caption("Análisis automático de temperaturas de unidades refrigeradas y congeladas")

st.sidebar.header("Configuración")

operacion = st.sidebar.radio(
    "Tipo de operación",
    ["Refrigerado", "Congelado"]
)

col1, col2 = st.sidebar.columns(2)
with col1:
    temp_min = st.number_input("Mínima °C", value=2.0, step=0.5)
with col2:
    temp_max = st.number_input("Máxima °C", value=8.0, step=0.5)

if temp_min >= temp_max:
    st.sidebar.error("La temperatura mínima debe ser menor que la máxima.")

archivo = st.file_uploader(
    "📂 Carga el archivo Excel de seguimiento",
    type=["xlsx", "xls"]
)

def detectar_columna(df, candidatos):
    normalizadas = {str(c).strip().lower(): c for c in df.columns}
    for candidato in candidatos:
        if candidato.lower() in normalizadas:
            return normalizadas[candidato.lower()]
    for c in df.columns:
        nombre = str(c).strip().lower()
        if any(x in nombre for x in candidatos):
            return c
    return None

def semaforo(compliance):
    if compliance >= 95:
        return "🟢 VERDE"
    elif compliance >= 90:
        return "🟡 AMARILLO"
    return "🔴 ROJO"

def analizar(df, nombre_hoja):
    fecha_col = detectar_columna(df, ["fecha", "date"])
    hora_col = detectar_columna(df, ["hora", "time"])
    temp_col = detectar_columna(df, ["°c", "° c", "temperatura", "temp", "temperature"])
    unidad_col = detectar_columna(df, ["unidad", "thermo", "truck", "camion", "camión", "economizador"])
    evento_col = detectar_columna(df, ["eventos", "evento", "events", "event"])

    if temp_col is None:
        raise ValueError("No se encontró una columna de temperatura.")

    trabajo = df.copy()

    trabajo[temp_col] = pd.to_numeric(
        trabajo[temp_col].astype(str).str.replace(",", ".", regex=False),
        errors="coerce"
    )
    trabajo = trabajo.dropna(subset=[temp_col]).copy()

    if fecha_col:
        fechas = pd.to_datetime(trabajo[fecha_col], errors="coerce")
    else:
        fechas = pd.Series(pd.NaT, index=trabajo.index)

    if hora_col:
        horas = pd.to_datetime(
            trabajo[hora_col].astype(str),
            errors="coerce"
        )
        # combinar fecha + hora cuando sea posible
        if fecha_col:
            trabajo["_DATETIME"] = fechas.dt.normalize() + pd.to_timedelta(
                horas.dt.hour.fillna(0) * 3600
                + horas.dt.minute.fillna(0) * 60
                + horas.dt.second.fillna(0),
                unit="s"
            )
        else:
            trabajo["_DATETIME"] = horas
    else:
        trabajo["_DATETIME"] = fechas

    if unidad_col:
        trabajo["_UNIDAD"] = trabajo[unidad_col].fillna("Sin identificar").astype(str)
    else:
        trabajo["_UNIDAD"] = "Unidad"

    trabajo["_FUERA"] = (
        (trabajo[temp_col] < temp_min) |
        (trabajo[temp_col] > temp_max)
    )

    # ordenar para análisis temporal
    if trabajo["_DATETIME"].notna().any():
        trabajo = trabajo.sort_values(["_UNIDAD", "_DATETIME"])

    resumen = []

    for unidad, g in trabajo.groupby("_UNIDAD", dropna=False):
        total = len(g)
        dentro = (~g["_FUERA"]).sum()
        fuera = g["_FUERA"].sum()

        compliance = dentro / total * 100 if total else 0
        fuera_pct = fuera / total * 100 if total else 0

        temps = g[temp_col].dropna()
        minimo = temps.min() if len(temps) else np.nan
        maximo = temps.max() if len(temps) else np.nan
        promedio = temps.mean() if len(temps) else np.nan

        # Eventos: grupos consecutivos fuera de rango
        if total:
            cambios = g["_FUERA"].astype(int).diff().fillna(0)
            desviaciones = int(((cambios == 1)).sum())
        else:
            desviaciones = 0

        horas_periodo = np.nan
        if g["_DATETIME"].notna().sum() >= 2:
            delta = g["_DATETIME"].max() - g["_DATETIME"].min()
            horas_periodo = delta.total_seconds() / 3600

        desviaciones_24h = (
            desviaciones / horas_periodo * 24
            if pd.notna(horas_periodo) and horas_periodo > 0
            else np.nan
        )

        resumen.append({
            "THERMO / UNIDAD": unidad,
            "LECTURAS": total,
            "CUMPLIMIENTO %": round(compliance, 2),
            "FUERA DE RANGO %": round(fuera_pct, 2),
            "DESVIACIONES": desviaciones,
            "DESVIACIONES / 24H": round(desviaciones_24h, 2) if pd.notna(desviaciones_24h) else np.nan,
            "TEMP. MÍN °C": round(minimo, 2) if pd.notna(minimo) else np.nan,
            "TEMP. MÁX °C": round(maximo, 2) if pd.notna(maximo) else np.nan,
            "TEMP. PROM. °C": round(promedio, 2) if pd.notna(promedio) else np.nan,
            "SEMAFORO": semaforo(compliance)
        })

    resumen_df = pd.DataFrame(resumen)

    trabajo["CUMPLE"] = np.where(trabajo["_FUERA"], "NO", "SÍ")
    detalle_cols = [c for c in df.columns if c in trabajo.columns]
    extra = [c for c in ["_DATETIME", "_UNIDAD", "CUMPLE"] if c in trabajo.columns]
    detalle = trabajo[detalle_cols + extra].copy()

    return resumen_df, detalle, {
        "temp_col": temp_col,
        "fecha_col": fecha_col,
        "hora_col": hora_col,
        "unidad_col": unidad_col,
        "evento_col": evento_col,
        "filas": len(trabajo)
    }

def excel_salida(resumen, detalle, tendencia, operacion, tmin, tmax):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        resumen.to_excel(writer, sheet_name="THERMOS", index=False)

        dashboard = pd.DataFrame({
            "INDICADOR": [
                "Tipo de operación",
                "Temperatura mínima °C",
                "Temperatura máxima °C",
                "Total de Thermos",
                "Thermos VERDE",
                "Thermos AMARILLO",
                "Thermos ROJO",
                "Cumplimiento promedio %"
            ],
            "VALOR": [
                operacion,
                tmin,
                tmax,
                len(resumen),
                int(resumen["SEMAFORO"].eq("🟢 VERDE").sum()),
                int(resumen["SEMAFORO"].eq("🟡 AMARILLO").sum()),
                int(resumen["SEMAFORO"].eq("🔴 ROJO").sum()),
                round(resumen["CUMPLIMIENTO %"].mean(), 2) if len(resumen) else 0
            ]
        })
        dashboard.to_excel(writer, sheet_name="DASHBOARD", index=False)
        detalle.to_excel(writer, sheet_name="DETALLE", index=False)
        if tendencia is not None and not tendencia.empty:
            tendencia.to_excel(writer, sheet_name="TENDENCIA", index=False)

    output.seek(0)
    return output

if archivo is None:
    st.info("👆 Carga un Excel para comenzar el análisis.")
    st.markdown("""
### ¿Qué calcula esta aplicación?

- **% de cumplimiento de temperatura**
- **% de tiempo/lecturas fuera de rango**
- **Número de desviaciones**
- **Desviaciones por 24 horas**
- **Temperatura mínima, máxima y promedio**
- **Semáforo automático 🟢 🟡 🔴**
- **Dashboard y reporte Excel**
""")
    st.stop()

try:
    xls = pd.ExcelFile(archivo)
    hoja = "SEGUIMIENTO" if "SEGUIMIENTO" in xls.sheet_names else xls.sheet_names[0]
    # Los reportes de Thermo pueden traer varias filas informativas antes de
    # los encabezados reales. Buscamos automáticamente la fila que contiene
    # Fecha + Hora + temperatura (°C) y usamos esa fila como encabezado.
    muestra = pd.read_excel(archivo, sheet_name=hoja, header=None, nrows=30)
    fila_encabezado = None
    for i in range(len(muestra)):
        valores = [str(v).strip().lower() for v in muestra.iloc[i].tolist() if pd.notna(v)]
        tiene_fecha = any(v == "fecha" for v in valores)
        tiene_hora = any(v == "hora" for v in valores)
        tiene_temp = any(
            v in {"°c", "° c", "temperatura", "temp", "temperature"}
            or "temperatura" in v
            for v in valores
        )
        if tiene_fecha and tiene_hora and tiene_temp:
            fila_encabezado = i
            break

    if fila_encabezado is not None:
        df = pd.read_excel(archivo, sheet_name=hoja, header=fila_encabezado)
    else:
        df = pd.read_excel(archivo, sheet_name=hoja)

    df = df.dropna(axis=1, how="all").dropna(axis=0, how="all")

    resumen, detalle, meta = analizar(df, hoja)

    if resumen.empty:
        st.warning("No se encontraron registros válidos para analizar.")
        st.stop()

    tendencia = None
    if "_DATETIME" in detalle.columns:
        temp_col = meta["temp_col"]
        tendencia = detalle[["_DATETIME", "_UNIDAD", temp_col, "CUMPLE"]].copy()
        tendencia.columns = ["FECHA/HORA", "THERMO / UNIDAD", "TEMPERATURA °C", "CUMPLE"]
        tendencia = tendencia.sort_values("FECHA/HORA")

    st.success(f"Análisis completado: hoja **{hoja}**, {meta['filas']:,} lecturas.")

    # Métricas generales
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Thermos analizados", len(resumen))
    c2.metric("Cumplimiento promedio", f"{resumen['CUMPLIMIENTO %'].mean():.2f}%")
    c3.metric("🟢 Verdes", int(resumen["SEMAFORO"].eq("🟢 VERDE").sum()))
    c4.metric("🔴 Rojos", int(resumen["SEMAFORO"].eq("🔴 ROJO").sum()))

    st.subheader("📊 Resultado por Thermo")
    st.dataframe(resumen, use_container_width=True, hide_index=True)

    st.subheader("📋 Resumen automático")
    total = len(resumen)
    verdes = int(resumen["SEMAFORO"].eq("🟢 VERDE").sum())
    amarillos = int(resumen["SEMAFORO"].eq("🟡 AMARILLO").sum())
    rojos = int(resumen["SEMAFORO"].eq("🔴 ROJO").sum())
    promedio = resumen["CUMPLIMIENTO %"].mean()

    st.write(
        f"**Operación:** {operacion}. "
        f"Rango permitido: **{temp_min:g} °C a {temp_max:g} °C**. "
        f"Se analizaron **{total} Thermos** con un cumplimiento promedio de **{promedio:.2f}%**. "
        f"Clasificación: **{verdes} verdes, {amarillos} amarillos y {rojos} rojos**."
    )

    if tendencia is not None and not tendencia.empty:
        st.subheader("📈 Tendencia de temperatura")
        unidades = list(tendencia["THERMO / UNIDAD"].dropna().unique())
        seleccion = st.selectbox("Selecciona un Thermo para ver su tendencia", unidades)

        graf = tendencia[tendencia["THERMO / UNIDAD"] == seleccion].copy()
        graf = graf.set_index("FECHA/HORA")[["TEMPERATURA °C"]]
        st.line_chart(graf)

    salida = excel_salida(
        resumen, detalle, tendencia,
        operacion, temp_min, temp_max
    )

    nombre = archivo.name.rsplit(".", 1)[0] + "_ANALISIS_THERMOS.xlsx"

    st.download_button(
        "⬇️ DESCARGAR REPORTE EXCEL",
        data=salida,
        file_name=nombre,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

except Exception as e:
    st.error("No fue posible analizar el archivo.")
    st.exception(e)
