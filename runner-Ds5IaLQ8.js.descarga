try{window.__oaiDilBootstrap?.moduleEvaluationStarted?.()}catch{}(function(){const e=document.createElement("link").relList;if(e&&e.supports&&e.supports("modulepreload"))return;for(const o of document.querySelectorAll('link[rel="modulepreload"]'))n(o);new MutationObserver(o=>{for(const s of o)if(s.type==="childList")for(const i of s.addedNodes)i.tagName==="LINK"&&i.rel==="modulepreload"&&n(i)}).observe(document,{childList:!0,subtree:!0});function t(o){const s={};return o.integrity&&(s.integrity=o.integrity),o.referrerPolicy&&(s.referrerPolicy=o.referrerPolicy),o.crossOrigin==="use-credentials"?s.credentials="include":o.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function n(o){if(o.ep)return;o.ep=!0;const s=t(o);fetch(o.href,s)}})();const b=13,D=4e3,z=500,K=2,J="__dil_confirm_startup";function Q(r){return r!=null&&typeof r=="object"&&r.__oaiDilFrame===!0&&r.kind==="createRunner"&&r.protocolVersion===b&&typeof r.compiledDil=="string"&&typeof r.runnerId=="string"}function X(r){return r!=null&&typeof r=="object"&&r.__oaiDilFrame===!0&&r.kind==="disposeRunner"&&r.protocolVersion===b&&typeof r.runnerId=="string"}var k={exports:{}},G;function Y(){return G||(G=1,(function(r,e){r.path="dil_renderer/src/DILDictation",Object.defineProperty(e,"__esModule",{value:!0}),e.normalizeDILDictationOptions=e.DILDictationEventKind=e.DILDictationStatus=void 0;var t;(function(s){s.Idle="idle",s.Starting="starting",s.Recording="recording",s.Stopping="stopping",s.Done="done",s.Error="error"})(t||(e.DILDictationStatus=t={}));var n;(function(s){s.Recording="recording",s.Transcript="transcript",s.Stopping="stopping",s.Done="done",s.Error="error",s.Cancelled="cancelled"})(n||(e.DILDictationEventKind=n={}));function o(s){if(s===null||typeof s!="object"||Array.isArray(s))return null;const i=s.language;return i===void 0?{}:typeof i!="string"||!i.trim()||i.length>128?null:{language:i}}e.normalizeDILDictationOptions=o})(k,k.exports)),k.exports}Y();globalThis.crypto?.getRandomValues.bind(globalThis.crypto);globalThis.crypto?.getRandomValues.bind(globalThis.crypto);function Z(r,e){return r==="speechState"&&e.speechSynthesis===!0||r==="dictationEvent"&&e.dictation===!0}const ee=["host_setup","encode_globals","read_persistence","acquire_frame","iframe_create","iframe_load","iframe_resource","observer_bootstrap","module_load","module_resource","module_entry","frame_ready","manager_create","worker_create","worker_control","worker_module","harden_worker","runner_create","worker_ready","decode_globals","decode_persistence","unsafe_runner","runtime_construct","seed_runtime","hydrate_state","prepare_source","update_source","compile","evaluate","render","render_operations","snapshot_post","commit_state","persist_state","flush","flush_render","flush_effects","restore_source","command","host_call","snapshot_receive","snapshot_forward","apply_tree","notify","react_snapshot","react_materialize","react_commit","react_snapshot_effect","react_node_error","host_error","fallback","render_result","frame_timer","worker_timer","request_timer","health_probe","idle_probe","visibility","pagehide","pageshow","freeze","resume","frame_probe","event_loop","recovery","quarantine","runner_dispose","worker_stop","frame_dispose","message","error","coverage"],A=typeof performance>"u"?Date.now.bind(Date):performance.now.bind(performance),te=typeof performance>"u"?0:performance.timeOrigin,M=Object.getOwnPropertyDescriptor,ne=Object.getPrototypeOf,oe=Error.isError,re=new Map([[Error.prototype,"Error"],[TypeError.prototype,"TypeError"],[RangeError.prototype,"RangeError"],[SyntaxError.prototype,"SyntaxError"],[ReferenceError.prototype,"ReferenceError"],[URIError.prototype,"URIError"],[EvalError.prototype,"EvalError"],[AggregateError.prototype,"AggregateError"]]);let se=0;const R=256,ie=32768,N=512,E=32,v=64,ae=65536,le=8192,de=12288,U=40,q=new Set(["iframe_create:returned","iframe_load:received","iframe_resource:received","observer_bootstrap:returned","module_entry:returned","module_load:begin","module_resource:returned","module_load:reported_error","runner_module_script_error","runner_module_csp_enforced","runner_module_exception","frame_ready:sent","frame_ready:received","worker_create:begin","worker_create:returned","worker_control:sent","worker_control:received","worker_module:returned","harden_worker:begin","harden_worker:returned","runner_create:sent","runner_create:received","runner_create:begin","runner_create:returned","worker_ready:sent","worker_ready:received","snapshot_post:sent","snapshot_receive:received","host_ingress_lifecycle","host_ingress_snapshot","snapshot_forward:sent","apply_tree:returned","request_timer:fired","worker_timer:fired","frame_timer:fired"]);function W(r){if(r.operation==="module_load"&&r.reason==="runner_module_exception")return"runner_module_exception";if(r.fault||r.phase==="threw")return"first_fault";if(r.operation==="module_load"&&r.phase==="reported_error"){if(r.reason==="runner_module_script_error")return"runner_module_script_error";if(r.reason==="csp_violation"&&r.cspResource==="runner_module"&&r.cspDisposition==="enforce")return"runner_module_csp_enforced"}if(r.operation==="quarantine"||r.operation==="error")return r.operation;if(r.operation==="worker_control"&&(r.reason==="execution_started"||r.reason==="execution_finished"))return"worker_execution";if(r.realm==="host"&&r.operation==="message"&&r.phase==="received"&&(r.command==="snapshot"||r.command==="lifecycle"))return`host_ingress_${r.command}`;const e=`${r.operation}:${r.phase}`;if(q.has(e))return e;if(r.operation==="health_probe"&&r.reason?.startsWith("target_"))return"worker_target";if(r.operation==="health_probe")return r.phase==="fired"?"health_probe_expired":"health_probe";if(r.operation==="recovery")return"recovery";if(r.operation==="event_loop")return"event_loop";if(["visibility","pagehide","pageshow","freeze","resume"].includes(r.operation))return"lifecycle";if(r.operation==="frame_probe")return"frame_probe";if(r.operation==="module_load"&&r.reason==="document_state")return"document_state";if(r.operation==="module_resource")return"module_resource";if(r.operation!=="message"&&r.operation!=="coverage")return"last_progress"}function T(r){return[r.realm,r.documentBootId,r.realm==="worker"?r.workerGeneration:void 0,r.sourceId].join(":")}const ue=new Set(ee),ce=new Set(["begin","returned","threw","reported_error","sent","received","acknowledged","resolved","rejected","armed","paused","rearmed","cancelled","fired","ignored","decision"]),pe=new Set(["initialize","__dil_initialize","createRunner","disposeRunner","initializeControl","registerMessengerTransport","unregisterMessengerTransport","setCompiledDil","setData","setStateSnapshot","trigger","invokeGlobal","invokeMessengerCommand","snapshot","lifecycle","messengerEvent"]),_e=["workerGeneration","sessionGeneration","startupAttempt","snapshotVersion","renderPass","spanId","parentSpanId","count","pendingRequests","pendingHostCalls","peers","budgetMs","deadlineMs","elapsedMs","httpStatus","resourceStartMs","resourceEndMs","navigationResponseEndMs","navigationDomInteractiveMs"],me=["triggerAcknowledged","workerReadySent","hidden","persisted","acknowledged","replaySafe","hasSuccessfulSnapshot","treePresent","hasError","moduleEvaluationSupported"],he=["documentBootId","artifactId","runnerId","activeRunnerId","resourceArtifactId","triggerRunnerId","triggerRequestId","requestId","relatedRequestId"],H=/^[a-zA-Z0-9_-]{1,96}$/;function O(r){const e={};for(const t of _e){const n=r[t];typeof n=="number"&&Number.isFinite(n)&&n>=(t==="httpStatus"?100:0)&&(t!=="httpStatus"||n<=599)&&(e[t]=n)}for(const t of me)typeof r[t]=="boolean"&&(e[t]=r[t]);for(const t of he){const n=r[t];typeof n=="string"&&H.test(n)&&(e[t]=n)}for(const t of["command","triggerCommand"]){const n=r[t];n&&pe.has(n)&&(e[t]=n)}return(r.documentReadyState==="loading"||r.documentReadyState==="interactive"||r.documentReadyState==="complete")&&(e.documentReadyState=r.documentReadyState),r.cspDirective&&["script-src","script-src-elem","script-src-attr","worker-src","other"].includes(r.cspDirective)&&(e.cspDirective=r.cspDirective),(r.cspDisposition==="enforce"||r.cspDisposition==="report")&&(e.cspDisposition=r.cspDisposition),r.cspResource&&["runner_module","inline","eval","unknown"].includes(r.cspResource)&&(e.cspResource=r.cspResource),typeof r.reason=="string"&&/^[a-z_]{1,48}$/.test(r.reason)&&(e.reason=r.reason),e}function ge(r){const e=[];let t="unknown";try{if(oe?.(r)){t=re.get(ne(r))??t;const n=M(r,"name")?.value;typeof n=="string"&&/^(Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)$/.test(n)&&(t=n);const o=M(r,"stack")?.value;if(typeof o=="string"){t=/^(Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)(?=:|$)/.exec(o)?.[1]??t;for(const s of o.slice(0,4096).split(`
`).slice(1,17)){const i=/:(\d{1,7}):(\d{1,7})\)?$/.exec(s.trim());i&&e.push({line:Number(i[1]),column:Number(i[2])})}}}}catch{}return Object.freeze({name:t,locations:Object.freeze(e.map(n=>Object.freeze(n))),stackUnavailable:e.length===0})}function C(r){if(r===null||typeof r!="object")return;const e=r;if(!["host","bootstrap","iframe","worker"].includes(e.realm)||typeof e.operation!="string"||!ue.has(e.operation)||typeof e.phase!="string"||!ce.has(e.phase)||!Number.isSafeInteger(e.sequence)||e.sequence<0||typeof e.localTimeMs!="number"||!Number.isFinite(e.localTimeMs)||typeof e.timeOriginMs!="number"||!Number.isFinite(e.timeOriginMs))return;const t={...O(e),realm:e.realm,sequence:e.sequence,localTimeMs:e.localTimeMs,timeOriginMs:e.timeOriginMs,operation:e.operation,phase:e.phase};Number.isSafeInteger(e.sourceId)&&e.sourceId>=0&&(t.sourceId=e.sourceId);const n=e.fault;if(n&&typeof n.name=="string"&&/^(unknown|Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)$/.test(n.name)&&Array.isArray(n.locations)&&n.locations.length<=16){const o=n.locations.filter(s=>s&&Number.isSafeInteger(s.line)&&s.line>=0&&s.line<1e7&&Number.isSafeInteger(s.column)&&s.column>=0&&s.column<1e7).map(({line:s,column:i})=>Object.freeze({line:s,column:i}));t.fault=Object.freeze({name:n.name,locations:Object.freeze(o),stackUnavailable:o.length===0})}return t}function y(r){return[r.realm,r.documentBootId,r.workerGeneration,r.sourceId,r.runnerId,r.sessionGeneration,r.startupAttempt].join(":")}function P(r,e,t){const n=t?e.hostReceivedAtMs:A();return{...r,...typeof n=="number"&&Number.isFinite(n)&&n>=0?{hostReceivedAtMs:n}:{}}}class fe{context;now=A;realm;emit;sequence=0;sourceId=++se;span=0;parentSpanId;dropped=0;bytes=0;faultCount=0;emitted=0;open=new Map;completedSpans=new Map;observedRealms=new Set;upstreamDropped=new Map;upstreamTruncated=!1;entries=[];sequences=new Map;progress=new Map;progressSources=new Map;retainedRunners=new Map;progressBytes=0;progressDropped=0;progressLoss=new Map;constructor(e){this.realm=e.realm,this.context=Object.freeze(O(e.context??{})),this.emit=e.emit}record(e,t,n={}){try{const o={...this.context,...O(n),realm:this.realm,sequence:++this.sequence,sourceId:this.sourceId,localTimeMs:A(),timeOriginMs:te,operation:e,phase:t};n.error!==void 0&&this.faultCount<4&&(o.fault=ge(n.error),this.faultCount++),this.retain(o,"complete"),this.forward(o),this.sequence===N&&this.record("coverage","ignored",{reason:"overflow"})}catch{this.dropped++}}trace(e,t,n={}){const o=++this.span,s=this.parentSpanId,i={...n,spanId:o,parentSpanId:s};this.record(e,"begin",i),this.parentSpanId=o;try{const l=t();return this.record(e,"returned",i),l}catch(l){throw this.fault(e,l,i),l}finally{this.parentSpanId=s}}fault(e,t,n={}){this.record(e,"threw",{...n,error:t})}ingest(e,t=!1,n=!1){try{const o=C(e);if(!o){this.dropped++;return}const s=y(o);if(o.sequence<=(this.sequences.get(s)??-1))return;this.sequences.set(s,o.sequence),this.sequences.size>32&&this.sequences.delete(this.sequences.keys().next().value);const i=P(o,e,n),l=T(o),a=this.progressSources.get(l),d=a?a.complete&&o.sequence===a.sequence+1&&o.operation!=="coverage":o.sequence===1&&o.operation!=="coverage";if(o.sequence>(a?.sequence??-1)&&(this.progressSources.set(l,{sequence:o.sequence,complete:d}),this.progressSources.size>v&&this.progressSources.delete(this.progressSources.keys().next().value),!d))for(const m of this.progress.values())T(m.slots.values().next().value)===l&&(m.coverage="interrupted");this.retain(i,d?"complete":"interrupted"),t&&this.forward(o)}catch{this.dropped++}}mergeSnapshot(e,t=!1,n,o="merge"){try{if(e===null||typeof e!="object")return this.dropped++,!1;const s=e;if(s.schemaVersion!==1||!Array.isArray(s.records)||!Array.isArray(s.openOperations))return this.dropped++,!1;if(n){const u=h=>h!==null&&typeof h=="object"&&Object.entries(n).every(([x,w])=>w===void 0||h[x]===w),_=[...s.records.slice(0,R),...s.openOperations.slice(0,E)];if(Array.isArray(s.progress))for(const h of s.progress.slice(0,v)){if(!h||!Array.isArray(h.records))return this.markProgressDropped(n.runnerId),!1;for(const x of h.records.slice(0,U))_.push({...h.context,...x})}if(!_.every(u))return this.markProgressDropped(n.runnerId),!1}if(Array.isArray(s.observedRealms))for(const u of s.observedRealms.slice(0,4))(u==="host"||u==="bootstrap"||u==="iframe"||u==="worker")&&this.observedRealms.add(u);for(const u of s.records.slice(0,R))this.ingest(u,!1,t);o==="replace"&&Array.isArray(s.progress)&&this.resetDocumentProgress();for(const u of s.openOperations.slice(0,E)){const _=C(u);if(!_||_.phase!=="begin"||_.spanId===void 0){this.dropped++;continue}this.observeSpan(P(_,u,t))}let i=!0;if(Array.isArray(s.progress)){const u=this.progressDropped;for(const _ of s.progress.slice(0,v))this.mergeProgress(_,t);s.progress.length>v&&this.markProgressDropped(),i=u===this.progressDropped}if(Number.isSafeInteger(s.progressDropped)&&s.progressDropped>0){this.progressDropped=Math.max(this.progressDropped,s.progressDropped);const u=typeof s.runnerId=="string"&&H.test(s.runnerId)&&(this.progressLoss.has(s.runnerId)||this.progressLoss.size<v)?s.runnerId:"";this.progressLoss.set(u,Math.max(this.progressLoss.get(u)??0,s.progressDropped))}const l=C(s.records[0]??s.openOperations[0]),a=l?y(l):"empty",d=this.upstreamDropped.get(a)??0,m=typeof s.dropped=="number"&&Number.isSafeInteger(s.dropped)&&s.dropped>=0?s.dropped:0,f=Math.max(0,s.records.length-R)+Math.max(0,s.openOperations.length-E),I=Math.min(Number.MAX_SAFE_INTEGER,m+f);return this.dropped=Math.min(Number.MAX_SAFE_INTEGER,this.dropped+Math.max(0,I-d)),this.upstreamDropped.set(a,Math.max(d,I)),this.upstreamDropped.size>32&&this.upstreamDropped.delete(this.upstreamDropped.keys().next().value),this.upstreamTruncated||=s.truncated===!0||f>0,i}catch{return this.dropped++,!1}}resetDocumentProgress(){this.progress.clear(),this.progressSources.clear(),this.progressLoss.clear(),this.progressBytes=0,this.progressDropped=0,this.open.clear(),this.completedSpans.clear()}retainRunner(e){if(!this.retainedRunners.has(e)&&this.retainedRunners.size>=v)return this.markProgressDropped(e),()=>{};this.retainedRunners.set(e,(this.retainedRunners.get(e)??0)+1);let t=!1;return()=>{if(t)return;t=!0;const n=(this.retainedRunners.get(e)??1)-1;n?this.retainedRunners.set(e,n):this.retainedRunners.delete(e)}}snapshot(e={}){const t=[...this.progress.values()].filter(l=>{const a=l.slots.values().next().value;return!e.runnerId||!a.runnerId||a.runnerId===e.runnerId}).map(l=>{const a=[...l.slots.values()],{realm:d,sourceId:m,timeOriginMs:f,documentBootId:I,artifactId:u,runnerId:_,workerGeneration:h,sessionGeneration:x,startupAttempt:w}=a[0];return{context:{realm:d,sourceId:m,timeOriginMs:f,documentBootId:I,artifactId:u,runnerId:_,workerGeneration:h,sessionGeneration:x,startupAttempt:w},records:a.map(({realm:De,sourceId:Ue,timeOriginMs:Pe,documentBootId:je,artifactId:Le,runnerId:Ae,workerGeneration:Oe,sessionGeneration:ze,startupAttempt:Ge,...$})=>$),lastSequence:l.lastSequence,coverage:l.coverage}}),n=e.runnerId?[...ve(t,e.runnerId,this.context.documentBootId)].sort((l,a)=>+(a.context.runnerId===e.runnerId)-+(l.context.runnerId===e.runnerId)):t,o=[];let s=2,i=0;for(const l of n){const a=JSON.stringify(JSON.stringify(l)).length+1;if(s+a>le){i++;continue}s+=a,o.push(Object.freeze({...l,context:Object.freeze(l.context),records:Object.freeze(l.records.map(d=>Object.freeze(d)))}))}return Object.freeze({schemaVersion:1,observedRealms:Object.freeze([...this.observedRealms]),documentBootId:this.context.documentBootId,runnerId:e.runnerId,progress:Object.freeze(o),progressDropped:i+(e.runnerId?(this.progressLoss.get(e.runnerId)??0)+(this.progressLoss.get("")??0):this.progressDropped),records:Object.freeze(e.records===!1?[]:this.entries.map(l=>l.record)),openOperations:Object.freeze(e.records===!1?[]:[...this.open.values()]),dropped:this.dropped,truncated:this.dropped>0||this.upstreamTruncated})}markProgressDropped(e){this.progressDropped++;const t=e&&(this.progressLoss.has(e)||this.progressLoss.size<v)?e:"";this.progressLoss.set(t,(this.progressLoss.get(t)??0)+1)}observeProgress(e,t,n){const o=W(e);if(!o)return;const s=y(e);let i=this.progress.get(s);const l=i?.slots.get(o);if(i&&(i.lastSequence=Math.max(i.lastSequence,e.sequence)),l&&o==="event_loop"&&(l.elapsedMs??0)-(l.budgetMs??0)>=(e.elapsedMs??0)-(e.budgetMs??0)||l&&(o==="first_fault"||q.has(o)?l.sequence<=e.sequence:l.sequence>=e.sequence))return;n??=JSON.stringify(e).length;const a=n-(l?JSON.stringify(l).length:0);for(;!i&&this.progress.size>=v||this.progressBytes+a>ae;){const d=[...this.progress].find(([m,f])=>{const I=f.slots.values().next().value.runnerId;return m!==s&&I&&!this.retainedRunners.has(I)});if(!d){this.markProgressDropped(e.runnerId),i&&(i.coverage="interrupted");return}this.progressBytes-=d[1].bytes,this.progress.delete(d[0]),this.markProgressDropped(d[1].slots.values().next().value.runnerId)}if(i||(i={slots:new Map,lastSequence:0,coverage:t,bytes:0},this.progress.set(s,i)),i.bytes+a>de||!l&&i.slots.size>=U){this.markProgressDropped(e.runnerId),i.coverage="interrupted";return}i.slots.set(o,Object.freeze(e)),i.lastSequence=Math.max(i.lastSequence,e.sequence),t!=="complete"&&(i.coverage=t),i.bytes+=a,this.progressBytes+=a}mergeProgress(e,t){if(!e||typeof e!="object"){this.markProgressDropped();return}const n=e;if(!Array.isArray(n.records)||n.records.length===0||n.records.length>U||!Number.isSafeInteger(n.lastSequence)||n.lastSequence<0||!["complete","interrupted","unavailable"].includes(n.coverage??"")){this.markProgressDropped();return}const o=n.records.map(d=>C({...n.context,...d})),s=o[0];if(!s||o.some(d=>!d||y(d)!==y(s)||d.sequence>n.lastSequence||!W(d))){this.markProgressDropped();return}const i=this.progress.get(y(s));if(i&&n.lastSequence<i.lastSequence)return;const l=this.progressDropped;for(let d=0;d<o.length;d++)this.observeProgress(P(o[d],n.records[d],t),n.coverage);const a=this.progress.get(y(s));a&&(a.lastSequence=Math.max(a.lastSequence,n.lastSequence),a.coverage=this.progressDropped===l?n.coverage:"interrupted")}observeSpan(e){if(e.spanId!==void 0){const t=`${y(e)}:${e.spanId}`;if(e.phase==="begin"){if((this.completedSpans.get(t)??-1)>=e.sequence||(this.open.get(t)?.sequence??-1)>=e.sequence)return;this.open.has(t)||this.open.size<E?this.open.set(t,Object.freeze(e)):this.dropped++}else(e.phase==="returned"||e.phase==="threw")&&(this.open.delete(t),this.completedSpans.set(t,e.sequence),this.completedSpans.size>R&&this.completedSpans.delete(this.completedSpans.keys().next().value))}}retain(e,t){const n=JSON.stringify(e).length;this.observeProgress(e,t,n),this.observedRealms.add(e.realm),this.observeSpan(e);const o=this.entries.length<8||e.fault!==void 0&&!this.entries.some(s=>s.record.fault);for(;this.entries.length>=R||this.bytes+n>ie;){const s=this.entries.findIndex(i=>!i.pinned);if(s<0){this.dropped++;return}this.bytes-=this.entries[s].bytes,this.entries.splice(s,1),this.dropped++}this.entries.push({record:Object.freeze(e),bytes:n,pinned:o}),this.bytes+=n}forward(e){if(this.emit){if(this.emitted++>=N+1){this.dropped++;return}try{this.emit(e)}catch{this.dropped++}}}}function ve(r,e,t){const n=r.filter(({context:a})=>(!e||!a.runnerId||a.runnerId===e)&&(!t||!a.documentBootId||a.documentBootId===t)),o=n.map(a=>a.context).filter(a=>a.runnerId===e),s=Math.max(-1,...o.map(a=>a.workerGeneration??-1)),i=Math.max(-1,...o.filter(a=>a.workerGeneration===s).map(a=>a.sessionGeneration??-1)),l=Math.max(-1,...o.filter(a=>a.workerGeneration===s&&a.sessionGeneration===i).map(a=>a.startupAttempt??-1));return n.filter(({context:a})=>(a.workerGeneration===void 0||a.workerGeneration===s)&&(a.sessionGeneration===void 0||a.sessionGeneration===i)&&(a.startupAttempt===void 0||a.startupAttempt===l))}const c="__dil_initialize",j="__dil_startup_confirmation_",ye=1e4,be=16;class Ie{activeRunnerId=null;executionEpoch=0;disposed=!1;createChannel;createWorker;diagnostics;healthChecks=new Map;diagnosticProbeCount=0;diagnosticProbes=new Map;healthCheckTimeoutMs;idleHealthCheck=null;isVisible;nextMessageId=0;nextSessionGeneration=0;requestTimeoutMs;sessions=new Map;retiredDiagnosticSessions=new Map;unattributedRestarts=0;visibilityDocument;worker=null;workerControlPort=null;workerGeneration=0;constructor(e){this.diagnostics=e.diagnostics,this.createChannel=e.createChannel??(()=>new MessageChannel),this.createWorker=e.createWorker,this.healthCheckTimeoutMs=e.healthCheckTimeoutMs??z,this.requestTimeoutMs=e.requestTimeoutMs??2e3,this.isVisible=e.isVisible??(()=>typeof document>"u"||!document.hidden),this.visibilityDocument=typeof document>"u"?null:document,this.visibilityDocument?.addEventListener("visibilitychange",this.handleVisibilityChange),this.diagnostics?.record("manager_create","begin",this.diagnosticDetails()),this.startWorker(),this.diagnostics?.record("manager_create","returned",this.diagnosticDetails())}createRunner(e,t){if(this.disposed){t.close();return}this.disposeRunner(e.runnerId);const n={diagnosticFailureReported:!1,diagnosticGeneration:++this.nextSessionGeneration,releaseDiagnosticRunner:this.diagnostics?.retainRunner(e.runnerId),hasSuccessfulSnapshot:!1,handleHostMessage:o=>{this.receiveHostMessage(n,o.data)},handleWorkerMessage:o=>{this.receiveWorkerMessage(n,o.data,o.currentTarget)},hostPort:t,lastSnapshotVersion:0,message:{...e,...e.statePersistence?{statePersistence:{...e.statePersistence}}:{}},pendingRequests:new Map,pendingWorkerCommands:new Map,quarantined:!1,restoringCommands:new Set,startupAttempts:0,startupRetrySafe:!0,transports:new Set,workerPort:null};if(this.sessions.set(e.runnerId,n),this.diagnostics?.record("runner_create","received",this.diagnosticDetails(n)),t.addEventListener("message",n.handleHostMessage),t.start(),!this.worker&&!this.startWorker()){this.failSession(n,"worker_start_error");return}this.startSession(n)}disposeRunner(e){const t=this.sessions.get(e);if(!t)return;const n=t.pendingRequests.has(c)&&this.isOnlyActiveSession(t);if(this.diagnostics?.record("runner_dispose","begin",this.diagnosticDetails(t)),this.sessions.delete(e),!this.disposed&&this.diagnostics&&t.pendingRequests.has(c)){this.releaseRetiredDiagnosticSession(e),this.retiredDiagnosticSessions.size>=be&&this.releaseRetiredDiagnosticSession(this.retiredDiagnosticSessions.keys().next().value);const o=globalThis.setTimeout(()=>this.releaseRetiredDiagnosticSession(e),ye);this.retiredDiagnosticSessions.set(e,{workerGeneration:this.workerGeneration,sessionGeneration:t.diagnosticGeneration,startupAttempt:t.startupAttempts,timeout:o,releaseDiagnosticRunner:t.releaseDiagnosticRunner})}else t.releaseDiagnosticRunner?.();this.cancelHealthChecks(t),this.clearRequests(t,!1),this.closeWorkerPort(t),t.hostPort.removeEventListener("message",t.handleHostMessage),t.hostPort.close(),this.notifyWorkerToDispose(e),this.activeRunnerId===e&&(this.activeRunnerId=null),n&&this.checkIdleWorker(),this.diagnostics?.record("runner_dispose","returned",this.diagnosticDetails(t))}dispose(){if(!this.disposed){this.disposed=!0;for(const e of this.retiredDiagnosticSessions.keys())this.releaseRetiredDiagnosticSession(e);this.visibilityDocument?.removeEventListener("visibilitychange",this.handleVisibilityChange);for(const e of[...this.sessions.keys()])this.disposeRunner(e);this.stopWorker()}}probeTarget(e,t){if(!this.diagnostics||!e||this.disposed){t();return}const n=this.sessions.get(e),o=n?void 0:this.retiredDiagnosticSessions.get(e),s={...this.diagnosticContext(n),...o?{workerGeneration:o.workerGeneration,sessionGeneration:o.sessionGeneration,startupAttempt:o.startupAttempt}:{},runnerId:e},i=this.workerControlPort;if(!i||this.diagnosticProbeCount++>=4){this.diagnostics.record("health_probe","ignored",{...s,reason:i?"target_probe_budget_exhausted":"target_control_unavailable"}),t();return}const l=`diagnostic_${this.nextMessageId++}`,a=(m,f)=>{if(this.diagnosticProbes.delete(l)){globalThis.clearTimeout(d),this.diagnostics?.record("health_probe","received",{...s,requestId:l,reason:`target_${m}`,workerReadySent:f});try{t()}catch{}}},d=globalThis.setTimeout(()=>a("no_response"),z);this.diagnosticProbes.set(l,{context:s,finish:a}),this.diagnostics.record("health_probe","sent",{...s,requestId:l,reason:"target_requested"});try{i.postMessage({__oaiDilWorker:!0,kind:"healthCheck",requestId:l,runnerId:e})}catch{a("control_unavailable")}}releaseRetiredDiagnosticSession(e){const t=this.retiredDiagnosticSessions.get(e);t&&(globalThis.clearTimeout(t.timeout),t.releaseDiagnosticRunner?.(),this.retiredDiagnosticSessions.delete(e))}startWorker(){if(this.disposed)return!1;let e,t,n="worker_create";this.workerGeneration+=1,this.diagnostics?.record(n,"begin",this.diagnosticDetails());try{return e=this.createWorker(),this.diagnostics?.record(n,"returned",this.diagnosticDetails()),n="worker_control",this.diagnostics?.record(n,"begin",this.diagnosticDetails()),t=this.createChannel(),t.port1.addEventListener("message",this.receiveWorkerControl),t.port1.start(),e.postMessage({__oaiDilWorker:!0,kind:"initializeControl",protocolVersion:b,...this.diagnostics?{diagnostics:this.diagnosticContext()}:{}},[t.port2]),this.diagnostics?.record(n,"sent",this.diagnosticDetails()),this.worker=e,this.workerControlPort=t.port1,!0}catch(o){return this.diagnostics?.fault(n,o,this.diagnosticDetails()),t?.port1.removeEventListener("message",this.receiveWorkerControl),t?.port1.close(),t?.port2.close(),e?.terminate(),this.worker=null,this.workerControlPort=null,!1}}stopWorker(){this.diagnostics?.record("worker_stop","begin",{...this.diagnosticDetails(),count:this.healthChecks.size}),this.cancelIdleHealthCheck();for(const n of this.diagnosticProbes.values())n.finish(this.disposed?"disposed":"worker_replaced");for(const n of this.healthChecks.values())globalThis.clearTimeout(n.timeout);this.healthChecks.clear(),this.activeRunnerId=null;const e=this.workerControlPort;this.workerControlPort=null,e?.removeEventListener("message",this.receiveWorkerControl),e?.close();const t=this.worker;this.worker=null,t?.terminate(),this.diagnostics?.record("worker_stop","returned",this.diagnosticDetails())}checkIdleWorker(){const e=this.workerControlPort;if(!e||this.disposed)return;this.cancelIdleHealthCheck();const t={controlPort:e,requestId:`idle_health_${this.nextMessageId++}`,timeout:null};this.idleHealthCheck=t,this.armIdleHealthCheck(t);try{e.postMessage({__oaiDilWorker:!0,kind:"healthCheck",requestId:t.requestId}),this.diagnostics?.record("idle_probe","sent",{...this.diagnosticDetails(),requestId:t.requestId})}catch(n){this.diagnostics?.fault("idle_probe",n,{...this.diagnosticDetails(),requestId:t.requestId}),this.idleHealthCheck===t&&this.stopWorker()}}armIdleHealthCheck(e){if(e.timeout!=null&&globalThis.clearTimeout(e.timeout),e.timeout=null,this.visibilityDocument&&!this.isVisible()){this.diagnostics?.record("idle_probe","paused",{...this.diagnosticDetails(),requestId:e.requestId,hidden:!0});return}const t=globalThis.setTimeout(()=>{if(!(this.idleHealthCheck!==e||this.workerControlPort!==e.controlPort||e.timeout!==t)){if(!this.isVisible()){this.armIdleHealthCheck(e);return}this.diagnostics?.record("idle_probe","fired",{...this.diagnosticDetails(),requestId:e.requestId}),this.stopWorker()}},D+this.healthCheckTimeoutMs);e.timeout=t,this.diagnostics?.record("idle_probe","armed",{...this.diagnosticDetails(),requestId:e.requestId,budgetMs:D+this.healthCheckTimeoutMs})}cancelIdleHealthCheck(){const e=this.idleHealthCheck;e&&this.diagnostics?.record("idle_probe","cancelled",{...this.diagnosticDetails(),requestId:e.requestId}),this.idleHealthCheck=null,e?.timeout!=null&&globalThis.clearTimeout(e.timeout)}startSession(e){if(e.quarantined||this.disposed)return;if(this.idleHealthCheck&&(this.stopWorker(),!this.startWorker())){this.failSession(e,"worker_start_error");return}const t=this.workerControlPort;if(!t){this.diagnostics?.record("runner_create","ignored",{...this.diagnosticDetails(e),reason:"control_unavailable"});return}this.diagnostics?.record("runner_create","begin",{...this.diagnosticDetails(e),startupAttempt:e.startupAttempts+1}),this.closeWorkerPort(e);const n=this.createChannel();e.startupAttempts+=1,e.workerPort=n.port1,n.port1.addEventListener("message",e.handleWorkerMessage),n.port1.start(),this.trackRequest(e,c,"initialize");try{t.postMessage(this.diagnostics?{...e.message,diagnosticContext:this.diagnosticContext(e)}:e.message,[n.port2]),this.diagnostics?.record("runner_create","sent",this.diagnosticDetails(e));for(const o of e.transports){const s=`__dil_restore_${this.nextMessageId++}`;e.restoringCommands.add(s),n.port1.postMessage({__oaiDilMessage:!0,command:"registerMessengerTransport",data:{channelId:o},id:s,kind:"command"}),this.diagnostics?.record("command","sent",{...this.diagnosticDetails(e),requestId:s,command:"registerMessengerTransport",reason:"restore_transport"})}}catch(o){this.diagnostics?.fault("runner_create",o,this.diagnosticDetails(e)),this.failSession(e,"worker_start_error")}}receiveHostMessage(e,t){if(!this.isLiveSession(e)||!V(t))return;if(t.kind==="response"){if(typeof t.id!="string")return;const o=e.pendingWorkerCommands.get(t.id);if(!o){this.diagnostics?.record("host_call","ignored",{...this.diagnosticDetails(e),requestId:t.id,reason:"stale_generation"});return}this.diagnostics?.record("host_call","received",{...this.diagnosticDetails(e),requestId:t.id,relatedRequestId:o}),e.pendingWorkerCommands.delete(t.id),e.workerPort?.postMessage({...t,id:o}),this.diagnostics?.record("host_call",e.workerPort?"sent":"ignored",{...this.diagnosticDetails(e),requestId:o});return}if(t.kind==="event"){!e.quarantined&&Z(t.event,e.message)&&e.workerPort?.postMessage(t);return}if(t.kind!=="command"||typeof t.id!="string")return;this.diagnostics?.record("command","received",{...this.diagnosticDetails(e),requestId:t.id,command:t.command});const n=this.rememberHostCommand(e,t);if(e.quarantined){if(t.command==="setCompiledDil"&&n){if(this.diagnostics?.record("recovery","decision",{...this.diagnosticDetails(e),reason:"source_changed"}),e.diagnosticGeneration=++this.nextSessionGeneration,e.diagnosticFailureReported=!1,e.hasSuccessfulSnapshot=!1,e.startupAttempts=0,e.startupRetrySafe=!0,e.quarantined=!1,this.unattributedRestarts=0,this.replyToHost(e,t.id,t.command),!this.worker&&!this.startWorker()){this.failSession(e,"worker_start_error");return}this.startSession(e)}else this.replyToHost(e,t.id,t.command);return}if(!e.workerPort){this.replyToHost(e,t.id,t.command);return}this.trackRequest(e,t.id,t.command??"unknown"),e.workerPort.postMessage({...t,...t.command==="trigger"?{acknowledge:!0}:{}}),this.diagnostics?.record("command","sent",{...this.diagnosticDetails(e),requestId:t.id,command:t.command})}rememberHostCommand(e,t){if(!p(t.data))return e.startupRetrySafe=!1,!1;switch(t.command){case"setCompiledDil":{if(typeof t.data.compiledDil!="string")return!1;const n=e.message.compiledDil!==t.data.compiledDil;return e.message.compiledDil=t.data.compiledDil,t.data.data!==void 0&&(e.message.data=t.data.data),n}case"setData":return e.message.data=t.data.data,!1;case"setStateSnapshot":if(e.message.statePersistence){const n=t.data.widgetId;if(typeof n=="string"){const o={...e.message.statePersistence.widgetSnapshots};if(t.data.snapshot===void 0)delete o[n];else{const s=L(t.data.snapshot);s&&Object.defineProperty(o,n,{value:s,enumerable:!0,configurable:!0,writable:!0})}return e.message.statePersistence.widgetSnapshots=o,!1}if(t.data.snapshot===void 0)delete e.message.statePersistence.snapshot;else{const o=L(t.data.snapshot);o&&(e.message.statePersistence.snapshot=o)}}return!1;case"registerMessengerTransport":return typeof t.data.channelId=="string"&&e.transports.add(t.data.channelId),!1;case"unregisterMessengerTransport":return typeof t.data.channelId=="string"&&e.transports.delete(t.data.channelId),!1;default:return e.startupRetrySafe=!1,!1}}receiveWorkerMessage(e,t,n){if(!this.isLiveSession(e)||!V(t))return;if(t.kind==="response"&&typeof t.id=="string"&&t.id.startsWith(j)){const s=t.id.slice(j.length),i=this.healthChecks.get(s);i?.session===e&&i.confirmationPort===n&&n===e.workerPort&&this.finishStartupConfirmation(s);return}let o=t;if(this.diagnostics?.record(t.kind==="event"&&t.event==="lifecycle"&&p(t.data)&&t.data.kind==="worker_ready"?"worker_ready":"message","received",{...this.diagnosticDetails(e),requestId:t.id,command:t.command}),(t.kind!=="event"||t.event!=="lifecycle"||!p(t.data)||t.data.kind!=="worker_ready")&&(e.startupRetrySafe=!1),t.kind==="ack"){const s=typeof t.id=="string"?e.pendingRequests.get(t.id):void 0;s?.command==="trigger"&&(s.acknowledged=!0,this.diagnostics?.record("command","acknowledged",{...this.diagnosticDetails(e),requestId:t.id,command:s.command,acknowledged:!0}));return}if(t.kind==="response"){if(typeof t.id!="string"||e.restoringCommands.delete(t.id))return;this.diagnostics?.record("command",t.error?"rejected":"resolved",{...this.diagnosticDetails(e),requestId:t.id}),this.clearRequest(e,t.id)}if(t.kind==="event"&&t.event==="snapshot"){if(this.diagnostics?.record("snapshot_receive","received",{...this.diagnosticDetails(e),...p(t.data)&&typeof t.data.version=="number"?{snapshotVersion:t.data.version}:{}}),p(t.data)&&t.data.error!=null){this.diagnostics?.record("snapshot_receive","reported_error",{...this.diagnosticDetails(e),error:t.data.error});const i=this.captureFailure(e);i&&(o={...t,data:{...t.data,diagnostics:i}})}const s=e.pendingRequests.has(c);if(this.clearRequest(e,c),s)for(const[i,l]of[...e.pendingRequests])this.trackRequest(e,i,l.command);p(t.data)&&typeof t.data.version=="number"&&(t.data.error==null&&(e.hasSuccessfulSnapshot=!0,e.diagnosticFailureReported=!1),e.lastSnapshotVersion=Math.max(e.lastSnapshotVersion,t.data.version))}if(t.kind==="command"&&typeof t.id=="string"){this.rememberPersistedState(e,t);const s=`worker_${this.nextMessageId}`;this.nextMessageId+=1,e.pendingWorkerCommands.set(s,t.id),this.diagnostics?.record("host_call","sent",{...this.diagnosticDetails(e),requestId:s,relatedRequestId:t.id,command:t.command}),e.hostPort.postMessage({...t,id:s});return}e.hostPort.postMessage(o),t.kind==="event"&&t.event==="lifecycle"&&p(t.data)&&t.data.kind==="worker_ready"&&this.diagnostics?.record("worker_ready","sent",this.diagnosticDetails(e)),t.kind==="event"&&t.event==="snapshot"&&this.diagnostics?.record("snapshot_forward","sent",{...this.diagnosticDetails(e),snapshotVersion:e.lastSnapshotVersion})}rememberPersistedState(e,t){const n=e.message.statePersistence;if(!n||t.command!=="invokeGlobal"||!p(t.data)||t.data.id!==n.persistState.__oaiDilGlobalFunction||!Array.isArray(t.data.args))return;const o=L(t.data.args[0]);if(o){const s=t.data.args[1];typeof s=="string"?n.widgetSnapshots={...n.widgetSnapshots,[s]:o}:s===void 0&&(n.snapshot=o)}}handleVisibilityChange=()=>{if(this.disposed)return;this.idleHealthCheck&&this.armIdleHealthCheck(this.idleHealthCheck);const e=this.isVisible();this.diagnostics?.record("visibility","received",{...this.diagnosticDetails(),hidden:!e});for(const t of this.sessions.values()){this.cancelHealthChecks(t);for(const[n,o]of[...t.pendingRequests])e?this.trackRequest(t,n,o.command):o.timeout!=null&&(globalThis.clearTimeout(o.timeout),o.timeout=null,delete o.diagnosticDeadlineMs,this.diagnostics?.record("request_timer","paused",{...this.diagnosticDetails(t),requestId:n,command:o.command,hidden:!0}))}};trackRequest(e,t,n){const o=e.pendingRequests.get(t),s=o?.acknowledged??!1;this.clearRequest(e,t);const i=n==="initialize"||e.pendingRequests.has(c)?D:this.requestTimeoutMs,l=this.diagnostics?.now(),a=this.visibilityDocument&&!this.isVisible()?null:globalThis.setTimeout(()=>{this.requestTimedOut(e,t)},i);e.pendingRequests.set(t,{acknowledged:s,command:n,timeout:a,...l!=null?{diagnosticStartedAt:l,...a!=null?{diagnosticDeadlineMs:l+i}:{}}:{}}),this.diagnostics?.record("request_timer",a==null?"paused":o?"rearmed":"armed",{...this.diagnosticDetails(e),requestId:t,command:n,budgetMs:i,deadlineMs:a!=null&&l!=null?l+i:void 0,acknowledged:s,hidden:a==null})}clearRequest(e,t){const n=e.pendingRequests.get(t);n&&(this.diagnostics?.record("request_timer","cancelled",{...this.diagnosticDetails(e),requestId:t,command:n.command,acknowledged:n.acknowledged,deadlineMs:n.diagnosticDeadlineMs}),n.timeout!=null&&globalThis.clearTimeout(n.timeout),e.pendingRequests.delete(t),this.cancelHealthChecks(e,t))}clearRequests(e,t){this.diagnostics?.record("request_timer","cancelled",{...this.diagnosticDetails(e),reason:"clear_all"});for(const[n,o]of e.pendingRequests)o.timeout!=null&&globalThis.clearTimeout(o.timeout),t&&n!==c&&this.replyToHost(e,n,o.command);e.pendingRequests.clear(),e.pendingWorkerCommands.clear(),e.restoringCommands.clear()}requestTimedOut(e,t){if(!this.isLiveSession(e)||e.quarantined||!e.pendingRequests.has(t)||e.pendingRequests.has(c)&&(t=c,[...this.healthChecks.values()].some(a=>a.session===e&&a.requestId===t)))return;const n=e.pendingRequests.get(t);if(this.diagnostics?.record("request_timer","fired",{...this.diagnosticDetails(e),requestId:t,command:n?.command,acknowledged:n?.acknowledged,deadlineMs:n?.diagnosticDeadlineMs,elapsedMs:n?.diagnosticStartedAt!=null?this.diagnostics.now()-n.diagnosticStartedAt:void 0}),!this.isVisible()){const a=e.pendingRequests.get(t)?.command;a&&this.trackRequest(e,t,a);return}const o=this.diagnosticTrigger(e,t),s=this.workerControlPort;if(!s){if(this.diagnostics?.record("health_probe","ignored",{...this.diagnosticDetails(e),requestId:t,reason:"control_unavailable"}),this.recoverStartup(e,o))return;this.canRestoreCallback(e,t)||this.quarantineSession(e,"control_unavailable",o),this.restartWorker(o);return}const i=`health_${this.nextMessageId}`;this.nextMessageId+=1;const l=globalThis.setTimeout(()=>{this.healthCheckTimedOut(i)},this.healthCheckTimeoutMs);this.healthChecks.set(i,{executionEpoch:this.executionEpoch,diagnosticStartedAt:this.diagnostics?.now(),requestId:t,session:e,timeout:l}),this.diagnostics?.record("health_probe","armed",{...this.diagnosticDetails(e),requestId:i,relatedRequestId:t,budgetMs:this.healthCheckTimeoutMs,deadlineMs:this.diagnostics.now()+this.healthCheckTimeoutMs,acknowledged:n?.acknowledged});try{s.postMessage({__oaiDilWorker:!0,kind:"healthCheck",requestId:i,...this.diagnostics?{runnerId:e.message.runnerId}:{}}),this.diagnostics?.record("health_probe","sent",{...this.diagnosticDetails(e),requestId:i})}catch(a){this.diagnostics?.fault("health_probe",a,{...this.diagnosticDetails(e),requestId:i}),this.healthCheckTimedOut(i)}}receiveWorkerControl=e=>{if(xe(e.data))switch(e.data.kind){case"diagnostic":{if(!this.diagnostics||e.currentTarget!==this.workerControlPort)return;const t=C(e.data.record);if(!t||t.realm!=="worker"||t.documentBootId!==this.diagnostics.context.documentBootId||t.workerGeneration!==this.workerGeneration)return;if(t.runnerId){const n=this.sessions.get(t.runnerId),o=this.retiredDiagnosticSessions.get(t.runnerId);if(!(n&&t.sessionGeneration===n.diagnosticGeneration&&t.startupAttempt===n.startupAttempts||!n&&o&&t.workerGeneration===o.workerGeneration&&t.sessionGeneration===o.sessionGeneration&&t.startupAttempt===o.startupAttempt))return}this.diagnostics.ingest(t,!0);break}case"executionStarted":this.diagnostics?.record("worker_control","received",{...this.diagnosticDetails(this.sessions.get(e.data.runnerId)),reason:"execution_started"}),this.executionEpoch+=1,this.activeRunnerId=e.data.runnerId;break;case"executionFinished":this.diagnostics?.record("worker_control","received",{...this.diagnosticDetails(this.sessions.get(e.data.runnerId)),reason:"execution_finished"}),this.activeRunnerId===e.data.runnerId&&(this.activeRunnerId=null);break;case"healthy":{const t=this.diagnosticProbes.get(e.data.requestId);if(t){if(e.currentTarget!==this.workerControlPort)return;const i=e.data.target,l=i&&Object.entries(t.context).every(([a,d])=>!i.present&&(a==="sessionGeneration"||a==="startupAttempt")||i[a]===d);e.data.diagnostics&&(!i||l)&&this.diagnostics?.mergeSnapshot(e.data.diagnostics,!1,t.context),t.finish(i?l?i.present===!0?"present":i.present===!1?"absent":"status_unavailable":"changed":"status_unavailable",l&&typeof i?.workerReadySent=="boolean"?i.workerReadySent:void 0);return}const n=this.idleHealthCheck;if(n?.requestId===e.data.requestId){this.diagnostics?.record("idle_probe","received",{...this.diagnosticDetails(),requestId:e.data.requestId}),n.controlPort===this.workerControlPort&&this.cancelIdleHealthCheck();return}const o=this.healthChecks.get(e.data.requestId);if(!o||o.confirmationPort)return;this.diagnostics&&e.currentTarget===this.workerControlPort&&e.data.diagnostics&&this.diagnostics.mergeSnapshot(e.data.diagnostics,!1,this.diagnosticContext(o.session)),this.diagnostics?.record("health_probe","received",{...this.diagnosticDetails(o.session),requestId:e.data.requestId,relatedRequestId:o.requestId,budgetMs:this.healthCheckTimeoutMs,elapsedMs:o.diagnosticStartedAt===void 0?void 0:this.diagnostics.now()-o.diagnosticStartedAt,acknowledged:o.session.pendingRequests.get(o.requestId)?.acknowledged});const s=o.session.pendingRequests.get(o.requestId);if(this.isLiveSession(o.session)&&s&&this.isVisible()&&o.requestId===c&&!this.isOnlyActiveSession(o.session)&&o.session.workerPort){o.confirmationPort=o.session.workerPort;try{o.confirmationPort.postMessage({__oaiDilMessage:!0,command:J,id:j+e.data.requestId,kind:"command"})}catch{this.finishStartupConfirmation(e.data.requestId)}return}if(globalThis.clearTimeout(o.timeout),this.healthChecks.delete(e.data.requestId),this.isLiveSession(o.session)&&s){if(!this.isVisible()){this.requestTimedOut(o.session,o.requestId);return}const i=this.diagnosticTrigger(o.session,o.requestId);if(this.recoverStartup(o.session,i))return;s.acknowledged?this.trackRequest(o.session,o.requestId,s.command):this.canRestoreCallback(o.session,o.requestId)?this.restartSession(o.session,i):this.quarantineSession(o.session,"probe_healthy_unacknowledged",i)}break}}};finishStartupConfirmation(e){const t=this.healthChecks.get(e);if(t?.confirmationPort&&(globalThis.clearTimeout(t.timeout),this.healthChecks.delete(e),!(!this.isLiveSession(t.session)||t.confirmationPort!==t.session.workerPort||!t.session.pendingRequests.has(c)))){if(!this.isVisible()){this.requestTimedOut(t.session,c);return}this.quarantineSession(t.session,"probe_healthy_unacknowledged",this.diagnosticTrigger(t.session,c))}}healthCheckTimedOut(e){const t=this.healthChecks.get(e);if(!t)return;if(this.diagnostics?.record("health_probe","fired",{...this.diagnosticDetails(t.session),requestId:e,relatedRequestId:t.requestId,budgetMs:this.healthCheckTimeoutMs,elapsedMs:t.diagnosticStartedAt===void 0?void 0:this.diagnostics.now()-t.diagnosticStartedAt,acknowledged:t.session.pendingRequests.get(t.requestId)?.acknowledged,count:this.unattributedRestarts}),t.confirmationPort){this.finishStartupConfirmation(e);return}if(this.healthChecks.delete(e),globalThis.clearTimeout(t.timeout),!this.isLiveSession(t.session))return;if(!this.isVisible()){this.requestTimedOut(t.session,t.requestId);return}const n=t.executionEpoch===this.executionEpoch&&this.activeRunnerId?this.sessions.get(this.activeRunnerId):void 0,o=this.diagnosticTrigger(t.session,t.requestId);this.recoverStartup(t.session,o)||(n?(this.unattributedRestarts=0,this.canRestoreCallback(n,n===t.session?t.requestId:void 0)||this.quarantineSession(n,"peer_probe_timeout",o)):this.canRestoreCallback(t.session,t.requestId)?this.unattributedRestarts=0:this.unattributedRestarts>0?this.quarantineSession(t.session,"probe_timeout",o):this.unattributedRestarts+=1,this.restartWorker(o))}recoverStartup(e,t){return e.hasSuccessfulSnapshot||!e.pendingRequests.has(c)||!this.isOnlyActiveSession(e)?!1:(this.canRetryStartup(e)?(this.diagnostics?.record("recovery","decision",{...this.diagnosticDetails(e),reason:"startup_retry",...t}),this.restartWorker(t)):(this.diagnostics?.record("recovery","decision",{...this.diagnosticDetails(e),reason:"startup_exhausted",...t}),this.stopWorker(),this.quarantineSession(e,"startup_exhausted",t)),!0)}canRetryStartup(e){return!e.quarantined&&(e.message.recoverSafeStartupPeers===!0||this.isOnlyActiveSession(e))&&e.startupRetrySafe&&e.startupAttempts<K}isOnlyActiveSession(e){return!e.quarantined&&[...this.sessions.values()].every(t=>t===e||t.quarantined)}canRestoreCallback(e,t){return e.hasSuccessfulSnapshot?t!=null?e.pendingRequests.get(t)?.command==="trigger":[...e.pendingRequests.values()].some(n=>n.command==="trigger"):!1}restartSession(e,t){this.diagnostics?.record("recovery","decision",{...this.diagnosticDetails(e),reason:"session_restart",...t}),this.cancelHealthChecks(e),this.clearRequests(e,!0),this.closeWorkerPort(e),this.notifyWorkerToDispose(e.message.runnerId),this.startSession(e)}restartWorker(e){this.diagnostics?.record("recovery","decision",{...this.diagnosticDetails(),reason:"worker_restart",...e,count:this.unattributedRestarts});const t=[...this.sessions.values()].filter(o=>!o.hasSuccessfulSnapshot&&!this.canRetryStartup(o));for(const o of t)this.quarantineSession(o,"worker_restart",e);this.stopWorker();const n=[...this.sessions.values()].filter(o=>!o.quarantined);if(n.length!==0){for(const o of n)this.clearRequests(o,!0),this.closeWorkerPort(o);if(!this.startWorker()){for(const o of n)this.failSession(o,"worker_start_error");return}for(const o of n)this.startSession(o)}}quarantineSession(e,t,n){if(!this.isLiveSession(e)||e.quarantined)return;this.diagnostics?.record("quarantine","decision",{...this.diagnosticDetails(e),reason:t,...n});const o=this.captureFailure(e);e.quarantined=!0,this.cancelHealthChecks(e),this.clearRequests(e,!0),this.closeWorkerPort(e),this.notifyWorkerToDispose(e.message.runnerId),this.failSession(e,"worker_timeout",o)}failSession(e,t,n){this.diagnostics?.record("error","reported_error",{...this.diagnosticDetails(e),reason:t});const o=n??this.captureFailure(e);e.quarantined=!0,this.clearRequests(e,!0),this.closeWorkerPort(e),e.lastSnapshotVersion+=1,e.hostPort.postMessage({__oaiDilMessage:!0,data:{...o?{diagnostics:o}:{},error:{message:t==="worker_timeout"?"The DIL runner request timed out":"The DIL runner worker could not be started",name:"Error"},tree:null,version:e.lastSnapshotVersion},event:"snapshot",kind:"event"}),e.hostPort.postMessage({__oaiDilMessage:!0,data:{kind:"failure",stage:t},event:"lifecycle",kind:"event"})}cancelHealthChecks(e,t){for(const[n,o]of this.healthChecks)o.session===e&&(t==null||o.requestId===t)&&(this.diagnostics?.record("health_probe","cancelled",{...this.diagnosticDetails(e),requestId:n,relatedRequestId:o.requestId}),globalThis.clearTimeout(o.timeout),this.healthChecks.delete(n))}closeWorkerPort(e){e.workerPort&&(this.diagnostics?.record("message","cancelled",this.diagnosticDetails(e)),e.workerPort.removeEventListener("message",e.handleWorkerMessage),e.workerPort.close(),e.workerPort=null,e.pendingWorkerCommands.clear(),e.restoringCommands.clear())}notifyWorkerToDispose(e){try{this.workerControlPort?.postMessage({__oaiDilFrame:!0,kind:"disposeRunner",protocolVersion:b,runnerId:e}),this.diagnostics?.record("runner_dispose",this.workerControlPort?"sent":"ignored",{...this.diagnosticDetails(this.sessions.get(e)),runnerId:e})}catch(t){this.diagnostics?.fault("runner_dispose",t,{...this.diagnosticDetails(this.sessions.get(e)),runnerId:e})}}replyToHost(e,t,n){e.hostPort.postMessage({__oaiDilMessage:!0,id:t,kind:"response",...n==="setCompiledDil"||n==="setData"?{result:{inputApplied:!1}}:{}}),this.diagnostics?.record("command","resolved",{...this.diagnosticDetails(e),requestId:t})}diagnosticTrigger(e,t){const n=e.pendingRequests.get(t);return{triggerRunnerId:e.message.runnerId,triggerRequestId:t,triggerCommand:n?.command,triggerAcknowledged:n?.acknowledged}}diagnosticContext(e){return{...this.diagnostics?.context,workerGeneration:this.workerGeneration,...e?{runnerId:e.message.runnerId,sessionGeneration:e.diagnosticGeneration,startupAttempt:e.startupAttempts}:{}}}diagnosticDetails(e){return{...this.diagnosticContext(e),activeRunnerId:this.activeRunnerId??void 0,peers:this.sessions.size,...e?{pendingRequests:e.pendingRequests.size,pendingHostCalls:e.pendingWorkerCommands.size,replaySafe:e.startupRetrySafe,hasSuccessfulSnapshot:e.hasSuccessfulSnapshot,snapshotVersion:e.lastSnapshotVersion}:{}}}captureFailure(e){if(!(!this.diagnostics||e.diagnosticFailureReported))return e.diagnosticFailureReported=!0,this.diagnostics.snapshot({runnerId:e.message.runnerId})}isLiveSession(e){return!this.disposed&&this.sessions.get(e.message.runnerId)===e}}function V(r){return p(r)&&r.__oaiDilMessage===!0&&(r.kind==="ack"||r.kind==="command"||r.kind==="event"||r.kind==="response")}function xe(r){return p(r)&&r.__oaiDilWorker===!0&&(r.kind==="diagnostic"?p(r.record):r.kind==="healthCheck"||r.kind==="healthy"?typeof r.requestId=="string":(r.kind==="executionStarted"||r.kind==="executionFinished")&&typeof r.runnerId=="string")}function p(r){return typeof r=="object"&&r!==null}function L(r){if(!(!p(r)||Array.isArray(r)))try{return JSON.parse(JSON.stringify(r))}catch{return}}const B=`(function(){"use strict";var ne=typeof globalThis<"u"?globalThis:typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},_t={exports:{}},oe;function ot(){return oe||(oe=1,(function(a,t){a.path="dil_renderer/src/DILApiFacade",Object.defineProperty(t,"__esModule",{value:!0}),t.freezeObjectGraph=t.readDILModelNamedEntity=t.isDILModelEntityReference=t.createDILModelGenUIFacade=t.createDILGenUIFacade=t.hardenApiFacade=t.bindDILClientAction=void 0;const e=new WeakMap;function r(D,o){const p=Object.assign({},D);return e.set(p,o),p}t.bindDILClientAction=r;const l=3,i=128,u=/^turn(?:0|[1-9]\\d*)(product|business)(?:0|[1-9]\\d*)(?![\\s\\S])/,d="GenUI.openEntityDetail requires one reference or named entity.",s=new Set(["product","business","local_business","restaurant","hotel","hospital","point_of_interest","urgent_care","entity_sidebar_follow_up"]);function m(D){return Object.setPrototypeOf(D,null),P(D,!1),D}t.hardenApiFacade=m;function h(D){return m({dispatchAction(o,p){const g=y(o,0,e.get(o));D(g,g.handler==="client"&&g.type==="log_event"?p:void 0)},dispatchWidgetAction(o){const p=o.nativeWidgetResolutionId,g=o.componentName;if(typeof p!="string"||!p||typeof g!="string"||!g)throw new Error("Registered component action is missing its bound target.");D(Object.assign(Object.assign({},y(o,0,void 0)),{handler:"server",nativeWidgetResolutionId:p,componentName:g}))},logEvent(o){D({handler:"client",payload:o,type:"log_event"})},issueNewTurn(o,p){D({handler:"client",payload:Object.assign(Object.assign({},p),{query:o}),type:"issue_new_turn"})},openEntityDetail(o,p,g){const b={category:o,query:p};g!==void 0&&(b.extraParams=g),D({handler:"client",payload:b,type:"open_entity_detail"})},openImageLightbox(o,p){D({handler:"client",payload:{images:o,selected_index:p},type:"open_image_lightbox"})},openUrl(o){D({handler:"client",payload:{url:o},type:"open_url"})}})}t.createDILGenUIFacade=h;function x(D){return m({copy(o){if(arguments.length!==1||typeof o!="string")throw new TypeError("GenUI.copy requires one text string.");D.dispatchAction({handler:"client",payload:{value:o},type:"copy"})},issueNewTurn(o){if(arguments.length!==1||typeof o!="string")throw new TypeError("GenUI.issueNewTurn requires one query string.");D.issueNewTurn(o)},openEntityDetail(o){if(arguments.length!==1)throw new TypeError(d);if(o!==null&&typeof o=="object"&&"refId"in o){const p=n(o);D.openEntityDetail(p.category,p.refId)}else{const p=c(o);D.dispatchAction({handler:"client",type:"open_entity_detail",payload:Object.assign({},p)})}},openUrl(o){if(arguments.length!==1||typeof o!="string")throw new TypeError("GenUI.openUrl requires one URL string.");D.openUrl(o)}})}t.createDILModelGenUIFacade=x;function _(D,o){var p;return o.length<=i&&((p=u.exec(o))===null||p===void 0?void 0:p[1])===D}t.isDILModelEntityReference=_;function n(D){if(D===null||typeof D!="object"||Array.isArray(D))throw new TypeError(d);const o=D,p=Reflect.ownKeys(o),g=o.category,b=o.refId;if(p.length!==2||p.some(E=>E!=="category"&&E!=="refId")||g!=="product"&&g!=="business"||typeof b!="string"||!_(g,b))throw new TypeError(d);return{category:g,refId:b}}function c(D){if(D===null||typeof D!="object"||Array.isArray(D))throw new TypeError(d);const o=D,p=Reflect.ownKeys(o);if(!p.includes("category")||!p.includes("value")||p.some(b=>b!=="category"&&b!=="value"&&b!=="disambig"))throw new TypeError(d);const g=f(o.category,128).toLowerCase();if(s.has(g))throw new TypeError(d);return Object.assign({category:g,value:f(o.value,1024)},p.includes("disambig")?{disambig:f(o.disambig,1024)}:{})}t.readDILModelNamedEntity=c;function f(D,o){if(typeof D!="string"||D.length>o||!D.trim())throw new TypeError(d);return D.trim()}function y(D,o,p){var g;if(D===null||typeof D!="object"||Array.isArray(D))throw new Error("GenUI.dispatchAction requires an action object.");const b=D,E={handler:(g=w(b.handler,"handler"))!==null&&g!==void 0?g:"client"},k=w(b.type,"type");k!==void 0&&(E.type=k);const j=w(b.loadingBehavior,"loadingBehavior");j!==void 0&&(E.loadingBehavior=j);const L=b.payload;if(L!==void 0){if(L===null||typeof L!="object"||Array.isArray(L))throw new Error("GenUI.dispatchAction requires payload to be an object.");E.payload=Object.assign({},L),delete E.payload.followup_metadata}const O=b.fallbackAction;if(O!==void 0){if(o>=l)throw new Error("GenUI.dispatchAction exceeds the maximum fallback depth.");E.fallbackAction=y(O,o+1,p)}return p===void 0?E:Object.assign(Object.assign({},E),p)}function w(D,o){if(D!==void 0){if(typeof D!="string")throw new Error(\`GenUI.dispatchAction requires \${o} to be a string.\`);return D}}function P(D,o){N(D,o,new WeakSet)}t.freezeObjectGraph=P;function N(D,o,p){if(!(!H(D)||p.has(D))){p.add(D),o&&N(Object.getPrototypeOf(D),o,p);for(const g of Reflect.ownKeys(D)){const b=Object.getOwnPropertyDescriptor(D,g);b!==void 0&&("value"in b?N(b.value,o,p):(N(b.get,o,p),N(b.set,o,p)))}if(Object.freeze(D),!Object.isFrozen(D))throw new Error("Failed to freeze an object in the object graph.")}}function H(D){return typeof D=="object"&&D!==null||typeof D=="function"}})(_t,_t.exports)),_t.exports}var re=ot(),mt={exports:{}},ie;function st(){return ie||(ie=1,(function(a,t){a.path="dil_renderer/src/DILElement",Object.defineProperty(t,"__esModule",{value:!0}),t.createDilElement=t.isDILRuntimeElement=t.readRuntimeElementKey=t.propsWithChildren=t.createDilJsxRuntime=t.getDilComponentResolver=t.getDilComponentScope=t.createDilComponentPlaceholder=t.getDilElementInteractionScope=t.setDilElementInteractionScope=t.DIL_RENDERED_PROP_NAME=t.DIL_RENDERED_PROP_ELEMENT_TYPE=t.TEXT_ELEMENT_TYPE=t.DIL_FRAGMENT=void 0;const e=Symbol("openai.valdi.dil.runtimeElement");t.DIL_FRAGMENT=Symbol("oai.dil.fragment"),t.TEXT_ELEMENT_TYPE="text",t.DIL_RENDERED_PROP_ELEMENT_TYPE="__dil-rendered-prop",t.DIL_RENDERED_PROP_NAME="__dilRenderedPropName";const r=new WeakMap,l=new WeakMap,i=new WeakMap;function u(y,w){i.set(y,{scope:w})}t.setDilElementInteractionScope=u;function d(y){return i.get(y)}t.getDilElementInteractionScope=d;function s(y,w,P){const N=()=>{throw new Error(\`DIL component placeholder '\${y}' must be used as a JSX element.\`)};return Object.defineProperty(N,"name",{value:y}),r.set(N,w),P!==void 0&&l.set(N,P),N}t.createDilComponentPlaceholder=s;function m(y){return l.get(y)}t.getDilComponentScope=m;function h(y){return r.get(y)}t.getDilComponentResolver=h;function x(y){return{Fragment:t.DIL_FRAGMENT,jsx:(w,P,...N)=>{const H=f(w,P,N);return y?.(H),H}}}t.createDilJsxRuntime=x;function _(y,w){const P={};if(y)for(const N in y)N!=="key"&&(P[N]=y[N]);return w.length===1?P.children=w[0]:w.length>1&&(P.children=w),P}t.propsWithChildren=_;function n(y){var w;const P=(w=y.props)===null||w===void 0?void 0:w.key;if(typeof P=="string"||typeof P=="number")return P}t.readRuntimeElementKey=n;function c(y){return y!==null&&typeof y=="object"&&y[e]===!0}t.isDILRuntimeElement=c;function f(y,w,P){return{[e]:!0,type:y,props:w??void 0,children:P}}t.createDilElement=f})(mt,mt.exports)),mt.exports}var Ft=st(),ft={exports:{}},se;function Vt(){return se||(se=1,(function(a,t){a.path="dil_renderer/src/DILHtmlViewMessenger",Object.defineProperty(t,"__esModule",{value:!0}),t.getDILHtmlViewMessengerHost=t.createDILHtmlViewMessengerApiFacade=t.createDILHtmlViewMessengerHost=t.DILHtmlViewMessengerApiImpl=void 0;const e=ot(),r=Symbol("DILHtmlViewMessengerHost");class l{constructor(h,x){this.renderer=h,this.eventHandlers=new Map,this.options=x,this.channelId=h.nextHtmlViewMessengerChannelId(),this.host=i(this.channelId,{command:(_,n)=>this.receiveCommand(_,n),event:(_,n)=>this.receiveEvent(_,n),registerTransport:_=>this.renderer.registerHtmlViewMessengerTransport(this.channelId,_)}),this.unregisterReceiver=h.registerHtmlViewMessengerReceiver(this.channelId,{command:(_,n)=>this.receiveCommand(_,n),event:(_,n)=>this.receiveEvent(_,n)})}updateOptions(h){this.options=h}receiveCommand(h,x){var _,n;const c=(n=(_=this.options)===null||_===void 0?void 0:_.commands)===null||n===void 0?void 0:n[h];if(c===void 0)throw new Error(\`Unknown DIL html-view messenger command "\${h}"\`);return c(x)}receiveEvent(h,x){const _=this.eventHandlers.get(h);if(_!==void 0)for(const n of _)n(x)}emit(h,x){this.renderer.emitHtmlViewMessengerEvent(this.channelId,h,x)}sendCommand(h,x){return this.renderer.sendHtmlViewMessengerCommand(this.channelId,h,x)}on(h,x){let _=this.eventHandlers.get(h);return _===void 0&&(_=new Set,this.eventHandlers.set(h,_)),_.add(x),()=>{_?.delete(x)}}getHost(){return this.host}dispose(){this.unregisterReceiver(),this.eventHandlers.clear()}}t.DILHtmlViewMessengerApiImpl=l;function i(m,h){const x={channelId:m,command:h.command,event:h.event,registerTransport:h.registerTransport};return Object.freeze(s(x,x))}t.createDILHtmlViewMessengerHost=i;function u(m){const h=new Map,x=new Proxy(Object.create(null),{get:(n,c)=>{if(typeof c!="string"||c==="then")return;let f=h.get(c);return f===void 0&&(f=Object.freeze(y=>m.sendCommand(c,y)),h.set(c,f)),f}}),_=s({commands:x,emit:(n,c)=>{m.emit(n,c)},on:(n,c)=>{const f=m.on(n,c);return Object.freeze(()=>{f()})}},m.getHost());return(0,e.hardenApiFacade)(_)}t.createDILHtmlViewMessengerApiFacade=u;function d(m){if(!((typeof m!="object"||m===null)&&typeof m!="function"))return m[r]}t.getDILHtmlViewMessengerHost=d;function s(m,h){return new Proxy(m,{get:(x,_,n)=>_===r?h:Reflect.get(x,_,n)})}})(ft,ft.exports)),ft.exports}var Qe=Vt(),ht={exports:{}},gt={exports:{}},yt={exports:{}},vt={exports:{}},ae;function Tt(){return ae||(ae=1,(function(a,t){a.path="dil_renderer/src/DILRuntimeUtils",Object.defineProperty(t,"__esModule",{value:!0}),t.toError=t.isRecord=t.isPromiseLike=void 0;function e(i){return i!==null&&typeof i=="object"&&typeof i.then=="function"}t.isPromiseLike=e;function r(i){return i!==null&&typeof i=="object"}t.isRecord=r;function l(i){return i instanceof Error?i:new Error(String(i))}t.toError=l})(vt,vt.exports)),vt.exports}var le;function de(){return le||(le=1,(function(a,t){a.path="dil_renderer/src/DILHookRuntime",Object.defineProperty(t,"__esModule",{value:!0}),t.runCleanup=t.areDependenciesEqual=void 0;const e=Tt();function r(i,u){if(i.length!==u.length)return!1;for(let d=0;d<i.length;d++)if(!Object.is(i[d],u[d]))return!1;return!0}t.areDependenciesEqual=r;function l(i,u){try{i()}catch(d){u.reportError((0,e.toError)(d))}}t.runCleanup=l})(yt,yt.exports)),yt.exports}var It={exports:{}},bt={exports:{}},xt={exports:{}},ue;function Ht(){return ue||(ue=1,(function(a,t){a.path="dil_renderer/src/DILSpeechSynthesis",Object.defineProperty(t,"__esModule",{value:!0}),t.sanitizeDILSpeechState=t.normalizeDILSpeechSource=t.UNAVAILABLE_DIL_SPEECH=t.normalizeDILSpeechRequestLog=t.DILSpeechFailureStage=t.DILSpeechStatus=void 0;var e;(function(h){h.Idle="idle",h.Loading="loading",h.Playing="playing"})(e||(t.DILSpeechStatus=e={}));var r;(function(h){h.Play="play",h.Request="request",h.Response="response",h.Streaming="streaming"})(r||(t.DILSpeechFailureStage=r={}));const l=console,i=["event_name","statsig_event_name","structured_event_name"];function u(h){try{if(h===null||typeof h!="object"||Array.isArray(h))return;const x=h,_={};for(const c of i){const f=x[c];if(f!==void 0){if(typeof f!="string"||!f.trim()||f.length>256)return;_[c]=f}}if(Object.keys(_).length===0)return;const n=x.event_data;if(n!==void 0){if(n===null||typeof n!="object"||Array.isArray(n))return;const c=Object.keys(n);if(c.length>32)return;const f=Object.create(null);for(const y of c){const w=n[y];if(y.length>128||!(w===null||typeof w=="boolean"||typeof w=="string"&&w.length<=2048||typeof w=="number"&&Number.isFinite(w)))return;f[y]=w}_.event_data=f}if(JSON.stringify(_).length<=16384)return _}catch{l.warn("DIL speech logging metadata could not be read")}}t.normalizeDILSpeechRequestLog=u,t.UNAVAILABLE_DIL_SPEECH=Object.freeze({status:e.Idle,available:!1,error:null});const d={language:128,pronunciationHint:4096,version:256,source:128};function s(h){if(h===null||typeof h!="object")return null;const x=h,_=x.text;if(typeof _!="string"||!_.trim()||_.length>32768)return null;const n={text:_};for(const f of Object.keys(d)){const y=x[f];if(y===void 0)continue;const w=d[f];if(typeof y!="string"||y.length>w)return null;(f!=="version"||y!=="")&&(n[f]=y)}const c=x.playbackSpeed;return typeof c=="number"&&Number.isFinite(c)&&c>=.25&&c<=4&&(n.playbackSpeed=c),n}t.normalizeDILSpeechSource=s;function m(h){if(h===null||typeof h!="object")return t.UNAVAILABLE_DIL_SPEECH;const x=h;let _=null;if(x.error!==null&&typeof x.error=="object"){const n=x.error,c=n.failureStage;if(c===r.Play||c===r.Request||c===r.Response||c===r.Streaming){const f=n.httpStatus;_=Object.assign({failureStage:c},typeof f=="number"&&Number.isInteger(f)&&f>=100&&f<=599?{httpStatus:f}:{})}}return{available:x.available===!0,status:_!==null?e.Idle:x.status===e.Loading||x.status===e.Playing?x.status:e.Idle,error:_}}t.sanitizeDILSpeechState=m})(xt,xt.exports)),xt.exports}var ce;function Xe(){return ce||(ce=1,(function(a,t){a.path="dil_renderer/src/DILSpeechOwner",Object.defineProperty(t,"__esModule",{value:!0}),t.DILSpeechOwner=void 0;const e=ot(),r=Ht(),l=console;class i{constructor(d,s,m,h){if(this.sourceKey=d,this.runtime=m,this.scheduleRender=h,this.disposed=!1,this.state=r.UNAVAILABLE_DIL_SPEECH,this.logging={},this.play=()=>{var x;if(!(this.disposed||this.session===void 0||!this.state.available||this.state.status!==r.DILSpeechStatus.Idle||!(!((x=this.runtime)===null||x===void 0)&&x.isUserInteraction())))try{this.session.play(this.logging.play_requested)}catch{this.fail(r.DILSpeechFailureStage.Play)}},this.stop=()=>{var x;if(!(this.disposed||this.session===void 0))try{this.session.stop(this.logging.stop_requested!==void 0&&this.state.available&&((x=this.runtime)===null||x===void 0?void 0:x.isUserInteraction())===!0?this.logging.stop_requested:void 0)}catch{this.fail(r.DILSpeechFailureStage.Play)}},!(s===null||m===void 0))try{const x=m.createSession(s,_=>this.receive(_));this.disposed?x.dispose():this.session=x}catch{this.state=r.UNAVAILABLE_DIL_SPEECH,this.fail(r.DILSpeechFailureStage.Request),this.disposed=!0}}setLogging(d){this.logging={};try{this.logging={play_requested:(0,r.normalizeDILSpeechRequestLog)(d?.play_requested),stop_requested:(0,r.normalizeDILSpeechRequestLog)(d?.stop_requested)}}catch{l.warn("DIL speech logging metadata could not be read")}}snapshot(){return(0,e.hardenApiFacade)(Object.assign(Object.assign({},this.state),{play:this.play,stop:this.stop}))}dispose(){if(this.disposed)return;this.disposed=!0;const d=this.session;this.session=void 0;try{d?.dispose()}catch{l.warn("DIL speech session disposal failed")}}receive(d){this.disposed||(this.state=(0,r.sanitizeDILSpeechState)(d),this.scheduleRender())}fail(d){l.warn(\`DIL speech session failed during \${d}\`),this.receive(Object.assign(Object.assign({},this.state),{status:r.DILSpeechStatus.Idle,error:{failureStage:d}}))}}t.DILSpeechOwner=i})(bt,bt.exports)),bt.exports}var Rt={exports:{}},Ct={exports:{}},pe;function _e(){return pe||(pe=1,(function(a,t){a.path="dil_renderer/src/DILDictation",Object.defineProperty(t,"__esModule",{value:!0}),t.normalizeDILDictationOptions=t.DILDictationEventKind=t.DILDictationStatus=void 0;var e;(function(i){i.Idle="idle",i.Starting="starting",i.Recording="recording",i.Stopping="stopping",i.Done="done",i.Error="error"})(e||(t.DILDictationStatus=e={}));var r;(function(i){i.Recording="recording",i.Transcript="transcript",i.Stopping="stopping",i.Done="done",i.Error="error",i.Cancelled="cancelled"})(r||(t.DILDictationEventKind=r={}));function l(i){if(i===null||typeof i!="object"||Array.isArray(i))return null;const u=i.language;return u===void 0?{}:typeof u!="string"||!u.trim()||u.length>128?null:{language:u}}t.normalizeDILDictationOptions=l})(Ct,Ct.exports)),Ct.exports}var me;function Ye(){return me||(me=1,(function(a,t){a.path="dil_renderer/src/DILDictationOwner",Object.defineProperty(t,"__esModule",{value:!0}),t.DILDictationOwner=void 0;const e=ot(),r=_e(),l=console,i=Object.freeze({status:r.DILDictationStatus.Idle,transcript:"",error:null});class u{constructor(s,m){this.runtime=s,this.scheduleRender=m,this.disposed=!1,this.generation=0,this.state=i,this.start=()=>{if(this.disposed||this.attempt!==void 0)return;const h=this.runtime;if(h===void 0){this.update(Object.assign(Object.assign({},i),{status:r.DILDictationStatus.Error,error:{code:"integration_error",message:"The dictation host service is not configured."}}));return}if(!h.isUserInteraction())return;const x={generation:++this.generation,session:void 0,startInvoked:!1,stopSent:!1};this.attempt=x,this.state=Object.assign(Object.assign({},i),{status:r.DILDictationStatus.Starting});let _;try{_=(0,r.normalizeDILDictationOptions)(this.options===void 0?{}:this.options)}catch{_=null}if(_===null){this.finish(x,{code:"invalid_options",message:"Dictation language must be a nonempty string of at most 128 characters."},void 0);return}if(this.scheduleRender(),!!this.isCurrent(x))try{const n=h.createSession(_,c=>this.receive(x,c));if(!this.isCurrent(x)){this.disposeSession(n);return}x.session=n,x.startInvoked=!0,n.start(),this.sendStop(x)}catch{this.commandFailed(x)}},this.stop=()=>{const h=this.attempt;h===void 0||this.state.status===r.DILDictationStatus.Stopping||(this.update(Object.assign(Object.assign({},this.state),{status:r.DILDictationStatus.Stopping})),this.sendStop(h))},this.cancel=()=>{if(this.disposed||this.attempt===void 0&&this.state===i)return;const h=this.invalidate();if(this.state=i,h?.session!==void 0){try{h.session.cancel()}catch{l.warn("DIL dictation cancellation failed")}this.disposeSession(h.session)}this.scheduleRender()}}setOptions(s){this.options=s}snapshot(){return(0,e.hardenApiFacade)(Object.assign(Object.assign({},this.state),{start:this.start,stop:this.stop,cancel:this.cancel}))}sendStop(s){if(!(!this.isCurrent(s)||this.state.status!==r.DILDictationStatus.Stopping||!s.startInvoked||s.session===void 0||s.stopSent)){s.stopSent=!0;try{s.session.stop()}catch{this.commandFailed(s)}}}dispose(){if(this.disposed)return;this.disposed=!0,this.options=void 0;const s=this.invalidate();this.state=i,s?.session!==void 0&&this.disposeSession(s.session)}receive(s,m){if(this.isCurrent(s))switch(m.kind){case r.DILDictationEventKind.Recording:this.state.status===r.DILDictationStatus.Starting&&this.update(Object.assign(Object.assign({},this.state),{status:r.DILDictationStatus.Recording}));break;case r.DILDictationEventKind.Transcript:this.update(Object.assign(Object.assign({},this.state),{transcript:m.transcript}));break;case r.DILDictationEventKind.Stopping:s.stopSent=!0,this.update(Object.assign(Object.assign({},this.state),{status:r.DILDictationStatus.Stopping}));break;case r.DILDictationEventKind.Done:this.finish(s,null,m.transcript);break;case r.DILDictationEventKind.Error:this.finish(s,{code:m.error.code,message:m.error.message},void 0);break;case r.DILDictationEventKind.Cancelled:this.invalidate(),this.state=i,s.session!==void 0&&this.disposeSession(s.session),this.scheduleRender();break}}finish(s,m,h){this.isCurrent(s)&&(this.invalidate(),this.state={status:m===null?r.DILDictationStatus.Done:r.DILDictationStatus.Error,transcript:h??this.state.transcript,error:m},s.session!==void 0&&this.disposeSession(s.session),this.scheduleRender())}commandFailed(s){l.warn("DIL dictation host command failed"),this.finish(s,{code:"host_error",message:"Dictation could not complete. Please try again."},void 0)}invalidate(){const s=this.attempt;return this.attempt=void 0,this.generation++,s}isCurrent(s){return!this.disposed&&s.generation===this.generation}update(s){this.state=s,this.scheduleRender()}disposeSession(s){try{s.dispose()}catch{l.warn("DIL dictation session disposal failed")}}}t.DILDictationOwner=u})(Rt,Rt.exports)),Rt.exports}var fe;function Ze(){return fe||(fe=1,(function(a,t){a.path="dil_renderer/src/DILRuntimeApiImpl",Object.defineProperty(t,"__esModule",{value:!0}),t.DILRuntimeApiImpl=void 0;const e=de(),r=Vt(),l=Xe(),i=Ye(),u=Ht(),d=st(),s=setInterval.bind(globalThis),m=clearInterval.bind(globalThis);class h{constructor(_,n,c,f,y){this.htmlViewMessengerRuntime=_,this.host=n,this.statePersistence=c,this.speechSynthesis=f,this.dictation=y,this.activeBreakpoints=[],this.appData={},this.constants={},this.theme="light",this.timeSubscriptions=new Map}get renderedRootValue(){return this.rootValue}clearRenderedRootValue(){this.rootValue=void 0}updateVariables(_,n,c,f){if(this.hostIsMobile===void 0){const y=_.__dilHost;this.hostIsMobile=y!==null&&typeof y=="object"&&!Array.isArray(y)&&y.isMobile===!0}this.appData=_,this.constants=n,this.theme=c,this.activeBreakpoints=f}render(_){var n;if(this.rootValue=_,(0,d.isDILRuntimeElement)(_)&&typeof _.type=="function"&&typeof((n=_.props)===null||n===void 0?void 0:n.key)=="string"&&/^body:\\d+$/.test(_.props.key)){const f=Object.assign({},_.props);delete f.key,this.rootValue=(0,d.createDilElement)(_.type,f,_.children)}return _}useAppData(_){return _===void 0?this.appData:_(this.appData)}useConstants(_){return _===void 0?this.constants:_(this.constants)}useCallback(_,n){return this.useMemo(()=>_,n)}useEffect(_,n){const c=this.host.requireCurrentHookFrame("useEffect");let f=this.readHook(c,0);if(f===void 0&&(f={kind:0,cleanup:void 0,deps:void 0},c.hooks[c.hookIndex-1]=f),n===void 0||f.deps===void 0||!(0,e.areDependenciesEqual)(f.deps,n)){const y=f.deps;f.deps=n,this.host.enqueuePendingEffect({frame:c,hook:f,effect:_,previousDeps:y})}}useId(){const _=this.host.requireCurrentHookFrame("useId"),n=this.readHook(_,1);if(n!==void 0)return n.value;const c=\`dil-\${_.id}-\${_.hookIndex-1}\`;return _.hooks[_.hookIndex-1]={kind:1,value:c},c}useDILMessenger(_){return this.useHtmlViewMessengerHook("useDILMessenger",_)}useHtmlViewMessenger(_){return this.useHtmlViewMessengerHook("useHtmlViewMessenger",_)}useHtmlViewMessengerHook(_,n){const c=this.host.requireCurrentHookFrame(_),f=this.readHook(c,3);if(f!==void 0)return f.messenger.updateOptions(n),f.publicApi;const y=new r.DILHtmlViewMessengerApiImpl(this.htmlViewMessengerRuntime,n),w=(0,r.createDILHtmlViewMessengerApiFacade)(y);return c.hooks[c.hookIndex-1]={kind:3,messenger:y,publicApi:w},w}useMemo(_,n){const c=this.host.requireCurrentHookFrame("useMemo"),f=this.readHook(c,2);if(f!==void 0&&(0,e.areDependenciesEqual)(f.deps,n))return f.value;const y=_();return f===void 0?c.hooks[c.hookIndex-1]={kind:2,value:y,deps:n}:(f.value=y,f.deps=n),y}useNow(_,n){const c=_===void 0?!0:_;if(typeof c!="boolean")throw new TypeError("DIL.useNow expects a boolean");const f=n===void 0?1e3:n;if(f!==50&&f!==1e3)throw new TypeError("DIL.useNow expects intervalMs to be 50 or 1000");const y=this.host.requireCurrentHookFrame("useNow");return this.useEffect(()=>{var w;if(!(!c||!y.isMounted))return this.timeSubscriptions.set(f,((w=this.timeSubscriptions.get(f))!==null&&w!==void 0?w:0)+1),this.updateTimeInterval(),()=>{var P;const N=((P=this.timeSubscriptions.get(f))!==null&&P!==void 0?P:0)-1;N<=0?this.timeSubscriptions.delete(f):this.timeSubscriptions.set(f,N),this.updateTimeInterval()}},[c,f]),Date.now()}updateTimeInterval(){const _=this.timeSubscriptions.has(50)?50:this.timeSubscriptions.has(1e3)?1e3:void 0;_!==this.timeIntervalMs&&(this.timeInterval!==void 0&&(m(this.timeInterval),this.timeInterval=void 0),this.timeIntervalMs=_,_!==void 0&&(this.timeInterval=s(()=>this.host.scheduleRender(),_)))}useRef(_){const n=this.host.requireCurrentHookFrame("useRef"),c=this.readHook(n,4);if(c!==void 0)return c.ref;const f={current:_};return n.hooks[n.hookIndex-1]={kind:4,ref:f},f}useDictation(_){const n=this.host.requireCurrentHookFrame("useDictation");let c=this.readHook(n,7);return c===void 0&&(c={kind:7,owner:new i.DILDictationOwner(this.dictation,()=>{n.isMounted&&this.host.scheduleRender()})},n.hooks[n.hookIndex-1]=c),c.owner.setOptions(_),c.owner.snapshot()}useSpeechSynthesizer(_,n){const c=this.host.requireCurrentHookFrame("useSpeechSynthesizer"),f=(0,u.normalizeDILSpeechSource)(_),y=JSON.stringify(f);let w=this.readHook(c,6);return(w===void 0||w.owner.sourceKey!==y)&&(w?.owner.dispose(),w={kind:6,owner:new l.DILSpeechOwner(y,f,this.speechSynthesis,()=>{c.isMounted&&this.host.scheduleRender()})},c.hooks[c.hookIndex-1]=w),w.owner.setLogging(n),w.owner.snapshot()}useState(_,n){const c=this.host.requireCurrentHookFrame("useState"),f=this.readHook(c,5);if(f!==void 0)return[f.value,f.setter];const y=typeof _=="function"?_():_,w=this.statePersistence.createStateHook(c,y,n);return c.hooks[c.hookIndex-1]=w,[w.value,w.setter]}useTheme(){return{isDark:this.theme==="dark",isLight:this.theme==="light",theme:this.theme}}useBreakpoint(_){return this.activeBreakpoints.includes(_)}useIsMobile(){return this.hostIsMobile===!0}readHook(_,n){const c=_.hooks[_.hookIndex];if(_.hookIndex++,c!==void 0){if(c.kind!==n)throw new Error("DIL hooks must be called in the same order on every render.");return c}}}t.DILRuntimeApiImpl=h})(It,It.exports)),It.exports}var Et={exports:{}},wt={exports:{}},he;function tn(){return he||(he=1,(function(a,t){a.path="dil_renderer/src/DILStateSnapshotCodec",Object.defineProperty(t,"__esModule",{value:!0}),t.removeDILStateSnapshotValue=t.setDILStateSnapshotValue=t.parseDILStateSnapshot=t.DIL_WIDGET_STATE_MAX_ENTRIES=t.DIL_ROOT_STATE_MAX_ENTRIES=void 0;const e=8*1024,r=8;t.DIL_ROOT_STATE_MAX_ENTRIES=128,t.DIL_WIDGET_STATE_MAX_ENTRIES=512;function l(n,c){try{return d(JSON.parse(n),c)}catch{return null}}t.parseDILStateSnapshot=l;function i(n,c,f,y){const w=s(n?.state);return w[c]=f,d(w,y)}t.setDILStateSnapshotValue=i;function u(n,c,f){const y=s(n?.state);return delete y[c],d(y,f)}t.removeDILStateSnapshotValue=u;function d(n,c){try{if(!x(n)||!m(n,0,new WeakSet,{entries:0,maxEntries:c}))return null;const f=JSON.stringify(n);if(new TextEncoder().encode(f).byteLength>e)return null;const y=JSON.parse(f);return x(y)?{serialized:f,state:y}:null}catch{return null}}function s(n){const c=Object.create(null);if(n!==void 0)for(const f of Object.keys(n))c[f]=n[f];return c}function m(n,c,f,y){if(c>r)return!1;if(n===null||typeof n=="boolean")return!0;if(typeof n=="string")return!_(n);if(typeof n=="number")return Number.isFinite(n);if(typeof n!="object"||f.has(n))return!1;f.add(n);try{if(Array.isArray(n)){if(Object.getPrototypeOf(n)!==Array.prototype||n.length>y.maxEntries-y.entries||Reflect.ownKeys(n).length!==n.length+1)return!1;for(let w=0;w<n.length;w++)if(!h(n,String(w),c,f,y))return!1;return!0}if(!x(n))return!1;for(const w of Reflect.ownKeys(n))if(typeof w!="string"||_(w)||!h(n,w,c,f,y))return!1;return!0}finally{f.delete(n)}}function h(n,c,f,y,w){const P=Object.getOwnPropertyDescriptor(n,c);return P===void 0||!P.enumerable||P.value===void 0?!1:(w.entries++,w.entries<=w.maxEntries&&m(P.value,f+1,y,w))}function x(n){if(n===null||typeof n!="object"||Array.isArray(n))return!1;const c=Object.getPrototypeOf(n);return c===Object.prototype||c===null}function _(n){try{return encodeURIComponent(n),!1}catch{return!0}}})(wt,wt.exports)),wt.exports}var ge;function en(){return ge||(ge=1,(function(a,t){a.path="dil_renderer/src/DILStatePersistence",Object.defineProperty(t,"__esModule",{value:!0}),t.DILStatePersistence=t.DILStateSnapshotChangeOrigin=void 0;const e=tn();var r;(function(i){i[i.Initial=0]="Initial",i[i.LocalAction=1]="LocalAction"})(r||(t.DILStateSnapshotChangeOrigin=r={}));class l{get maxSnapshotEntries(){return this.widgetId===void 0?e.DIL_ROOT_STATE_MAX_ENTRIES:e.DIL_WIDGET_STATE_MAX_ENTRIES}constructor(u,d,s){this.scheduleRender=u,this.stateChangeHandler=d,this.stateSynchronizationErrorHandler=s,this.widgetScopes=new Map,this.allocatedSlots=new Set,this.allocationByOwner=new Map,this.nextAnonymousSlot=0,this.pendingInitialSnapshot=!1}createStateHook(u,d,s){var m;if(s?.widgetId!==void 0)return this.widgetScope(s.widgetId).createStateHook(u,d,{key:s.key});const h=s?.key;if(h!==void 0&&(typeof h!="string"||h.length===0))throw new Error("DIL state keys must be nonempty strings.");const x=u.stateIdentity,_=x?.nextStateSlot;x!==void 0&&x.nextStateSlot++;const n=u.hookIndex-1,c=x===void 0?\`\${u.id}:\${n}\`:\`\${h??_}\\0\${x.ownerKey}\`,f=this.resolveSlot(c,h,this.widgetId===void 0?x?.siblingOrdinal:void 0,x!==void 0),y=(m=this.snapshot)===null||m===void 0?void 0:m.state[f],w=y===void 0?d:y,P={kind:5,defaultValue:d,ownerId:c,slot:f,widgetId:this.widgetId,value:w,setter:()=>{}};if(P.setter=N=>{const H=typeof N=="function"?N(P.value):N;Object.is(P.value,H)||(P.value=H,this.updatePersistedHookValue(P,H),this.scheduleRender())},y===void 0){const N=(0,e.setDILStateSnapshotValue)(this.snapshot,f,d,this.maxSnapshotEntries);N!==null&&(this.snapshot=N,this.pendingInitialSnapshot=!0)}return P}releaseStateHook(u){if(u.widgetId!==this.widgetId&&u.widgetId!==void 0){this.widgetScope(u.widgetId).releaseStateHook(u);return}const d=this.allocationByOwner.get(u.ownerId);d===void 0||d.retainAfterUnmount||(this.allocationByOwner.delete(u.ownerId),this.allocatedSlots.delete(d.slot))}setStateSnapshot(u,d){var s;if(d!==void 0)return this.widgetScope(d).setStateSnapshot(u);const m=u===void 0?void 0:(0,e.parseDILStateSnapshot)(u,this.maxSnapshotEntries);return m===null||m?.serialized===((s=this.snapshot)===null||s===void 0?void 0:s.serialized)?!1:(this.snapshot=m,this.pendingInitialSnapshot=!1,!0)}applySnapshotToHook(u){var d;if(u.widgetId!==this.widgetId&&u.widgetId!==void 0)return this.widgetScope(u.widgetId).applySnapshotToHook(u);const s=(d=this.snapshot)===null||d===void 0?void 0:d.state[u.slot],m=s===void 0?u.defaultValue:s;return Object.is(u.value,m)?!1:(u.value=m,!0)}commitStateSnapshot(){for(const u of this.widgetScopes.values())u.commitStateSnapshot();!this.pendingInitialSnapshot||this.snapshot===void 0||(this.pendingInitialSnapshot=!1,this.notifyStateChange(this.snapshot.serialized,r.Initial))}updateRenderedRootIdentity(u){for(const d of this.widgetScopes.values())d.updateRenderedRootIdentity(u);if(this.renderedRootIdentity===void 0){this.renderedRootIdentity=u;return}this.renderedRootIdentity!==u&&(this.renderedRootIdentity=u,this.allocationByOwner.clear(),this.allocatedSlots.clear(),this.nextAnonymousSlot=0)}resolveSlot(u,d,s,m){const h=this.allocationByOwner.get(u);if(h!==void 0)return h.slot;let x;if(d===void 0)do x=String(this.nextAnonymousSlot),this.nextAnonymousSlot++;while(this.allocatedSlots.has(x));else{x=d;let _=s??1;for(_>1&&(x=\`\${d}:\${_}\`);this.allocatedSlots.has(x);)_++,x=\`\${d}:\${_}\`}return this.allocationByOwner.set(u,{retainAfterUnmount:m,slot:x}),this.allocatedSlots.add(x),x}updatePersistedHookValue(u,d){var s,m;let h=(0,e.setDILStateSnapshotValue)(this.snapshot,u.slot,d,this.maxSnapshotEntries);h===null&&(((s=this.snapshot)===null||s===void 0?void 0:s.state[u.slot])===void 0||(h=(0,e.removeDILStateSnapshotValue)(this.snapshot,u.slot,this.maxSnapshotEntries),h===null))||h.serialized!==((m=this.snapshot)===null||m===void 0?void 0:m.serialized)&&(this.snapshot=h,this.notifyStateChange(h.serialized,r.LocalAction))}notifyStateChange(u,d){if(this.stateChangeHandler!==void 0)try{this.stateChangeHandler(u,d,this.widgetId)}catch(s){this.stateSynchronizationErrorHandler(s instanceof Error?s:new Error(String(s)))}}widgetScope(u){if(typeof u!="string"||!u||u.length>1024)throw new Error("DIL widget state requires a valid widget identity.");let d=this.widgetScopes.get(u);return d===void 0&&(d=new l(this.scheduleRender,this.stateChangeHandler,this.stateSynchronizationErrorHandler),d.widgetId=u,d.renderedRootIdentity=this.renderedRootIdentity,this.widgetScopes.set(u,d)),d}}t.DILStatePersistence=l})(Et,Et.exports)),Et.exports}var Dt={exports:{}},ye;function ve(){return ye||(ye=1,(function(a,t){a.path="dil_renderer/src/DILSourceEvaluator",Object.defineProperty(t,"__esModule",{value:!0}),t.createDILRuntimeApiFacade=t.createDILDateConstructor=t.createDILJsxRuntimeFacade=void 0;const e=st(),r=ot();function l(d){return(0,r.hardenApiFacade)((0,e.createDilJsxRuntime)(d))}t.createDILJsxRuntimeFacade=l;function i(d){if(d===void 0)return Date;const s=function(...m){return new.target===void 0?new Date(d).toString():Reflect.construct(Date,m.length===0?[d]:m,new.target)};return Object.setPrototypeOf(s,Date),Object.defineProperty(s,"prototype",{value:Date.prototype}),Object.defineProperty(s,"now",{configurable:!1,enumerable:!1,value:Object.freeze(()=>d),writable:!1}),Object.freeze(s)}t.createDILDateConstructor=i;function u(d){const s={render(m){return d.render(m)},useAppData(m){return d.useAppData(m)},useConstants(m){return d.useConstants(m)},useCallback(m,h){return d.useCallback(m,h)},useEffect(m,h){d.useEffect(m,h)},useId(){return d.useId()},useDILMessenger(m){return d.useDILMessenger(m)},useHtmlViewMessenger(m){return d.useHtmlViewMessenger(m)},useMemo(m,h){return d.useMemo(m,h)},useNow(m,h){return d.useNow(m,h)},useRef(m){return d.useRef(m)},useDictation(m){return d.useDictation(m)},useSpeechSynthesizer(m,h){return d.useSpeechSynthesizer(m,h)},useState(m,h){return d.useState(m,{key:h?.key,widgetId:void 0})},useTheme(){return d.useTheme()},useBreakpoint(m){return d.useBreakpoint(m)},useIsMobile(){return d.useIsMobile()}};return(0,r.hardenApiFacade)(s)}t.createDILRuntimeApiFacade=u})(Dt,Dt.exports)),Dt.exports}var St={exports:{}},Ie;function nn(){return Ie||(Ie=1,(function(a,t){a.path="dil_renderer/src/DILSemanticKey",Object.defineProperty(t,"__esModule",{value:!0}),t.getSinglePotentialHostRootIndex=void 0;const e=st();function r(i){let u=-1;for(let d=0;d<i.length;d++){const s=l(i[d]);if(s!==0){if(s>1||u!==-1)return-1;u=d}}return u}t.getSinglePotentialHostRootIndex=r;function l(i){if(i==null||typeof i=="boolean"||i==="")return 0;const u=Array.isArray(i)?i:(0,e.isDILRuntimeElement)(i)&&i.type===e.DIL_FRAGMENT?i.children:void 0;if(u===void 0)return 1;let d=0;for(const s of u)if(d+=l(s),d>1)return 2;return d}})(St,St.exports)),St.exports}var be;function on(){return be||(be=1,(function(a,t){a.path="dil_renderer/src/DILRenderFunctionRuntime",Object.defineProperty(t,"__esModule",{value:!0}),t.DILRenderFunctionRuntime=void 0;const e=st(),r=de(),l=qt(),i=Ze(),u=en(),d=ve(),s=ot(),m=Tt(),h=nn(),x=Symbol("openai.valdi.dil.componentFunctionId"),_=Object.freeze([]);let n=0;class c{constructor(o,p,g,b,E,k,j,L,O,W,A,q,F,B){this.elementsMetadata=o,this.delegate=p,this.errorReporter=g,this.errorMode=b,this.scheduler=k,this.trace=j,this.dateConstructor=L,this.fixedTimeMs=O,this.genUIFacade=W,this.committedRootChildren=[],this.nextFrameId=0,this.nextNodeId=1,this.nodeStack=[],this.pendingDestroyedNodes=[],this.renderId=0,this.renderFailed=!1,this.sourceGeneration=0,this.rootNode={key:"root",kind:4,lastRenderId:0,parentIndex:0},this.nextRootChildren=[],this.namedFunctionIdentities=new Map,this.keyedComponents=new Map,this.renderedParentStack=[],this.resolvedComponents=Object.create(null),this.resolvedComponentScopes=new WeakMap,this.isFlushingEffects=!1,this.statePersistence=new u.DILStatePersistence(()=>this.scheduleRender(),A,v=>this.errorReporter.reportError(v)),this.runtimeApi=new i.DILRuntimeApiImpl(E,this,this.statePersistence,q,F===void 0?void 0:{createSession:(v,I)=>F.createSession(v,I),isUserInteraction:()=>this.nodeStack.length===0&&!this.isFlushingEffects&&F.isUserInteraction()}),this.runtimeApiFacade=(0,d.createDILRuntimeApiFacade)(this.runtimeApi),this.widgetRuntimeApiFacade=(0,s.hardenApiFacade)(Object.assign(Object.assign({},this.runtimeApiFacade),{useState:(v,I)=>this.runtimeApi.useState(v,I)})),this.modelGenUIFacade=W===void 0?void 0:(0,s.createDILModelGenUIFacade)(W),this.jsxRuntimeFacade=(0,d.createDILJsxRuntimeFacade)(v=>this.registerKeyedComponent(v)),this.sourceEvaluator=B({dateConstructor:this.dateConstructor,fixedTimeMs:this.fixedTimeMs,genUIFacade:this.genUIFacade,jsxRuntimeFacade:this.jsxRuntimeFacade,modelGenUIFacade:this.modelGenUIFacade,reportUnhandledError:v=>{this.errorReporter.reportUnhandledError!==void 0?this.errorReporter.reportUnhandledError(v):this.errorReporter.reportError(v)},runtimeApiFacade:this.runtimeApiFacade,widgetRuntimeApiFacade:this.widgetRuntimeApiFacade,trace:this.trace})}evaluate(o){this.sourceGeneration++,this.runtimeApi.clearRenderedRootValue();try{this.sourceEvaluator.evaluate(o)}catch(p){this.runtimeApi.clearRenderedRootValue(),this.reportError(p)}}clearRenderedRoot(){this.runtimeApi.clearRenderedRootValue()}setStateSnapshot(o,p){return this.statePersistence.setStateSnapshot(o,p)?(this.applyStateSnapshotToMountedHooks(this.rootNode,p)&&this.scheduleRender(),!0):!1}commitStateSnapshot(){this.statePersistence.commitStateSnapshot()}didLastRenderFail(){return this.renderFailed}render(o,p,g,b){this.runtimeApi.updateVariables(o,p,g,b),this.pendingEffects=void 0,this.renderFailed=!1,this.unmountCleanups=void 0,this.nodeStack.length=0,this.renderedParentStack.length=0,this.renderedParentStack.push(void 0),this.renderId++,this.pushRenderNode(this.rootNode);try{this.sourceEvaluator.beginRender();const E=this.runtimeApi.renderedRootValue;this.statePersistence.updateRenderedRootIdentity(this.getRenderedRootIdentity(E)),this.renderValue(E,"root",void 0)}catch(E){this.reportError(E)}finally{try{this.endRenderNode(this.rootNode)}catch(E){this.reportError(E)}if(!this.renderFailed)try{this.commitUpdates()}catch(E){this.reportError(E)}this.renderFailed&&this.discardPendingEffectsFrom(0),this.renderedParentStack.length=0,this.scheduleEffectFlush(void 0)}}dispose(){this.pendingEffects=void 0,this.unmountCleanups=void 0;const o=this.rootNode.children;if(o!==void 0){for(const p of o.children)this.destroyRenderNode(p);this.rootNode.children=void 0}this.runtimeApi.clearRenderedRootValue(),this.scheduleEffectFlush(()=>this.sourceEvaluator.dispose())}renderValue(o,p,g){if(!(o==null||typeof o=="boolean")){if(Array.isArray(o)){const b=this.beginRenderNode(0,\`array:\${p}\`);try{const E=g===void 0?-1:(0,h.getSinglePotentialHostRootIndex)(o);let k=0;for(const j of o)this.renderValue(j,P(j,k),k===E?g:void 0),k++}finally{this.endRenderNode(b)}return}if((0,e.isDILRuntimeElement)(o)){this.renderRuntimeElement(o,p,g);return}if(typeof o=="function"){const b=this.resolveComponent(o);this.renderComponent(b,void 0,[],this.getComponentNodeKey(b,p),void 0,void 0);return}this.renderText(String(o),\`t:\${p}\`)}}renderRuntimeElement(o,p,g){const b=o.type,E=(0,e.readRuntimeElementKey)(o),k=g??E;if(b===e.DIL_FRAGMENT){this.renderFragment(o.children,p,k);return}const j=E===void 0?p:\`k:\${typeof E}:\${String(E)}\`;if(typeof b=="function"){const L=this.resolveComponent(b);this.renderComponent(L,o.props,o.children,this.getComponentNodeKey(L,j),E===void 0?void 0:this.getComponentStateIdentity(L,E),k);return}this.renderElement(b,o.props,o.children,\`e:\${b}:\${j}\`,k)}renderFragment(o,p,g){const b=g===void 0?-1:(0,h.getSinglePotentialHostRootIndex)(o);let E=0;for(const k of o)this.renderValue(k,N(k,E,p),E===b?g:void 0),E++}renderChildren(o){let p=0;for(const g of o)this.renderValue(g,P(g,p),void 0),p++}renderComponent(o,p,g,b,E,k){var j,L,O;const W=this.beginRenderNode(1,b);W.hookFrame.stateIdentity=this.resolveComponentStateIdentity(E,W,b);const A=(L=(j=this.pendingEffects)===null||j===void 0?void 0:j.length)!==null&&L!==void 0?L:0,q=this.interactionScope;this.interactionScope=(O=this.resolvedComponentScopes.get(o))!==null&&O!==void 0?O:q;try{const F=o((0,e.propsWithChildren)(p,g));this.renderValue(F,"rendered",k)}catch(F){this.discardPendingEffectsFrom(A),this.reportSubtreeError(F)}finally{this.interactionScope=q,this.endRenderNode(W)}}resolveComponent(o){const p=(0,e.getDilComponentResolver)(o);if(p===void 0)return o;let g=this.resolvedComponents[o.name];if(g===void 0){g=p(this.widgetRuntimeApiFacade,this.jsxRuntimeFacade,this.genUIFacade),this.resolvedComponents[o.name]=g;const b=(0,e.getDilComponentScope)(o);b!==void 0&&this.resolvedComponentScopes.set(g,b)}return g}renderElement(o,p,g,b,E){var k;const j=this.elementsMetadata[o];if(j===void 0){this.reportSubtreeError(new Error(\`Unknown DIL element type "\${o}".\`));return}let L;try{L=j.renderedPropNames!==void 0&&p!==void 0?this.resolveRenderableProps(j.renderedPropNames,p):void 0}catch(W){this.reportSubtreeError(W);return}const O=this.beginRenderNode(2,b);try{let W=!0,A,q;switch(j.childrenMode){case l.DILElementChildrenMode.RenderedNodes:break;case l.DILElementChildrenMode.PrimitiveText:{q=H(g),W=q===void 0;break}case l.DILElementChildrenMode.ResolvedValues:break;case l.DILElementChildrenMode.OpaqueTree:W=!1,A=this.renderOpaqueChildren(g);break}const F=L===void 0?p:L.props;O.elementOutput={interactionScope:this.interactionScope,metadata:j,opaqueChildren:A,primitiveTextValue:q,props:j.semanticKeyPropName===void 0?F:Object.assign(Object.assign({},F),{[j.semanticKeyPropName]:E})};const B=this.getRenderedElement(O);B.lastResolvedRenderId=this.renderId,B.resolvedParent=this.renderedParentStack[this.renderedParentStack.length-1],this.renderedParentStack.push(B);try{if(L!==void 0)for(const v of L.elements)this.renderRuntimeElement(v,\`prop:\${JSON.stringify([(k=v.props)===null||k===void 0?void 0:k[e.DIL_RENDERED_PROP_NAME]])}\`,void 0);W&&this.renderChildren(g)}finally{this.renderedParentStack.pop()}}catch(W){this.reportSubtreeError(W)}finally{this.endRenderNode(O)}}resolveRenderableProps(o,p){let g;for(const b of o){const E=p[b];(0,e.isDILRuntimeElement)(E)&&(g=g??{elements:[],props:Object.assign({},p)},delete g.props[b],g.elements.push((0,e.createDilElement)(e.DIL_RENDERED_PROP_ELEMENT_TYPE,{[e.DIL_RENDERED_PROP_NAME]:b},[E])))}return g}renderText(o,p){const g=this.beginRenderNode(5,p);try{g.textOutput=o;const b=this.getRenderedText(g);b.lastResolvedRenderId=this.renderId,b.resolvedParent=this.renderedParentStack[this.renderedParentStack.length-1]}finally{this.endRenderNode(g)}}renderOpaqueChildren(o){const p=[];let g=0;for(const b of o)this.renderOpaqueValue(b,P(b,g),p,void 0),g++;return p}renderOpaqueValue(o,p,g,b){if(!(o==null||typeof o=="boolean")){if(Array.isArray(o)){const E=this.beginRenderNode(0,\`opaque-array:\${p}\`);try{const k=b===void 0?-1:(0,h.getSinglePotentialHostRootIndex)(o);let j=0;for(const L of o)this.renderOpaqueValue(L,P(L,j),g,j===k?b:void 0),j++}finally{this.endRenderNode(E)}return}if((0,e.isDILRuntimeElement)(o)){this.renderOpaqueRuntimeElement(o,p,g,b);return}if(typeof o=="function"){const E=this.resolveComponent(o);this.renderOpaqueComponent(E,void 0,[],this.getComponentNodeKey(E,p),void 0,g,void 0);return}if(typeof o=="string"||typeof o=="number"){g.push(o);return}g.push(String(o))}}renderOpaqueRuntimeElement(o,p,g,b){var E;const k=o.type,j=(0,e.readRuntimeElementKey)(o),L=b??j;if(k===e.DIL_FRAGMENT){this.renderOpaqueFragment(o.children,p,g,L);return}const O=j===void 0?p:\`k:\${typeof j}:\${String(j)}\`;if(typeof k=="function"){const A=this.resolveComponent(k);this.renderOpaqueComponent(A,o.props,o.children,this.getComponentNodeKey(A,O),j===void 0?void 0:this.getComponentStateIdentity(A,j),g,L);return}const W=this.beginRenderNode(3,\`opaque-element:\${k}:\${O}\`);try{const A=this.elementsMetadata[k],q=A?.semanticKeyPropName;let F=f(o.props);for(const B of(E=A?.renderedPropNames)!==null&&E!==void 0?E:[]){const v=F[B];if((0,e.isDILRuntimeElement)(v)){const I=[];this.renderOpaqueValue(v,\`opaque-prop:\${JSON.stringify(B)}\`,I,void 0),F=Object.assign(Object.assign({},F),{[B]:I.length===0?null:I.length===1?I[0]:I})}}g.push({type:k,props:q===void 0?F:Object.assign(Object.assign({},F),{[q]:L}),children:this.renderOpaqueChildren(o.children)})}finally{this.endRenderNode(W)}}renderOpaqueFragment(o,p,g,b){const E=b===void 0?-1:(0,h.getSinglePotentialHostRootIndex)(o);let k=0;for(const j of o)this.renderOpaqueValue(j,N(j,k,p),g,k===E?b:void 0),k++}renderOpaqueComponent(o,p,g,b,E,k,j){var L,O;const W=this.beginRenderNode(1,b);W.hookFrame.stateIdentity=this.resolveComponentStateIdentity(E,W,b);const A=k.length,q=(O=(L=this.pendingEffects)===null||L===void 0?void 0:L.length)!==null&&O!==void 0?O:0;try{const F=o((0,e.propsWithChildren)(p,g));this.renderOpaqueValue(F,"rendered",k,j)}catch(F){k.length=A,this.discardPendingEffectsFrom(q),this.reportSubtreeError(F)}finally{this.endRenderNode(W)}}reportSubtreeError(o){this.errorMode===l.DILRenderErrorMode.ReportAndAbortRender&&(this.renderFailed=!0),this.errorReporter.reportError((0,m.toError)(o))}reportError(o){this.renderFailed=!0,this.errorReporter.reportError((0,m.toError)(o))}getHookFrame(o){if(o.hookFrame!==void 0)return o.hookFrame;const p={id:this.nextFrameId,isMounted:!0,hookIndex:0,hooks:[],stateIdentity:void 0};return this.nextFrameId++,o.hookFrame=p,p}getFunctionId(o){var p;const g=o,b=g[x];if(b!==void 0)return b;const E=this.claimStableFunctionIdentity(o.name),k=(p=E?.id)!==null&&p!==void 0?p:n++;return Object.defineProperty(g,x,{value:k}),k}claimStableFunctionIdentity(o){if(o!==""){const g=this.namedFunctionIdentities.get(o);if(g===void 0){const b=this.createStableFunctionIdentity();return this.namedFunctionIdentities.set(o,b),b}return g.claimedGeneration!==this.sourceGeneration?(g.claimedGeneration=this.sourceGeneration,g):void 0}const p=this.firstAnonymousFunctionIdentity;if(p===void 0){const g=this.createStableFunctionIdentity();return this.firstAnonymousFunctionIdentity=g,g}if(p.claimedGeneration!==this.sourceGeneration)return p.claimedGeneration=this.sourceGeneration,p}createStableFunctionIdentity(){return{id:n++,claimedGeneration:this.sourceGeneration}}getComponentNodeKey(o,p){return\`c:\${this.getFunctionId(o)}:\${p}\`}getComponentStateIdentity(o,p){const g=\`\${typeof p}:\${String(p)}\`;let b=1;for(const[E,k]of this.keyedComponents)k===o&&\`\${typeof E}:\${String(E)}\`<g&&b++;return{key:p,nextStateSlot:0,ownerKey:g,siblingOrdinal:b}}resolveComponentStateIdentity(o,p,g){return o===void 0||p.key===g?o:{key:o.key,nextStateSlot:0,ownerKey:\`\${o.ownerKey}\\0\${p.key}\`,siblingOrdinal:o.siblingOrdinal}}registerKeyedComponent(o){const p=(0,e.readRuntimeElementKey)(o);p!==void 0&&typeof o.type=="function"&&this.keyedComponents.set(p,this.resolveComponent(o.type))}getRenderedRootIdentity(o){if((0,e.isDILRuntimeElement)(o)){const p=(0,e.readRuntimeElementKey)(o),g=p===void 0?"":\`\${typeof p}:\${String(p)}\`;return typeof o.type=="function"?\`component:\${this.getFunctionId(this.resolveComponent(o.type))}:\${g}\`:\`element:\${String(o.type)}:\${g}\`}return typeof o=="function"?\`component:\${this.getFunctionId(this.resolveComponent(o))}\`:Array.isArray(o)?"array":typeof o}requireCurrentHookFrame(o){const p=this.nodeStack[this.nodeStack.length-1],g=p?.hookFrame;if(g===void 0)throw new Error(\`DIL.\${o} can only be called while rendering a DIL component.\`);return g}beginRenderNode(o,p){const g=this.getCurrentRenderNode(),b=this.resolveRenderNode(g,o,p,void 0);if(o===1){const E=this.getHookFrame(b);E.hookIndex=0}else b.hookFrame=g.hookFrame;return this.pushRenderNode(b),b}pushRenderNode(o){o.children!==void 0&&(o.children.insertionIndex=0),o.lastRenderId=this.renderId,this.nodeStack.push(o)}endRenderNode(o){if(this.nodeStack.pop()!==o)throw new Error("Unbalanced DIL render node stack.");this.processChildrenUpdate(o)}getCurrentRenderNode(){const o=this.nodeStack[this.nodeStack.length-1];if(o===void 0)throw new Error("Unbalanced DIL render node stack.");return o}resolveRenderNode(o,p,g,b){const E=b===void 0?g:\`\${g}-\${b}\`;let k,j=o.children;if(j===void 0?(j={childByKey:{},children:[],insertionIndex:0},o.children=j):k=j.childByKey[E],k===void 0)k={key:E,kind:p,lastRenderId:this.renderId,parent:o,parentIndex:0},j.childByKey[E]=k;else if(k.kind!==p||k.lastRenderId===this.renderId){const L=j.insertionIndex-k.parentIndex+1;return this.resolveRenderNode(o,p,g,L)}return this.insertRenderNodeInParent(k,j),k}insertRenderNodeInParent(o,p){const g=p.insertionIndex;if(p.insertionIndex++,o.parentIndex=g,p.children!==p.previousChildren){p.children.push(o);return}if(p.children[g]!==o){const b=p.children.slice(0,g);b.push(o),p.children=b}}processChildrenUpdate(o){const p=o.children;if(p===void 0)return;if(p.children===p.previousChildren){const b=p.insertionIndex;if(b===p.children.length)return;p.children=p.children.slice(0,b)}const g=p.previousChildren;if(g!==void 0)for(const b of g)b.lastRenderId!==this.renderId&&(delete p.childByKey[b.key],this.destroyRenderNode(b));p.previousChildren=p.children}destroyRenderNode(o){const p=o.renderedNode;if(p?.committed&&this.pendingDestroyedNodes.push(p),o.kind===1&&o.hookFrame!==void 0){o.hookFrame.isMounted=!1;for(const b of o.hookFrame.hooks)b.kind===0&&b.cleanup!==void 0?(this.enqueueUnmountCleanup(b.cleanup),b.cleanup=void 0):b.kind===3?b.messenger.dispose():b.kind===6||b.kind===7?b.owner.dispose():b.kind===5&&this.statePersistence.releaseStateHook(b)}o.hookFrame=void 0;const g=o.children;if(g!==void 0){for(const b of g.children)this.destroyRenderNode(b);o.children=void 0}}applyStateSnapshotToMountedHooks(o,p){let g=!1;if(o.kind===1&&o.hookFrame!==void 0)for(const E of o.hookFrame.hooks)E.kind===5&&E.widgetId===p&&this.statePersistence.applySnapshotToHook(E)&&(g=!0);const b=o.children;if(b!==void 0)for(const E of b.children)this.applyStateSnapshotToMountedHooks(E,p)&&(g=!0);return g}commitUpdates(){for(const p of this.pendingDestroyedNodes)this.delegate.onNodeDestroyed(p.id),p.committed=!1;this.pendingDestroyedNodes.length=0,this.commitChildUpdates(void 0,this.committedRootChildren,this.nextRootChildren,this.rootNode);const o=this.committedRootChildren;this.committedRootChildren=this.nextRootChildren,this.nextRootChildren=o,this.nextRootChildren.length=0}commitChildUpdates(o,p,g,b){let E=0,k=0;this.forEachDirectRenderedChild(b,j=>{var L;const O=j.renderedNode;for(;E<p.length&&(p[E].lastResolvedRenderId!==this.renderId||p[E].resolvedParent!==o);)E++;if(this.emitRenderedNodeChanges(O,j),O!==p[E]?this.delegate.onNodeMoved(O.id,(L=o?.id)!==null&&L!==void 0?L:0,k):E++,g.push(O),O.kind===2){this.commitChildUpdates(O,O.children,O.nextChildren,j);const W=O.children;O.children=O.nextChildren,O.nextChildren=W,O.nextChildren.length=0}k++})}emitRenderedNodeChanges(o,p){var g,b,E;if(o.kind===5)this.emitRenderedTextChanges(o,p.textOutput);else{this.emitRenderedElementChanges(o,p.elementOutput);const k=(g=p.elementOutput)===null||g===void 0?void 0:g.interactionScope;o.interactionScope!==k&&((E=(b=this.delegate).onNodeInteractionScopeChanged)===null||E===void 0||E.call(b,o.id,k),o.interactionScope=k)}}emitRenderedElementChanges(o,p){var g;const b=o.metadata,E=p.props,k=b.childrenMode===l.DILElementChildrenMode.PrimitiveText?b.primitiveTextProp:void 0;if(!o.committed)this.delegate.onElementNodeCreated(o.id,b.typeId);else for(const L of o.propNames)L==="key"||L===k||E?.[L]===void 0&&o.props[L]!==void 0&&(this.delegate.onNodePropChanged(o.id,L,void 0),o.props[L]=void 0);const j=E===void 0?_:Object.keys(E);if(o.propNames=j,E!==void 0)for(const L of j){if(L==="key"||L===k)continue;const O=E[L];(!o.committed||o.props[L]!==O)&&(this.delegate.onNodePropChanged(o.id,L,O),o.props[L]=O)}if(b.childrenMode===l.DILElementChildrenMode.PrimitiveText){const L=b.primitiveTextProp,O=(g=p.primitiveTextValue)!==null&&g!==void 0?g:E?.[L];o.props[L]!==O&&this.delegate.onNodePropChanged(o.id,L,O),o.props[L]=O}if(b.childrenMode===l.DILElementChildrenMode.OpaqueTree){const L=p.opaqueChildren;(!o.committed||!y(o.opaqueChildren,L))&&this.delegate.onNodeOpaqueChildrenChanged(o.id,L),o.opaqueChildren=L}o.committed=!0}emitRenderedTextChanges(o,p){if(!o.committed){this.delegate.onTextNodeCreated(o.id,p),o.value=p,o.committed=!0;return}o.value!==p&&(this.delegate.onTextNodeChanged(o.id,p),o.value=p)}getRenderedElement(o){const p=o.renderedNode;if(p!==void 0)return p;const g={id:this.nextNodeId++,kind:2,metadata:o.elementOutput.metadata,children:[],committed:!1,lastResolvedRenderId:0,nextChildren:[],opaqueChildren:void 0,props:{},propNames:_,resolvedParent:void 0};return o.renderedNode=g,g}getRenderedText(o){const p=o.renderedNode;if(p!==void 0)return p;const g={id:this.nextNodeId++,kind:5,committed:!1,lastResolvedRenderId:0,resolvedParent:void 0,value:""};return o.renderedNode=g,g}forEachDirectRenderedChild(o,p){const g=o.children;if(g!==void 0)for(const b of g.children)b.kind===2||b.kind===5?p(b):this.forEachDirectRenderedChild(b,p)}scheduleRender(){this.scheduler.scheduleRender()}enqueuePendingEffect(o){this.pendingEffects===void 0&&(this.pendingEffects=[]),this.pendingEffects.push(o)}discardPendingEffectsFrom(o){if(this.pendingEffects!==void 0){for(let p=this.pendingEffects.length-1;p>=o;p--){const g=this.pendingEffects[p];g.hook.deps=g.previousDeps}this.pendingEffects.length=o}}enqueueUnmountCleanup(o){this.unmountCleanups===void 0&&(this.unmountCleanups=[]),this.unmountCleanups.push(o)}scheduleEffectFlush(o){const p=this.pendingEffects,g=this.unmountCleanups,b=()=>{const E=this.isFlushingEffects;this.isFlushingEffects=!0;try{if(g!==void 0)for(const k of g)(0,r.runCleanup)(k,this.errorReporter);if(p!==void 0)for(const k of p){k.hook.cleanup!==void 0&&((0,r.runCleanup)(k.hook.cleanup,this.errorReporter),k.hook.cleanup=void 0);try{const j=k.effect();k.hook.cleanup=typeof j=="function"?j:void 0}catch(j){this.reportError(j)}}o?.()}finally{this.isFlushingEffects=E}};this.scheduler.scheduleFlush(b)}}t.DILRenderFunctionRuntime=c;function f(D){const o={};if(D!==void 0)for(const p in D)p!=="key"&&(o[p]=D[p]);return o}function y(D,o){if(D===void 0||D.length!==o.length)return!1;for(let p=0;p<D.length;p++){const g=D[p],b=o[p];if(typeof g!="object"||typeof b!="object"){if(g!==b)return!1;continue}if(g.type!==b.type||!w(g.props,b.props)||!y(g.children,b.children))return!1}return!0}function w(D,o){const p=Object.keys(D),g=Object.keys(o);if(p.length!==g.length)return!1;for(const b of p)if(D[b]!==o[b])return!1;return!0}function P(D,o){if((0,e.isDILRuntimeElement)(D)&&D.type!==e.DIL_FRAGMENT){const p=(0,e.readRuntimeElementKey)(D);if(p!==void 0)return\`k:\${typeof p}:\${String(p)}\`}return\`i:\${o}\`}function N(D,o,p){return o===0?p:\`f:\${p}:\${P(D,o)}\`}function H(D){if(D.length===0)return;let o="";for(const p of D)if(!(p==null||typeof p=="boolean")){if(typeof p!="string"&&typeof p!="number")return;o+=String(p)}return o}})(gt,gt.exports)),gt.exports}var kt={exports:{}},Ut={exports:{}},xe;function rn(){return xe||(xe=1,(function(a,t){a.path="dil_renderer/src/DILHtmlViewMessengerTransportRegistry",Object.defineProperty(t,"__esModule",{value:!0}),t.DILHtmlViewMessengerTransportRegistry=void 0;const e=Tt();class r{constructor(i){this.errorReporter=i,this.htmlViewMessengerChannelIndex=0,this.htmlViewMessengerTransports=new Map,this.queuedHtmlViewMessengerMessages=new Map}register(i,u){return this.htmlViewMessengerTransports.set(i,u),this.flushQueuedHtmlViewMessengerMessages(i,u),()=>{this.htmlViewMessengerTransports.get(i)===u&&this.htmlViewMessengerTransports.delete(i)}}nextChannelId(){const i=\`dil_html_view_messenger_\${this.htmlViewMessengerChannelIndex}\`;return this.htmlViewMessengerChannelIndex++,i}sendCommand(i,u,d){const s=this.htmlViewMessengerTransports.get(i);if(s===void 0)return new Promise((m,h)=>{this.queueHtmlViewMessengerMessage(i,{data:d,kind:0,reject:h,resolve:m,type:u})});try{return Promise.resolve(s.command(u,d))}catch(m){return Promise.reject(m)}}emitEvent(i,u,d){const s=this.htmlViewMessengerTransports.get(i);if(s===void 0){this.queueHtmlViewMessengerMessage(i,{data:d,kind:1,type:u});return}s.event(u,d)}queueHtmlViewMessengerMessage(i,u){var d;const s=(d=this.queuedHtmlViewMessengerMessages.get(i))!==null&&d!==void 0?d:[];s.push(u),this.queuedHtmlViewMessengerMessages.set(i,s)}flushQueuedHtmlViewMessengerMessages(i,u){const d=this.queuedHtmlViewMessengerMessages.get(i);if(d!==void 0){this.queuedHtmlViewMessengerMessages.delete(i);for(const s of d)if(s.kind===0)try{Promise.resolve(u.command(s.type,s.data)).then(s.resolve,s.reject)}catch(m){s.reject(m)}else try{u.event(s.type,s.data)}catch(m){this.errorReporter.reportError((0,e.toError)(m))}}}}t.DILHtmlViewMessengerTransportRegistry=r})(Ut,Ut.exports)),Ut.exports}var Re;function sn(){return Re||(Re=1,(function(a,t){a.path="dil_renderer/src/DILRendererHtmlViewMessengerState",Object.defineProperty(t,"__esModule",{value:!0}),t.DILRendererHtmlViewMessengerState=void 0;const e=rn();class r{constructor(i){this.receivers=new Map,this.transports=new e.DILHtmlViewMessengerTransportRegistry(i)}registerReceiver(i,u){return this.receivers.set(i,u),()=>{this.receivers.get(i)===u&&this.receivers.delete(i)}}registerTransport(i,u){return this.transports.register(i,u)}receiveCommand(i,u,d){const s=this.receivers.get(i);if(s===void 0)throw new Error(\`Unknown DIL html-view messenger channel "\${i}"\`);return s.command(u,d)}receiveEvent(i,u,d){var s;(s=this.receivers.get(i))===null||s===void 0||s.event(u,d)}nextChannelId(){return this.transports.nextChannelId()}sendCommand(i,u,d){return this.transports.sendCommand(i,u,d)}emitEvent(i,u,d){this.transports.emitEvent(i,u,d)}}t.DILRendererHtmlViewMessengerState=r})(kt,kt.exports)),kt.exports}var Ce;function qt(){return Ce||(Ce=1,(function(a,t){a.path="dil_renderer/src/DILRenderer",Object.defineProperty(t,"__esModule",{value:!0}),t.DILRenderer=t.DILElementRenderNodeKind=t.DILElementChildrenMode=t.DILSkippedChildError=t.DILSkippedChildReason=t.DILRenderErrorMode=t.DILStreamingAnimation=void 0;const e=on(),r=ve(),l=sn();var i;(function(_){_[_.Disabled=0]="Disabled",_[_.Normal=1]="Normal",_[_.Snappy=2]="Snappy",_[_.Neutral=3]="Neutral"})(i||(t.DILStreamingAnimation=i={}));var u;(function(_){_[_.ReportAndAbortRender=0]="ReportAndAbortRender",_[_.ReportAndSkipSubtree=1]="ReportAndSkipSubtree"})(u||(t.DILRenderErrorMode=u={}));var d;(function(_){_.UnregisteredElement="unregistered-element",_.MissingRetainedNode="missing-retained-node",_.NodeIdentityMismatch="node-identity-mismatch"})(d||(t.DILSkippedChildReason=d={}));class s extends Error{constructor(n,c){super(\`Skipped invalid DIL selected child (\${n}).\`),this.reason=n,this.parentNodeType=c,Object.setPrototypeOf(this,s.prototype),this.name="DILSkippedChildError"}}t.DILSkippedChildError=s;var m;(function(_){_[_.RenderedNodes=0]="RenderedNodes",_[_.PrimitiveText=1]="PrimitiveText",_[_.ResolvedValues=2]="ResolvedValues",_[_.OpaqueTree=3]="OpaqueTree"})(m||(t.DILElementChildrenMode=m={}));var h;(function(_){_[_.Element=0]="Element",_[_.Text=1]="Text"})(h||(t.DILElementRenderNodeKind=h={}));class x{constructor(n){this.options=n,this.runtimeHtmlViewMessenger={emitHtmlViewMessengerEvent:(c,f,y)=>{this.emitHtmlViewMessengerEvent(c,f,y)},nextHtmlViewMessengerChannelId:()=>this.nextHtmlViewMessengerChannelId(),registerHtmlViewMessengerReceiver:(c,f)=>this.registerDILHtmlViewMessengerReceiver(c,f),registerHtmlViewMessengerTransport:(c,f)=>this.registerDILHtmlViewMessengerTransport(c,f),sendHtmlViewMessengerCommand:(c,f,y)=>this.sendHtmlViewMessengerCommand(c,f,y)}}createRenderFunction(n){const c=this.createRenderContext(void 0,u.ReportAndAbortRender);return c.updateSource(n),(f,y,w,P)=>{c.render(f,y,w,P),c.didLastRenderFail()||c.commitStateSnapshot()}}createRenderContext(n,c){const f=new e.DILRenderFunctionRuntime(this.options.elementsMetadata,this.options.delegate,this.options.errorReporter,c,this.runtimeHtmlViewMessenger,this.options.scheduler,this.options.trace,(0,r.createDILDateConstructor)(n),n,this.options.genUI,this.options.stateChangeHandler,this.options.speechSynthesis,this.options.dictation,this.options.sourceEvaluatorFactory);return{render:(y,w,P,N)=>{this.options.trace("DILRenderer.render",()=>{var H;f.render(y,(H=N.constants)!==null&&H!==void 0?H:{},w,P)})},commitStateSnapshot:()=>{f.commitStateSnapshot()},didLastRenderFail:()=>f.didLastRenderFail(),setStateSnapshot:(y,w)=>f.setStateSnapshot(y,w),updateSource:y=>{f.evaluate(y)},clearRenderedRoot:()=>{f.clearRenderedRoot()},dispose:()=>{f.dispose()}}}registerDILHtmlViewMessengerTransport(n,c){return this.getHtmlViewMessengerState().registerTransport(n,c)}registerDILHtmlViewMessengerReceiver(n,c){return this.getHtmlViewMessengerState().registerReceiver(n,c)}receiveDILHtmlViewMessengerCommand(n,c,f){const y=this.htmlViewMessengerState;if(y===void 0)throw new Error(\`Unknown DIL html-view messenger channel "\${n}"\`);return y.receiveCommand(n,c,f)}receiveDILHtmlViewMessengerEvent(n,c,f){var y;(y=this.htmlViewMessengerState)===null||y===void 0||y.receiveEvent(n,c,f)}nextHtmlViewMessengerChannelId(){return this.getHtmlViewMessengerState().nextChannelId()}sendHtmlViewMessengerCommand(n,c,f){return this.getHtmlViewMessengerState().sendCommand(n,c,f)}emitHtmlViewMessengerEvent(n,c,f){this.getHtmlViewMessengerState().emitEvent(n,c,f)}getHtmlViewMessengerState(){var n;const c=(n=this.htmlViewMessengerState)!==null&&n!==void 0?n:new l.DILRendererHtmlViewMessengerState(this.options.errorReporter);return this.htmlViewMessengerState=c,c}}t.DILRenderer=x})(ht,ht.exports)),ht.exports}var Ee=qt(),Lt={exports:{}},Bt={exports:{}},we;function an(){return we||(we=1,(function(a){a.path="valdi_core/src/tslib.js";var t,e,r,l,i,u,d,s,m,h,x,_,n,c,f,y,w,P,N,H,D,o,p,g,b,E,k,j,L,O,W;(function(A){var q=typeof ne=="object"?ne:typeof self=="object"?self:typeof this=="object"?this:{};A(F(q,F(a.exports)));function F(B,v){return B!==q&&(typeof Object.create=="function"?Object.defineProperty(B,"__esModule",{value:!0}):B.__esModule=!0),function(I,R){return B[I]=v?v(I,R):R}}})(function(A){var q=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(v,I){v.__proto__=I}||function(v,I){for(var R in I)Object.prototype.hasOwnProperty.call(I,R)&&(v[R]=I[R])};t=function(v,I){if(typeof I!="function"&&I!==null)throw new TypeError("Class extends value "+String(I)+" is not a constructor or null");q(v,I);function R(){this.constructor=v}v.prototype=I===null?Object.create(I):(R.prototype=I.prototype,new R)},e=Object.assign||function(v){for(var I,R=1,C=arguments.length;R<C;R++){I=arguments[R];for(var U in I)Object.prototype.hasOwnProperty.call(I,U)&&(v[U]=I[U])}return v},r=function(v,I){var R={};for(var C in v)Object.prototype.hasOwnProperty.call(v,C)&&I.indexOf(C)<0&&(R[C]=v[C]);if(v!=null&&typeof Object.getOwnPropertySymbols=="function")for(var U=0,C=Object.getOwnPropertySymbols(v);U<C.length;U++)I.indexOf(C[U])<0&&Object.prototype.propertyIsEnumerable.call(v,C[U])&&(R[C[U]]=v[C[U]]);return R},l=function(v,I,R,C){var U=arguments.length,S=U<3?I:C===null?C=Object.getOwnPropertyDescriptor(I,R):C,z;if(typeof Reflect=="object"&&typeof Reflect.decorate=="function")S=Reflect.decorate(v,I,R,C);else for(var M=v.length-1;M>=0;M--)(z=v[M])&&(S=(U<3?z(S):U>3?z(I,R,S):z(I,R))||S);return U>3&&S&&Object.defineProperty(I,R,S),S},i=function(v,I){return function(R,C){I(R,C,v)}},u=function(v,I,R,C,U,S){function z(pt){if(pt!==void 0&&typeof pt!="function")throw new TypeError("Function expected");return pt}for(var M=C.kind,K=M==="getter"?"get":M==="setter"?"set":"value",G=!I&&v?C.static?v:v.prototype:null,V=I||(G?Object.getOwnPropertyDescriptor(G,C.name):{}),$,T=!1,Y=R.length-1;Y>=0;Y--){var et={};for(var nt in C)et[nt]=nt==="access"?{}:C[nt];for(var nt in C.access)et.access[nt]=C.access[nt];et.addInitializer=function(pt){if(T)throw new TypeError("Cannot add initializers after decoration has completed");S.push(z(pt||null))};var it=(0,R[Y])(M==="accessor"?{get:V.get,set:V.set}:V[K],et);if(M==="accessor"){if(it===void 0)continue;if(it===null||typeof it!="object")throw new TypeError("Object expected");($=z(it.get))&&(V.get=$),($=z(it.set))&&(V.set=$),($=z(it.init))&&U.unshift($)}else($=z(it))&&(M==="field"?U.unshift($):V[K]=$)}G&&Object.defineProperty(G,C.name,V),T=!0},d=function(v,I,R){for(var C=arguments.length>2,U=0;U<I.length;U++)R=C?I[U].call(v,R):I[U].call(v);return C?R:void 0},s=function(v){return typeof v=="symbol"?v:"".concat(v)},m=function(v,I,R){return typeof I=="symbol"&&(I=I.description?"[".concat(I.description,"]"):""),Object.defineProperty(v,"name",{configurable:!0,value:R?"".concat(R," ",I):I})},h=function(v,I){if(typeof Reflect=="object"&&typeof Reflect.metadata=="function")return Reflect.metadata(v,I)},x=function(v,I,R,C){function U(S){return S instanceof R?S:new R(function(z){z(S)})}return new(R||(R=Promise))(function(S,z){function M(V){try{G(C.next(V))}catch($){z($)}}function K(V){try{G(C.throw(V))}catch($){z($)}}function G(V){V.done?S(V.value):U(V.value).then(M,K)}G((C=C.apply(v,I||[])).next())})},_=function(v,I){var R={label:0,sent:function(){if(S[0]&1)throw S[1];return S[1]},trys:[],ops:[]},C,U,S,z;return z={next:M(0),throw:M(1),return:M(2)},typeof Symbol=="function"&&(z[Symbol.iterator]=function(){return this}),z;function M(G){return function(V){return K([G,V])}}function K(G){if(C)throw new TypeError("Generator is already executing.");for(;z&&(z=0,G[0]&&(R=0)),R;)try{if(C=1,U&&(S=G[0]&2?U.return:G[0]?U.throw||((S=U.return)&&S.call(U),0):U.next)&&!(S=S.call(U,G[1])).done)return S;switch(U=0,S&&(G=[G[0]&2,S.value]),G[0]){case 0:case 1:S=G;break;case 4:return R.label++,{value:G[1],done:!1};case 5:R.label++,U=G[1],G=[0];continue;case 7:G=R.ops.pop(),R.trys.pop();continue;default:if(S=R.trys,!(S=S.length>0&&S[S.length-1])&&(G[0]===6||G[0]===2)){R=0;continue}if(G[0]===3&&(!S||G[1]>S[0]&&G[1]<S[3])){R.label=G[1];break}if(G[0]===6&&R.label<S[1]){R.label=S[1],S=G;break}if(S&&R.label<S[2]){R.label=S[2],R.ops.push(G);break}S[2]&&R.ops.pop(),R.trys.pop();continue}G=I.call(v,R)}catch(V){G=[6,V],U=0}finally{C=S=0}if(G[0]&5)throw G[1];return{value:G[0]?G[1]:void 0,done:!0}}},n=function(v,I){for(var R in v)R!=="default"&&!Object.prototype.hasOwnProperty.call(I,R)&&L(I,v,R)},L=Object.create?(function(v,I,R,C){C===void 0&&(C=R);var U=Object.getOwnPropertyDescriptor(I,R);(!U||("get"in U?!I.__esModule:U.writable||U.configurable))&&(U={enumerable:!0,get:function(){return I[R]}}),Object.defineProperty(v,C,U)}):(function(v,I,R,C){C===void 0&&(C=R),v[C]=I[R]}),c=function(v){var I=typeof Symbol=="function"&&Symbol.iterator,R=I&&v[I],C=0;if(R)return R.call(v);if(v&&typeof v.length=="number")return{next:function(){return v&&C>=v.length&&(v=void 0),{value:v&&v[C++],done:!v}}};throw new TypeError(I?"Object is not iterable.":"Symbol.iterator is not defined.")},f=function(v,I){var R=typeof Symbol=="function"&&v[Symbol.iterator];if(!R)return v;var C=R.call(v),U,S=[],z;try{for(;(I===void 0||I-- >0)&&!(U=C.next()).done;)S.push(U.value)}catch(M){z={error:M}}finally{try{U&&!U.done&&(R=C.return)&&R.call(C)}finally{if(z)throw z.error}}return S},y=function(){for(var v=[],I=0;I<arguments.length;I++)v=v.concat(f(arguments[I]));return v},w=function(){for(var v=0,I=0,R=arguments.length;I<R;I++)v+=arguments[I].length;for(var C=Array(v),U=0,I=0;I<R;I++)for(var S=arguments[I],z=0,M=S.length;z<M;z++,U++)C[U]=S[z];return C},P=function(v,I,R){if(R||arguments.length===2)for(var C=0,U=I.length,S;C<U;C++)(S||!(C in I))&&(S||(S=Array.prototype.slice.call(I,0,C)),S[C]=I[C]);return v.concat(S||Array.prototype.slice.call(I))},N=function(v){return this instanceof N?(this.v=v,this):new N(v)},H=function(v,I,R){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var C=R.apply(v,I||[]),U,S=[];return U={},z("next"),z("throw"),z("return"),U[Symbol.asyncIterator]=function(){return this},U;function z(T){C[T]&&(U[T]=function(Y){return new Promise(function(et,nt){S.push([T,Y,et,nt])>1||M(T,Y)})})}function M(T,Y){try{K(C[T](Y))}catch(et){$(S[0][3],et)}}function K(T){T.value instanceof N?Promise.resolve(T.value.v).then(G,V):$(S[0][2],T)}function G(T){M("next",T)}function V(T){M("throw",T)}function $(T,Y){T(Y),S.shift(),S.length&&M(S[0][0],S[0][1])}},D=function(v){var I,R;return I={},C("next"),C("throw",function(U){throw U}),C("return"),I[Symbol.iterator]=function(){return this},I;function C(U,S){I[U]=v[U]?function(z){return(R=!R)?{value:N(v[U](z)),done:!1}:S?S(z):z}:S}},o=function(v){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var I=v[Symbol.asyncIterator],R;return I?I.call(v):(v=typeof c=="function"?c(v):v[Symbol.iterator](),R={},C("next"),C("throw"),C("return"),R[Symbol.asyncIterator]=function(){return this},R);function C(S){R[S]=v[S]&&function(z){return new Promise(function(M,K){z=v[S](z),U(M,K,z.done,z.value)})}}function U(S,z,M,K){Promise.resolve(K).then(function(G){S({value:G,done:M})},z)}},p=function(v,I){return Object.defineProperty?Object.defineProperty(v,"raw",{value:I}):v.raw=I,v};var F=Object.create?(function(v,I){Object.defineProperty(v,"default",{enumerable:!0,value:I})}):function(v,I){v.default=I};g=function(v){if(v&&v.__esModule)return v;var I={};if(v!=null)for(var R in v)R!=="default"&&Object.prototype.hasOwnProperty.call(v,R)&&L(I,v,R);return F(I,v),I},b=function(v){return v&&v.__esModule?v:{default:v}},E=function(v,I,R,C){if(R==="a"&&!C)throw new TypeError("Private accessor was defined without a getter");if(typeof I=="function"?v!==I||!C:!I.has(v))throw new TypeError("Cannot read private member from an object whose class did not declare it");return R==="m"?C:R==="a"?C.call(v):C?C.value:I.get(v)},k=function(v,I,R,C,U){if(C==="m")throw new TypeError("Private method is not writable");if(C==="a"&&!U)throw new TypeError("Private accessor was defined without a setter");if(typeof I=="function"?v!==I||!U:!I.has(v))throw new TypeError("Cannot write private member to an object whose class did not declare it");return C==="a"?U.call(v,R):U?U.value=R:I.set(v,R),R},j=function(v,I){if(I===null||typeof I!="object"&&typeof I!="function")throw new TypeError("Cannot use 'in' operator on non-object");return typeof v=="function"?I===v:v.has(I)},O=function(v,I,R){if(I!=null){if(typeof I!="object"&&typeof I!="function")throw new TypeError("Object expected.");var C;if(R){if(!Symbol.asyncDispose)throw new TypeError("Symbol.asyncDispose is not defined.");C=I[Symbol.asyncDispose]}if(C===void 0){if(!Symbol.dispose)throw new TypeError("Symbol.dispose is not defined.");C=I[Symbol.dispose]}if(typeof C!="function")throw new TypeError("Object not disposable.");v.stack.push({value:I,dispose:C,async:R})}else R&&v.stack.push({async:!0});return I};var B=typeof SuppressedError=="function"?SuppressedError:function(v,I,R){var C=new Error(R);return C.name="SuppressedError",C.error=v,C.suppressed=I,C};W=function(v){function I(C){v.error=v.hasError?new B(C,v.error,"An error was suppressed during disposal."):C,v.hasError=!0}function R(){for(;v.stack.length;){var C=v.stack.pop();try{var U=C.dispose&&C.dispose.call(C.value);if(C.async)return Promise.resolve(U).then(R,function(S){return I(S),R()})}catch(S){I(S)}}if(v.hasError)throw v.error}return R()},A("__extends",t),A("__assign",e),A("__rest",r),A("__decorate",l),A("__param",i),A("__esDecorate",u),A("__runInitializers",d),A("__propKey",s),A("__setFunctionName",m),A("__metadata",h),A("__awaiter",x),A("__generator",_),A("__exportStar",n),A("__createBinding",L),A("__values",c),A("__read",f),A("__spread",y),A("__spreadArrays",w),A("__spreadArray",P),A("__await",N),A("__asyncGenerator",H),A("__asyncDelegator",D),A("__asyncValues",o),A("__makeTemplateObject",p),A("__importStar",g),A("__importDefault",b),A("__classPrivateFieldGet",E),A("__classPrivateFieldSet",k),A("__classPrivateFieldIn",j),A("__addDisposableResource",O),A("__disposeResources",W)})})(Bt)),Bt.exports}var jt={exports:{}},Pt={exports:{}},De;function ln(){return De||(De=1,(function(a,t){a.path="valdi_core/src/utils/Buffer",Object.defineProperty(t,"__esModule",{value:!0}),t.Buffer=void 0;class e{constructor(l){const i=new ArrayBuffer(l);this.array=new DataView(i),this.pos=0}inner(){return this.array.buffer}empty(){return!this.pos}rewind(){this.pos=0}size(){return this.pos}ensureCapacity(l){const i=this.array;if(l<i.byteLength)return i;const u=new ArrayBuffer(Math.max(i.byteLength*2,l));new Uint8Array(u).set(new Uint8Array(i.buffer));const d=new DataView(u);return this.array=d,d}putUint32(l){const i=this.pos;this.ensureCapacity(i+4).setUint32(i,l,!0),this.pos=i+4}putUint32_2(l,i){const u=this.pos,d=this.ensureCapacity(u+8);d.setUint32(u,l,!0),d.setUint32(u+4,i,!0),this.pos=u+8}putUint32_3(l,i,u){const d=this.pos,s=this.ensureCapacity(d+12);s.setUint32(d,l,!0),s.setUint32(d+4,i,!0),s.setUint32(d+8,u,!0),this.pos=d+12}putUint32_4(l,i,u,d){const s=this.pos,m=this.ensureCapacity(s+16);m.setUint32(s,l,!0),m.setUint32(s+4,i,!0),m.setUint32(s+8,u,!0),m.setUint32(s+12,d,!0),this.pos=s+16}putUint32_5(l,i,u,d,s){const m=this.pos,h=this.ensureCapacity(m+20);h.setUint32(m,l,!0),h.setUint32(m+4,i,!0),h.setUint32(m+8,u,!0),h.setUint32(m+12,d,!0),h.setUint32(m+16,s,!0),this.pos=m+20}putFloat64(l){const i=this.pos;this.ensureCapacity(i+8).setFloat64(i,l,!0),this.pos=i+8}}t.Buffer=e})(Pt,Pt.exports)),Pt.exports}var At={exports:{}},Se;function dn(){return Se||(Se=1,(function(a,t){a.path="dil_sandbox/src/WeakRef",Object.defineProperty(t,"__esModule",{value:!0}),t.WeakRef=void 0;class e{constructor(i){this.value=i}deref(){return this.value}}const r=globalThis.WeakRef;t.WeakRef=r??e})(At,At.exports)),At.exports}var ke;function un(){return ke||(ke=1,(function(a,t){a.path="dil_sandbox/src/DILRenderOperations",Object.defineProperty(t,"__esModule",{value:!0}),t.applyDILRenderOperations=t.DILRenderBufferDelegate=void 0;const e=st(),r=Vt(),l=ln(),i=dn();class u{constructor(n){this.elementsMetadata=n,this.attachedStringIndexes=new Map,this.attachedValues=[],this.buffer=new l.Buffer(512),this.functionsById=new Map,this.functionIds=new WeakMap,this.nextFunctionId=1,this.interactionScopes=[]}beginBatch(){this.buffer.rewind(),this.attachedValues=[],this.attachedStringIndexes.clear(),this.interactionScopes=[]}finishBatch(){const n={descriptor:this.buffer.inner(),descriptorSize:this.buffer.size(),attachedValues:this.attachedValues,interactionScopes:this.interactionScopes};return this.buffer.rewind(),this.attachedValues=[],this.attachedStringIndexes.clear(),this.interactionScopes=[],n}discardBatch(){this.buffer.rewind(),this.attachedValues=[],this.attachedStringIndexes.clear(),this.interactionScopes=[]}invokeFunction(n,c){var f;const y=(f=this.functionsById.get(n))===null||f===void 0?void 0:f.deref();if(y===void 0)throw new Error(\`Unknown DIL sandbox function \${n}.\`);return y(...c)}dispose(){this.discardBatch(),this.functionsById.clear()}onElementNodeCreated(n,c){this.writeOperation(1),this.buffer.putUint32_2(n,c)}onNodeInteractionScopeChanged(n,c){this.interactionScopes.push({nodeId:n,scope:c})}onTextNodeCreated(n,c){this.writeOperation(2),this.buffer.putUint32_2(n,this.attach(c))}onNodeDestroyed(n){this.writeOperation(3),this.buffer.putUint32(n)}onNodeMoved(n,c,f){this.writeOperation(4),this.buffer.putUint32_3(n,c,f)}onNodePropChanged(n,c,f){this.writeOperation(5),this.buffer.putUint32_2(n,this.attach(c)),this.writeValue(f)}onNodeOpaqueChildrenChanged(n,c){this.writeOperation(7),this.buffer.putUint32(n),this.writeValue(c)}onTextNodeChanged(n,c){this.writeOperation(6),this.buffer.putUint32_2(n,this.attach(c))}writeOperation(n){this.buffer.putUint32(n)}attach(n){if(typeof n=="string"){const f=this.attachedStringIndexes.get(n);if(f!==void 0)return f;const y=this.attachedValues.length;return this.attachedValues.push(n),this.attachedStringIndexes.set(n,y),y}const c=this.attachedValues.length;return this.attachedValues.push(n),c}writeValue(n){if(n===void 0){this.buffer.putUint32(0);return}if(n===null){this.buffer.putUint32(1);return}if(n===!1){this.buffer.putUint32(2);return}if(n===!0){this.buffer.putUint32(3);return}if(typeof n=="number"){this.buffer.putUint32(4),this.buffer.putFloat64(n);return}if(typeof n=="string"){this.buffer.putUint32_2(5,this.attach(n));return}if(typeof n=="function"){this.buffer.putUint32_2(8,this.getFunctionId(n));return}if(Array.isArray(n)){this.buffer.putUint32_2(6,n.length);for(const c of n)this.writeValue(c);return}if((0,e.isDILRuntimeElement)(n)){this.writeRuntimeElement(n);return}if(m(n)){const c=(0,r.getDILHtmlViewMessengerHost)(n);if(c!==void 0){this.buffer.putUint32_2(12,this.attach(c.channelId));return}const f=Object.keys(n);this.buffer.putUint32_2(7,f.length);for(const y of f)this.buffer.putUint32(this.attach(y)),this.writeValue(n[y]);return}this.buffer.putUint32_2(11,this.attach(n))}writeRuntimeElement(n){const c=n.type;if(c===e.DIL_FRAGMENT||typeof c=="function"){this.buffer.putUint32(10),this.writeValue(n.children);return}const f=this.elementsMetadata[c];if(f===void 0)throw new Error(\`Unknown DIL element type "\${c}".\`);this.buffer.putUint32_2(9,f.typeId),this.writeValue(n.props),this.writeValue(n.children)}getFunctionId(n){let c=this.functionIds.get(n);return c===void 0&&(c=this.nextFunctionId++,this.functionIds.set(n,c)),this.functionsById.set(c,new i.WeakRef(n)),c}}t.DILRenderBufferDelegate=u;function d(_,n,c){var f,y;new s(_,n,c).apply();for(const P of(f=_.interactionScopes)!==null&&f!==void 0?f:[])(y=n.onNodeInteractionScopeChanged)===null||y===void 0||y.call(n,P.nodeId,P.scope)}t.applyDILRenderOperations=d;class s{constructor(n,c,f){this.encoded=n,this.consumer=c,this.valueResolver=f,this.offset=0;const y=n.descriptorSize;if(!Number.isInteger(y)||y<0||y>n.descriptor.byteLength||y%4!==0)throw new Error("Invalid DIL render operations descriptor size.");this.view=new DataView(n.descriptor,0,y)}apply(){for(;this.offset<this.view.byteLength;){const n=this.readUint32();switch(n){case 1:{const c=this.readUint32(),f=this.readUint32();this.consumer.onElementNodeCreated(c,f);break}case 2:{const c=this.readUint32(),f=this.readString();this.consumer.onTextNodeCreated(c,f);break}case 3:this.consumer.onNodeDestroyed(this.readUint32());break;case 4:this.consumer.onNodeMoved(this.readUint32(),this.readUint32(),this.readUint32());break;case 5:this.consumer.onNodePropChanged(this.readUint32(),this.readString(),this.readValue());break;case 6:{const c=this.readUint32(),f=this.readString();this.consumer.onTextNodeChanged(c,f);break}case 7:{const c=this.readUint32(),f=this.readValue();if(!h(f))throw new Error("Invalid DIL render operation opaque children.");this.consumer.onNodeOpaqueChildrenChanged(c,f);break}default:throw new Error(\`Unknown DIL render operation kind \${n}.\`)}}}readValue(){const n=this.readUint32();switch(n){case 0:return;case 1:return null;case 2:return!1;case 3:return!0;case 4:return this.readFloat64();case 5:return this.readString();case 6:{const c=this.readUint32(),f=[];for(let y=0;y<c;y++)f.push(this.readValue());return f}case 7:{const c=this.readUint32(),f={};for(let y=0;y<c;y++)f[this.readString()]=this.readValue();return f}case 8:return this.valueResolver.resolveFunction(this.readUint32());case 9:{const c=this.valueResolver.resolveType(this.readUint32()),f=this.readValue();if(f!==void 0&&!m(f))throw new Error("Invalid DIL render operation element props.");const y=this.readValue();if(!Array.isArray(y))throw new Error("Invalid DIL render operation element children.");return(0,e.createDilElement)(c,f,y)}case 10:{const c=this.readValue();if(!Array.isArray(c))throw new Error("Invalid DIL render operation fragment children.");return(0,e.createDilElement)(e.DIL_FRAGMENT,void 0,c)}case 11:return this.readAttached();case 12:return this.valueResolver.resolveHtmlViewMessenger(this.readString());default:throw new Error(\`Unknown DIL render value kind \${n}.\`)}}readString(){const n=this.readAttached();if(typeof n!="string")throw new Error("Invalid DIL render operation string value.");return n}readAttached(){const n=this.readUint32();if(n>=this.encoded.attachedValues.length)throw new Error("Invalid DIL render operation attached value index.");return this.encoded.attachedValues[n]}readUint32(){if(this.offset+4>this.view.byteLength)throw new Error("Truncated DIL render operations descriptor.");const n=this.view.getUint32(this.offset,!0);return this.offset+=4,n}readFloat64(){if(this.offset+8>this.view.byteLength)throw new Error("Truncated DIL render operations descriptor.");const n=this.view.getFloat64(this.offset,!0);return this.offset+=8,n}}function m(_){if(_===null||typeof _!="object"||(0,e.isDILRuntimeElement)(_))return!1;const n=Object.getPrototypeOf(_);return n===null||n===Object.prototype}function h(_){if(!Array.isArray(_))return!1;for(const n of _)if(typeof n!="string"&&typeof n!="number"&&!x(n))return!1;return!0}function x(_){return m(_)?typeof _.type=="string"&&m(_.props)&&h(_.children):!1}})(jt,jt.exports)),jt.exports}var Ue;function cn(){return Ue||(Ue=1,(function(a,t){a.path="dil_sandbox/src/DILSandboxRuntime",Object.defineProperty(t,"__esModule",{value:!0}),t.DILSandboxRuntime=void 0;const e=an(),r=qt(),l=un();class i{constructor(s){var{requestRender:m,fixedTimeMs:h,errorMode:x,asyncErrorHandler:_}=s,n=e.__rest(s,["requestRender","fixedTimeMs","errorMode","asyncErrorHandler"]);this.errors=[],this.pendingFlushes=[],this.requestRender=m,this.asyncErrorHandler=_,this.delegate=new l.DILRenderBufferDelegate(n.elementsMetadata),this.renderer=new r.DILRenderer(Object.assign(Object.assign({},n),{delegate:this.delegate,errorReporter:this,scheduler:this})),this.context=this.renderer.createRenderContext(h,x)}reportError(s){this.errors.push(s)}reportUnhandledError(s){this.asyncErrorHandler(s)}scheduleFlush(s){this.pendingFlushes.push(s)}scheduleRender(){this.requestRender()}updateSource(s){return this.errors.length=0,this.context.updateSource(s),this.takeErrors()}setStateSnapshot(s,m){return this.context.setStateSnapshot(s,m)}commitStateSnapshot(){this.context.commitStateSnapshot()}render(s){return{encoded:this.renderOnce(s),errors:this.takeErrors()}}renderSourceUpdate(s){let m=this.renderOnce(s),h=this.takeErrors();return m!==void 0?{encoded:m,errors:h}:(this.context.clearRenderedRoot(),m=this.renderOnce(s),h=u(h,this.takeErrors()),{encoded:m,errors:h})}invokeFunction(s,m){return this.delegate.invokeFunction(s,m)}registerHtmlViewMessengerTransport(s,m){return this.renderer.registerDILHtmlViewMessengerTransport(s,m)}receiveHtmlViewMessengerCommand(s,m,h){return this.renderer.receiveDILHtmlViewMessengerCommand(s,m,h)}receiveHtmlViewMessengerEvent(s,m,h){this.renderer.receiveDILHtmlViewMessengerEvent(s,m,h)}flush(){if(this.pendingFlushes.length===0)return;this.errors.length=0;const s=this.pendingFlushes.splice(0);for(const m of s)m();return this.takeErrors()}dispose(){return this.errors.length=0,this.context.dispose(),this.delegate.dispose(),u(this.takeErrors(),this.flush())}renderOnce(s){if(this.errors.length=0,this.delegate.beginBatch(),this.context.render(s.appData,s.theme,s.activeBreakpoints,{constants:s.constants,isSourceStreaming:!1,streamingAnimation:r.DILStreamingAnimation.Disabled}),this.context.didLastRenderFail()){this.delegate.discardBatch();return}return this.delegate.finishBatch()}takeErrors(){if(this.errors.length!==0)return this.errors.splice(0)}}t.DILSandboxRuntime=i;function u(d,s){return s===void 0?d:d===void 0?s.slice():(d.push(...s),d)}})(Lt,Lt.exports)),Lt.exports}var pn=cn();const _n=globalThis.setInterval.bind(globalThis),Le=globalThis.clearInterval.bind(globalThis);class mn{disposed=!1;intervals=new Map;now=Date.now();getSnapshot=()=>this.now;subscribe=(t,e=1e3)=>{if(this.disposed)return()=>{};const r=()=>t();let l=this.intervals.get(e);if(!l){const d=new Set;this.now=Date.now(),l={handle:_n(()=>{this.now=Date.now();for(const m of d)m()},e),listeners:d},this.intervals.set(e,l)}const{handle:i,listeners:u}=l;return u.add(r),()=>{u.delete(r)&&u.size===0&&(Le(i),this.intervals.delete(e))}};dispose(){this.disposed=!0;for(const{handle:t,listeners:e}of this.intervals.values())e.clear(),Le(t);this.intervals.clear()}}var rt=Ht(),J=_e();function fn(a){if(a?.kind==="ready")return a.service;if(a?.kind==="requires-auth")return{createSession(t,e){let r=!1;const l=()=>{r||(r=!0,e({kind:J.DILDictationEventKind.Cancelled}))};return{start(){r||(l(),a.requestAuthentication())},stop:l,cancel:l,dispose(){r=!0}}}}}const hn={idle:rt.DILSpeechStatus.Idle,loading:rt.DILSpeechStatus.Loading,playing:rt.DILSpeechStatus.Playing};function gn(a,t){const e=fn(a.dictation);if(e)return{isUserInteraction:t,createSession:(r,l)=>e.createSession(r,l)}}const yn={play:rt.DILSpeechFailureStage.Play,request:rt.DILSpeechFailureStage.Request,response:rt.DILSpeechFailureStage.Response,streaming:rt.DILSpeechFailureStage.Streaming};function vn(a,t){const e=a.speechSynthesis;if(e)return{isUserInteraction:t,createSession:(r,l)=>{const i=e.createSession(r,u=>{const d=u.error;l({available:u.available,status:hn[u.status],error:d===null?null:{failureStage:yn[d.failureStage],...d.httpStatus===void 0?{}:{httpStatus:d.httpStatus}}})});return{play:u=>i.play(u),stop:u=>i.stop(u),dispose:()=>i.dispose()}}}}var Ot={exports:{}},zt={exports:{}},$t={},Gt={exports:{}},je;function Pe(){return je||(je=1,(function(a,t){a.path="dil_generated_components/src/DILPublicComponentSources.generated",Object.defineProperty(t,"__esModule",{value:!0}),t.DIL_COMPONENT_SOURCES=void 0,t.DIL_COMPONENT_SOURCES=Object.freeze({OpGenuiResolvedComponentBoundary:\`(() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region internal/ResolvedComponentBoundary.dil.tsx
	function ResolvedComponentBoundary({ Component, componentName, componentProps }) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (componentProps.__state !== void 0) return /* @__PURE__ */ __dil.jsx(Component, componentProps);
		const result = (typeof componentProps.__resolutionId === "string" ? opGenui?.componentResults?.[componentProps.__resolutionId] : void 0) ?? opGenui?.componentResults?.[componentDataKey(componentName, componentProps)];
		const delegatesFailedResultToComponent = !opGenui?.showFailedComponents && (componentName === "AsyncImage" || componentName === "AsyncImageGroup");
		if (isComponentResultEnvelope(result) && result.status === "failed" && !delegatesFailedResultToComponent && !((componentName === "Link" || componentName === "LinkCard") && typeof componentProps.title === "string" && componentProps.title.length > 0 && typeof componentProps.url === "string" && componentProps.url.length > 0)) {
			if (componentProps.fallback != null) return componentProps.fallback;
			return opGenui?.showFailedComponents ? /* @__PURE__ */ __dil.jsx("text", {
				color: "danger",
				size: "sm"
			}, \\\`\\\${componentName}: \\\${result.code}\\\`) : null;
		}
		return /* @__PURE__ */ __dil.jsx(Component, componentProps);
	}

//#endregion
return ResolvedComponentBoundary;
})();
return __dilDefaultExport;
})()\`,AsyncImage:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentAsyncImage(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "AsyncImage",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "AsyncImage", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentAsyncImage, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function hasImageSource(image) {
		return Boolean(image?.content_url || image?.thumbnail_url);
	}
	function normalizedAspectRatio(value) {
		return value?.replace(":", " / ");
	}
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region AsyncImage.dil.tsx
/** Mirror v1: only pixel max-widths supply a non-shrinking preferred width. */
	function hasPreferredPixelWidth(value) {
		if (typeof value === "number") return Number.isFinite(value) && value >= 0;
		return typeof value === "string" && /^\\\\d+(?:\\\\.\\\\d+)?(?:px)?$/.test(value.trim());
	}
	function normalizedDimension(value) {
		return typeof value === "string" && /^\\\\d+(?:\\\\.\\\\d+)?$/.test(value.trim()) ? Number(value) : value;
	}
	/** Mirror the v1 intrinsic frame while image resolution is still pending. */
	function unresolvedAspectWidth(maxHeight, aspectRatio) {
		return \\\`calc(\\\${typeof maxHeight === "number" ? \\\`\\\${maxHeight}px\\\` : /^\\\\d+(?:\\\\.\\\\d+)?$/.test(maxHeight.trim()) ? \\\`\\\${maxHeight.trim()}px\\\` : maxHeight.trim()} * \\\${normalizedAspectRatio(aspectRatio)})\\\`;
	}
	function containsSource(value, src) {
		if (value === src) return true;
		if (value === null || typeof value !== "object") return false;
		return Object.values(value).some((child) => containsSource(child, src));
	}
	function directImages(props, sourceAllowed) {
		if (!sourceAllowed || !props.src || props.query != null || props.ref != null) return [];
		return [{
			url: props.src,
			content_url: props.src,
			thumbnail_url: props.src,
			title: props.alt ?? ""
		}];
	}
	function ImageContent(props) {
		return /* @__PURE__ */ __dil.jsx("search-image", props);
	}
	function AsyncImage(props) {
		const sourceAllowed = DIL.useAppData((appData) => Boolean(props.src) && containsSource(appData.opGenui?.modelDataBindings, props.src));
		const resolved = useResolvedComponentResult("AsyncImage", props);
		const isDirect = "src" in props;
		const state = isDirect ? void 0 : resolved.state;
		const resolutionComplete = isDirect || resolved.resolutionComplete;
		const isLoading = state?.is_loading ?? !resolutionComplete;
		const images = isDirect ? directImages(props, sourceAllowed) : state?.images ?? [];
		const image = images[0];
		const hasImage = hasImageSource(image);
		const isProduct = image?.refs?.some((ref) => ref.ref_type === "product");
		const needsLocalSizing = state == null;
		const frameMaxWidth = state?.frame_max_width ?? normalizedDimension(props.maxWidth) ?? (needsLocalSizing ? "100%" : void 0);
		const frameAspectRatio = state?.frame_aspect_ratio ?? props.aspectRatio;
		const presentation = state?.presentation;
		const hasAuthoredDimensions = props.width != null || props.height != null;
		const defaultMaxHeight = needsLocalSizing && !hasAuthoredDimensions ? normalizedDimension(props.maxHeight) ?? 220 : void 0;
		const unresolvedSize = frameAspectRatio == null ? defaultMaxHeight : void 0;
		const unresolvedWidth = defaultMaxHeight != null && frameAspectRatio != null ? unresolvedAspectWidth(defaultMaxHeight, frameAspectRatio) : unresolvedSize;
		const fallbackElement = props.fallback ?? /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			ariaLabel: "Image unavailable",
			background: "surface-tertiary",
			height: "100%",
			justify: "center",
			role: "img",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "tertiary",
			name: "image-square",
			size: "lg"
		}));
		const imageElement = /* @__PURE__ */ __dil.jsx(ImageContent, {
			key: isDirect ? props.src : void 0,
			attributionOverlay: !isDirect,
			alt: props.alt ?? image?.title ?? "",
			aspectRatio: normalizedAspectRatio(frameAspectRatio),
			background: isProduct ? "#f3f3f3" : void 0,
			bitmapBlendMode: isProduct ? "darken" : void 0,
			containOutsideAspectRatio: isProduct && props.fit == null ? {
				min: .6,
				max: 1.8
			} : void 0,
			fallback: fallbackElement,
			contentCropFit: props.fit,
			fit: props.fit ?? (isProduct ? "cover" : state?.image_fit ?? (isDirect && frameAspectRatio == null ? "contain" : "cover")),
			height: "100%",
			hideOnFailure: true,
			minHeight: isProduct ? 0 : void 0,
			position: isProduct ? "center" : void 0,
			radius: "none",
			searchImage: image,
			width: "100%"
		});
		return /* @__PURE__ */ __dil.jsx("box", {
			imageObservation: !isLoading && !hasImage ? "unavailable" : "active",
			ariaLabel: isLoading ? "Loading image" : void 0,
			aspectRatio: normalizedAspectRatio(frameAspectRatio),
			background: "surface-tertiary",
			border: (presentation?.frame ?? props.frame ?? true) && !isLoading && hasImage ? {
				color: "subtle",
				size: 1
			} : void 0,
			clip: true,
			flex: hasPreferredPixelWidth(frameMaxWidth) ? "0 0 auto" : void 0,
			height: state?.frame_height ?? normalizedDimension(props.height) ?? (props.width != null || frameAspectRatio != null ? void 0 : unresolvedSize ?? "100%"),
			maxHeight: (state?.max_height !== void 0 ? state.max_height ?? void 0 : normalizedDimension(props.maxHeight) ?? defaultMaxHeight) ?? (isProduct ? "100%" : void 0),
			maxWidth: frameMaxWidth,
			minHeight: presentation?.min_height ?? props.minHeight,
			minWidth: presentation?.min_width ?? props.minWidth ?? 0,
			radius: presentation?.radius ?? props.radius ?? "2xl",
			role: isLoading ? "status" : void 0,
			width: state?.frame_width ?? normalizedDimension(props.width) ?? unresolvedWidth ?? "100%"
		}, !isLoading && !hasImage ? fallbackElement : /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: image?.title ? \\\`Open \\\${image.title}\\\` : "Open image",
			background: "transparent",
			disabled: isLoading,
			height: "100%",
			onClick: () => state?.default_on_click_action ? GenUI.dispatchAction(state.default_on_click_action) : GenUI.openImageLightbox(images, 0),
			radius: "none",
			width: "100%"
		}, imageElement));
	}

//#endregion
return AsyncImage;
})();
return __dilDefaultExport;
})()))\`,AsyncImageGroup:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentAsyncImageGroup(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "AsyncImageGroup",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "AsyncImageGroup", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentAsyncImageGroup, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function hasImageSource(image) {
		return Boolean(image?.content_url || image?.thumbnail_url);
	}
	function normalizedAspectRatio(value) {
		return value?.replace(":", " / ");
	}
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region AsyncImageGroup.dil.tsx
/** Display the complete gallery count on the final visible desktop tile. */
	function ImageCount({ count }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			align: "end",
			ariaHidden: true,
			height: "100%",
			justify: "end",
			padding: {
				bottom: 2.5,
				right: 2.5
			},
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			background: "rgba(0, 0, 0, 0.4)",
			gap: .5,
			padding: {
				bottom: 1,
				left: 1.5,
				right: 2,
				top: 1
			},
			radius: "full",
			width: "fit-content"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "white",
			name: "images",
			size: "xs"
		}), /* @__PURE__ */ __dil.jsx("text", {
			color: "white",
			inline: true,
			size: "xs",
			weight: "semibold"
		}, count)));
	}
	const PLACEHOLDER_INDEXES = [
		0,
		1,
		2
	];
	function ImageFailure() {
		return /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			ariaLabel: "Image unavailable",
			background: "surface-tertiary",
			height: "100%",
			justify: "center",
			role: "img",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "tertiary",
			name: "image-square",
			size: "lg"
		}));
	}
	function ImageFallbackFrame({ aspectRatio, children, itemHeight, itemWidth }) {
		return /* @__PURE__ */ __dil.jsx("box", {
			imageObservation: "unavailable",
			aspectRatio: normalizedAspectRatio(aspectRatio ?? "5:4"),
			clip: true,
			height: itemHeight,
			minWidth: itemWidth,
			radius: "2xl",
			width: itemWidth
		}, children);
	}
	/** Keep one loading surface mounted while its resolved image source arrives. */
	function GroupImageTile({ aspectRatio, failed = false, fallback, flex, height, image, images, index, minWidth, radius, showCount = false, width }) {
		const isProduct = image?.refs?.some((ref) => ref.ref_type === "product");
		return /* @__PURE__ */ __dil.jsx("box", {
			imageObservation: failed ? "unavailable" : "active",
			aspectRatio: normalizedAspectRatio(aspectRatio),
			background: "surface-tertiary",
			clip: true,
			flex,
			height,
			minWidth,
			radius,
			width
		}, failed ? /* @__PURE__ */ __dil.jsx(ImageFailure, null) : /* @__PURE__ */ __dil.jsx("search-image", {
			alt: image?.title ?? "",
			aspectRatio: normalizedAspectRatio(aspectRatio),
			background: isProduct ? "#f3f3f3" : void 0,
			bitmapBlendMode: isProduct ? "darken" : void 0,
			containOutsideAspectRatio: isProduct ? {
				min: .6,
				max: 1.8
			} : void 0,
			fallback,
			fit: "cover",
			frame: true,
			height: "100%",
			hideOnFailure: true,
			minHeight: isProduct ? 0 : void 0,
			position: isProduct ? "center" : void 0,
			radius,
			searchImage: image,
			width: "100%"
		}, image ? /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: image.title ? \\\`Open \\\${image.title}\\\` : "Open image",
			background: "transparent",
			height: "100%",
			onClick: () => GenUI.openImageLightbox(images, index),
			radius: "none",
			width: "100%"
		}, showCount ? /* @__PURE__ */ __dil.jsx(ImageCount, { count: images.length }) : null) : null));
	}
	/** Render the v1-compatible responsive image strip, preserving loading and fallback states. */
	function AsyncImageGroup(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("AsyncImageGroup", props);
		const isSm = DIL.useBreakpoint("sm");
		const layout = state?.layout ?? props.layout ?? "carousel";
		const isDesktopCarousel = layout === "carousel" && isSm;
		const images = (state?.images ?? []).filter(hasImageSource);
		const isLoading = state?.is_loading ?? !resolutionComplete;
		const failed = !isLoading && images.length === 0;
		const aspectRatio = state?.aspect_ratio ?? props.aspectRatio ?? "5:4";
		const itemHeight = state?.item_height;
		const itemWidth = state?.item_width;
		if (failed && props.fallback) return /* @__PURE__ */ __dil.jsx(ImageFallbackFrame, {
			aspectRatio,
			itemHeight,
			itemWidth
		}, props.fallback);
		const fallbackElement = props.fallback ?? /* @__PURE__ */ __dil.jsx(ImageFailure, null);
		if (layout === "bento" && (isLoading || failed || images.length >= 3)) return /* @__PURE__ */ __dil.jsx("row", {
			ariaLabel: isLoading ? "Loading images" : void 0,
			aspectRatio: "363 / 200",
			flexInRow: true,
			gap: .5,
			maxWidth: 768,
			minHeight: 0,
			minWidth: 0,
			role: isLoading ? "status" : void 0,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx(GroupImageTile, {
			failed,
			fallback: fallbackElement,
			flex: 1,
			height: "100%",
			image: images[0],
			images,
			index: 0,
			radius: {
				bottomLeft: "2xl",
				topLeft: "2xl"
			},
			width: "100%"
		}), /* @__PURE__ */ __dil.jsx("col", {
			gap: .5,
			width: "40%"
		}, [1, 2].map((index) => /* @__PURE__ */ __dil.jsx(GroupImageTile, {
			failed,
			fallback: fallbackElement,
			flex: 1,
			height: "100%",
			image: images[index],
			images,
			index,
			key: \\\`async-image-group-tile:\\\${index}\\\`,
			radius: index === 1 ? { topRight: "2xl" } : { bottomRight: "2xl" },
			showCount: index === 2 && images.length > 3,
			width: "100%"
		}))));
		if (isDesktopCarousel && (isLoading || failed || images.length >= 3)) return /* @__PURE__ */ __dil.jsx("row", {
			flexInRow: true,
			maxWidth: 768,
			minWidth: 0,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("row", {
			ariaLabel: isLoading ? "Loading images" : void 0,
			gap: 2,
			maxWidth: "100%",
			minWidth: 0,
			role: isLoading ? "status" : void 0,
			width: 768
		}, PLACEHOLDER_INDEXES.map((index) => /* @__PURE__ */ __dil.jsx(GroupImageTile, {
			aspectRatio,
			failed,
			fallback: fallbackElement,
			flex: "1 1 0%",
			image: images[index],
			images,
			index,
			key: \\\`async-image-group-tile:\\\${index}\\\`,
			minWidth: 0,
			radius: "2xl",
			showCount: index === 2 && images.length > 3,
			width: "100%"
		}))));
		const scrollImages = isLoading || failed ? PLACEHOLDER_INDEXES.map(() => void 0) : images;
		return /* @__PURE__ */ __dil.jsx("box", {
			ariaLabel: isLoading ? "Loading images" : void 0,
			flexInRow: true,
			role: isLoading ? "status" : void 0,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("carousel", {
			flush: true,
			gap: 2,
			showArrows: false,
			snap: "none"
		}, scrollImages.map((image, index) => /* @__PURE__ */ __dil.jsx("carousel-item", {
			height: itemHeight,
			key: \\\`async-image-group-tile:\\\${index}\\\`,
			minWidth: itemWidth,
			width: itemWidth ?? (isLoading || failed ? 140 : void 0)
		}, /* @__PURE__ */ __dil.jsx(GroupImageTile, {
			aspectRatio,
			failed,
			fallback: fallbackElement,
			height: itemHeight,
			image,
			images,
			index,
			radius: "2xl",
			width: "100%"
		})))));
	}

//#endregion
return AsyncImageGroup;
})();
return __dilDefaultExport;
})()))\`,AsyncVideo:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentAsyncVideo(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "AsyncVideo",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "AsyncVideo", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentAsyncVideo, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region AsyncVideo.dil.tsx
	function AsyncVideo(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("AsyncVideo", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading video" });
		const video = state.video;
		if (!video) return null;
		return /* @__PURE__ */ __dil.jsx("box", {
			background: "surface-secondary",
			clip: true,
			maxWidth: "100%",
			radius: "3xl",
			width: "640px"
		}, /* @__PURE__ */ __dil.jsx("youtube", {
			aspectRatio: "16 / 9",
			maxWidth: "100%",
			title: video.title,
			videoId: video.video_id,
			width: "100%"
		}));
	}

//#endregion
return AsyncVideo;
})();
return __dilDefaultExport;
})()))\`,AutomationPlanSummary:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentAutomationPlanSummary(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "AutomationPlanSummary",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "AutomationPlanSummary", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentAutomationPlanSummary, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) {
			if (result.status === "pending") return {
				status: "pending",
				resolutionComplete: false,
				state: void 0
			};
			return result.status === "resolved" ? {
				status: "resolved",
				resolutionComplete: true,
				state: result.state
			} : {
				status: "failed",
				resolutionComplete: true,
				state: void 0
			};
		}
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "pending") return true;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region AutomationPlanSummary.dil.tsx
	function AutomationPlanSummary(props) {
		const [expanded, setExpanded] = DIL.useState(false);
		const [collapsed, setCollapsed] = DIL.useState(false);
		const { state, resolutionComplete } = useResolvedComponentResult("AutomationPlanSummary", props);
		if (!state) return resolutionComplete ? props.fallback ?? null : /* @__PURE__ */ __dil.jsx("loading-block", {
			width: "100%",
			height: 240
		});
		const currentStepIndex = state.steps?.findIndex((step) => step.status === "in_progress") ?? -1;
		const nextStepIndex = currentStepIndex >= 0 ? currentStepIndex : state.steps?.findIndex((step) => step.status === "pending") ?? -1;
		const previousStepCompleted = nextStepIndex > 0 && state.steps?.[nextStepIndex - 1]?.status === "completed";
		const firstVisibleIndex = expanded ? 0 : nextStepIndex < 0 ? Math.max(0, (state.steps?.length ?? 0) - 3) : Math.max(0, nextStepIndex - (previousStepCompleted ? 1 : 0));
		const visibleSteps = expanded ? state.steps : state.steps?.slice(firstVisibleIndex, firstVisibleIndex + 3);
		return /* @__PURE__ */ __dil.jsx("card", {
			size: "full",
			padding: 5,
			gap: 4
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "start",
			gap: 2
		}, /* @__PURE__ */ __dil.jsx("col", {
			flex: 1,
			minWidth: 0,
			gap: 1
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			color: "tertiary"
		}, state.goal_label), /* @__PURE__ */ __dil.jsx("title", { size: "sm" }, state.title)), /* @__PURE__ */ __dil.jsx("row", {
			align: "start",
			gap: 2,
			flex: "0 0 auto"
		}, state.show_plan_label && state.hide_plan_label && /* @__PURE__ */ __dil.jsx("pressable", {
			size: 16,
			align: "center",
			justify: "center",
			radius: "full",
			ariaLabel: collapsed ? state.show_plan_label : state.hide_plan_label,
			tooltip: collapsed ? state.show_plan_label : state.hide_plan_label,
			onClick: () => setCollapsed(!collapsed)
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: collapsed ? "expand-large" : "collapse-large",
			size: "md",
			color: "tertiary"
		})), state.steps != null && state.expand_label && state.collapse_label && /* @__PURE__ */ __dil.jsx("pressable", {
			size: 16,
			align: "center",
			justify: "center",
			radius: "full",
			ariaLabel: !collapsed && expanded ? state.collapse_label : state.expand_label,
			tooltip: !collapsed && expanded ? state.collapse_label : state.expand_label,
			onClick: () => {
				setExpanded(collapsed || !expanded);
				setCollapsed(false);
			}
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "dots-horizontal",
			size: "md",
			color: "tertiary"
		})))), !collapsed && /* @__PURE__ */ __dil.jsx("box", {
			height: 1,
			background: {
				light: "#ededed",
				dark: "alpha-10"
			},
			ariaHidden: true
		}), !collapsed && (state.steps == null ? /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			padding: { y: 5 }
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "md",
			color: "secondary"
		}, state.summary_error_label)) : /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			role: "list"
		}, visibleSteps?.map((step, index) => /* @__PURE__ */ __dil.jsx("row", {
			key: step.id,
			gap: 1,
			align: "stretch",
			minHeight: index === visibleSteps.length - 1 ? 20 : 50,
			role: "listitem"
		}, /* @__PURE__ */ __dil.jsx("col", {
			width: 28,
			flex: "0 0 auto",
			align: "center",
			gap: 0
		}, /* @__PURE__ */ __dil.jsx("box", {
			height: step.status === "in_progress" ? 28 : 20,
			flex: "0 0 auto",
			align: "center",
			justify: "center",
			role: "img",
			ariaLabel: state.status_labels[step.status]
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: step.status === "completed" ? "check-circle-filled" : step.status === "in_progress" ? "spinner" : "empty-circle",
			size: "xl",
			color: step.status === "pending" ? {
				light: "gray-300",
				dark: "gray-600"
			} : step.status === "in_progress" ? "secondary" : "tertiary"
		})), index < visibleSteps.length - 1 && /* @__PURE__ */ __dil.jsx("box", {
			width: 1,
			flex: 1,
			background: {
				light: "#ededed",
				dark: "alpha-10"
			},
			ariaHidden: true
		})), /* @__PURE__ */ __dil.jsx("col", {
			gap: 1,
			flex: 1,
			minWidth: 0,
			padding: { bottom: index === visibleSteps.length - 1 ? 0 : 2 }
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "md",
			color: step.status === "completed" ? "tertiary" : "primary"
		}, step.title), expanded && step.description && /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			color: "secondary"
		}, step.description)))))));
	}

//#endregion
return AutomationPlanSummary;
})();
return __dilDefaultExport;
})()))\`,Citation:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentCitation(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "Citation",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "Citation", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentCitation, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) {
			if (result.status === "pending") return {
				status: "pending",
				resolutionComplete: false,
				state: void 0
			};
			return result.status === "resolved" ? {
				status: "resolved",
				resolutionComplete: true,
				state: result.state
			} : {
				status: "failed",
				resolutionComplete: true,
				state: void 0
			};
		}
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "pending") return true;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region Cite.dil.tsx
	function clampedIndex(index, itemCount) {
		if (typeof index === "number" && Number.isInteger(index) && index >= 0 && index < itemCount) return index;
		return 0;
	}
	function ResolvedCite({ activeIndex: serverActiveIndex, items }) {
		const initialActiveIndex = clampedIndex(serverActiveIndex, items.length);
		const [activeIndex, setActiveIndex] = DIL.useState(initialActiveIndex);
		const [badgeHovered, setBadgeHovered] = DIL.useState(false);
		const isSm = DIL.useBreakpoint("sm");
		const isMobile = DIL.useIsMobile();
		DIL.useEffect(() => {
			setActiveIndex(initialActiveIndex);
		}, [serverActiveIndex, items.length]);
		const activeItem = items[clampedIndex(activeIndex, items.length)];
		const url = activeItem.url ?? "";
		const hasUrl = url !== "";
		const hasDetails = [
			activeItem.title,
			activeItem.metadata_label,
			activeItem.snippet,
			activeItem.thumbnail_url
		].some(Boolean);
		const showPopover = items.length > 1 || (!isMobile || !hasUrl) && hasDetails;
		const isInteractive = showPopover || hasUrl;
		const sourceLabel = activeItem.source_label ?? activeItem.title ?? "Source";
		const badge = /* @__PURE__ */ __dil.jsx("badge", {
			color: isInteractive && badgeHovered ? {
				light: "#e8e8e8",
				dark: "gray-300"
			} : {
				light: "gray-75",
				dark: "gray-400"
			},
			maxWidth: "100%",
			onHover: isInteractive ? setBadgeHovered : void 0,
			padding: {
				left: 1,
				right: 1.5,
				y: 1
			},
			size: "sm",
			variant: "soft",
			weight: "normal"
		}, hasUrl ? /* @__PURE__ */ __dil.jsx("row", { flex: "none" }, /* @__PURE__ */ __dil.jsx("favicon", {
			size: 12,
			url
		})) : null, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			flex: "0 1 auto",
			gap: .75,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			flex: "0 1 auto",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			inline: true,
			maxLines: 1,
			size: "3xs",
			truncate: true
		}, sourceLabel)), items.length > 1 ? /* @__PURE__ */ __dil.jsx("row", { flex: "none" }, /* @__PURE__ */ __dil.jsx("text", {
			color: "tertiary",
			inline: true,
			size: "3xs"
		}, "+", items.length - 1)) : null));
		if (!showPopover) return hasUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`Open \\\${sourceLabel}\\\`,
			inline: true,
			onClick: () => GenUI.openUrl(url)
		}, badge) : badge;
		return /* @__PURE__ */ __dil.jsx("popover", {
			hoverOpenDelay: 80,
			showOnHover: true
		}, /* @__PURE__ */ __dil.jsx("popover-trigger", { onClick: () => !isMobile && isSm && hasUrl ? GenUI.openUrl(url) : void 0 }, badge), /* @__PURE__ */ __dil.jsx("popover-content", {
			align: "start",
			showCloseButton: isMobile ? false : void 0,
			side: "bottom",
			sideOffset: 8
		}, isMobile ? /* @__PURE__ */ __dil.jsx(MobileCitationSources, { items }) : /* @__PURE__ */ __dil.jsx(DesktopCitationSources, { items })));
	}
	function getCitationDetail(item) {
		return [item.metadata_label, item.snippet].filter(Boolean).join(" — ");
	}
	function DesktopCitationSources({ items }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			maxHeight: 320,
			maxWidth: "100%",
			padding: {
				bottom: 2,
				top: 2,
				x: 5
			},
			scrollable: true,
			width: 384
		}, items.map((item, index) => {
			const itemUrl = item.url ?? "";
			const itemSourceLabel = item.source_label ?? item.title ?? "Source";
			const itemTitle = item.title ?? "";
			const itemDetail = getCitationDetail(item);
			const source = /* @__PURE__ */ __dil.jsx("col", {
				border: index === 0 ? void 0 : { top: {
					color: "default",
					size: 1
				} },
				gap: 1.5,
				padding: { y: 3 },
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2,
				minWidth: 0,
				width: "100%"
			}, itemUrl ? /* @__PURE__ */ __dil.jsx("favicon", {
				size: 16,
				url: itemUrl
			}) : null, /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				inline: true,
				maxLines: 1,
				size: "xs",
				truncate: true
			}, itemSourceLabel)), itemTitle ? /* @__PURE__ */ __dil.jsx("text", {
				maxLines: 2,
				size: "sm",
				weight: "medium"
			}, itemTitle) : null, itemDetail || item.thumbnail_url ? /* @__PURE__ */ __dil.jsx("row", {
				align: "start",
				gap: 4,
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("col", {
				flex: 1,
				minWidth: 0
			}, itemDetail ? /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				maxLines: 3,
				size: "sm"
			}, itemDetail) : null), item.thumbnail_url ? /* @__PURE__ */ __dil.jsx("image", {
				alt: "",
				fit: "cover",
				height: 56,
				hideOnFailure: true,
				radius: "xl",
				src: item.thumbnail_url,
				width: 56
			}) : null) : null);
			return itemUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`Open \\\${itemSourceLabel}\\\`,
				key: \\\`\\\${itemUrl}:\\\${index}\\\`,
				onClick: () => GenUI.openUrl(itemUrl),
				width: "100%"
			}, source) : /* @__PURE__ */ __dil.jsx("col", {
				key: \\\`source:\\\${index}\\\`,
				width: "100%"
			}, source);
		}));
	}
	function MobileCitationSources({ items }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			maxHeight: 560,
			scrollable: true,
			width: "100%"
		}, items.map((item, index) => {
			const itemUrl = item.url ?? "";
			const itemSourceLabel = item.source_label ?? item.title ?? "Source";
			const itemTitle = item.title ?? "";
			const source = /* @__PURE__ */ __dil.jsx("col", {
				gap: 1,
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2,
				minWidth: 0,
				width: "100%"
			}, itemUrl ? /* @__PURE__ */ __dil.jsx("favicon", {
				size: 16,
				url: itemUrl
			}) : null, /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				weight: "semibold"
			}, itemSourceLabel)), itemTitle ? /* @__PURE__ */ __dil.jsx("text", { size: "sm" }, itemTitle) : null, item.metadata_label ? /* @__PURE__ */ __dil.jsx("caption", null, item.metadata_label) : null);
			return /* @__PURE__ */ __dil.jsx("col", {
				gap: 3,
				key: \\\`\\\${itemUrl}:\\\${index}\\\`,
				width: "100%"
			}, index > 0 ? /* @__PURE__ */ __dil.jsx("divider", { color: "subtle" }) : null, itemUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`Open \\\${itemSourceLabel}\\\`,
				onClick: () => GenUI.openUrl(itemUrl),
				width: "100%"
			}, source) : source);
		}));
	}
	function Cite(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("Cite", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx("loading", { label: "Loading citations" }));
		const items = state.items ?? [];
		if (!items.length) return null;
		return /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx(ResolvedCite, {
			activeIndex: state.active_index,
			items
		}));
	}

//#endregion
//#region Citation.dil.tsx
	function Citation(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("Citation", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx("loading", { label: "Loading citation" }));
		return /* @__PURE__ */ __dil.jsx(Cite, {
			...props,
			__state: state
		});
	}

//#endregion
return Citation;
})();
return __dilDefaultExport;
})()))\`,Cite:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentCite(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "Cite",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "Cite", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentCite, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) {
			if (result.status === "pending") return {
				status: "pending",
				resolutionComplete: false,
				state: void 0
			};
			return result.status === "resolved" ? {
				status: "resolved",
				resolutionComplete: true,
				state: result.state
			} : {
				status: "failed",
				resolutionComplete: true,
				state: void 0
			};
		}
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "pending") return true;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region Cite.dil.tsx
	function clampedIndex(index, itemCount) {
		if (typeof index === "number" && Number.isInteger(index) && index >= 0 && index < itemCount) return index;
		return 0;
	}
	function ResolvedCite({ activeIndex: serverActiveIndex, items }) {
		const initialActiveIndex = clampedIndex(serverActiveIndex, items.length);
		const [activeIndex, setActiveIndex] = DIL.useState(initialActiveIndex);
		const [badgeHovered, setBadgeHovered] = DIL.useState(false);
		const isSm = DIL.useBreakpoint("sm");
		const isMobile = DIL.useIsMobile();
		DIL.useEffect(() => {
			setActiveIndex(initialActiveIndex);
		}, [serverActiveIndex, items.length]);
		const activeItem = items[clampedIndex(activeIndex, items.length)];
		const url = activeItem.url ?? "";
		const hasUrl = url !== "";
		const hasDetails = [
			activeItem.title,
			activeItem.metadata_label,
			activeItem.snippet,
			activeItem.thumbnail_url
		].some(Boolean);
		const showPopover = items.length > 1 || (!isMobile || !hasUrl) && hasDetails;
		const isInteractive = showPopover || hasUrl;
		const sourceLabel = activeItem.source_label ?? activeItem.title ?? "Source";
		const badge = /* @__PURE__ */ __dil.jsx("badge", {
			color: isInteractive && badgeHovered ? {
				light: "#e8e8e8",
				dark: "gray-300"
			} : {
				light: "gray-75",
				dark: "gray-400"
			},
			maxWidth: "100%",
			onHover: isInteractive ? setBadgeHovered : void 0,
			padding: {
				left: 1,
				right: 1.5,
				y: 1
			},
			size: "sm",
			variant: "soft",
			weight: "normal"
		}, hasUrl ? /* @__PURE__ */ __dil.jsx("row", { flex: "none" }, /* @__PURE__ */ __dil.jsx("favicon", {
			size: 12,
			url
		})) : null, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			flex: "0 1 auto",
			gap: .75,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			flex: "0 1 auto",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			inline: true,
			maxLines: 1,
			size: "3xs",
			truncate: true
		}, sourceLabel)), items.length > 1 ? /* @__PURE__ */ __dil.jsx("row", { flex: "none" }, /* @__PURE__ */ __dil.jsx("text", {
			color: "tertiary",
			inline: true,
			size: "3xs"
		}, "+", items.length - 1)) : null));
		if (!showPopover) return hasUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`Open \\\${sourceLabel}\\\`,
			inline: true,
			onClick: () => GenUI.openUrl(url)
		}, badge) : badge;
		return /* @__PURE__ */ __dil.jsx("popover", {
			hoverOpenDelay: 80,
			showOnHover: true
		}, /* @__PURE__ */ __dil.jsx("popover-trigger", { onClick: () => !isMobile && isSm && hasUrl ? GenUI.openUrl(url) : void 0 }, badge), /* @__PURE__ */ __dil.jsx("popover-content", {
			align: "start",
			showCloseButton: isMobile ? false : void 0,
			side: "bottom",
			sideOffset: 8
		}, isMobile ? /* @__PURE__ */ __dil.jsx(MobileCitationSources, { items }) : /* @__PURE__ */ __dil.jsx(DesktopCitationSources, { items })));
	}
	function getCitationDetail(item) {
		return [item.metadata_label, item.snippet].filter(Boolean).join(" — ");
	}
	function DesktopCitationSources({ items }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			maxHeight: 320,
			maxWidth: "100%",
			padding: {
				bottom: 2,
				top: 2,
				x: 5
			},
			scrollable: true,
			width: 384
		}, items.map((item, index) => {
			const itemUrl = item.url ?? "";
			const itemSourceLabel = item.source_label ?? item.title ?? "Source";
			const itemTitle = item.title ?? "";
			const itemDetail = getCitationDetail(item);
			const source = /* @__PURE__ */ __dil.jsx("col", {
				border: index === 0 ? void 0 : { top: {
					color: "default",
					size: 1
				} },
				gap: 1.5,
				padding: { y: 3 },
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2,
				minWidth: 0,
				width: "100%"
			}, itemUrl ? /* @__PURE__ */ __dil.jsx("favicon", {
				size: 16,
				url: itemUrl
			}) : null, /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				inline: true,
				maxLines: 1,
				size: "xs",
				truncate: true
			}, itemSourceLabel)), itemTitle ? /* @__PURE__ */ __dil.jsx("text", {
				maxLines: 2,
				size: "sm",
				weight: "medium"
			}, itemTitle) : null, itemDetail || item.thumbnail_url ? /* @__PURE__ */ __dil.jsx("row", {
				align: "start",
				gap: 4,
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("col", {
				flex: 1,
				minWidth: 0
			}, itemDetail ? /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				maxLines: 3,
				size: "sm"
			}, itemDetail) : null), item.thumbnail_url ? /* @__PURE__ */ __dil.jsx("image", {
				alt: "",
				fit: "cover",
				height: 56,
				hideOnFailure: true,
				radius: "xl",
				src: item.thumbnail_url,
				width: 56
			}) : null) : null);
			return itemUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`Open \\\${itemSourceLabel}\\\`,
				key: \\\`\\\${itemUrl}:\\\${index}\\\`,
				onClick: () => GenUI.openUrl(itemUrl),
				width: "100%"
			}, source) : /* @__PURE__ */ __dil.jsx("col", {
				key: \\\`source:\\\${index}\\\`,
				width: "100%"
			}, source);
		}));
	}
	function MobileCitationSources({ items }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			maxHeight: 560,
			scrollable: true,
			width: "100%"
		}, items.map((item, index) => {
			const itemUrl = item.url ?? "";
			const itemSourceLabel = item.source_label ?? item.title ?? "Source";
			const itemTitle = item.title ?? "";
			const source = /* @__PURE__ */ __dil.jsx("col", {
				gap: 1,
				width: "100%"
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2,
				minWidth: 0,
				width: "100%"
			}, itemUrl ? /* @__PURE__ */ __dil.jsx("favicon", {
				size: 16,
				url: itemUrl
			}) : null, /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				weight: "semibold"
			}, itemSourceLabel)), itemTitle ? /* @__PURE__ */ __dil.jsx("text", { size: "sm" }, itemTitle) : null, item.metadata_label ? /* @__PURE__ */ __dil.jsx("caption", null, item.metadata_label) : null);
			return /* @__PURE__ */ __dil.jsx("col", {
				gap: 3,
				key: \\\`\\\${itemUrl}:\\\${index}\\\`,
				width: "100%"
			}, index > 0 ? /* @__PURE__ */ __dil.jsx("divider", { color: "subtle" }) : null, itemUrl ? /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`Open \\\${itemSourceLabel}\\\`,
				onClick: () => GenUI.openUrl(itemUrl),
				width: "100%"
			}, source) : source);
		}));
	}
	function Cite(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("Cite", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx("loading", { label: "Loading citations" }));
		const items = state.items ?? [];
		if (!items.length) return null;
		return /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx(ResolvedCite, {
			activeIndex: state.active_index,
			items
		}));
	}

//#endregion
return Cite;
})();
return __dilDefaultExport;
})()))\`,CoTToolGroup:\`(() => {
var __dilDefaultExport = (function() {


//#region src/messages.dil.ts
	const fallbackMessages = { moreItems: "+{count} more" };
	function useMessages() {
		const messages = DIL.useAppData((data) => data.messages);
		return {
			...fallbackMessages,
			...messages
		};
	}
	function formatMessage(template, values = {}) {
		return template.replace(/\\\\{(\\\\w+)\\\\}/g, (placeholder, key) => values[key] === void 0 ? placeholder : String(values[key]));
	}

//#endregion
//#region src/SourceCards.dil.tsx
	const OVERFLOW_THRESHOLD = 8;
	const INITIAL_VISIBLE_COUNT = 6;
	function SourceCards({ children, label }) {
		const [expanded, setExpanded] = DIL.useState(false);
		const messages = useMessages();
		const visibleCount = expanded || children.length <= OVERFLOW_THRESHOLD ? children.length : INITIAL_VISIBLE_COUNT;
		return /* @__PURE__ */ __dil.jsx("carousel", {
			ariaLabel: label,
			gap: 2,
			flush: true,
			snap: "none"
		}, [...children.slice(0, visibleCount), visibleCount < children.length && /* @__PURE__ */ __dil.jsx("carousel-item", { key: "overflow" }, /* @__PURE__ */ __dil.jsx("pressable", {
			onClick: () => setExpanded(true),
			height: "100%",
			justify: "center",
			align: "start"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary"
		}, formatMessage(messages.moreItems, { count: children.length - visibleCount }))))]);
	}

//#endregion
//#region src/CalendarSources.dil.tsx
	function CalendarSources({ sources, label }) {
		return /* @__PURE__ */ __dil.jsx(SourceCards, { label }, sources.map((source, index) => /* @__PURE__ */ __dil.jsx("carousel-item", {
			key: \\\`\\\${source.url ?? source.title}-\\\${index}\\\`,
			maxWidth: 200
		}, source.url ? /* @__PURE__ */ __dil.jsx("link", {
			href: source.url,
			title: source.title
		}, /* @__PURE__ */ __dil.jsx(CalendarCard, { source })) : /* @__PURE__ */ __dil.jsx(CalendarCard, { source }))));
	}
	function CalendarCard({ source }) {
		const [hovered, setHovered] = DIL.useState(false);
		return /* @__PURE__ */ __dil.jsx("box", {
			radius: "lg",
			clip: true
		}, /* @__PURE__ */ __dil.jsx("badge", {
			color: hovered ? "var(--color-background-secondary-soft-alpha-hover)" : "secondary",
			variant: "soft",
			pill: false,
			padding: 0,
			onHover: source.url ? setHovered : void 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			gap: 2,
			align: "stretch",
			padding: {
				top: 2,
				right: 2,
				bottom: 2,
				left: 1.5
			},
			maxWidth: 200
		}, /* @__PURE__ */ __dil.jsx("box", {
			width: 4,
			flex: "none",
			radius: "full",
			background: source.color ?? "info-solid",
			ariaHidden: true
		}), /* @__PURE__ */ __dil.jsx("col", {
			gap: .5,
			padding: { bottom: .5 },
			minWidth: 0,
			flex: 1
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary",
			weight: "medium",
			truncate: true
		}, source.title), /* @__PURE__ */ __dil.jsx("text", {
			size: "2xs",
			color: "tertiary",
			truncate: true
		}, source.date && source.time ? \\\`\\\${source.date} • \\\${source.time}\\\` : source.date || source.time)))));
	}

//#endregion
//#region src/EmailSources.dil.tsx
	function EmailSources({ sources, label }) {
		return /* @__PURE__ */ __dil.jsx(SourceCards, { label }, sources.map((source, index) => /* @__PURE__ */ __dil.jsx("carousel-item", {
			key: \\\`\\\${source.url ?? source.subject}-\\\${index}\\\`,
			maxWidth: 200
		}, source.url ? /* @__PURE__ */ __dil.jsx("link", {
			href: source.url,
			title: source.subject
		}, /* @__PURE__ */ __dil.jsx(EmailCard, { source })) : /* @__PURE__ */ __dil.jsx(EmailCard, { source }))));
	}
	function EmailCard({ source }) {
		const [hovered, setHovered] = DIL.useState(false);
		return /* @__PURE__ */ __dil.jsx("box", {
			radius: "lg",
			clip: true
		}, /* @__PURE__ */ __dil.jsx("badge", {
			color: hovered ? "var(--color-background-secondary-soft-alpha-hover)" : "secondary",
			variant: "soft",
			pill: false,
			padding: 0,
			onHover: source.url ? setHovered : void 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			gap: 2,
			align: "start",
			padding: 2,
			maxWidth: 200
		}, /* @__PURE__ */ __dil.jsx("box", {
			width: 20,
			height: 20,
			flex: "none",
			ariaHidden: true
		}, source.senderIcon ? /* @__PURE__ */ __dil.jsx("image", {
			src: source.senderIcon,
			alt: "",
			width: 20,
			height: 20,
			radius: "full",
			fit: "cover",
			fallback: /* @__PURE__ */ __dil.jsx(SenderInitial, { sender: source.sender })
		}) : /* @__PURE__ */ __dil.jsx(SenderInitial, { sender: source.sender })), /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			minWidth: 0,
			flex: 1
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary",
			weight: "medium",
			truncate: true
		}, source.subject), /* @__PURE__ */ __dil.jsx("text", {
			size: "2xs",
			color: "tertiary",
			truncate: true
		}, source.date ? \\\`\\\${source.date} • \\\${source.sender}\\\` : source.sender)))));
	}
	function SenderInitial({ sender }) {
		return /* @__PURE__ */ __dil.jsx("box", {
			width: 20,
			height: 20,
			radius: "full",
			background: "discovery-solid",
			align: "center",
			justify: "center"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "2xs",
			color: "white",
			weight: "medium"
		}, sender.slice(0, 1).toUpperCase()));
	}

//#endregion
//#region src/WebSearch.dil.tsx
	function useSearchFaviconUrl(urls, isActive) {
		const now = DIL.useNow(isActive && (urls?.length ?? 0) > 1);
		const firstUrl = DIL.useRef(urls?.[0]);
		const startedAt = DIL.useRef(now);
		const index = DIL.useRef(isActive ? 0 : (urls?.length ?? 0) - 1);
		if (firstUrl.current !== urls?.[0]) {
			firstUrl.current = urls?.[0];
			startedAt.current = now;
			index.current = isActive ? 0 : (urls?.length ?? 0) - 1;
		}
		if (isActive && urls != null) index.current = Math.min(Math.floor((now - startedAt.current) / 1500), urls.length - 1);
		return urls?.[Math.min(index.current, urls.length - 1)];
	}
	function SearchFavicon({ url }) {
		return /* @__PURE__ */ __dil.jsx("box", {
			width: 20,
			height: 20,
			align: "stretch",
			justify: "center",
			flex: "0 0 auto",
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("transition", {
			initial: { opacity: 0 },
			enter: {
				opacity: 1,
				duration: 100,
				delay: 0
			},
			exit: {
				opacity: 0,
				duration: 100,
				delay: 0
			},
			preventInitialTransition: true
		}, url != null && /* @__PURE__ */ __dil.jsx("favicon", {
			key: url,
			url,
			size: 20,
			frame: true
		})));
	}
	function WebSearchDetails({ item }) {
		const [allQueries, setAllQueries] = DIL.useState(false);
		const [allResources, setAllResources] = DIL.useState(false);
		const queries = item.queries ?? [];
		const resources = item.resources?.filter((resource) => resource.type === "web_search_source") ?? [];
		const queryOverflow = queries.length > 3 && item.moreQueriesLabel != null;
		const resourceOverflow = resources.length > 8 && item.moreResourcesLabel != null;
		return /* @__PURE__ */ __dil.jsx("row", {
			gap: 2,
			wrap: "wrap",
			align: "center",
			width: "100%"
		}, resources.length > 0 ? /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, (resourceOverflow && !allResources ? resources.slice(0, 7) : resources).map((source) => /* @__PURE__ */ __dil.jsx("link", {
			key: source.url,
			href: source.url,
			title: source.title
		}, /* @__PURE__ */ __dil.jsx(SearchPill, {
			key: \\\`source-pill-\\\${item.id}-\\\${source.url}\\\`,
			label: source.attribution,
			resources: [source],
			interactive: true
		}))), resourceOverflow && /* @__PURE__ */ __dil.jsx("pressable", {
			key: "resource-overflow",
			onClick: () => setAllResources(!allResources),
			ariaPressed: allResources
		}, /* @__PURE__ */ __dil.jsx(SearchPill, {
			label: allResources ? item.showLessLabel : item.moreResourcesLabel,
			resources: allResources ? void 0 : resources.slice(7, 10)
		}))) : /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, (queryOverflow && !allQueries ? queries.slice(0, 2) : queries).map((query) => /* @__PURE__ */ __dil.jsx(SearchPill, {
			key: \\\`query-pill-\\\${item.id}-\\\${query}\\\`,
			label: query,
			query: true
		})), queryOverflow && /* @__PURE__ */ __dil.jsx("pressable", {
			key: "query-overflow",
			onClick: () => setAllQueries(!allQueries),
			ariaPressed: allQueries
		}, /* @__PURE__ */ __dil.jsx(SearchPill, { label: allQueries ? item.showLessLabel : item.moreQueriesLabel }))), item.pattern != null && /* @__PURE__ */ __dil.jsx(SearchPill, {
			label: item.pattern,
			query: true
		}));
	}
	function SearchPill({ label, resources, query = false, interactive = false }) {
		const [hovered, setHovered] = DIL.useState(false);
		return /* @__PURE__ */ __dil.jsx("badge", {
			size: "lg",
			padding: {
				left: query || resources?.length ? 2 : 3,
				right: 3
			},
			maxWidth: "100%",
			weight: "normal",
			color: hovered ? "var(--color-background-secondary-soft-alpha-hover)" : "secondary",
			variant: "soft",
			onHover: interactive ? setHovered : void 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			gap: 1,
			align: "center",
			minWidth: 0
		}, query && /* @__PURE__ */ __dil.jsx("icon", {
			name: "search",
			size: "xs",
			color: "secondary"
		}), resources != null && /* @__PURE__ */ __dil.jsx("row", {
			gap: 0,
			flex: "none",
			ariaHidden: true
		}, resources.map((source, index) => /* @__PURE__ */ __dil.jsx("box", {
			key: source.url,
			width: index === resources.length - 1 ? 12 : 8,
			flex: "none"
		}, /* @__PURE__ */ __dil.jsx("favicon", {
			url: source.url,
			size: 12,
			frame: resources.length > 1
		})))), /* @__PURE__ */ __dil.jsx("box", {
			minWidth: 0,
			maxWidth: query ? "8rem" : void 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary",
			truncate: true
		}, label))));
	}

//#endregion
//#region src/CoTToolGroup.dil.tsx
	const nativeIconNames = {
		api_tool: "plug",
		"book-open": "book-open",
		"code-searching": "search",
		"edit-files": "pencil",
		finances: "chart-no-axes-combined",
		globe: "globe",
		library: "library",
		"list-files": "folder",
		"run-command": "terminal"
	};
	function ToolIcon({ icon, expanded, faviconUrl }) {
		if (icon.type === "favicons") return /* @__PURE__ */ __dil.jsx(SearchFavicon, { url: faviconUrl });
		return /* @__PURE__ */ __dil.jsx("box", {
			width: 20,
			height: 20,
			align: "center",
			justify: "center",
			flex: "0 0 auto",
			ariaHidden: true
		}, icon.type === "native" ? /* @__PURE__ */ __dil.jsx("icon", {
			name: nativeIconNames[icon.name],
			size: "lg",
			color: expanded && icon.name !== "globe" ? "primary" : "secondary"
		}) : /* @__PURE__ */ __dil.jsx("image", {
			src: icon.src,
			alt: "",
			width: 20,
			height: 20,
			fit: "contain",
			radius: icon.kind === "favicon" ? "full" : void 0,
			frame: icon.kind === "favicon",
			fallback: /* @__PURE__ */ __dil.jsx("icon", {
				name: icon.kind === "favicon" ? "globe" : "plug",
				size: "lg",
				color: "secondary"
			})
		}));
	}
	function ActivityLabel({ title, isActive, icon, expanded, onToggle }) {
		const [hovered, setHovered] = DIL.useState(false);
		const faviconUrl = useSearchFaviconUrl(icon?.type === "favicons" ? icon.urls : void 0, isActive);
		const Container = onToggle != null ? "pressable" : "box";
		const color = onToggle != null && hovered ? "primary" : "tertiary";
		return /* @__PURE__ */ __dil.jsx(Container, {
			direction: "row",
			align: "center",
			gap: 2,
			maxWidth: "100%",
			ariaLabel: onToggle != null ? title : void 0,
			onClick: onToggle,
			onHover: onToggle != null ? setHovered : void 0
		}, icon != null && /* @__PURE__ */ __dil.jsx(ToolIcon, {
			icon,
			expanded,
			faviconUrl
		}), /* @__PURE__ */ __dil.jsx("row", {
			gap: 1,
			align: "center",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("box", {
			minWidth: 0,
			ariaHidden: onToggle != null
		}, isActive && (onToggle == null || !hovered) ? /* @__PURE__ */ __dil.jsx("shimmer-text", {
			size: "md",
			color,
			weight: "normal",
			truncate: true
		}, title) : /* @__PURE__ */ __dil.jsx("text", {
			size: "md",
			color,
			weight: "normal",
			truncate: true
		}, title)), onToggle != null && /* @__PURE__ */ __dil.jsx("box", {
			width: 16,
			height: 16,
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("transition", {
			initial: {
				rotate: expanded ? -90 : 90,
				opacity: 1
			},
			enter: {
				rotate: 0,
				opacity: 1,
				duration: 150,
				delay: 0
			},
			exit: {
				opacity: 0,
				duration: 0,
				delay: 0
			},
			layoutEnter: {
				duration: 0,
				delay: 0
			},
			layoutExit: {
				duration: 0,
				delay: 0
			},
			layoutMove: {
				duration: 0,
				delay: 0
			},
			preventInitialTransition: true
		}, /* @__PURE__ */ __dil.jsx("box", {
			key: expanded ? "expanded" : "collapsed",
			width: 16,
			height: 16,
			align: "center",
			justify: "center"
		}, (expanded || hovered) && /* @__PURE__ */ __dil.jsx("icon", {
			name: expanded ? "chevron-down" : "chevron-right",
			size: "sm",
			color
		}))))));
	}
	function CoTToolGroup() {
		const data = DIL.useAppData((data$1) => data$1);
		const [expanded, setExpanded] = DIL.useState(false);
		const headerItem = data.isActive ? data.items[data.items.length - 1] : void 0;
		const currentStatus = data.isActive ? data.current_status : void 0;
		const singleItem = data.items.length === 1 ? data.items[0] : null;
		if (singleItem != null) return /* @__PURE__ */ __dil.jsx(Activity, {
			key: singleItem.id,
			item: singleItem,
			currentStatus,
			isActive: data.isActive,
			autoExpand: data.isActive,
			indentDetails: true
		});
		const groupContent = expanded ? /* @__PURE__ */ __dil.jsx(NestedContent, {
			key: "tool-group-content",
			indentItems: true
		}, data.items.map((item, index) => /* @__PURE__ */ __dil.jsx(Activity, {
			key: item.id,
			item,
			isActive: item.isActive,
			autoExpand: data.isActive && index === data.items.length - 1
		}))) : headerItem != null && hasResourceCards(headerItem) ? /* @__PURE__ */ __dil.jsx(NestedContent, { key: \\\`tool-group-header-details-\\\${headerItem.id}\\\` }, /* @__PURE__ */ __dil.jsx(ActivityDetails, {
			item: headerItem,
			topPadding: 0,
			withGuide: true
		})) : false;
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			align: "start",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx(ActivityLabel, {
			title: currentStatus ?? data.title,
			isActive: data.isActive,
			icon: data.icon,
			expanded,
			onToggle: data.items.length > 0 ? () => setExpanded(!expanded) : void 0
		}), /* @__PURE__ */ __dil.jsx(ExpandableContent, {
			revealAfterResize: headerItem != null && hasResourceCards(headerItem),
			slideUpOnEnter: !expanded && headerItem != null && hasResourceCards(headerItem),
			slideDownOnExit: expanded && headerItem != null && hasResourceCards(headerItem)
		}, groupContent));
	}
	function Activity({ item, currentStatus, isActive, autoExpand = false, indentDetails = false }) {
		const [userExpanded, setUserExpanded] = DIL.useState(false);
		const hasDetails = hasActivityDetails(item);
		const expanded = hasDetails && (autoExpand || userExpanded);
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 0,
			align: "start",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx(ActivityLabel, {
			title: currentStatus ?? item.label,
			isActive,
			icon: item.icon,
			expanded,
			onToggle: hasDetails && !autoExpand ? () => setUserExpanded(!userExpanded) : void 0
		}), hasDetails && /* @__PURE__ */ __dil.jsx(ExpandableContent, null, expanded && /* @__PURE__ */ __dil.jsx(NestedContent, {
			key: "activity-details",
			topPadding: indentDetails ? 3 : 0,
			bottomPadding: indentDetails ? 3 : 0,
			showGuide: indentDetails
		}, /* @__PURE__ */ __dil.jsx(ActivityDetails, {
			item,
			topPadding: indentDetails ? 0 : 3,
			withGuide: indentDetails
		}))));
	}
	function NestedContent({ children, topPadding = 3, bottomPadding = 0, indentItems = false, showGuide = true }) {
		return /* @__PURE__ */ __dil.jsx("row", {
			width: "100%",
			gap: showGuide ? 1 : 0,
			align: "stretch",
			padding: {
				top: topPadding,
				bottom: bottomPadding
			}
		}, /* @__PURE__ */ __dil.jsx("row", {
			width: 20,
			flex: "0 0 auto",
			justify: "center",
			gap: 0,
			ariaHidden: true
		}, showGuide && /* @__PURE__ */ __dil.jsx("divider", {
			color: "default",
			spacing: 0
		})), /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			flex: 1,
			minWidth: 0,
			padding: {
				left: indentItems ? 2 : 0,
				bottom: indentItems ? 2 : 0
			}
		}, children));
	}
	function ActivityDetails({ item, topPadding = 3, withGuide }) {
		const search = item.type === "web_search" ? item : void 0;
		const emails = item.resources?.filter((resource) => resource.type === "email_source");
		const events = item.resources?.filter((resource) => resource.type === "calendar_source");
		const hasSourceCards = !!emails?.length || !!events?.length;
		return /* @__PURE__ */ __dil.jsx("box", {
			padding: {
				top: topPadding,
				left: hasSourceCards || search != null ? withGuide ? 1 : 2 : 0,
				right: hasSourceCards ? 4 : 0
			},
			width: "100%"
		}, search != null && /* @__PURE__ */ __dil.jsx(WebSearchDetails, { item: search }), !!emails?.length && /* @__PURE__ */ __dil.jsx(EmailSources, {
			sources: emails,
			label: item.label
		}), !!events?.length && /* @__PURE__ */ __dil.jsx(CalendarSources, {
			sources: events,
			label: item.label
		}));
	}
	function hasActivityDetails(item) {
		return hasResourceCards(item) || item.type === "web_search" && (!!item.queries?.length || item.pattern != null);
	}
	function hasResourceCards(item) {
		return !!item.resources?.some((resource) => resource.type === "email_source" || resource.type === "calendar_source" || item.type === "web_search" && resource.type === "web_search_source");
	}
	function ExpandableContent({ children, revealAfterResize = false, slideUpOnEnter = false, slideDownOnExit = false }) {
		return /* @__PURE__ */ __dil.jsx("box", { width: "100%" }, /* @__PURE__ */ __dil.jsx("transition", {
			dimension: "height",
			initial: {
				opacity: revealAfterResize ? 0 : 1,
				translateY: slideUpOnEnter ? 4 : 0
			},
			enter: {
				opacity: 1,
				translateY: 0,
				duration: slideUpOnEnter ? 200 : revealAfterResize ? 150 : 0,
				delay: slideUpOnEnter ? 100 : revealAfterResize ? 300 : 0
			},
			exit: {
				opacity: revealAfterResize ? 0 : 1,
				translateY: slideDownOnExit ? 4 : 0,
				duration: slideUpOnEnter ? 100 : slideDownOnExit ? 150 : 0,
				delay: 0
			},
			layoutEnter: {
				duration: 300,
				delay: 0,
				timingFunction: "ease-in-out"
			},
			layoutExit: {
				duration: 300,
				delay: 0,
				timingFunction: "ease-in-out"
			},
			layoutMove: {
				duration: revealAfterResize ? 300 : 0,
				delay: 0,
				timingFunction: "ease-in-out"
			},
			hideOverflow: true,
			preventInitialTransition: true
		}, children));
	}

//#endregion
return CoTToolGroup;
})();
return __dilDefaultExport;
})()\`,CodeBlock:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentCodeBlock(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "CodeBlock",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "CodeBlock", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentCodeBlock, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region CodeBlock.dil.tsx
	function CodeBlock({ content, language }) {
		return /* @__PURE__ */ __dil.jsx("card", { size: "full" }, /* @__PURE__ */ __dil.jsx("col", { gap: 2 }, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm",
			weight: "medium"
		}, language ?? "code"), /* @__PURE__ */ __dil.jsx("box", {
			background: "surface-secondary",
			padding: 3,
			radius: "md"
		}, /* @__PURE__ */ __dil.jsx("text", {
			preserveWhitespace: true,
			size: "sm"
		}, content))));
	}

//#endregion
return CodeBlock;
})();
return __dilDefaultExport;
})()))\`,CodeCite:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentCodeCite(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "CodeCite",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "CodeCite", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentCodeCite, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region CodeCite.dil.tsx
	function ResolvedCodeCite({ componentKey, state }) {
		const isMobile = DIL.useIsMobile();
		const [hovered, setHovered] = DIL.useState(false);
		const label = state.display_label;
		const openCitation = () => GenUI.dispatchAction({
			handler: "client",
			type: "open_coding_citation",
			payload: { component_key: componentKey }
		});
		return /* @__PURE__ */ __dil.jsx("popover", {
			hoverOpenDelay: 0,
			showOnHover: true
		}, /* @__PURE__ */ __dil.jsx("popover-trigger", { onClick: openCitation }, /* @__PURE__ */ __dil.jsx("badge", {
			color: hovered ? {
				light: "#e8e8e8",
				dark: "gray-300"
			} : {
				light: "gray-75",
				dark: "gray-400"
			},
			onHover: setHovered,
			padding: {
				x: 1,
				y: 1
			},
			size: "sm",
			variant: "soft",
			weight: "normal"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			ariaLabel: label,
			role: "img"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "secondary",
			name: "file-code",
			size: "md"
		})))), /* @__PURE__ */ __dil.jsx("popover-content", {
			align: "start",
			side: "bottom",
			sideOffset: 4
		}, /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			maxWidth: "100%",
			padding: 3,
			width: isMobile ? "100%" : 324
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: label,
			gap: 2,
			onClick: openCitation
		}, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "xs",
			weight: "medium"
		}, state.preview_label), /* @__PURE__ */ __dil.jsx("divider", null), /* @__PURE__ */ __dil.jsx("box", {
			background: "surface-tertiary",
			padding: 2,
			radius: "md"
		}, /* @__PURE__ */ __dil.jsx("code", null, state.highlighted_text))))));
	}
	function CodeCite(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("CodeCite", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading code citation" });
		return state.highlighted_text ? /* @__PURE__ */ __dil.jsx(ResolvedCodeCite, {
			componentKey: props.__resolutionId ?? componentDataKey("CodeCite", props),
			state
		}) : null;
	}

//#endregion
return CodeCite;
})();
return __dilDefaultExport;
})()))\`,Entity:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentEntity(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "Entity",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "Entity", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentEntity, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region Entity.dil.tsx
	function Entity(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("Entity", props);
		const isMobile = DIL.useIsMobile();
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading entity" });
		const onClick = () => state.click_action ? GenUI.dispatchAction(state.click_action) : state.action_payload ? GenUI.dispatchAction({
			handler: "client",
			type: "open_entity_detail",
			payload: state.action_payload
		}) : GenUI.openEntityDetail(props.category ?? "ask_sidebar", props.query ?? state.value);
		const entity = state.entity_data;
		if (!isMobile && state.action_payload != null && entity != null) {
			const name = entity.name || state.value;
			const categories = entity.categories?.filter(Boolean) ?? [];
			const hasRating = typeof entity.rating === "number" && Number.isFinite(entity.rating);
			const hasPrice = Boolean(entity.price_str);
			const hasOpenStatus = typeof entity.is_open === "boolean";
			const directionsUrl = state.directions_url;
			const legacyWebsiteUrl = entity.website_url;
			const legacyWebsiteMatch = typeof legacyWebsiteUrl === "string" ? /^https:\\\\/\\\\/(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\\\.)+(?:[a-z]{2,63}|xn--[a-z0-9](?:[a-z0-9-]{0,57}[a-z0-9])?)(?::(\\\\d{1,5}))?(?:[/?#][^\\\\s\\\\\\\\]*)?$/i.exec(legacyWebsiteUrl) : null;
			const websiteUrl = state.website_url ?? (legacyWebsiteMatch && (!legacyWebsiteMatch[1] || Number(legacyWebsiteMatch[1]) <= 65535) ? legacyWebsiteUrl : void 0);
			return /* @__PURE__ */ __dil.jsx("popover", {
				hoverOpenDelay: 150,
				showOnHover: true
			}, /* @__PURE__ */ __dil.jsx("popover-trigger", { onClick }, /* @__PURE__ */ __dil.jsx("text", {
				inline: true,
				underline: "dotted"
			}, state.value)), /* @__PURE__ */ __dil.jsx("popover-content", {
				align: "center",
				side: "top",
				sideOffset: 8
			}, /* @__PURE__ */ __dil.jsx("col", {
				gap: 3,
				maxWidth: "100%",
				padding: 4,
				width: 420
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "start",
				gap: 3,
				wrap: "nowrap"
			}, state.image_url ? /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`View details for \\\${name}\\\`,
				onClick
			}, /* @__PURE__ */ __dil.jsx("image", {
				alt: name,
				fit: "cover",
				height: 96,
				hideOnFailure: true,
				radius: "xl",
				src: state.image_url,
				width: 96
			})) : null, /* @__PURE__ */ __dil.jsx("col", {
				flex: 1,
				gap: 1,
				minWidth: 0
			}, /* @__PURE__ */ __dil.jsx("pressable", {
				ariaLabel: \\\`View details for \\\${name}\\\`,
				maxWidth: "100%",
				onClick,
				width: "fit-content"
			}, /* @__PURE__ */ __dil.jsx("text", {
				inline: true,
				maxLines: 1,
				size: "lg",
				weight: "semibold"
			}, name)), hasRating || categories.length > 0 ? /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 1,
				wrap: "wrap"
			}, hasRating ? /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 1,
				wrap: "nowrap"
			}, /* @__PURE__ */ __dil.jsx("icon", {
				color: "primary",
				name: "star-filled",
				size: "sm"
			}), /* @__PURE__ */ __dil.jsx("text", {
				inline: true,
				size: "md"
			}, Math.round(entity.rating * 10) / 10)) : null, hasRating && categories.length > 0 ? /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				inline: true,
				size: "md"
			}, "•") : null, categories.length > 0 ? /* @__PURE__ */ __dil.jsx("text", {
				inline: true,
				maxLines: 1,
				size: "md"
			}, categories.join(", ")) : null) : null, hasPrice || hasOpenStatus ? /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 1,
				wrap: "wrap"
			}, hasPrice ? /* @__PURE__ */ __dil.jsx("text", {
				inline: true,
				size: "md"
			}, entity.price_str) : null, hasPrice && hasOpenStatus ? /* @__PURE__ */ __dil.jsx("text", {
				color: "secondary",
				inline: true,
				size: "md"
			}, "•") : null, hasOpenStatus ? /* @__PURE__ */ __dil.jsx("text", {
				color: entity.is_open ? "success" : "secondary",
				inline: true,
				size: "md"
			}, entity.is_open ? "Open" : "Closed") : null) : null)), directionsUrl || websiteUrl ? /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2,
				width: "100%",
				wrap: "nowrap"
			}, directionsUrl ? /* @__PURE__ */ __dil.jsx("button", {
				block: true,
				color: "secondary",
				onClick: () => GenUI.openUrl(directionsUrl),
				size: "md",
				variant: "outline"
			}, "Directions") : null, websiteUrl ? /* @__PURE__ */ __dil.jsx("button", {
				block: true,
				color: "secondary",
				onClick: () => GenUI.openUrl(websiteUrl),
				size: "md",
				variant: "outline"
			}, "Website") : null) : null)));
		}
		return /* @__PURE__ */ __dil.jsx("pressable", {
			inline: true,
			onClick
		}, /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			underline: "dotted"
		}, state.value));
	}

//#endregion
return Entity;
})();
return __dilDefaultExport;
})()))\`,FileCite:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFileCite(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FileCite",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FileCite", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFileCite, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FileCite.dil.tsx
	function storedLocationLabel(payload) {
		const page = payload?.page_range_start;
		const lastPage = payload?.page_range_end;
		if (typeof page === "number" && Number.isInteger(page) && page > 0) return typeof lastPage === "number" && Number.isInteger(lastPage) && lastPage > page ? \\\`Pages \\\${page}–\\\${lastPage}\\\` : \\\`Page \\\${page}\\\`;
		const line = payload?.input_pointer?.line_range_start;
		const lastLine = payload?.input_pointer?.line_range_end;
		if (typeof line === "number" && Number.isInteger(line) && line >= 0) return typeof lastLine === "number" && Number.isInteger(lastLine) && lastLine > line ? \\\`Lines \\\${line}–\\\${lastLine}\\\` : \\\`Line \\\${line}\\\`;
		return null;
	}
	function ResolvedFileCite({ state }) {
		const isMobile = DIL.useIsMobile();
		const isSm = DIL.useBreakpoint("sm");
		const [hovered, setHovered] = DIL.useState(false);
		const name = state.file_name ?? "Document";
		const payload = state.file_action_payload;
		const snippet = typeof payload?.snippet === "string" ? payload.snippet : typeof payload?.text === "string" ? payload.text : null;
		const locationLabel = storedLocationLabel(payload);
		const openFile = () => {
			if (payload) GenUI.dispatchAction({
				handler: "client",
				type: "open_file_citation",
				payload
			});
			else if (state.safe_file_url) GenUI.openUrl(state.safe_file_url);
		};
		return /* @__PURE__ */ __dil.jsx("popover", {
			hoverOpenDelay: 80,
			showOnHover: true
		}, /* @__PURE__ */ __dil.jsx("popover-trigger", { onClick: () => !isMobile && isSm ? openFile() : void 0 }, /* @__PURE__ */ __dil.jsx("badge", {
			color: hovered ? {
				light: "#e8e8e8",
				dark: "gray-300"
			} : {
				light: "gray-75",
				dark: "gray-400"
			},
			onHover: setHovered,
			padding: {
				left: 1,
				right: 1.5,
				y: 1
			},
			size: "sm",
			variant: "soft",
			weight: "normal"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "secondary",
			name: "document",
			size: "sm"
		}), /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			inline: true,
			maxLines: 1,
			size: "3xs",
			truncate: true
		}, name))), /* @__PURE__ */ __dil.jsx("popover-content", {
			align: "start",
			side: "bottom",
			sideOffset: 8
		}, /* @__PURE__ */ __dil.jsx("col", {
			gap: 2,
			maxWidth: "100%",
			padding: 4,
			width: isMobile ? "100%" : 345
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`Open \\\${name}\\\`,
			gap: 2,
			onClick: openFile
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "secondary",
			name: "document",
			size: "md"
		}), /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 2,
			size: "sm",
			weight: "semibold"
		}, name)), locationLabel ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "xs"
		}, locationLabel) : null, snippet ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 6,
			size: "sm"
		}, snippet) : null))));
	}
	function FileCite(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("FileCite", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading file citation" });
		return state.file_name ? /* @__PURE__ */ __dil.jsx(ResolvedFileCite, { state }) : null;
	}

//#endregion
return FileCite;
})();
return __dilDefaultExport;
})()))\`,FileNavList:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFileNavList(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FileNavList",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FileNavList", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFileNavList, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FileNavList.dil.tsx
	function ResolvedFileNavList({ componentKey, items }) {
		const isSm = DIL.useBreakpoint("sm");
		return /* @__PURE__ */ __dil.jsx("row", {
			gap: 2,
			width: "100%",
			wrap: "wrap"
		}, items.map((item) => /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: item.name,
			key: item.id + ":" + item.item_index,
			onClick: () => GenUI.dispatchAction({
				handler: "client",
				type: "open_file_navlist_item",
				payload: {
					component_key: componentKey,
					item_index: item.item_index
				}
			}),
			width: isSm ? 320 : 205
		}, /* @__PURE__ */ __dil.jsx("card", {
			background: "surface-primary",
			padding: 2.5,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			minWidth: 0,
			width: "100%",
			wrap: "nowrap"
		}, /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			ariaHidden: true,
			flex: "0 0 auto",
			height: 40,
			justify: "center",
			width: 40
		}, /* @__PURE__ */ __dil.jsx("icon", {
			color: "secondary",
			name: "document",
			size: "2xl"
		})), /* @__PURE__ */ __dil.jsx("col", {
			flex: 1,
			gap: .5,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 1,
			size: "sm",
			truncate: true,
			weight: "semibold"
		}, item.name), /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 1,
			size: "sm",
			truncate: true
		}, item.description)))))));
	}
	function FileNavList(props) {
		const hideInaccessibleFiles = DIL.useAppData((appData) => appData.opGenui?.hideInaccessibleFiles === true);
		const { resolutionComplete, state } = useResolvedComponentResult("FileNavList", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading files" });
		const items = state.items?.map((item, item_index) => ({
			...item,
			item_index
		})).filter((item) => item.id && item.name && item.is_actionable && (!hideInaccessibleFiles || item.safe_file_url)) ?? [];
		if (items.length === 0) return null;
		return /* @__PURE__ */ __dil.jsx(ResolvedFileNavList, {
			componentKey: componentDataKey("FileNavList", props),
			items
		});
	}

//#endregion
return FileNavList;
})();
return __dilDefaultExport;
})()))\`,FlightCard:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFlightCard(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FlightCard",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FlightCard", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFlightCard, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FlightCard.dil.tsx
	function FlightCard(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("FlightCard", props);
		const isMobile = DIL.useIsMobile();
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading flight" });
		return /* @__PURE__ */ __dil.jsx("card", {
			background: "surface",
			gap: 4,
			padding: 5,
			size: "sm"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "start",
			gap: 3,
			justify: "between",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("col", {
			flex: 1,
			gap: .5,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1.5,
			minWidth: 0
		}, state.airline_logo_url ? /* @__PURE__ */ __dil.jsx("image", {
			alt: state.airline_logo_alt,
			fit: "contain",
			height: 18,
			hideOnFailure: true,
			radius: "full",
			src: state.airline_logo_url,
			width: 18
		}) : null, /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 1,
			size: "md",
			truncate: true,
			weight: "medium"
		}, state.airline_name)), state.operating_airlines_label ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm"
		}, state.operating_airlines_label) : null, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 1,
			size: "sm",
			truncate: true
		}, state.trip_summary_label)), state.price_label ? /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 1,
			size: "lg",
			textAlign: "end",
			weight: "semibold"
		}, state.price_label) : null), /* @__PURE__ */ __dil.jsx("row", {
			align: "start",
			gap: 3,
			width: "100%",
			wrap: "nowrap"
		}, /* @__PURE__ */ __dil.jsx("col", {
			flex: 1,
			gap: .5,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: isMobile ? "md" : "lg",
			weight: "semibold"
		}, state.departure_time_label), /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm",
			weight: "medium"
		}, state.departure_airport_code)), /* @__PURE__ */ __dil.jsx("col", {
			align: "center",
			flex: 1,
			gap: 0,
			justify: "center",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1,
			height: 25,
			justify: "between",
			width: "100%"
		}, [
			...[
				0,
				1,
				2
			].map((index) => /* @__PURE__ */ __dil.jsx("box", {
				background: "border-subtle",
				key: \\\`outbound-dot-\\\${index}\\\`,
				radius: "full",
				size: 4
			})),
			...state.duration_label ? [/* @__PURE__ */ __dil.jsx("box", { key: "flight-duration" }, /* @__PURE__ */ __dil.jsx("text", {
				maxLines: 1,
				size: "xs",
				weight: "medium"
			}, state.duration_label))] : [],
			...[
				0,
				1,
				2
			].map((index) => /* @__PURE__ */ __dil.jsx("box", {
				background: "border-subtle",
				key: \\\`arrival-dot-\\\${index}\\\`,
				radius: "full",
				size: 4
			}))
		])), /* @__PURE__ */ __dil.jsx("col", {
			align: "end",
			flex: 1,
			gap: .5,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: isMobile ? "md" : "lg",
			textAlign: "end",
			weight: "semibold"
		}, state.arrival_time_label), /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm",
			textAlign: "end",
			weight: "medium"
		}, state.arrival_airport_code))), state.booking_urls.length ? /* @__PURE__ */ __dil.jsx("col", {
			gap: 4,
			width: "100%"
		}, state.booking_urls.map((url) => /* @__PURE__ */ __dil.jsx("button", {
			block: true,
			color: "secondary",
			key: url,
			onClick: () => GenUI.openUrl(url),
			pill: true,
			size: "lg",
			variant: "outline"
		}, state.select_flight_label))) : null);
	}

//#endregion
return FlightCard;
})();
return __dilDefaultExport;
})()))\`,FlightCarousel:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFlightCarousel(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FlightCarousel",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FlightCarousel", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFlightCarousel, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FlightCarousel.dil.tsx
	function FlightCarousel(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("FlightCarousel", props);
		const isMobile = DIL.useIsMobile();
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading flights" });
		return /* @__PURE__ */ __dil.jsx("carousel", {
			ariaLabel: state.aria_label,
			gap: 4
		}, state.items.map((item) => /* @__PURE__ */ __dil.jsx("carousel-item", {
			key: item.candidate_id,
			variant: "none",
			width: isMobile ? "84%" : 360
		}, /* @__PURE__ */ __dil.jsx("card", {
			background: "surface",
			gap: 4,
			height: "100%",
			padding: 5,
			size: "sm",
			width: "100%"
		}, item.title ? /* @__PURE__ */ __dil.jsx("title", {
			size: "lg",
			weight: "semibold"
		}, item.title) : null, /* @__PURE__ */ __dil.jsx("col", {
			border: { left: {
				size: 1,
				color: "subtle"
			} },
			gap: 2,
			padding: { left: 3 },
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1.5,
			minWidth: 0
		}, item.airline_logo_url ? /* @__PURE__ */ __dil.jsx("image", {
			alt: item.airline_logo_alt,
			fit: "contain",
			height: 18,
			hideOnFailure: true,
			radius: "full",
			src: item.airline_logo_url,
			width: 18
		}) : null, /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 1,
			size: "md",
			truncate: true
		}, item.airline_name), item.duration_label ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 1,
			size: "md"
		}, "· " + item.duration_label) : null), item.operating_airlines_label ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm"
		}, item.operating_airlines_label) : null, /* @__PURE__ */ __dil.jsx("title", {
			size: "lg",
			weight: "semibold"
		}, item.departure_time_label + " → " + item.arrival_time_label), item.price_label ? /* @__PURE__ */ __dil.jsx("text", { size: "md" }, item.price_label) : null), item.commentary ? /* @__PURE__ */ __dil.jsx("text", { size: "md" }, item.commentary) : null, item.booking_urls.length ? /* @__PURE__ */ __dil.jsx("col", {
			flex: 1,
			gap: 4,
			justify: "end",
			width: "100%"
		}, item.booking_urls.map((url) => /* @__PURE__ */ __dil.jsx("button", {
			block: true,
			color: "secondary",
			key: url,
			onClick: () => GenUI.openUrl(url),
			pill: true,
			size: "lg",
			variant: "outline"
		}, state.select_flight_label))) : null))));
	}

//#endregion
return FlightCarousel;
})();
return __dilDefaultExport;
})()))\`,FlightTracker:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFlightTracker(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FlightTracker",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FlightTracker", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFlightTracker, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FlightTracker.dil.tsx
	function FlightDetails({ details, isDesktop, arrival }) {
		return /* @__PURE__ */ __dil.jsx("grid", {
			columns: isDesktop ? 3 : [
				1.4,
				1,
				1
			],
			gap: isDesktop ? 4 : 3
		}, details.map((detail, index) => {
			const alignEnd = isDesktop ? arrival : index > 0;
			return /* @__PURE__ */ __dil.jsx("grid-item", { key: index }, /* @__PURE__ */ __dil.jsx("col", {
				gap: .5,
				align: alignEnd ? "end" : "start"
			}, /* @__PURE__ */ __dil.jsx("caption", {
				size: "sm",
				color: "secondary",
				textAlign: alignEnd ? "end" : "start"
			}, detail.title), /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				weight: "medium",
				textAlign: alignEnd ? "end" : "start"
			}, detail.value)));
		}));
	}
	function ResolvedFlightTracker({ state }) {
		const isDesktop = DIL.useBreakpoint("sm");
		const completedDots = isDesktop ? state.completed_progress_dot_count : state.mobile_completed_progress_dot_count;
		const progressLeft = isDesktop ? state.flight_progress_left : state.mobile_flight_progress_left;
		const progressDots = isDesktop ? [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7,
			8,
			9
		] : [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7
		];
		const departureDetails = [
			{
				title: state.departure_detail_title,
				value: state.departure_detail_value
			},
			{
				title: state.departure_terminal_title,
				value: state.departure_terminal_value
			},
			{
				title: state.departure_gate_title,
				value: state.departure_gate_value
			}
		];
		const arrivalDetails = [
			{
				title: state.arrival_detail_title,
				value: state.arrival_detail_value
			},
			{
				title: state.arrival_terminal_title,
				value: state.arrival_terminal_value
			},
			{
				title: state.arrival_gate_title,
				value: state.arrival_gate_value
			}
		];
		return /* @__PURE__ */ __dil.jsx("card", {
			background: "surface",
			size: "full",
			padding: 0
		}, /* @__PURE__ */ __dil.jsx("col", { gap: 0 }, /* @__PURE__ */ __dil.jsx("box", { padding: {
			x: 5,
			y: 4
		} }, /* @__PURE__ */ __dil.jsx("col", { gap: 3 }, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			flex: "auto",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium",
			truncate: true
		}, state.header_label)), /* @__PURE__ */ __dil.jsx("badge", {
			color: state.badge_color,
			variant: "soft",
			size: "sm"
		}, state.badge_label)), /* @__PURE__ */ __dil.jsx("col", { gap: 1.5 }, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 4
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: isDesktop ? "xl" : "lg",
			weight: "medium"
		}, state.origin_code), /* @__PURE__ */ __dil.jsx("col", {
			flex: "auto",
			align: "center",
			justify: "center",
			gap: 0,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			justify: "center",
			width: "100%",
			height: 28
		}, /* @__PURE__ */ __dil.jsx("box", {
			width: "100%",
			maxWidth: "400px",
			height: "100%",
			gap: 0
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			justify: "between",
			width: "100%",
			height: "100%"
		}, progressDots.flatMap((item) => [!state.show_progress_plane && state.progress_center_label !== "" && item === progressDots.length / 2 && /* @__PURE__ */ __dil.jsx("box", {
			key: "duration",
			background: "surface",
			padding: { x: 1 },
			flex: "none"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			weight: "medium"
		}, state.progress_center_label)), state.show_progress_plane && progressLeft !== "" && item === completedDots ? /* @__PURE__ */ __dil.jsx("box", {
			key: item,
			width: 4,
			height: 28,
			align: "center",
			justify: "center"
		}, /* @__PURE__ */ __dil.jsx("box", {
			width: 28,
			height: 28,
			align: "center",
			justify: "center",
			background: "surface",
			radius: "full"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "plane",
			size: "2xl",
			color: "default"
		}))) : /* @__PURE__ */ __dil.jsx("box", {
			key: item,
			width: 4,
			height: 4,
			radius: "full",
			background: item < completedDots ? "surface-inverted" : "border-subtle"
		})]))))), /* @__PURE__ */ __dil.jsx("title", {
			size: isDesktop ? "xl" : "lg",
			weight: "medium",
			textAlign: "end"
		}, state.destination_code)), /* @__PURE__ */ __dil.jsx("row", {
			align: "start",
			gap: 4
		}, /* @__PURE__ */ __dil.jsx("col", {
			gap: .5,
			flex: 1,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium",
			maxLines: 2
		}, state.origin_city), /* @__PURE__ */ __dil.jsx("row", {
			align: "baseline",
			gap: 1,
			wrap: "wrap"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: isDesktop ? "md" : "sm",
			weight: "medium",
			color: state.departure_time_color
		}, state.departure_time_label), state.departure_scheduled_time_label !== "" && /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary",
			lineThrough: true
		}, state.departure_scheduled_time_label))), /* @__PURE__ */ __dil.jsx("col", {
			gap: .5,
			align: "end",
			flex: 1,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium",
			textAlign: "end",
			maxLines: 2
		}, state.destination_city), /* @__PURE__ */ __dil.jsx("row", {
			align: "baseline",
			gap: 1,
			wrap: "wrap",
			justify: "end"
		}, state.arrival_scheduled_time_label !== "" && /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary",
			textAlign: "end",
			lineThrough: true
		}, state.arrival_scheduled_time_label), /* @__PURE__ */ __dil.jsx("text", {
			size: isDesktop ? "md" : "sm",
			weight: "medium",
			textAlign: "end",
			color: state.arrival_time_color
		}, state.arrival_time_label))))))), /* @__PURE__ */ __dil.jsx("divider", {
			flush: true,
			color: "subtle"
		}), /* @__PURE__ */ __dil.jsx("box", { padding: {
			x: 5,
			y: 3
		} }, /* @__PURE__ */ __dil.jsx("row", {
			align: "baseline",
			gap: .5,
			wrap: "wrap"
		}, state.summary_lead !== "" && /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium"
		}, state.summary_lead), state.summary_emphasis !== "" && /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium",
			color: state.summary_emphasis_color
		}, state.summary_emphasis), state.summary_trail !== "" && /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "medium"
		}, state.summary_trail))), /* @__PURE__ */ __dil.jsx("divider", {
			flush: true,
			color: "subtle"
		}), /* @__PURE__ */ __dil.jsx("box", { padding: {
			x: 5,
			y: 4
		} }, /* @__PURE__ */ __dil.jsx("grid", {
			columns: isDesktop ? 2 : 1,
			gap: isDesktop ? 8 : 4
		}, /* @__PURE__ */ __dil.jsx("grid-item", null, /* @__PURE__ */ __dil.jsx(FlightDetails, {
			details: departureDetails,
			isDesktop,
			arrival: false
		})), /* @__PURE__ */ __dil.jsx("grid-item", null, /* @__PURE__ */ __dil.jsx(FlightDetails, {
			details: arrivalDetails,
			isDesktop,
			arrival: true
		})))), /* @__PURE__ */ __dil.jsx("divider", {
			flush: true,
			color: "subtle"
		}), /* @__PURE__ */ __dil.jsx("box", { padding: {
			x: 5,
			y: 4
		} }, /* @__PURE__ */ __dil.jsx("text", {
			size: "xs",
			color: "secondary"
		}, state.attribution_label))));
	}
	function FlightTracker(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("FlightTracker", props);
		if (state?.is_loading === true || !state && !resolutionComplete) return /* @__PURE__ */ __dil.jsx("loading-block", {
			width: "100%",
			height: 376
		});
		if (!state) return props.fallback ?? null;
		return /* @__PURE__ */ __dil.jsx(ResolvedFlightTracker, { state });
	}

//#endregion
return FlightTracker;
})();
return __dilDefaultExport;
})()))\`,FollowUp:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFollowUp(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FollowUp",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FollowUp", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFollowUp, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region FollowUp.dil.tsx
	function FollowUp({ query, value }) {
		return /* @__PURE__ */ __dil.jsx("pressable", {
			inline: true,
			onClick: () => GenUI.issueNewTurn(query ?? value)
		}, /* @__PURE__ */ __dil.jsx("text", { inline: true }, /* @__PURE__ */ __dil.jsx("icon", {
			inline: true,
			name: "arrow-curved"
		}), " ", /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			underline: "dotted"
		}, value)));
	}

//#endregion
return FollowUp;
})();
return __dilDefaultExport;
})()))\`,FollowUpActionBar:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentFollowUpActionBar(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "FollowUpActionBar",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "FollowUpActionBar", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentFollowUpActionBar, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region internal/FollowUpActionBar.dil.tsx
	function FollowUpFooter({ actions, onAction }) {
		const isSm = DIL.useBreakpoint("sm");
		const isXs = DIL.useBreakpoint("xs");
		const visibleActions = actions.slice(0, isSm ? 3 : isXs ? 2 : 1);
		return actions.length ? /* @__PURE__ */ __dil.jsx("box", { width: "100%" }, /* @__PURE__ */ __dil.jsx("box", { padding: {
			x: 5,
			y: 3
		} }, /* @__PURE__ */ __dil.jsx("divider", null)), /* @__PURE__ */ __dil.jsx("box", { padding: {
			bottom: 5,
			left: 5,
			right: 5
		} }, /* @__PURE__ */ __dil.jsx("box", {
			background: "surface-secondary",
			border: {
				color: "alpha-12",
				size: 1
			},
			padding: {
				x: .5,
				y: .5
			},
			radius: "lg"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			ariaLabel: "Suggested follow-ups",
			gap: 0,
			role: "group",
			width: "100%"
		}, visibleActions.map((action, index) => /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			direction: "row",
			flex: 1,
			key: \\\`\\\${action.query}:\\\${index}\\\`,
			minWidth: 0
		}, index > 0 ? /* @__PURE__ */ __dil.jsx("box", {
			ariaHidden: true,
			background: "alpha-10",
			height: 24,
			width: 1
		}) : null, /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			flex: 1,
			justify: "center",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("button", {
			block: true,
			color: "secondary",
			onClick: () => onAction(action),
			size: "sm",
			variant: "ghost"
		}, action.icon ? /* @__PURE__ */ __dil.jsx("icon", { name: action.icon }) : null, " ", action.label)))))))) : null;
	}

//#endregion
//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region FollowUpActionBar.dil.tsx
	function FollowUpActionBar(props) {
		const componentKey = DIL.useAppData((appData) => typeof props.__resolutionId === "string" && appData.opGenui?.componentResults?.[props.__resolutionId] != null ? props.__resolutionId : componentDataKey("FollowUpActionBar", props));
		const { resolutionComplete, state } = useResolvedComponentResult("FollowUpActionBar", {
			...props,
			__resolutionId: componentKey
		});
		if (!state) return resolutionComplete ? props.fallback ?? null : /* @__PURE__ */ __dil.jsx("loading-block", {
			width: "100%",
			height: 64
		});
		if (!state.actions.length) return null;
		const contentReferenceType = state.content_reference_type ?? state.contentReferenceType;
		return state.presentation === "wrapped_pills" ? /* @__PURE__ */ __dil.jsx("col", {
			role: "group",
			ariaLabel: "Suggested follow-ups",
			gap: 2,
			width: "100%",
			align: "start"
		}, state.actions.map((action, index) => /* @__PURE__ */ __dil.jsx("box", {
			key: action.query + "|" + action.label + "|" + index,
			width: "fit-content",
			height: 40,
			flex: "0 1 auto",
			...GenUI.logEvent ? {
				onVisibleWhen: action.onboarding_action_id != null && action.onboarding_action_id !== "",
				onVisible: () => GenUI.logEvent?.({
					event_name: "chatgpt_conversational_onboarding_action_shown",
					statsig_event_name: "chatgpt_conversational_onboarding_action_shown",
					event_data: {
						renderer: action.onboarding_renderer,
						level: action.onboarding_level,
						use_case: action.onboarding_use_case,
						action_id: action.onboarding_action_id,
						source: action.source
					}
				})
			} : {}
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			width: "fit-content",
			height: 40,
			flex: "0 1 auto",
			padding: {
				top: 2,
				right: 4,
				bottom: 2,
				left: 2
			},
			radius: "full",
			border: {
				size: 1,
				color: "default"
			},
			background: "surface",
			clip: true,
			ariaLabel: action.label,
			onClick: () => GenUI.dispatchAction({
				handler: "client",
				type: action.onboarding_client_action === "open_image_generation_composer" || action.onboarding_client_action === "start_voice_mode" ? action.onboarding_client_action : "issue_new_turn",
				loadingBehavior: action.onboarding_action_id || action.source === "image_gen_follow_up_dil_buttons" ? "none" : "auto",
				payload: {
					...action.onboarding_client_action === "start_voice_mode" ? {
						component_key: componentKey,
						action_index: index
					} : {},
					query: action.query,
					append_to_current_leaf: true,
					event_source: action.onboarding_client_action !== void 0 ? "conversational_onboarding" : null,
					event_name: action.onboarding_action_id ? "chatgpt_conversational_onboarding_action_clicked" : null,
					statsig_event_name: action.onboarding_action_id ? "chatgpt_conversational_onboarding_action_clicked" : null,
					event_data: {
						renderer: action.onboarding_renderer,
						level: action.onboarding_level,
						use_case: action.onboarding_use_case,
						action_id: action.onboarding_action_id,
						source: action.source
					},
					message_metadata: action.source ? {
						followups_v2_followup_clicked: true,
						followups_v2_followup_source: action.source
					} : {}
				}
			})
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			width: "100%",
			height: "100%"
		}, action.icon_url ? /* @__PURE__ */ __dil.jsx("box", {
			size: 24,
			flex: "0 0 auto"
		}, /* @__PURE__ */ __dil.jsx("image", {
			src: action.icon_url,
			alt: "",
			fit: "contain",
			width: 24,
			height: 24,
			hideOnFailure: true
		})) : null, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "normal",
			color: "primary",
			maxLines: 1
		}, action.label)))))) : /* @__PURE__ */ __dil.jsx(FollowUpFooter, {
			actions: state.actions,
			onAction: (action) => GenUI.dispatchAction({
				handler: "client",
				type: "issue_new_turn",
				payload: {
					query: action.query,
					prompt: action.query,
					event_name: "chatgpt_widget_action",
					event_data: {
						widget_affordance: "OPTION",
						widget_action_target: "follow_up",
						widget_action_value: action.label,
						surface_location: "RESPONSE",
						...contentReferenceType ? { content_reference_type: contentReferenceType } : {}
					}
				}
			})
		});
	}

//#endregion
return FollowUpActionBar;
})();
return __dilDefaultExport;
})()))\`,GenImage:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentGenImage(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "GenImage",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "GenImage", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentGenImage, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function hasImageSource(image) {
		return Boolean(image?.content_url || image?.thumbnail_url);
	}
	function normalizedAspectRatio(value) {
		return value?.replace(":", " / ");
	}
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region GenImage.dil.tsx
/** Mirror v1: only pixel max-widths supply a non-shrinking preferred width. */
	function hasPreferredPixelWidth(value) {
		if (typeof value === "number") return Number.isFinite(value) && value >= 0;
		return typeof value === "string" && /^\\\\d+(?:\\\\.\\\\d+)?(?:px)?$/.test(value.trim());
	}
	/** Mirror the v1 intrinsic frame while image resolution is still pending. */
	function unresolvedAspectWidth(maxHeight, aspectRatio) {
		return \\\`calc(\\\${typeof maxHeight === "number" ? \\\`\\\${maxHeight}px\\\` : /^\\\\d+(?:\\\\.\\\\d+)?$/.test(maxHeight.trim()) ? \\\`\\\${maxHeight.trim()}px\\\` : maxHeight.trim()} * \\\${normalizedAspectRatio(aspectRatio)})\\\`;
	}
	function GenImage(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("GenImage", props);
		const isLoading = state?.is_loading ?? !resolutionComplete;
		const image = state?.images?.[0];
		const hasImage = hasImageSource(image);
		if (!isLoading && !hasImage && (!props.fallback || state == null)) return /* @__PURE__ */ __dil.jsx("box", { height: 0 });
		const frameMaxWidth = state?.frame_max_width ?? props.maxWidth;
		const frameAspectRatio = state?.frame_aspect_ratio ?? props.aspectRatio;
		const presentation = state?.presentation;
		const hasAuthoredDimensions = props.width != null || props.height != null;
		const unresolvedSize = isLoading && state == null && props.aspectRatio == null && !hasAuthoredDimensions ? props.maxHeight ?? 220 : void 0;
		const unresolvedWidth = isLoading && state == null && props.aspectRatio != null ? unresolvedAspectWidth(props.maxHeight ?? 220, props.aspectRatio) : unresolvedSize;
		const imageElement = /* @__PURE__ */ __dil.jsx("search-image", {
			alt: image?.title ?? "",
			aspectRatio: normalizedAspectRatio(frameAspectRatio),
			fallback: props.fallback,
			fit: state?.image_fit ?? "cover",
			height: "100%",
			hideOnFailure: true,
			radius: "none",
			searchImage: image,
			width: "100%"
		});
		return /* @__PURE__ */ __dil.jsx("box", {
			ariaLabel: isLoading ? "Loading image" : void 0,
			aspectRatio: normalizedAspectRatio(frameAspectRatio),
			background: "surface-tertiary",
			border: (presentation?.frame ?? props.frame ?? true) && !isLoading && hasImage ? {
				color: "subtle",
				size: 1
			} : void 0,
			clip: true,
			flex: hasPreferredPixelWidth(frameMaxWidth) ? "0 0 auto" : void 0,
			height: state?.frame_height ?? props.height ?? (props.width != null || frameAspectRatio != null ? void 0 : unresolvedSize ?? "100%"),
			maxHeight: state?.max_height !== void 0 ? state.max_height ?? void 0 : props.maxHeight ?? (hasAuthoredDimensions ? void 0 : unresolvedSize),
			maxWidth: frameMaxWidth,
			minHeight: presentation?.min_height ?? props.minHeight,
			minWidth: presentation?.min_width ?? props.minWidth ?? 0,
			radius: presentation?.radius ?? props.radius ?? "2xl",
			role: isLoading ? "status" : void 0,
			width: state?.frame_width ?? props.width ?? unresolvedWidth ?? "100%"
		}, !isLoading && !hasImage ? props.fallback : props.onClickAction === null ? imageElement : /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: image?.title ? \\\`Open \\\${image.title}\\\` : "Open image",
			background: "transparent",
			disabled: isLoading,
			height: "100%",
			onClick: () => props.onClickAction ? GenUI.dispatchAction(props.onClickAction) : state?.default_on_click_action ? GenUI.dispatchAction(state.default_on_click_action) : GenUI.openImageLightbox(state?.images ?? [], 0),
			radius: "none",
			width: "100%"
		}, imageElement));
	}

//#endregion
return GenImage;
})();
return __dilDefaultExport;
})()))\`,LearningSpeakCard:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentLearningSpeakCard(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "LearningSpeakCard",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "LearningSpeakCard", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentLearningSpeakCard, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region SpeechSynthesizer.dil.tsx
	const unavailable = {
		available: false,
		status: "idle",
		error: null,
		play: () => {},
		stop: () => {}
	};
	const { useSpeechSynthesizer = () => unavailable } = DIL;
	function SpeechSynthesizer({ controls, disabled = false, logging, ...source }) {
		const speech = useSpeechSynthesizer(source, logging);
		DIL.useEffect(() => {
			if (disabled) speech.stop();
		}, [disabled, speech.stop]);
		const play = () => {
			if (!disabled) speech.play();
		};
		const stop = () => {
			if (!disabled) speech.stop();
		};
		if (controls) return controls({
			...speech,
			play,
			stop
		});
		if (!speech.available) return /* @__PURE__ */ __dil.jsx("text", null, "Audio unavailable");
		return speech.status === "idle" ? /* @__PURE__ */ __dil.jsx("button", {
			disabled,
			onClick: play
		}, "Play") : /* @__PURE__ */ __dil.jsx("button", { onClick: stop }, "Stop");
	}

//#endregion
//#region learning/primitives/LearningExercisePager.dil.tsx
	function LearningExercisePager({ exercises, previousLabel, nextLabel, nextButtonLabel, progressLabels, newTurnQuery, renderExercise, renderFooter, getResponse, isExerciseComplete = (_, selectedIds$1) => selectedIds$1.length > 0 }) {
		const instanceId = DIL.useId();
		const [viewState, setViewState] = DIL.useState({
			currentId: null,
			answers: {}
		});
		const currentViewState = DIL.useRef(viewState);
		currentViewState.current = viewState;
		const updateViewState = (next) => {
			currentViewState.current = next;
			setViewState(next);
		};
		const index = Math.max(0, exercises.findIndex((exercise$1) => exercise$1.id === viewState.currentId));
		const exercise = exercises[index];
		if (!exercise) return null;
		const answer = viewState.answers[exercise.id];
		const selectedIds = answer?.revision === exercise.revision ? answer.selectedIds : [];
		const canAdvance = index < exercises.length - 1 && isExerciseComplete(exercise.data, selectedIds);
		const navigate = (nextIndex) => {
			if (nextIndex > index && !canAdvance) return;
			const next = exercises[nextIndex];
			if (next) updateViewState({
				...currentViewState.current,
				currentId: next.id
			});
		};
		const navigation = exercises.length > 1 ? /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1.25,
			flex: "0 0 auto"
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			size: 36,
			radius: "full",
			background: "transparent",
			ariaLabel: previousLabel,
			disabled: index === 0,
			onClick: () => navigate(index - 1)
		}, /* @__PURE__ */ __dil.jsx("box", {
			height: "100%",
			align: "center",
			justify: "center",
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "chevron-left",
			size: "xl",
			color: index === 0 ? "alpha-35" : "secondary"
		}))), /* @__PURE__ */ __dil.jsx("box", {
			role: "status",
			minWidth: 48,
			align: "center",
			justify: "center"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			color: "secondary"
		}, progressLabels[index])), /* @__PURE__ */ __dil.jsx("pressable", {
			size: 36,
			radius: "full",
			background: "transparent",
			ariaLabel: nextLabel,
			disabled: !canAdvance,
			onClick: () => navigate(index + 1)
		}, /* @__PURE__ */ __dil.jsx("box", {
			height: "100%",
			align: "center",
			justify: "center",
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "chevron-right",
			size: "xl",
			color: canAdvance ? "secondary" : "alpha-35"
		})))) : null;
		return /* @__PURE__ */ __dil.jsx("box", {
			key: \\\`\\\${instanceId}:\\\${exercise.id}:\\\${exercise.revision}\\\`,
			width: "100vw",
			maxWidth: "100%"
		}, renderExercise(exercise.data, {
			selectedIds,
			setSelectedIds: (update) => {
				const current = currentViewState.current;
				const previous = current.answers[exercise.id];
				const ids = previous?.revision === exercise.revision ? previous.selectedIds : [];
				const nextIds = update(ids);
				const answers = {
					...current.answers,
					[exercise.id]: {
						revision: exercise.revision,
						selectedIds: nextIds
					}
				};
				updateViewState({
					...current,
					answers
				});
				if (newTurnQuery && index === exercises.length - 1 && !isExerciseComplete(exercise.data, ids) && isExerciseComplete(exercise.data, nextIds)) {
					const responses = exercises.flatMap((item, itemIndex) => {
						const exerciseAnswer = answers[item.id];
						if (exerciseAnswer?.revision !== item.revision || !exerciseAnswer.selectedIds.length) return [];
						const response = getResponse(item.data, exerciseAnswer.selectedIds);
						return [\\\`\\\${itemIndex + 1}. \\\${response.question}\\\\n→ \\\${response.answer}\\\`];
					});
					GenUI.issueNewTurn([newTurnQuery, ...responses].join("\\\\n\\\\n"), {
						append_to_current_leaf: true,
						followup_metadata: {}
					});
				}
			}
		}, navigation, renderFooter ? renderFooter(canAdvance ? () => navigate(index + 1) : null) : exercises.length > 1 ? /* @__PURE__ */ __dil.jsx("row", {
			justify: "end",
			minHeight: "40px"
		}, /* @__PURE__ */ __dil.jsx("button", {
			size: "lg",
			color: "primary",
			variant: canAdvance ? "solid" : "outline",
			disabled: !canAdvance,
			onClick: () => navigate(index + 1)
		}, nextButtonLabel ?? nextLabel)) : null));
	}

//#endregion
//#region learning/speaking.dil.ts
	const REPEAT_ATTEMPT_TIMEOUT_MS = 1e4;
	function wordKey(text) {
		return text.toLowerCase().normalize("NFD").replace(/(\\\\p{Script=Latin})\\\\p{M}+/gu, "$1").replace(/[^\\\\p{L}\\\\p{N}\\\\p{M}]/gu, "");
	}
	function hasSpeakingSegmenter() {
		return typeof Intl !== "undefined" && typeof Intl.Segmenter === "function";
	}
	/** Keep display spans intact while comparing normalized, whole words. */
	function speakingParts(text, language) {
		if (!hasSpeakingSegmenter()) return [];
		let segmenter;
		try {
			segmenter = new Intl.Segmenter(language || void 0, { granularity: "word" });
		} catch {
			segmenter = new Intl.Segmenter(void 0, { granularity: "word" });
		}
		const parts = Array.from(segmenter.segment(text), (part) => ({
			text: part.segment,
			word: part.isWordLike ? wordKey(part.segment) || null : null
		}));
		const displayParts = [];
		for (const part of parts) {
			const previous = displayParts[displayParts.length - 1];
			const opening = part.word && previous && !previous.word ? previous.text.match(/[¿¡]+$/u)?.[0] : void 0;
			if (opening) {
				previous.text = previous.text.slice(0, -opening.length);
				if (!previous.text) displayParts.pop();
				displayParts.push({
					text: opening + part.text,
					word: part.word
				});
				continue;
			}
			const punctuation = !part.word && previous?.word ? part.text.match(/^(?:(?![¿¡])\\\\p{P})+/u)?.[0] : void 0;
			if (punctuation) {
				previous.text += punctuation;
				const rest = part.text.slice(punctuation.length);
				if (rest) displayParts.push({
					text: rest,
					word: null
				});
			} else if (!part.word && previous && !previous.word) previous.text += part.text;
			else displayParts.push(part);
		}
		return displayParts;
	}
	/** Every transcript is a replacement, never an additional batch of words. */
	function matchSpeakingWords(parts, transcript, language) {
		const counts = /* @__PURE__ */ new Map();
		for (const { word } of speakingParts(transcript, language)) if (word) counts.set(word, (counts.get(word) ?? 0) + 1);
		let remaining = 0;
		return {
			matched: parts.map(({ word }) => {
				if (!word) return false;
				const count = counts.get(word) ?? 0;
				if (count > 0) {
					counts.set(word, count - 1);
					return true;
				}
				remaining++;
				return false;
			}),
			complete: parts.some((part) => part.word !== null) && remaining === 0
		};
	}
	/** New occurrences count as activity even when they are not target words. */
	function hasNewSpeakingWords(previousTranscript, transcript, language) {
		if (transcript === previousTranscript) return false;
		const parts = speakingParts(transcript, language);
		return parts.some((part) => part.word !== null) && !matchSpeakingWords(parts, previousTranscript, language).complete;
	}

//#endregion
//#region learning/cards/LearningSpeakCard.dil.tsx
	const { useDictation = () => void 0 } = DIL;
	const SUCCESS = "spoken";
	const CARD_WIDTH = 399;
	const ACTION_HEIGHT = 48;
	const HEADER_CONTROL_SIZE = 40;
	const STOP_CONTROL_SIZE = 32;
	function LearningSpeakCard$1(props) {
		return /* @__PURE__ */ __dil.jsx(LearningExercisePager, {
			...props,
			newTurnQuery: null,
			isExerciseComplete: (_, ids) => ids.includes(SUCCESS),
			getResponse: (data) => ({
				question: data.text,
				answer: data.text
			}),
			renderFooter: (onNext) => onNext ? /* @__PURE__ */ __dil.jsx("pressable", {
				height: ACTION_HEIGHT,
				flex: "0 0 auto",
				padding: { x: 4 },
				radius: "full",
				background: "surface-inverted",
				ariaLabel: props.nextButtonLabel ?? props.nextLabel,
				onClick: onNext
			}, /* @__PURE__ */ __dil.jsx("row", {
				height: "100%",
				align: "center",
				justify: "center"
			}, /* @__PURE__ */ __dil.jsx("text", {
				size: "md",
				weight: "medium",
				color: {
					light: "white",
					dark: "black"
				}
			}, props.nextButtonLabel ?? props.nextLabel))) : null,
			renderExercise: (data, selection, navigation, footer) => /* @__PURE__ */ __dil.jsx(SpeakExercise, {
				...data,
				selection,
				navigation,
				footer
			})
		});
	}
	function SpeakExercise({ text, language, mode = "repeat", sourceText, labels, selection, navigation, footer }) {
		const dictation = useDictation(language ? { language } : void 0);
		const parts = DIL.useMemo(() => {
			const segmented = speakingParts(text, language);
			return segmented.length ? segmented : [{
				text,
				word: text
			}];
		}, [text, language]);
		const attempt = DIL.useRef({
			phase: "idle",
			lastActivityAt: null,
			transcript: "",
			matched: [],
			error: false
		});
		const [, refresh] = DIL.useState(0);
		const update = () => refresh((value) => value + 1);
		const succeeded = selection.selectedIds.includes(SUCCESS);
		const recall = mode === "recall";
		const active = !succeeded && attempt.current.phase === "active";
		const now = DIL.useNow(active && dictation?.status !== "starting");
		const transcript = dictation?.transcript ?? "";
		const liveMatch = DIL.useMemo(() => matchSpeakingWords(parts, transcript, language), [
			parts,
			transcript,
			language
		]);
		const unavailable$1 = !dictation || dictation.error?.code === "integration_error" || !hasSpeakingSegmenter();
		function startAttempt(stopPlayback) {
			if (!dictation || unavailable$1 || attempt.current.phase === "active") return;
			stopPlayback();
			dictation.cancel();
			selection.setSelectedIds(() => []);
			attempt.current = {
				phase: "active",
				lastActivityAt: null,
				transcript: "",
				matched: [],
				error: false
			};
			dictation.start();
			update();
		}
		function finish(success, error = false) {
			if (attempt.current.phase !== "active") return;
			attempt.current = {
				...attempt.current,
				phase: success ? "success" : "failure",
				error
			};
			dictation?.stop();
			if (success) selection.setSelectedIds(() => [SUCCESS]);
			update();
		}
		DIL.useEffect(() => {
			if (succeeded) {
				if (attempt.current.phase === "active") {
					attempt.current = {
						...attempt.current,
						phase: "success"
					};
					dictation?.cancel();
				}
				return;
			}
			if (!active || !dictation) return;
			if (dictation.status === "error" || dictation.status === "idle") {
				finish(false, true);
				return;
			}
			if (dictation.status === "starting") return;
			const lastActivityAt = attempt.current.lastActivityAt ?? now;
			if (now - lastActivityAt >= REPEAT_ATTEMPT_TIMEOUT_MS) {
				finish(false);
				return;
			}
			attempt.current = {
				...attempt.current,
				lastActivityAt: hasNewSpeakingWords(attempt.current.transcript, dictation.transcript, language) ? now : lastActivityAt,
				transcript: dictation.transcript,
				matched: liveMatch.matched
			};
			if (liveMatch.complete) finish(true);
			else if (dictation.status === "done") finish(false);
		});
		const cancel = dictation?.cancel;
		DIL.useEffect(() => () => cancel?.(), [cancel]);
		const failed = attempt.current.phase === "failure";
		const showPlayback = !recall || succeeded || failed && !attempt.current.error;
		const expired = attempt.current.lastActivityAt !== null && now - attempt.current.lastActivityAt >= REPEAT_ATTEMPT_TIMEOUT_MS;
		const matched = active && !expired ? liveMatch.matched : attempt.current.matched;
		const showMissingWords = failed && !succeeded && !attempt.current.error;
		const wordColors = parts.map(({ word }, index) => {
			if (!word || succeeded) return "primary";
			if (matched[index]) return active ? "info" : "primary";
			return showMissingWords ? "danger" : "primary";
		});
		const message = succeeded ? null : unavailable$1 ? labels.unavailable : failed && attempt.current.error ? labels.error : null;
		return /* @__PURE__ */ __dil.jsx(SpeechSynthesizer, {
			text,
			language: language ?? void 0,
			source: "learning_speak_card",
			disabled: active || !showPlayback,
			controls: (speech) => /* @__PURE__ */ __dil.jsx("col", {
				width: CARD_WIDTH,
				maxWidth: "100%",
				padding: 5,
				gap: 2,
				radius: "4xl",
				background: "surface-elevated",
				border: {
					size: .5,
					color: "default"
				},
				role: "group",
				ariaLabel: labels.title,
				disableAutoSpacing: true
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				justify: "between",
				minHeight: HEADER_CONTROL_SIZE,
				gap: 2,
				wrap: "wrap"
			}, /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 1.5,
				flex: "1 1 auto"
			}, /* @__PURE__ */ __dil.jsx("box", { ariaHidden: true }, /* @__PURE__ */ __dil.jsx("icon", {
				name: "voice",
				size: "lg",
				color: "secondary"
			})), /* @__PURE__ */ __dil.jsx("text", {
				size: "md",
				color: "secondary",
				weight: "medium"
			}, labels.title)), /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, navigation), showPlayback ? /* @__PURE__ */ __dil.jsx("pressable", {
				size: HEADER_CONTROL_SIZE,
				radius: "full",
				background: "transparent",
				ariaLabel: !speech.available ? labels.playbackUnavailable : speech.status === "idle" ? labels.play : labels.stopPlayback,
				disabled: active || !speech.available,
				onClick: speech.status === "idle" ? speech.play : speech.stop
			}, /* @__PURE__ */ __dil.jsx("box", {
				height: "100%",
				align: "center",
				justify: "center",
				ariaHidden: true
			}, /* @__PURE__ */ __dil.jsx("icon", {
				name: speech.status === "idle" ? "sound-on-read-out-loud-speaker" : "stop",
				size: "xl",
				color: "secondary"
			}))) : null), recall ? /* @__PURE__ */ __dil.jsx("col", {
				gap: 4,
				padding: { bottom: 4 }
			}, /* @__PURE__ */ __dil.jsx("col", { gap: 1.5 }, /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				color: "secondary"
			}, labels.recallInstruction), /* @__PURE__ */ __dil.jsx("text", {
				size: "xl",
				preserveWhitespace: true
			}, sourceText)), /* @__PURE__ */ __dil.jsx(RecallPhrase, {
				parts,
				matched,
				wordColors,
				succeeded,
				failed: showMissingWords,
				hiddenWord: labels.hiddenWord ?? ""
			})) : /* @__PURE__ */ __dil.jsx("box", { padding: { bottom: 4 } }, /* @__PURE__ */ __dil.jsx("text", {
				size: "xl",
				preserveWhitespace: true
			}, parts.map((part, index) => part.word ? /* @__PURE__ */ __dil.jsx("text", {
				key: index,
				inline: true,
				color: wordColors[index]
			}, part.text) : part.text))), /* @__PURE__ */ __dil.jsx("col", {
				role: "status",
				gap: 2
			}, succeeded ? /* @__PURE__ */ __dil.jsx("row", {
				align: "center",
				gap: 2
			}, /* @__PURE__ */ __dil.jsx("row", {
				height: ACTION_HEIGHT,
				flex: "1 1 auto",
				padding: { x: 4 },
				radius: "full",
				background: "green-500",
				align: "center",
				justify: "between"
			}, /* @__PURE__ */ __dil.jsx("text", {
				color: "white",
				weight: "medium"
			}, labels.success), /* @__PURE__ */ __dil.jsx("box", { ariaHidden: true }, /* @__PURE__ */ __dil.jsx("icon", {
				name: "check-md",
				color: "white",
				size: "xl"
			}))), /* @__PURE__ */ __dil.jsx("pressable", {
				size: ACTION_HEIGHT,
				flex: "0 0 auto",
				radius: "full",
				background: "surface-tertiary",
				ariaLabel: labels.retry,
				disabled: unavailable$1,
				onClick: () => startAttempt(speech.stop)
			}, /* @__PURE__ */ __dil.jsx("box", {
				height: "100%",
				align: "center",
				justify: "center",
				ariaHidden: true
			}, /* @__PURE__ */ __dil.jsx("icon", {
				name: "reload",
				color: "primary",
				size: "xl"
			}))), /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, footer)) : active ? /* @__PURE__ */ __dil.jsx("row", {
				height: ACTION_HEIGHT,
				padding: {
					left: 4,
					right: 2
				},
				radius: "full",
				background: "surface-tertiary",
				align: "center",
				justify: "between"
			}, /* @__PURE__ */ __dil.jsx("shimmer-text", { weight: "medium" }, dictation?.status === "starting" ? labels.starting : labels.listening), /* @__PURE__ */ __dil.jsx("pressable", {
				size: STOP_CONTROL_SIZE,
				radius: "full",
				background: "surface-inverted",
				ariaLabel: labels.stop,
				onClick: () => {
					const withinDeadline = attempt.current.lastActivityAt !== null && now - attempt.current.lastActivityAt < REPEAT_ATTEMPT_TIMEOUT_MS;
					if (withinDeadline) attempt.current = {
						...attempt.current,
						matched: liveMatch.matched
					};
					finish(withinDeadline && liveMatch.complete);
				}
			}, /* @__PURE__ */ __dil.jsx("box", {
				height: "100%",
				align: "center",
				justify: "center",
				ariaHidden: true
			}, /* @__PURE__ */ __dil.jsx("icon", {
				name: "stop",
				color: {
					light: "white",
					dark: "black"
				},
				size: "lg"
			})))) : /* @__PURE__ */ __dil.jsx("pressable", {
				height: ACTION_HEIGHT,
				width: "100%",
				radius: "full",
				background: "surface-inverted",
				ariaLabel: failed ? labels.retry : labels.start,
				disabled: unavailable$1 || !parts.some((part) => part.word),
				onClick: () => startAttempt(speech.stop)
			}, /* @__PURE__ */ __dil.jsx("row", {
				height: "100%",
				align: "center",
				justify: "center",
				gap: 1.5
			}, /* @__PURE__ */ __dil.jsx("box", { ariaHidden: true }, /* @__PURE__ */ __dil.jsx("icon", {
				name: failed ? "reload" : "mic",
				color: {
					light: "white",
					dark: "black"
				}
			})), /* @__PURE__ */ __dil.jsx("text", {
				color: {
					light: "white",
					dark: "black"
				},
				weight: "medium"
			}, failed ? labels.retry : labels.start))), message ? /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				color: "secondary"
			}, message) : null, speech.error ? /* @__PURE__ */ __dil.jsx("text", {
				size: "sm",
				color: "secondary"
			}, labels.playbackError) : null))
		});
	}
	function RecallPhrase({ parts, matched, wordColors, succeeded, failed, hiddenWord }) {
		const lines = [[]];
		parts.forEach((part, index) => {
			part.text.split(/\\\\r\\\\n|\\\\r|\\\\n/).forEach((text, line) => {
				if (line > 0) lines.push([]);
				if (text) lines[lines.length - 1].push({
					text,
					index
				});
			});
		});
		return /* @__PURE__ */ __dil.jsx("col", {
			gap: 1,
			padding: {
				x: 6,
				y: 4
			},
			radius: "full",
			background: succeeded || failed ? "surface-tertiary" : "transparent",
			border: succeeded || failed ? void 0 : {
				size: 1,
				color: "strong",
				style: "dashed"
			}
		}, lines.map((line, lineIndex) => /* @__PURE__ */ __dil.jsx("row", {
			key: lineIndex,
			wrap: "wrap",
			gap: 0,
			rowGap: 1,
			align: "center"
		}, line.length === 0 ? /* @__PURE__ */ __dil.jsx("box", { ariaHidden: true }, /* @__PURE__ */ __dil.jsx("text", {
			size: "xl",
			preserveWhitespace: true
		}, "\\\\xA0")) : line.map(({ text, index }) => parts[index].word && !succeeded && !failed && !matched[index] ? /* @__PURE__ */ __dil.jsx("box", {
			key: index,
			radius: "xs",
			background: "surface-tertiary",
			maxWidth: "100%",
			role: "img",
			ariaLabel: hiddenWord
		}, /* @__PURE__ */ __dil.jsx("box", { ariaHidden: true }, /* @__PURE__ */ __dil.jsx("text", {
			size: "xl",
			color: "transparent",
			preserveWhitespace: true
		}, text))) : /* @__PURE__ */ __dil.jsx("text", {
			key: index,
			size: "xl",
			inline: true,
			color: wordColors[index],
			preserveWhitespace: true
		}, text)))));
	}

//#endregion
//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) {
			if (result.status === "pending") return {
				status: "pending",
				resolutionComplete: false,
				state: void 0
			};
			return result.status === "resolved" ? {
				status: "resolved",
				resolutionComplete: true,
				state: result.state
			} : {
				status: "failed",
				resolutionComplete: true,
				state: void 0
			};
		}
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "pending") return true;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region LearningSpeakCard.dil.tsx
	function LearningSpeakCard(props) {
		const { state } = useResolvedComponentResult("LearningSpeakCard", props);
		if (state) return /* @__PURE__ */ __dil.jsx(LearningSpeakCard$1, state);
		if ("progressLabels" in props) return /* @__PURE__ */ __dil.jsx(LearningSpeakCard$1, props);
		return props.fallback ?? null;
	}

//#endregion
return LearningSpeakCard;
})();
return __dilDefaultExport;
})()))\`,LearningVizDil:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentLearningVizDil(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "LearningVizDil",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "LearningVizDil", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentLearningVizDil, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region learning-viz-dil/lottie-playback.dil.ts
	function positionAt(playback, now, duration) {
		const elapsed = playback.startedAt === null ? 0 : (now - playback.startedAt) / 1e3;
		return Math.min(duration, playback.position + Math.max(0, elapsed));
	}
	function useLottiePlayback(source, animated) {
		const duration = (Number(source.op) - Number(source.ip)) / Number(source.fr);
		const [playback, setPlayback] = DIL.useState(() => ({
			position: 0,
			startedAt: animated ? Date.now() : null
		}));
		const now = DIL.useNow(playback.startedAt !== null);
		const playing = playback.startedAt !== null && positionAt(playback, now, duration) < duration;
		DIL.useEffect(() => {
			if (playback.startedAt !== null && !playing) setPlayback({
				position: duration,
				startedAt: null
			});
		}, [
			playing,
			playback.startedAt,
			duration
		]);
		const currentTime = DIL.useMemo(() => positionAt(playback, Date.now(), duration), [source, playback]);
		const toggle = () => {
			const timestamp = Date.now();
			setPlayback((previous) => {
				const position = positionAt(previous, timestamp, duration);
				return previous.startedAt !== null && position < duration ? {
					position,
					startedAt: null
				} : {
					position: position === duration ? 0 : position,
					startedAt: timestamp
				};
			});
		};
		return {
			playing,
			currentTime,
			toggle
		};
	}

//#endregion
//#region learning-viz-dil/lottie-diagram.dil.tsx
	function LottieDiagram({ data }) {
		const { theme } = DIL.useTheme();
		const playback = useLottiePlayback(data.src[theme], data.animated);
		return /* @__PURE__ */ __dil.jsx("col", {
			width: "100vw",
			maxWidth: "100%",
			align: "center",
			gap: 0
		}, /* @__PURE__ */ __dil.jsx("box", {
			width: "100%",
			maxWidth: 480
		}, /* @__PURE__ */ __dil.jsx("lottie", {
			key: theme,
			src: data.src,
			alt: data.alt,
			width: "100%",
			aspectRatio: "8/5",
			currentTime: playback.currentTime,
			advanceRate: playback.playing ? 1 : 0,
			loop: false
		})), data.animated ? /* @__PURE__ */ __dil.jsx("row", {
			width: "100%",
			maxWidth: 480,
			align: "end",
			justify: "end",
			gap: 0
		}, /* @__PURE__ */ __dil.jsx("box", { padding: {
			bottom: 3,
			right: 3
		} }, /* @__PURE__ */ __dil.jsx("pressable", {
			onClick: playback.toggle,
			ariaLabel: playback.playing ? data.pause_label : data.play_label,
			size: 36,
			radius: "full",
			align: "center",
			justify: "center"
		}, /* @__PURE__ */ __dil.jsx("box", {
			key: theme,
			size: 24,
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: playback.playing ? "pause-sm" : "play-sm",
			size: "2xl",
			color: theme === "dark" ? "#ffffff" : "#0d0d0d"
		}))))) : null);
	}

//#endregion
//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region LearningVizDil.dil.tsx
	function LearningVizDil(props) {
		const { state, resolutionComplete } = useResolvedComponentResult("LearningVizDil", props);
		if (!state) return resolutionComplete ? props.fallback ?? null : /* @__PURE__ */ __dil.jsx("loading-block", {
			width: "100%",
			height: 300
		});
		return /* @__PURE__ */ __dil.jsx(LottieDiagram, { data: state.block_data });
	}

//#endregion
return LearningVizDil;
})();
return __dilDefaultExport;
})()))\`,LearningVocabCard:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentLearningVocabCard(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "LearningVocabCard",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "LearningVocabCard", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentLearningVocabCard, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region SpeechSynthesizer.dil.tsx
	const unavailable = {
		available: false,
		status: "idle",
		error: null,
		play: () => {},
		stop: () => {}
	};
	const { useSpeechSynthesizer = () => unavailable } = DIL;
	function SpeechSynthesizer({ controls, disabled = false, logging, ...source }) {
		const speech = useSpeechSynthesizer(source, logging);
		DIL.useEffect(() => {
			if (disabled) speech.stop();
		}, [disabled, speech.stop]);
		const play = () => {
			if (!disabled) speech.play();
		};
		const stop = () => {
			if (!disabled) speech.stop();
		};
		if (controls) return controls({
			...speech,
			play,
			stop
		});
		if (!speech.available) return /* @__PURE__ */ __dil.jsx("text", null, "Audio unavailable");
		return speech.status === "idle" ? /* @__PURE__ */ __dil.jsx("button", {
			disabled,
			onClick: play
		}, "Play") : /* @__PURE__ */ __dil.jsx("button", { onClick: stop }, "Stop");
	}

//#endregion
//#region learning/primitives/LearningCard.dil.tsx
	function LearningCard({ icon, title, directions, prompt, children, navigation, footer, divider = true }) {
		return /* @__PURE__ */ __dil.jsx("col", {
			width: "100%",
			maxWidth: "100%",
			padding: 5,
			gap: 2,
			radius: "4xl",
			background: "surface-elevated",
			border: {
				size: .5,
				color: "strong"
			},
			role: "group",
			ariaLabel: title,
			disableAutoSpacing: true
		}, /* @__PURE__ */ __dil.jsx("row", {
			minHeight: "40px",
			gap: 2,
			align: "center",
			justify: "between",
			wrap: "wrap"
		}, /* @__PURE__ */ __dil.jsx("row", {
			gap: 1.5,
			align: "center",
			flex: "1 1 auto",
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("box", {
			ariaHidden: true,
			flex: "0 0 auto"
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: icon,
			size: "xl",
			color: "secondary"
		})), /* @__PURE__ */ __dil.jsx("text", {
			size: "md",
			color: "secondary",
			weight: "medium"
		}, title)), /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, navigation)), /* @__PURE__ */ __dil.jsx("col", { gap: 4 }, directions ? /* @__PURE__ */ __dil.jsx("text", { size: "md" }, directions) : null, /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, prompt), divider ? /* @__PURE__ */ __dil.jsx("box", {
			height: "1px",
			background: "border",
			role: "separator"
		}) : null, /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, children), /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, footer)));
	}

//#endregion
//#region learning/primitives/LearningExercisePager.dil.tsx
	function LearningExercisePager({ exercises, previousLabel, nextLabel, nextButtonLabel, progressLabels, newTurnQuery, renderExercise, renderFooter, getResponse, isExerciseComplete = (_, selectedIds$1) => selectedIds$1.length > 0 }) {
		const instanceId = DIL.useId();
		const [viewState, setViewState] = DIL.useState({
			currentId: null,
			answers: {}
		});
		const currentViewState = DIL.useRef(viewState);
		currentViewState.current = viewState;
		const updateViewState = (next) => {
			currentViewState.current = next;
			setViewState(next);
		};
		const index = Math.max(0, exercises.findIndex((exercise$1) => exercise$1.id === viewState.currentId));
		const exercise = exercises[index];
		if (!exercise) return null;
		const answer = viewState.answers[exercise.id];
		const selectedIds = answer?.revision === exercise.revision ? answer.selectedIds : [];
		const canAdvance = index < exercises.length - 1 && isExerciseComplete(exercise.data, selectedIds);
		const navigate = (nextIndex) => {
			if (nextIndex > index && !canAdvance) return;
			const next = exercises[nextIndex];
			if (next) updateViewState({
				...currentViewState.current,
				currentId: next.id
			});
		};
		const navigation = exercises.length > 1 ? /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1.25,
			flex: "0 0 auto"
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			size: 36,
			radius: "full",
			background: "transparent",
			ariaLabel: previousLabel,
			disabled: index === 0,
			onClick: () => navigate(index - 1)
		}, /* @__PURE__ */ __dil.jsx("box", {
			height: "100%",
			align: "center",
			justify: "center",
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "chevron-left",
			size: "xl",
			color: index === 0 ? "alpha-35" : "secondary"
		}))), /* @__PURE__ */ __dil.jsx("box", {
			role: "status",
			minWidth: 48,
			align: "center",
			justify: "center"
		}, /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			color: "secondary"
		}, progressLabels[index])), /* @__PURE__ */ __dil.jsx("pressable", {
			size: 36,
			radius: "full",
			background: "transparent",
			ariaLabel: nextLabel,
			disabled: !canAdvance,
			onClick: () => navigate(index + 1)
		}, /* @__PURE__ */ __dil.jsx("box", {
			height: "100%",
			align: "center",
			justify: "center",
			ariaHidden: true
		}, /* @__PURE__ */ __dil.jsx("icon", {
			name: "chevron-right",
			size: "xl",
			color: canAdvance ? "secondary" : "alpha-35"
		})))) : null;
		return /* @__PURE__ */ __dil.jsx("box", {
			key: \\\`\\\${instanceId}:\\\${exercise.id}:\\\${exercise.revision}\\\`,
			width: "100vw",
			maxWidth: "100%"
		}, renderExercise(exercise.data, {
			selectedIds,
			setSelectedIds: (update) => {
				const current = currentViewState.current;
				const previous = current.answers[exercise.id];
				const ids = previous?.revision === exercise.revision ? previous.selectedIds : [];
				const nextIds = update(ids);
				const answers = {
					...current.answers,
					[exercise.id]: {
						revision: exercise.revision,
						selectedIds: nextIds
					}
				};
				updateViewState({
					...current,
					answers
				});
				if (newTurnQuery && index === exercises.length - 1 && !isExerciseComplete(exercise.data, ids) && isExerciseComplete(exercise.data, nextIds)) {
					const responses = exercises.flatMap((item, itemIndex) => {
						const exerciseAnswer = answers[item.id];
						if (exerciseAnswer?.revision !== item.revision || !exerciseAnswer.selectedIds.length) return [];
						const response = getResponse(item.data, exerciseAnswer.selectedIds);
						return [\\\`\\\${itemIndex + 1}. \\\${response.question}\\\\n→ \\\${response.answer}\\\`];
					});
					GenUI.issueNewTurn([newTurnQuery, ...responses].join("\\\\n\\\\n"), {
						append_to_current_leaf: true,
						followup_metadata: {}
					});
				}
			}
		}, navigation, renderFooter ? renderFooter(canAdvance ? () => navigate(index + 1) : null) : exercises.length > 1 ? /* @__PURE__ */ __dil.jsx("row", {
			justify: "end",
			minHeight: "40px"
		}, /* @__PURE__ */ __dil.jsx("button", {
			size: "lg",
			color: "primary",
			variant: canAdvance ? "solid" : "outline",
			disabled: !canAdvance,
			onClick: () => navigate(index + 1)
		}, nextButtonLabel ?? nextLabel)) : null));
	}

//#endregion
//#region learning/cards/LearningVocabCard.dil.tsx
	function LearningVocabCard$1(props) {
		return /* @__PURE__ */ __dil.jsx("box", {
			width: "100vw",
			maxWidth: "100%"
		}, /* @__PURE__ */ __dil.jsx(LearningExercisePager, {
			...props,
			newTurnQuery: null,
			isExerciseComplete: () => true,
			getResponse: (data) => ({
				question: data.text,
				answer: ""
			}),
			renderExercise: (data, _selection, navigation, footer) => /* @__PURE__ */ __dil.jsx(SpeechSynthesizer, {
				text: data.text,
				language: data.language,
				pronunciationHint: data.pronunciationHint ?? void 0,
				source: "learning_vocab_card",
				controls: (speech) => {
					const playButton = /* @__PURE__ */ __dil.jsx("button", {
						size: "xl",
						variant: "solid",
						color: "info",
						label: !speech.available ? data.audioLabels.unavailable : speech.status === "idle" ? data.audioLabels.play : data.audioLabels.stop,
						disabled: !speech.available,
						onClick: speech.status === "idle" ? speech.play : speech.stop
					}, /* @__PURE__ */ __dil.jsx("row", {
						gap: 1,
						align: "center"
					}, /* @__PURE__ */ __dil.jsx("icon", {
						name: speech.status === "idle" ? "sound-on-read-out-loud-speaker" : "stop",
						size: "lg"
					}), /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, speech.status === "idle" ? data.audioLabels.play : data.audioLabels.stop)));
					return /* @__PURE__ */ __dil.jsx(LearningCard, {
						icon: "book",
						title: data.title,
						navigation: props.exercises.length > 1 ? navigation : playButton,
						footer,
						prompt: /* @__PURE__ */ __dil.jsx("row", {
							gap: 2,
							align: "center",
							justify: "between"
						}, /* @__PURE__ */ __dil.jsx("box", {
							flex: "1 1 auto",
							minWidth: 0
						}, /* @__PURE__ */ __dil.jsx("title", {
							size: "lg",
							weight: "normal"
						}, data.text)), props.exercises.length > 1 ? /* @__PURE__ */ __dil.jsx("box", { flex: "0 0 auto" }, playButton) : null)
					}, /* @__PURE__ */ __dil.jsx("col", { gap: 2 }, /* @__PURE__ */ __dil.jsx("text", { size: "md" }, data.translation), data.pronunciation ? /* @__PURE__ */ __dil.jsx("text", {
						size: "md",
						color: "secondary",
						italic: true
					}, data.pronunciation) : null, speech.error ? /* @__PURE__ */ __dil.jsx("box", { role: "status" }, /* @__PURE__ */ __dil.jsx("text", {
						size: "sm",
						color: "secondary"
					}, data.audioLabels.error)) : null));
				}
			})
		}));
	}

//#endregion
//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) {
			if (result.status === "pending") return {
				status: "pending",
				resolutionComplete: false,
				state: void 0
			};
			return result.status === "resolved" ? {
				status: "resolved",
				resolutionComplete: true,
				state: result.state
			} : {
				status: "failed",
				resolutionComplete: true,
				state: void 0
			};
		}
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "pending") return true;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region LearningVocabCard.dil.tsx
	function LearningVocabCard(props) {
		const { state } = useResolvedComponentResult("LearningVocabCard", props);
		if (state) return /* @__PURE__ */ __dil.jsx(LearningVocabCard$1, state);
		if ("progressLabels" in props) return /* @__PURE__ */ __dil.jsx(LearningVocabCard$1, props);
		return props.fallback ?? null;
	}

//#endregion
return LearningVocabCard;
})();
return __dilDefaultExport;
})()))\`,Link:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentLink(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "Link",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "Link", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentLink, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region Link.dil.tsx
	function Link(props) {
		const needsResolution = !props.url || !props.title;
		const { resolutionComplete, state } = useResolvedComponentResult("Link", props);
		if (!state && needsResolution) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading link" });
		const title = state?.title ?? props.title ?? props.url ?? "Link";
		const url = state?.url ?? props.url ?? "";
		const finalWordStart = /\\\\S+\\\\s*$/u.exec(title)?.index ?? 0;
		const leadingTitle = title.slice(0, finalWordStart);
		const trailingTitle = title.slice(finalWordStart);
		return /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`Open \\\${title}\\\`,
			inline: true,
			onClick: () => GenUI.openUrl(url)
		}, /* @__PURE__ */ __dil.jsx("text", { inline: true }, leadingTitle ? /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			underline: "dotted"
		}, leadingTitle) : null, /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			width: "max-content"
		}, /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			underline: "dotted"
		}, trailingTitle), "\\\\xA0", /* @__PURE__ */ __dil.jsx("icon", {
			inline: true,
			name: "arrow-up-right"
		}))));
	}

//#endregion
return Link;
})();
return __dilDefaultExport;
})()))\`,LinkCard:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentLinkCard(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "LinkCard",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "LinkCard", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentLinkCard, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region LinkCard.dil.tsx
	function LinkCard(props) {
		const needsResolution = !props.url || !props.title;
		const { resolutionComplete, state } = useResolvedComponentResult("LinkCard", props);
		if (!state && needsResolution) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading link" });
		const title = state?.title ?? props.title ?? props.url ?? "Link";
		const url = state?.url ?? props.url ?? "";
		const source = state?.source_label ?? props.subtitle;
		const snippet = state?.snippet ?? props.snippet;
		return /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`Open \\\${title}\\\`,
			onClick: () => GenUI.openUrl(url)
		}, /* @__PURE__ */ __dil.jsx("card", {
			gap: 2,
			size: "sm"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			minWidth: 0,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("favicon", {
			frame: true,
			size: 20,
			url
		}), source ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 1,
			size: "xs",
			truncate: true
		}, source) : null), /* @__PURE__ */ __dil.jsx("text", {
			color: "prose",
			maxLines: 2,
			size: "sm",
			truncate: true,
			weight: "medium"
		}, title), snippet ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 2,
			size: "sm",
			truncate: true
		}, snippet) : null));
	}

//#endregion
return LinkCard;
})();
return __dilDefaultExport;
})()))\`,MediaFallback:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentMediaFallback(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "MediaFallback",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "MediaFallback", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentMediaFallback, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region MediaFallback.dil.tsx
	function MediaFallback({ children, height = "100%", width = "100%" }) {
		return /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			background: "surface-tertiary",
			height,
			justify: "center",
			width
		}, children);
	}

//#endregion
return MediaFallback;
})();
return __dilDefaultExport;
})()))\`,MemoryCite:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentMemoryCite(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "MemoryCite",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "MemoryCite", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentMemoryCite, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region MemoryCite.dil.tsx
	function MemoryCite() {
		return null;
	}

//#endregion
return MemoryCite;
})();
return __dilDefaultExport;
})()))\`,MessageReaction:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentMessageReaction(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "MessageReaction",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "MessageReaction", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentMessageReaction, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region MessageReaction.dil.tsx
	function MessageReaction() {
		return null;
	}

//#endregion
return MessageReaction;
})();
return __dilDefaultExport;
})()))\`,NewsCarousel:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentNewsCarousel(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "NewsCarousel",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "NewsCarousel", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentNewsCarousel, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region NewsCarousel.dil.tsx
	function NewsCarousel(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("NewsCarousel", props);
		const isSm = DIL.useBreakpoint("sm");
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading news" });
		const items = state.items ?? [];
		return items.length ? /* @__PURE__ */ __dil.jsx("col", {
			gap: 3,
			width: "100%"
		}, state.title ? /* @__PURE__ */ __dil.jsx("text", { strong: true }, state.title) : null, /* @__PURE__ */ __dil.jsx("carousel", {
			ariaLabel: "News",
			gap: 4
		}, items.map((item) => /* @__PURE__ */ __dil.jsx("carousel-item", {
			background: "surface-elevated",
			key: item.ref,
			padding: 0,
			variant: "outline",
			width: isSm ? "31.5%" : "47.5%"
		}, /* @__PURE__ */ __dil.jsx("pressable", {
			onClick: () => GenUI.openUrl(item.url),
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("col", {
			gap: 4,
			height: "100%",
			padding: { bottom: 6 },
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("box", {
			align: "center",
			background: "surface-secondary",
			clip: true,
			height: "144px",
			justify: "center",
			width: "100%"
		}, item.thumbnail_url ? /* @__PURE__ */ __dil.jsx("image", {
			alt: item.title,
			fit: "cover",
			height: "100%",
			radius: "none",
			src: item.thumbnail_url,
			width: "100%"
		}) : /* @__PURE__ */ __dil.jsx("favicon", {
			frame: true,
			size: 40,
			url: item.url
		})), /* @__PURE__ */ __dil.jsx("col", {
			gap: 2,
			padding: { x: 4 },
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 1
		}, /* @__PURE__ */ __dil.jsx("favicon", {
			frame: true,
			size: 16,
			url: item.url
		}), /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 1,
			size: "xs",
			truncate: true
		}, item.source_label)), /* @__PURE__ */ __dil.jsx("text", {
			maxLines: 5,
			size: "sm"
		}, item.title), item.date_label ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "xs"
		}, item.date_label) : null))))))) : null;
	}

//#endregion
return NewsCarousel;
})();
return __dilDefaultExport;
})()))\`,ProductCard:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentProductCard(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "ProductCard",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "ProductCard", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentProductCard, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region shared.dil.ts
	function useResolvedComponentResult(componentName, props) {
		const opGenui = DIL.useAppData((appData) => appData.opGenui);
		if (props.__state !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: props.__state
		};
		const key = componentDataKey(componentName, props);
		const result = (typeof props.__resolutionId === "string" ? opGenui?.componentResults?.[props.__resolutionId] : void 0) ?? opGenui?.componentResults?.[key];
		if (isComponentResultEnvelope(result)) return result.status === "resolved" ? {
			status: "resolved",
			resolutionComplete: true,
			state: result.state
		} : {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		const legacyState = opGenui?.componentData?.[key];
		if (legacyState !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: legacyState
		};
		if (opGenui?.componentResults !== void 0) return {
			status: "failed",
			resolutionComplete: true,
			state: void 0
		};
		if (opGenui?.componentData !== void 0) return {
			status: "resolved",
			resolutionComplete: true,
			state: void 0
		};
		return {
			status: "pending",
			resolutionComplete: false,
			state: void 0
		};
	}
	function isComponentResultEnvelope(value) {
		if (typeof value !== "object" || value == null || Array.isArray(value)) return false;
		const result = value;
		if (result.status === "resolved") return typeof result.state === "object" && result.state != null && !Array.isArray(result.state);
		return result.status === "failed" && (result.code === "component_unavailable" || result.code === "tool_failed" || result.code === "invalid_tool_result") && typeof result.retryable === "boolean";
	}
	function componentDataKey(componentName, props) {
		return JSON.stringify([componentName, normalizeComponentProps(props)]);
	}
	function normalizeComponentProps(props) {
		const normalized = {};
		for (const key of Object.keys(props).sort()) {
			if (key === "__resolutionId" || key === "__state" || key === "children" || key === "fallback") continue;
			const value = normalizeComponentValue(props[key]);
			if (value !== void 0) normalized[key] = value;
		}
		return normalized;
	}
	function normalizeComponentValue(value) {
		if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") return value;
		if (Array.isArray(value)) return value.map(normalizeComponentValue);
		if (typeof value === "object") {
			const normalized = {};
			for (const key of Object.keys(value).sort()) {
				const nestedValue = normalizeComponentValue(value[key]);
				if (nestedValue !== void 0) normalized[key] = nestedValue;
			}
			return normalized;
		}
	}

//#endregion
//#region ProductCard.dil.tsx
	function ProductCard(props) {
		const { resolutionComplete, state } = useResolvedComponentResult("ProductCard", props);
		if (!state) return resolutionComplete ? null : /* @__PURE__ */ __dil.jsx("loading", { label: "Loading product" });
		if (!state.image_url) return null;
		const onClick = () => GenUI.openEntityDetail("product", state.title, { product: state.product });
		if (state.render_as === "item") return /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`View details for \\\${state.title}\\\`,
			height: "100%",
			onClick,
			padding: { x: 2 },
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("col", {
			gap: 2,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("box", {
			aspectRatio: "1 / 1",
			radius: "lg",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("image", {
			alt: state.title,
			fit: "contain",
			height: "100%",
			radius: "lg",
			src: state.image_url,
			width: "100%"
		})), /* @__PURE__ */ __dil.jsx("col", {
			gap: 1,
			minWidth: 0,
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: "sm",
			weight: "semibold"
		}, state.title), state.price || state.description ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			maxLines: 3,
			size: "sm"
		}, state.price ? /* @__PURE__ */ __dil.jsx("text", {
			inline: true,
			strong: true
		}, state.price) : null, state.description ? /* @__PURE__ */ __dil.jsx("text", { inline: true }, state.price ? " • " : "", state.description) : null) : null)));
		if (state.render_as === "hero") return /* @__PURE__ */ __dil.jsx("card", { width: "100%" }, /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`View details for \\\${state.title}\\\`,
			onClick
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 4,
			wrap: "nowrap",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("box", {
			aspectRatio: "4 / 3",
			maxWidth: "38%",
			minWidth: 144,
			width: 260
		}, /* @__PURE__ */ __dil.jsx("image", {
			alt: state.title,
			fit: "contain",
			height: "100%",
			radius: "lg",
			src: state.image_url,
			width: "100%"
		})), /* @__PURE__ */ __dil.jsx("col", {
			flex: "auto",
			gap: 2,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: "lg",
			weight: "semibold"
		}, state.title), /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			wrap: "wrap"
		}, state.price ? /* @__PURE__ */ __dil.jsx("text", { weight: "semibold" }, state.price) : null, state.merchant ? /* @__PURE__ */ __dil.jsx("text", { color: "secondary" }, state.merchant) : null), state.description ? /* @__PURE__ */ __dil.jsx("text", null, state.description) : null))));
		return /* @__PURE__ */ __dil.jsx("card", { width: "100%" }, /* @__PURE__ */ __dil.jsx("pressable", {
			ariaLabel: \\\`View details for \\\${state.title}\\\`,
			onClick
		}, /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 3,
			wrap: "nowrap",
			width: "100%"
		}, /* @__PURE__ */ __dil.jsx("box", {
			aspectRatio: "4 / 3",
			maxWidth: "32%",
			minWidth: 96,
			width: 132
		}, /* @__PURE__ */ __dil.jsx("image", {
			alt: state.title,
			fit: "contain",
			height: "100%",
			radius: "lg",
			src: state.image_url,
			width: "100%"
		})), /* @__PURE__ */ __dil.jsx("col", {
			flex: "auto",
			gap: 1,
			minWidth: 0
		}, /* @__PURE__ */ __dil.jsx("title", {
			size: "md",
			weight: "semibold"
		}, state.title), /* @__PURE__ */ __dil.jsx("row", {
			align: "center",
			gap: 2,
			wrap: "wrap"
		}, state.price ? /* @__PURE__ */ __dil.jsx("text", {
			size: "sm",
			weight: "semibold"
		}, state.price) : null, state.merchant ? /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm"
		}, state.merchant) : null), state.description ? /* @__PURE__ */ __dil.jsx("text", { size: "sm" }, state.description) : null))));
	}

//#endregion
return ProductCard;
})();
return __dilDefaultExport;
})()))\`,SpeechSynthesizer:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentSpeechSynthesizer(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "SpeechSynthesizer",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "SpeechSynthesizer", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentSpeechSynthesizer, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region SpeechSynthesizer.dil.tsx
	const unavailable = {
		available: false,
		status: "idle",
		error: null,
		play: () => {},
		stop: () => {}
	};
	const { useSpeechSynthesizer = () => unavailable } = DIL;
	function SpeechSynthesizer({ controls, disabled = false, logging, ...source }) {
		const speech = useSpeechSynthesizer(source, logging);
		DIL.useEffect(() => {
			if (disabled) speech.stop();
		}, [disabled, speech.stop]);
		const play = () => {
			if (!disabled) speech.play();
		};
		const stop = () => {
			if (!disabled) speech.stop();
		};
		if (controls) return controls({
			...speech,
			play,
			stop
		});
		if (!speech.available) return /* @__PURE__ */ __dil.jsx("text", null, "Audio unavailable");
		return speech.status === "idle" ? /* @__PURE__ */ __dil.jsx("button", {
			disabled,
			onClick: play
		}, "Play") : /* @__PURE__ */ __dil.jsx("button", { onClick: stop }, "Stop");
	}

//#endregion
return SpeechSynthesizer;
})();
return __dilDefaultExport;
})()))\`,WritingBlock:\`((createComponent) => {
    const hostGenUI = GenUI;
    const unscopedComponent = createComponent(DIL, hostGenUI);
    function ResolvedComponentWritingBlock(props) {
      const resolutionId = props.__resolutionId;
      const Component = DIL.useMemo(() => {
        if (typeof resolutionId !== "string") return unscopedComponent;
        const widgetGenUI = Object.freeze({
          ...hostGenUI,
          dispatchAction(action) {
            if (action.handler !== "server") return hostGenUI.dispatchAction(action);
            return hostGenUI.dispatchWidgetAction({
              type: action.type,
              payload: action.payload,
              nativeWidgetResolutionId: resolutionId,
              componentName: "WritingBlock",
            });
          },
        });
        const widgetDIL = Object.freeze({
          ...DIL,
          useState(initialState, options) {
            return DIL.useState(initialState, { ...options, widgetId: resolutionId });
          },
        });
        return createComponent(widgetDIL, widgetGenUI);
      }, [resolutionId]);
      return __dil.jsx(OpGenuiResolvedComponentBoundary, { componentName: "WritingBlock", componentProps: props, Component });
    }
    return Object.assign(ResolvedComponentWritingBlock, unscopedComponent);
  })((DIL, GenUI) => ((() => {
var __dilDefaultExport = (function() {


//#region WritingBlock.dil.tsx
	function WritingBlock({ children, content, subject, variant }) {
		const body = content ?? children;
		return /* @__PURE__ */ __dil.jsx("card", { size: "full" }, /* @__PURE__ */ __dil.jsx("col", { gap: 2 }, variant === "email" && subject ? /* @__PURE__ */ __dil.jsx(__dil.Fragment, null, /* @__PURE__ */ __dil.jsx("col", { gap: 1 }, /* @__PURE__ */ __dil.jsx("text", {
			color: "secondary",
			size: "sm",
			weight: "medium"
		}, "Subject"), /* @__PURE__ */ __dil.jsx("text", { weight: "semibold" }, subject)), /* @__PURE__ */ __dil.jsx("divider", null)) : /* @__PURE__ */ __dil.jsx("title", null, "Writing Block"), /* @__PURE__ */ __dil.jsx("text", { preserveWhitespace: true }, body)));
	}

//#endregion
return WritingBlock;
})();
return __dilDefaultExport;
})()))\`})})(Gt,Gt.exports)),Gt.exports}var Ae;function In(){if(Ae)return $t;Ae=1;const{DIL_COMPONENT_SOURCES:a}=Pe();return $t.DIL_COMPONENT_SOURCES=a,$t}var Nt={},Oe;function bn(){if(Oe)return Nt;Oe=1;const a=Object.freeze(typeof __RESTRICTED__<"u"&&__RESTRICTED__?["ArtistUpcomingEventsWidget","AskUserFiles","AskUserLocation","AskUserLocationV2","AskUserLocationV2Bidi","AsyncVideoCarousel","Bento","BusinessGalleryRefWidget","BusinessGalleryWidget","CalculatorAbcd2ScoreForTransientIschemicAttackWidget","CalculatorApacheIiScoreWidget","CalculatorApgarScoreWidget","CalculatorAsaPhysicalStatusClassificationWidget","CalculatorBilitoolWidget","CalculatorBisapScoreForPancreatitisWidget","CalculatorBishopScoreForCervicalRipeningWidget","CalculatorCanadianCtHeadRuleWidget","CalculatorCha2ds2VascScoreForAtrialFibrillationStrokeRiskWidget","CalculatorChildPughScoreForCirrhosisWidget","CalculatorCorrectedAdjustedAgeOfPretermInfantsWidget","CalculatorCurb65ScoreForPneumoniaWidget","CalculatorDukeTreadmillScoreWidget","CalculatorFourTScoreForHeparinInducedThrombocytopeniaWidget","CalculatorGlasgowBlatchfordScoreForUpperGiBleedingWidget","CalculatorGlasgowComaScaleGcsWidget","CalculatorGraceScoreForAcuteCoronarySyndromeWidget","CalculatorHasBledScoreForMajorBleedingRiskWidget","CalculatorHeartScoreForMajorCardiacEventsWidget","CalculatorHuntAndHessScoreForSubarachnoidHemorrhageWidget","CalculatorIchScoreWidget","CalculatorIsthDicScoreWidget","CalculatorModifiedRankinScaleWidget","CalculatorNexusCervicalSpineRuleWidget","CalculatorNihStrokeScaleNihssWidget","CalculatorOttawaAnkleRuleWidget","CalculatorOttawaKneeRuleWidget","CalculatorPaduaPredictionScoreForVenousThromboembolismRiskWidget","CalculatorPecarnPediatricHeadInjuryRuleWidget","CalculatorPediatricEarlyWarningScorePewsWidget","CalculatorPercRuleForPulmonaryEmbolismWidget","CalculatorPneumoniaSeverityIndexPsiPortWidget","CalculatorQsofaScoreWidget","CalculatorRansonCriteriaForPancreatitisWidget","CalculatorRevisedCardiacRiskIndexRcriWidget","CalculatorRevisedGenevaScoreForPulmonaryEmbolismWidget","CalculatorRochesterCriteriaForFebrileInfantsWidget","CalculatorRockallScoreForUpperGiBleedingWidget","CalculatorRoxIndexForHighFlowNasalCannulaWidget","CalculatorSirsCriteriaWidget","CalculatorSofaScoreWidget","CalculatorStopBangScoreForObstructiveSleepApneaWidget","CalculatorSurgicalApgarScoreWidget","CalculatorTimiRiskWidget","CalculatorWellsScoreForDeepVeinThrombosisWidget","CalculatorWellsScoreForPulmonaryEmbolismWidget","CalculatorWestleyCroupSeverityScoreWidget","CalculatorWidget","CalculatorYearsAlgorithmForPulmonaryEmbolismWidget","CalendarEventsWidget","CalendarList","CareProviderResultsWidget","CareProviderSidebarWidget","CfbGames","ChecklistWidget","ClockWidget","ConversationFollowUpActionList","ConversationalOnboardingAdvice","ConversationalOnboardingFollowUpPills","ConversationalOnboardingSearch","ConversationalOnboardingStudy","ConversationalOnboardingWriting","CopyWordsWidget","CricketSingleMatch","CurrencyConverterV2WidgetWithSource","CurrencyConverterWidgetWithSource","DigitalStopwatchWidget","DigitalTimerWidget","DraftEmail","EmailPreview","EntityCard","EntityExplorer","EntityOverviewCarouselWidget","EntityOverviewWidget","EntityReviewsRefWidget","EntityReviewsWidget","EntityThumbnailList","EplScheduleWidgetWithSource","EplStandingsWidgetWithSource","EventSidebarWidget","ExampleServerActionButton","F1RacesWidgetWithSource","F1StandingsWidgetWithSource","FollowUpChoiceCard","FollowUpLinkList","FollowUpPillGroup","FollowUpQuiz","Gpt4oSystemCard","Gpt5SystemCard","HolidayWidget","HomeworkHelperV2","ImageGenWidget","ImageGrid","InstantSuggestionsWidget","InternalPartnerAppWidget","IplScheduleWidgetWithSource","IplStandingsWidgetWithSource","JobsWidget","LearningAudioLabelCard","LearningFillBlankCard","LearningFlashcards","LearningImageChoiceCard","LearningImageLabelCard","LearningQuiz","LearningSentenceBuilderCard","LedgerAccountBreakdownWidget","LedgerAccountsWidget","LedgerCreditScoreDetail","LedgerCreditScoreWidget","LedgerEquityUpdatesWidget","LedgerFeeInterestPaidWidget","LedgerFinanceOnboardingWidget","LedgerFinanceStatusBannerWidget","LedgerIncomeTrackerWidget","LedgerLowConfidenceCategoryCorrection","LedgerLowConfidenceCategoryCorrectionLegacyWidget","LedgerNetWorthWidget","LedgerPortfolioDistributionWidget","LedgerRecentTransactionsWidget","LedgerRecurringTransactionsWidget","LedgerRepairBankConnectionWidget","LedgerSpendByCategoryDetail","LedgerSpendByCategoryRecentTransactions","LedgerSpendByCategoryWidget","LedgerSpendSoFarThisMonthWidget","LedgerTransactionDetail","LedgerUpcomingActivityRecentTransactions","LedgerUpcomingActivityWidget","LedgerWatchlistWidget","LocalBusinessWidget","LyricsWidgetWithSource","MarchMadness","MlbScheduleWidgetWithSource","MlbStandingsWidgetWithSource","MultipleChoiceBlockV2","NbaGameBoxscoreWidgetWithNbaGameBoxScoreSource","NbaPlayerSummaryWidgetWithSource","NbaScheduleWidgetWithSource","NbaScores","NbaStandingsWidgetWithSource","NcaambScheduleWidgetWithSource","NcaambStandingsWidgetWithSource","NcaawbScheduleWidgetWithSource","NcaawbStandingsWidgetWithSource","NewsArticleWidget","NewsArticleWidgetCarousel","NflGames","NflScheduleWidgetWithSource","NflStandingsWidgetWithSource","NhlScheduleWidgetWithSource","NhlStandingsWidgetWithSource","OfferScheduledPrompt","OfferVoiceConversation","OnboardingFeatureCard","OnboardingSelectionCard","OpenDetailWidget","OpenLearningFlashcards","OpenaiWidget","PackageTracker","PersistedWidgetDogfoodChecklistWidgetWithSource","PersistedWidgetDogfoodDailyNutritionWidgetWithSource","PersistedWidgetDogfoodExerciseLogWidgetWithSource","PersistedWidgetDogfoodGoalWidgetWithSource","PersonWidget","PersonWidgetAlwaysTrigger","PlacesMetadataBar","ProductCarousel","PromptChecklist","PulseDraftEmail","PulseExpansionCard","Rating","Reddit","RedditFromProductSearch","RedditFromSearch","ReservationTimePillsRefCarouselWidget","ReservationTimePillsRefWidget","RestaurantMenuRefWidget","RestaurantMenuWidget","SidebarFactTable","SidebarPeopleAlsoAsk","SoccerGames","StockChart","StockComparisonChart","StockHeatmap","SuggestAutomation","SuperbowlRiddleWidget","TabGroup","TabbedSectionWidget","TaskAutopauseCard","TaskExpansionCard","TennisPlayerSummaryWidgetWithSource","UnitConverterV2Widget","UnitConverterWidget","UpdateLearningFlashcards","VisualCardCarouselWidget","WeatherCurrentWithSource","WeatherSidebarTitleWidgetWithSource","WeatherWidgetV1WithSource","WeatherWidgetV3WithSource","WeatherWidgetWithSource","WebLinksCarousel","WnbaScheduleWidgetWithSource","WnbaStandingsWidgetWithSource","WordCardWidget"]:[]);return Nt.DIL_LAZY_COMPONENT_NAMES=a,Nt.DIL_COMPONENT_NAMES=Object.freeze(["OpGenuiResolvedComponentBoundary","AsyncImage","AsyncImageGroup","AsyncVideo","AutomationPlanSummary","Citation","Cite","CoTToolGroup","CodeBlock","CodeCite","Entity","FileCite","FileNavList","FlightCard","FlightCarousel","FlightTracker","FollowUp","FollowUpActionBar","GenImage","LearningSpeakCard","LearningVizDil","LearningVocabCard","Link","LinkCard","MediaFallback","MemoryCite","MessageReaction","NewsCarousel","ProductCard","SpeechSynthesizer","WritingBlock",...a]),Nt}var ze;function xn(){return ze||(ze=1,(function(a,t){a.path="dil_sandbox/src/DILComponentSources",Object.defineProperty(t,"__esModule",{value:!0}),t.getDILComponentSource=t.isDILRestrictedComponent=t.getDILComponentNames=t.DIL_COMPONENT_SOURCES=void 0;const e=In(),r=Pe(),l=bn();t.DIL_COMPONENT_SOURCES=e.DIL_COMPONENT_SOURCES;function i(){return l.DIL_COMPONENT_NAMES}t.getDILComponentNames=i;function u(s){return l.DIL_COMPONENT_NAMES.includes(s)&&!Object.prototype.hasOwnProperty.call(r.DIL_COMPONENT_SOURCES,s)}t.isDILRestrictedComponent=u;function d(s,m){var h;const x=(h=e.DIL_COMPONENT_SOURCES[s])!==null&&h!==void 0?h:m.get(s);if(x===void 0)throw new Error(\`DIL sandbox component '\${s}' is not loaded.\`);return x}t.getDILComponentSource=d})(zt,zt.exports)),zt.exports}var Ge;function Rn(){return Ge||(Ge=1,(function(a,t){a.path="dil_sandbox/src/DILSandboxGlobals",Object.defineProperty(t,"__esModule",{value:!0}),t.hardenSandboxGlobal=t.lockDownSandboxGlobal=t.getDILSandboxAllowedGlobalNames=void 0;const e=ot(),r=xn(),l=new Set(["AggregateError","Array","ArrayBuffer","Atomics","BigInt","BigInt64Array","BigUint64Array","Boolean","DataView","Date","DebuggerInternal","Error","EvalError","FinalizationRegistry","Float16Array","Float32Array","Float64Array","Function","HermesES6Internal","HermesInternal","Infinity","Intl","Int8Array","Int16Array","Int32Array","Iterator","JSON","Map","Math","NaN","Number","Object","Promise","Proxy","RangeError","ReferenceError","Reflect","RegExp","Set","SharedArrayBuffer","String","Symbol","SyntaxError","TextEncoder","TEMPORARY","PERSISTENT","TypeError","URIError","Uint8Array","Uint8ClampedArray","Uint16Array","Uint32Array","WeakMap","WeakRef","WeakSet","decodeURI","decodeURIComponent","encodeURI","encodeURIComponent","escape","eval","globalThis","isFinite","isNaN","onmessage","parseFloat","parseInt","undefined","unescape",...(0,r.getDILComponentNames)()]);function i(){return Array.from(l)}t.getDILSandboxAllowedGlobalNames=i;function u(h){s(h,!0),Object.freeze(h)}t.lockDownSandboxGlobal=u;function d(h,x){s(h,!1),x?(0,e.freezeObjectGraph)(h,!0):Object.freeze(h)}t.hardenSandboxGlobal=d;function s(h,x){for(let _=h;_!==null&&_!==Object.prototype;_=Object.getPrototypeOf(_))for(const n of Reflect.ownKeys(_))typeof n=="string"&&(x||n!=="onmessage")&&l.has(n)||m(_,n)}function m(h,x){try{Reflect.set(h,x,void 0)}catch{}try{Reflect.deleteProperty(h,x)}catch{}const _=Object.getOwnPropertyDescriptor(h,x);if(!(_===void 0||"value"in _&&_.value===void 0))throw new Error(\`Failed to remove sandbox global '\${String(x)}'.\`)}})(Ot,Ot.exports)),Ot.exports}var Cn=Rn();const En="__oaiDilWebElementProps";class wn extends pn.DILSandboxRuntime{pendingRenderFlushes;render(t){const e=[];this.pendingRenderFlushes=e;try{const r=super.render(t);if(r.encoded!==void 0&&!r.errors?.length)for(const l of e)super.scheduleFlush(l);return r}finally{this.pendingRenderFlushes=void 0}}scheduleFlush(t){this.pendingRenderFlushes?this.pendingRenderFlushes.push(t):super.scheduleFlush(t)}}class Dn{appDataProxies=new WeakMap;data;disposed=!1;dirty=!1;flushScheduled=!1;globals;lastSource;options;wrappedCallbacks=new WeakMap;renderedPropNames=[];rendering=!1;dispatchingCallback=!1;runtime;timeStore=new mn;types=[];wrappedDil=new WeakMap;wrappedJsx=new WeakMap;constructor(t,e){this.options=e;const r=()=>!this.disposed&&!this.rendering&&this.dispatchingCallback,l=vn(e,r),i=gn(e,r);this.globals=e.globals??{},this.data=Kt(e.data);for(const s of Object.keys(this.globals))if(Ne(s),s==="DIL"||s==="__dil")throw new Error(\`DIL global "\${s}" is reserved\`);const u=new Map,d=new Proxy(Object.create(null),{get:(s,m)=>{if(typeof m!="string")return;let h=u.get(m);return h||(h={childrenMode:Ee.DILElementChildrenMode.RenderedNodes,primitiveTextProp:void 0,renderedPropNames:this.renderedPropNames,typeId:this.types.push(m)},u.set(m,h)),h}});this.runtime=this.trace("runtime_construct",()=>new wn({elementsMetadata:d,requestRender:this.scheduleRender,trace:e.trace??((s,m)=>m()),errorMode:Ee.DILRenderErrorMode.ReportAndAbortRender,stateChangeHandler:(s,m,h)=>{try{this.options.onStateChange?.(JSON.parse(s),h)}catch{}},speechSynthesis:l,dictation:i,asyncErrorHandler:e.onError,sourceEvaluatorFactory:s=>this.createSourceEvaluator(s)})),this.trace("seed_runtime",()=>this.runtime.render(this.createRenderInput())),e.stateSnapshot&&this.trace("hydrate_state",()=>this.runtime.setStateSnapshot(JSON.stringify(e.stateSnapshot)));for(const[s,m]of Object.entries(e.widgetStateSnapshots??{}))this.runtime.setStateSnapshot(JSON.stringify(m),s);this.updateSource(t)}updateSource(t,e){if(this.disposed)return;try{const l=this.trace("update_source",()=>this.runtime.updateSource(t));if(l?.length){this.restoreSource(),this.options.onError(l[0]);return}}catch(l){this.restoreSource(),this.options.onError(l);return}const r=this.data;e&&(this.data=Kt(e)),this.render()?this.lastSource=t:(this.data=r,this.restoreSource())}setData(t){this.disposed||(this.data=Kt(t),this.render())}setStateSnapshot(t,e){this.disposed||(this.trace("hydrate_state",()=>this.runtime.setStateSnapshot(t===void 0?void 0:JSON.stringify(t),e)),this.flushRender())}invokeFunction(t,e,r){try{let l;this.dispatchingCallback=!0;try{l=this.runtime.invokeFunction(t,e)}finally{this.dispatchingCallback=!1}if(this.flushRender(),!l||typeof l.then!="function")return l;const i=Promise.resolve(l).then(u=>(this.flushRender(),u),u=>{if(this.options.onError(u),r)throw u});return r?i:void 0}catch(l){if(this.options.onError(l),r)throw l;return}}registerDilMessengerTransport(t,e){return this.runtime.registerHtmlViewMessengerTransport(t,e)}dispose(){if(!this.disposed){this.disposed=!0,this.timeStore.dispose();for(const t of this.runtime.dispose()??[])this.options.onError(t)}}scheduleRender=()=>{this.dirty=!0,this.scheduleFlush()};scheduleFlush(){this.flushScheduled||this.disposed||(this.flushScheduled=!0,Promise.resolve().then(()=>{if(this.flushScheduled=!1,this.disposed)return;const t=()=>this.trace("flush",()=>{this.flushRender(),this.flushEffects(),this.flushRender()});this.options.runWithExecutionAttribution?this.options.runWithExecutionAttribution(t):t()}))}flushRender(){!this.dirty||this.disposed||this.rendering||this.trace("flush_render",()=>{for(;this.dirty&&!this.disposed&&!this.rendering;)this.dirty=!1,this.render()})}flushEffects(){try{for(const t of this.trace("flush_effects",()=>this.runtime.flush())??[])this.options.onError(t)}catch(t){this.options.onError(t)}}render(){this.rendering=!0;try{const{encoded:t,errors:e}=this.trace("render_operations",()=>this.runtime.render(this.createRenderInput()));return e?.length||!t?(this.options.onError(e?.[0]??new Error("DIL render failed")),!1):(this.options.onOperations({...t,types:[...this.types]}),this.trace("commit_state",()=>this.runtime.commitStateSnapshot()),this.scheduleFlush(),!0)}catch(t){return this.options.onError(t),!1}finally{this.rendering=!1}}createRenderInput(){let t=this.appDataProxies.get(this.data.appData);return t||(t=new Proxy(this.data.appData,{get:(e,r,l)=>r==="__dilHost"?{isMobile:this.data.isMobile===!0}:Reflect.get(e,r,l)}),this.appDataProxies.set(this.data.appData,t)),{activeBreakpoints:this.data.activeBreakpoints,animated:!1,appData:t,constants:this.data.constants,contextId:0,kind:3,stateSnapshot:void 0,theme:this.data.theme}}wrapDilRuntime=t=>{const e=this.wrappedDil.get(t);if(e)return e;const r=re.hardenApiFacade({...t,useNow:(l=!0,i=1e3)=>{if(typeof l!="boolean")throw new TypeError("DIL.useNow expects a boolean");if(i!==50&&i!==1e3)throw new TypeError("DIL.useNow expects intervalMs to be 50 or 1000");return t.useEffect(()=>l?this.timeStore.subscribe(this.scheduleRender,i):void 0,[l,i]),Date.now()},render:l=>{if(!Ft.isDILRuntimeElement(l)||typeof l.type!="function"||typeof l.props?.key!="string"||!/^body:\\d+$/.test(l.props.key))return t.render(l);const i={...l.props};return delete i.key,t.render(Ft.createDilElement(l.type,i,l.children))}});return this.wrappedDil.set(t,r),r};wrapJsxRuntime=t=>{const e=this.wrappedJsx.get(t);if(e)return e;const r=re.hardenApiFacade({Fragment:t.Fragment,jsx:(l,i,...u)=>{if(typeof l!="string")return t.jsx(l,i,...u);const d={...i};for(const[s,m]of Object.entries(d)){typeof m=="function"&&!Object.isExtensible(m)&&(d[s]=this.wrapCallback(m)),Ft.isDILRuntimeElement(m)&&!this.renderedPropNames.includes(s)&&this.renderedPropNames.push(s);const h=Qe.getDILHtmlViewMessengerHost(m);h&&(d[s]={__dilMessenger:"html-view",channelId:h.channelId,command:h.command,commands:{},onEvent:h.event})}return t.jsx(l,{...d,[En]:Object.keys(d).filter(s=>s!=="key")},...u)}});return this.wrappedJsx.set(t,r),r};wrapCallback(t){const e=this.wrappedCallbacks.get(t);if(e)return e;const r=(...l)=>t(...l);return this.wrappedCallbacks.set(t,r),r}createSourceEvaluator(t){const e=this.wrapJsxRuntime(t.jsxRuntimeFacade),r={...this.globals,DIL:this.wrapDilRuntime(t.widgetRuntimeApiFacade),__dil:e},l={GenUI:t.modelGenUIFacade,Date:t.dateConstructor,...this.globals,DIL:this.wrapDilRuntime(t.runtimeApiFacade),__dil:e};let i;return{beginRender(){},evaluate:u=>{i??=new Function(...Object.keys(r),this.trace("prepare_source",()=>this.prepareWidgetSource()))(...Object.values(r));const d={...l,...i},s=t.trace("DILRenderer.compileJS",()=>new Function(...Object.keys(d),\`"use strict";
\${u}\`));t.trace("DILRenderer.evaluateJS",()=>s(...Object.values(d)))},dispose(){i=void 0}}}prepareWidgetSource(){const t=Object.entries(this.options.dilComponents??{}).map(([r,l])=>{if(Ne(r),!/^[A-Z]/.test(r))throw new Error(\`DIL component name "\${r}" must start with uppercase\`);if(r==="DIL"||r==="__dil")throw new Error(\`DIL component name "\${r}" is reserved\`);if(Object.hasOwn(this.globals,r))throw new Error(\`DIL component name "\${r}" conflicts with a global\`);return\`const \${r}=(\${l});\`}),e=Object.keys(this.options.dilComponents??{});return\`"use strict";\${t.join(\`
\`)}
return {\${e.join(",")}};\`}trace(t,e){return this.options.trace?this.options.trace(t,e):e()}restoreSource(){const t=this.lastSource;t!==void 0&&this.trace("restore_source",()=>this.runtime.updateSource(t))}}function Kt(a){return{activeBreakpoints:[],appData:{},constants:{},isMobile:!1,theme:"light",...a}}function Ne(a){if(!/^[A-Za-z_$][0-9A-Za-z_$]*$/.test(a))throw new Error(\`Invalid DIL global name "\${a}"\`)}const Sn=EventTarget.prototype.addEventListener,kn=EventTarget.prototype.removeEventListener;function dt(a,t,e){Reflect.apply(Sn,a,[t,e])}function Me(a,t,e){Reflect.apply(kn,a,[t,e])}class Un{disposed=!1;commandIndex=0;eventListeners=new Map;handlers;pendingCommands=new Map;port;diagnostics;diagnosticContext;constructor({handlers:t,port:e,diagnostics:r,diagnosticContext:l}){this.handlers=t,this.port=e,this.diagnostics=r,this.diagnosticContext=l,dt(this.port,"message",this.handleMessage),this.port.start()}commands=new Proxy(Object.create(null),{get:(t,e)=>{if(!(typeof e!="string"||e==="then"))return r=>this.sendCommand(e,r)}});emit(t,e){this.send({__oaiDilMessage:!0,data:e,event:String(t),kind:"event"})}on(t,e){const r=String(t),l=this.eventListeners.get(r)??new Set;return l.add(e),this.eventListeners.set(r,l),()=>{l.delete(e),l.size===0&&this.eventListeners.delete(r)}}dispose(t="DIL frame messenger disposed"){if(this.disposed)return;this.disposed=!0,Me(this.port,"message",this.handleMessage),this.port.close();const e=new Error(t);for(const[r,l]of this.pendingCommands)this.diagnostics?.record("command","cancelled",{...this.diagnosticContext,requestId:r,reason:"disposed"}),l.reject(e);this.pendingCommands.clear(),this.eventListeners.clear()}sendCommand(t,e){if(this.disposed)return Promise.reject(new Error("DIL frame messenger is disposed"));const r=\`command_\${this.commandIndex}\`;return this.commandIndex+=1,this.diagnostics?.record("command","begin",{...this.diagnosticContext,requestId:r,command:t,pendingRequests:this.pendingCommands.size+1}),new Promise((l,i)=>{this.pendingCommands.set(r,{reject:i,resolve:l});try{this.send({__oaiDilMessage:!0,command:t,data:e,id:r,kind:"command"})}catch(u){this.diagnostics?.fault("command",u,{...this.diagnosticContext,requestId:r,command:t}),this.pendingCommands.delete(r),i(u)}})}messageDetails(t){return{...this.diagnosticContext,command:t.kind==="event"?t.event:t.kind==="command"?t.command:void 0,requestId:"id"in t?t.id:void 0,reason:t.kind}}send(t){if(this.disposed)throw new Error("DIL frame messenger is disposed");try{this.port.postMessage(t)}catch(e){throw this.diagnostics?.fault("message",e,this.messageDetails(t)),e}this.diagnostics?.record("message","sent",this.messageDetails(t))}handleMessage=t=>{if(!jn(t.data))return;const e=t.data;switch(this.diagnostics?.record("message","received",this.messageDetails(e)),e.kind){case"ack":this.diagnostics?.record("command","acknowledged",{...this.diagnosticContext,requestId:e.id});break;case"command":this.handleCommand(e);break;case"event":for(const r of this.eventListeners.get(e.event)??[])r(e.data);break;case"response":{const r=this.pendingCommands.get(e.id);if(!r)return;this.pendingCommands.delete(e.id),this.diagnostics?.record("command",e.error?"rejected":"resolved",{...this.diagnosticContext,requestId:e.id,pendingRequests:this.pendingCommands.size}),e.error?r.reject(Ln(e.error)):r.resolve(e.result);break}}};async handleCommand(t){const e=t.command==="invokeGlobal"||t.command==="invokeMessengerCommand"?"host_call":"command",r=this.diagnostics?{...this.diagnosticContext,requestId:t.id,command:t.command}:void 0,l=Object.hasOwn(this.handlers,t.command)?this.handlers[t.command]:void 0;if(!l){this.sendResponseError(t.id,new Error(\`Unknown DIL frame command "\${t.command}"\`));return}let i=!1;try{this.diagnostics?.record(e,"begin",r);const u=l(t.data);i=!0,this.diagnostics?.record(e,"returned",r),t.acknowledge&&!this.disposed&&this.send({__oaiDilMessage:!0,id:t.id,kind:"ack"});const d=await u;if(this.diagnostics?.record(e,"resolved",r),this.disposed)return;try{this.send({__oaiDilMessage:!0,id:t.id,kind:"response",result:d})}catch(s){this.sendResponseError(t.id,s)}}catch(u){this.diagnostics?.record(e,i?"rejected":"threw",{...r,error:u}),this.disposed||this.sendResponseError(t.id,u)}}sendResponseError(t,e){this.send({__oaiDilMessage:!0,error:Jt(e),id:t,kind:"response"})}}function Jt(a){return a instanceof Error?{message:a.message,name:a.name}:{message:String(a),name:"Error"}}function Ln(a){const t=new Error(a.message);return Object.defineProperty(t,"name",{configurable:!0,enumerable:!0,value:a.name,writable:!0}),a.stack&&(t.stack=a.stack),t}function jn(a){if(a==null||typeof a!="object"||a.__oaiDilMessage!==!0)return!1;const t=a.kind;return t==="ack"||t==="command"||t==="event"||t==="response"}function We(a,t){const e=r=>Pn(r)?(...l)=>t(r.__oaiDilGlobalFunction,l):Array.isArray(r)?r.map(e):r!=null&&typeof r=="object"?Object.fromEntries(Object.entries(r).map(([l,i])=>[l,e(i)])):r;return e(a)}function Pn(a){return a!=null&&typeof a=="object"&&!Array.isArray(a)&&typeof a.__oaiDilGlobalFunction=="string"}const Qt=13,An="__dil_confirm_startup";function On(a){return a!=null&&typeof a=="object"&&a.__oaiDilFrame===!0&&a.kind==="createRunner"&&a.protocolVersion===Qt&&typeof a.compiledDil=="string"&&typeof a.runnerId=="string"}function zn(a){return a!=null&&typeof a=="object"&&a.__oaiDilFrame===!0&&a.kind==="disposeRunner"&&a.protocolVersion===Qt&&typeof a.runnerId=="string"}function Gn(a){return a!=null&&typeof a=="object"&&a.__oaiDilWorker===!0&&a.kind==="initializeControl"&&a.protocolVersion===Qt}const Nn=globalThis.crypto?.getRandomValues.bind(globalThis.crypto),Fe=(a,t)=>({kind:J.DILDictationEventKind.Error,error:{code:a,message:t}}),Mn=()=>Fe("host_error","Dictation could not complete. Please try again.");function Wn(a){if(!a||typeof a!="object")return;const t=a;switch(t.kind){case J.DILDictationEventKind.Recording:case J.DILDictationEventKind.Stopping:case J.DILDictationEventKind.Cancelled:return{kind:t.kind};case J.DILDictationEventKind.Transcript:case J.DILDictationEventKind.Done:return typeof t.transcript=="string"?{kind:t.kind,transcript:t.transcript}:void 0;case J.DILDictationEventKind.Error:if(typeof t.error?.code=="string"&&typeof t.error.message=="string")return{kind:t.kind,error:{code:t.error.code,message:t.error.message}}}}class Fn{constructor(t){this.send=t}send;index=0;prefix=Nn?.(new Uint8Array(16)).reduce((t,e)=>t+e.toString(16).padStart(2,"0"),"");observers=new Map;createSession(t,e){if(!this.prefix)throw new Error("Dictation transport identity unavailable");const r=\`\${this.prefix}:\${this.index++}\`;this.observers.set(r,{sequence:0,receive:e});try{this.send({action:"create",id:r,options:t})}catch(i){throw this.observers.delete(r),i}let l=!1;return{start:()=>{!l&&this.observers.has(r)&&this.send({action:"start",id:r})},stop:()=>{!l&&this.observers.has(r)&&this.send({action:"stop",id:r})},cancel:()=>{this.observers.delete(r),l||this.send({action:"cancel",id:r})},dispose:()=>{l||(l=!0,this.observers.delete(r),this.send({action:"dispose",id:r}))}}}receive=({id:t,sequence:e,event:r})=>{const l=this.observers.get(t);if(!l||!Number.isSafeInteger(e)||e<=l.sequence)return;l.sequence=e;const i=Wn(r)??Mn();(i.kind===J.DILDictationEventKind.Done||i.kind===J.DILDictationEventKind.Error||i.kind===J.DILDictationEventKind.Cancelled)&&this.observers.delete(t),l.receive(i)};fail(t){const e=this.observers.get(t);this.observers.delete(t),e?.receive(Fe("transport_error","The dictation connection was lost."))}dispose(){const t=[...this.observers.keys()];this.observers.clear();for(const e of t)this.send({action:"dispose",id:e})}}const Xt=Object.freeze({status:"idle",available:!1,error:null});function Vn(a){if(!a||typeof a!="object")return Xt;const t=a;let e=null;if(t.error&&typeof t.error=="object"){const r=t.error,l=r.failureStage;(l==="play"||l==="request"||l==="response"||l==="streaming")&&(e={failureStage:l},typeof r.httpStatus=="number"&&Number.isInteger(r.httpStatus)&&r.httpStatus>=100&&r.httpStatus<=599&&(e.httpStatus=r.httpStatus))}return{available:t.available===!0,status:e?"idle":t.status==="loading"||t.status==="playing"?t.status:"idle",error:e}}const Tn=globalThis.crypto?.getRandomValues.bind(globalThis.crypto);class Hn{constructor(t){this.send=t}send;index=0;prefix=Tn?.(new Uint8Array(16)).reduce((t,e)=>t+e.toString(16).padStart(2,"0"),"");observers=new Map;createSession(t,e){if(!this.prefix)return e(Xt),{play(){},stop(){},dispose(){}};const r=\`\${this.prefix}:\${this.index++}\`;return this.observers.set(r,e),e(Xt),this.send({action:"create",id:r,source:t}),{play:l=>this.send({action:"play",id:r,logging:l}),stop:l=>this.send({action:"stop",id:r,logging:l}),dispose:()=>{this.observers.delete(r),this.send({action:"dispose",id:r})}}}receive=({id:t,state:e})=>{this.observers.get(t)?.(Vn(e))}}function qn(a,t,e){const r=a.dictation===!0?new Fn(d=>{const s=e();t.commands.dictation(d.action==="start"&&s!==void 0?{...d,interactionCapability:s}:d).catch(()=>r?.fail(d.id))}):void 0,l=r?t.on("dictationEvent",r.receive):void 0,i=a.speechSynthesis?new Hn(d=>{const s=e(),m=(d.action==="play"||d.action==="stop"&&d.logging!==void 0)&&s!=null?{...d,interactionCapability:s}:d;t.commands.speech(m).catch(()=>{i?.receive({id:d.id,state:{available:!1,status:"idle",error:null}})})}):void 0,u=i?t.on("speechState",i.receive):void 0;return{options:{speechSynthesis:i,dictation:r?{kind:"ready",service:r}:void 0},dispose:()=>{l?.(),r?.dispose(),u?.()}}}const Bn=["host_setup","encode_globals","read_persistence","acquire_frame","iframe_create","iframe_load","iframe_resource","observer_bootstrap","module_load","module_resource","module_entry","frame_ready","manager_create","worker_create","worker_control","worker_module","harden_worker","runner_create","worker_ready","decode_globals","decode_persistence","unsafe_runner","runtime_construct","seed_runtime","hydrate_state","prepare_source","update_source","compile","evaluate","render","render_operations","snapshot_post","commit_state","persist_state","flush","flush_render","flush_effects","restore_source","command","host_call","snapshot_receive","snapshot_forward","apply_tree","notify","react_snapshot","react_materialize","react_commit","react_snapshot_effect","react_node_error","host_error","fallback","render_result","frame_timer","worker_timer","request_timer","health_probe","idle_probe","visibility","pagehide","pageshow","freeze","resume","frame_probe","event_loop","recovery","quarantine","runner_dispose","worker_stop","frame_dispose","message","error","coverage"],Yt=typeof performance>"u"?Date.now.bind(Date):performance.now.bind(performance),$n=typeof performance>"u"?0:performance.timeOrigin,Ve=Object.getOwnPropertyDescriptor,Kn=Object.getPrototypeOf,Jn=Error.isError,Qn=new Map([[Error.prototype,"Error"],[TypeError.prototype,"TypeError"],[RangeError.prototype,"RangeError"],[SyntaxError.prototype,"SyntaxError"],[ReferenceError.prototype,"ReferenceError"],[URIError.prototype,"URIError"],[EvalError.prototype,"EvalError"],[AggregateError.prototype,"AggregateError"]]);let Xn=0;const ut=256,Yn=32768,Te=512,Mt=32,Z=64,Zn=65536,to=8192,eo=12288,Zt=40,He=new Set(["iframe_create:returned","iframe_load:received","iframe_resource:received","observer_bootstrap:returned","module_entry:returned","module_load:begin","module_resource:returned","module_load:reported_error","runner_module_script_error","runner_module_csp_enforced","runner_module_exception","frame_ready:sent","frame_ready:received","worker_create:begin","worker_create:returned","worker_control:sent","worker_control:received","worker_module:returned","harden_worker:begin","harden_worker:returned","runner_create:sent","runner_create:received","runner_create:begin","runner_create:returned","worker_ready:sent","worker_ready:received","snapshot_post:sent","snapshot_receive:received","host_ingress_lifecycle","host_ingress_snapshot","snapshot_forward:sent","apply_tree:returned","request_timer:fired","worker_timer:fired","frame_timer:fired"]);function qe(a){if(a.operation==="module_load"&&a.reason==="runner_module_exception")return"runner_module_exception";if(a.fault||a.phase==="threw")return"first_fault";if(a.operation==="module_load"&&a.phase==="reported_error"){if(a.reason==="runner_module_script_error")return"runner_module_script_error";if(a.reason==="csp_violation"&&a.cspResource==="runner_module"&&a.cspDisposition==="enforce")return"runner_module_csp_enforced"}if(a.operation==="quarantine"||a.operation==="error")return a.operation;if(a.operation==="worker_control"&&(a.reason==="execution_started"||a.reason==="execution_finished"))return"worker_execution";if(a.realm==="host"&&a.operation==="message"&&a.phase==="received"&&(a.command==="snapshot"||a.command==="lifecycle"))return\`host_ingress_\${a.command}\`;const t=\`\${a.operation}:\${a.phase}\`;if(He.has(t))return t;if(a.operation==="health_probe"&&a.reason?.startsWith("target_"))return"worker_target";if(a.operation==="health_probe")return a.phase==="fired"?"health_probe_expired":"health_probe";if(a.operation==="recovery")return"recovery";if(a.operation==="event_loop")return"event_loop";if(["visibility","pagehide","pageshow","freeze","resume"].includes(a.operation))return"lifecycle";if(a.operation==="frame_probe")return"frame_probe";if(a.operation==="module_load"&&a.reason==="document_state")return"document_state";if(a.operation==="module_resource")return"module_resource";if(a.operation!=="message"&&a.operation!=="coverage")return"last_progress"}function Be(a){return[a.realm,a.documentBootId,a.realm==="worker"?a.workerGeneration:void 0,a.sourceId].join(":")}const no=new Set(Bn),oo=new Set(["begin","returned","threw","reported_error","sent","received","acknowledged","resolved","rejected","armed","paused","rearmed","cancelled","fired","ignored","decision"]),ro=new Set(["initialize","__dil_initialize","createRunner","disposeRunner","initializeControl","registerMessengerTransport","unregisterMessengerTransport","setCompiledDil","setData","setStateSnapshot","trigger","invokeGlobal","invokeMessengerCommand","snapshot","lifecycle","messengerEvent"]),io=["workerGeneration","sessionGeneration","startupAttempt","snapshotVersion","renderPass","spanId","parentSpanId","count","pendingRequests","pendingHostCalls","peers","budgetMs","deadlineMs","elapsedMs","httpStatus","resourceStartMs","resourceEndMs","navigationResponseEndMs","navigationDomInteractiveMs"],so=["triggerAcknowledged","workerReadySent","hidden","persisted","acknowledged","replaySafe","hasSuccessfulSnapshot","treePresent","hasError","moduleEvaluationSupported"],ao=["documentBootId","artifactId","runnerId","activeRunnerId","resourceArtifactId","triggerRunnerId","triggerRequestId","requestId","relatedRequestId"],$e=/^[a-zA-Z0-9_-]{1,96}$/;function te(a){const t={};for(const e of io){const r=a[e];typeof r=="number"&&Number.isFinite(r)&&r>=(e==="httpStatus"?100:0)&&(e!=="httpStatus"||r<=599)&&(t[e]=r)}for(const e of so)typeof a[e]=="boolean"&&(t[e]=a[e]);for(const e of ao){const r=a[e];typeof r=="string"&&$e.test(r)&&(t[e]=r)}for(const e of["command","triggerCommand"]){const r=a[e];r&&ro.has(r)&&(t[e]=r)}return(a.documentReadyState==="loading"||a.documentReadyState==="interactive"||a.documentReadyState==="complete")&&(t.documentReadyState=a.documentReadyState),a.cspDirective&&["script-src","script-src-elem","script-src-attr","worker-src","other"].includes(a.cspDirective)&&(t.cspDirective=a.cspDirective),(a.cspDisposition==="enforce"||a.cspDisposition==="report")&&(t.cspDisposition=a.cspDisposition),a.cspResource&&["runner_module","inline","eval","unknown"].includes(a.cspResource)&&(t.cspResource=a.cspResource),typeof a.reason=="string"&&/^[a-z_]{1,48}$/.test(a.reason)&&(t.reason=a.reason),t}function lo(a){const t=[];let e="unknown";try{if(Jn?.(a)){e=Qn.get(Kn(a))??e;const r=Ve(a,"name")?.value;typeof r=="string"&&/^(Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)$/.test(r)&&(e=r);const l=Ve(a,"stack")?.value;if(typeof l=="string"){e=/^(Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)(?=:|$)/.exec(l)?.[1]??e;for(const i of l.slice(0,4096).split(\`
\`).slice(1,17)){const u=/:(\\d{1,7}):(\\d{1,7})\\)?$/.exec(i.trim());u&&t.push({line:Number(u[1]),column:Number(u[2])})}}}}catch{}return Object.freeze({name:e,locations:Object.freeze(t.map(r=>Object.freeze(r))),stackUnavailable:t.length===0})}function Wt(a){if(a===null||typeof a!="object")return;const t=a;if(!["host","bootstrap","iframe","worker"].includes(t.realm)||typeof t.operation!="string"||!no.has(t.operation)||typeof t.phase!="string"||!oo.has(t.phase)||!Number.isSafeInteger(t.sequence)||t.sequence<0||typeof t.localTimeMs!="number"||!Number.isFinite(t.localTimeMs)||typeof t.timeOriginMs!="number"||!Number.isFinite(t.timeOriginMs))return;const e={...te(t),realm:t.realm,sequence:t.sequence,localTimeMs:t.localTimeMs,timeOriginMs:t.timeOriginMs,operation:t.operation,phase:t.phase};Number.isSafeInteger(t.sourceId)&&t.sourceId>=0&&(e.sourceId=t.sourceId);const r=t.fault;if(r&&typeof r.name=="string"&&/^(unknown|Error|TypeError|RangeError|SyntaxError|ReferenceError|URIError|EvalError|AggregateError)$/.test(r.name)&&Array.isArray(r.locations)&&r.locations.length<=16){const l=r.locations.filter(i=>i&&Number.isSafeInteger(i.line)&&i.line>=0&&i.line<1e7&&Number.isSafeInteger(i.column)&&i.column>=0&&i.column<1e7).map(({line:i,column:u})=>Object.freeze({line:i,column:u}));e.fault=Object.freeze({name:r.name,locations:Object.freeze(l),stackUnavailable:l.length===0})}return e}function tt(a){return[a.realm,a.documentBootId,a.workerGeneration,a.sourceId,a.runnerId,a.sessionGeneration,a.startupAttempt].join(":")}function ee(a,t,e){const r=e?t.hostReceivedAtMs:Yt();return{...a,...typeof r=="number"&&Number.isFinite(r)&&r>=0?{hostReceivedAtMs:r}:{}}}class uo{context;now=Yt;realm;emit;sequence=0;sourceId=++Xn;span=0;parentSpanId;dropped=0;bytes=0;faultCount=0;emitted=0;open=new Map;completedSpans=new Map;observedRealms=new Set;upstreamDropped=new Map;upstreamTruncated=!1;entries=[];sequences=new Map;progress=new Map;progressSources=new Map;retainedRunners=new Map;progressBytes=0;progressDropped=0;progressLoss=new Map;constructor(t){this.realm=t.realm,this.context=Object.freeze(te(t.context??{})),this.emit=t.emit}record(t,e,r={}){try{const l={...this.context,...te(r),realm:this.realm,sequence:++this.sequence,sourceId:this.sourceId,localTimeMs:Yt(),timeOriginMs:$n,operation:t,phase:e};r.error!==void 0&&this.faultCount<4&&(l.fault=lo(r.error),this.faultCount++),this.retain(l,"complete"),this.forward(l),this.sequence===Te&&this.record("coverage","ignored",{reason:"overflow"})}catch{this.dropped++}}trace(t,e,r={}){const l=++this.span,i=this.parentSpanId,u={...r,spanId:l,parentSpanId:i};this.record(t,"begin",u),this.parentSpanId=l;try{const d=e();return this.record(t,"returned",u),d}catch(d){throw this.fault(t,d,u),d}finally{this.parentSpanId=i}}fault(t,e,r={}){this.record(t,"threw",{...r,error:e})}ingest(t,e=!1,r=!1){try{const l=Wt(t);if(!l){this.dropped++;return}const i=tt(l);if(l.sequence<=(this.sequences.get(i)??-1))return;this.sequences.set(i,l.sequence),this.sequences.size>32&&this.sequences.delete(this.sequences.keys().next().value);const u=ee(l,t,r),d=Be(l),s=this.progressSources.get(d),m=s?s.complete&&l.sequence===s.sequence+1&&l.operation!=="coverage":l.sequence===1&&l.operation!=="coverage";if(l.sequence>(s?.sequence??-1)&&(this.progressSources.set(d,{sequence:l.sequence,complete:m}),this.progressSources.size>Z&&this.progressSources.delete(this.progressSources.keys().next().value),!m))for(const h of this.progress.values())Be(h.slots.values().next().value)===d&&(h.coverage="interrupted");this.retain(u,m?"complete":"interrupted"),e&&this.forward(l)}catch{this.dropped++}}mergeSnapshot(t,e=!1,r,l="merge"){try{if(t===null||typeof t!="object")return this.dropped++,!1;const i=t;if(i.schemaVersion!==1||!Array.isArray(i.records)||!Array.isArray(i.openOperations))return this.dropped++,!1;if(r){const n=f=>f!==null&&typeof f=="object"&&Object.entries(r).every(([y,w])=>w===void 0||f[y]===w),c=[...i.records.slice(0,ut),...i.openOperations.slice(0,Mt)];if(Array.isArray(i.progress))for(const f of i.progress.slice(0,Z)){if(!f||!Array.isArray(f.records))return this.markProgressDropped(r.runnerId),!1;for(const y of f.records.slice(0,Zt))c.push({...f.context,...y})}if(!c.every(n))return this.markProgressDropped(r.runnerId),!1}if(Array.isArray(i.observedRealms))for(const n of i.observedRealms.slice(0,4))(n==="host"||n==="bootstrap"||n==="iframe"||n==="worker")&&this.observedRealms.add(n);for(const n of i.records.slice(0,ut))this.ingest(n,!1,e);l==="replace"&&Array.isArray(i.progress)&&this.resetDocumentProgress();for(const n of i.openOperations.slice(0,Mt)){const c=Wt(n);if(!c||c.phase!=="begin"||c.spanId===void 0){this.dropped++;continue}this.observeSpan(ee(c,n,e))}let u=!0;if(Array.isArray(i.progress)){const n=this.progressDropped;for(const c of i.progress.slice(0,Z))this.mergeProgress(c,e);i.progress.length>Z&&this.markProgressDropped(),u=n===this.progressDropped}if(Number.isSafeInteger(i.progressDropped)&&i.progressDropped>0){this.progressDropped=Math.max(this.progressDropped,i.progressDropped);const n=typeof i.runnerId=="string"&&$e.test(i.runnerId)&&(this.progressLoss.has(i.runnerId)||this.progressLoss.size<Z)?i.runnerId:"";this.progressLoss.set(n,Math.max(this.progressLoss.get(n)??0,i.progressDropped))}const d=Wt(i.records[0]??i.openOperations[0]),s=d?tt(d):"empty",m=this.upstreamDropped.get(s)??0,h=typeof i.dropped=="number"&&Number.isSafeInteger(i.dropped)&&i.dropped>=0?i.dropped:0,x=Math.max(0,i.records.length-ut)+Math.max(0,i.openOperations.length-Mt),_=Math.min(Number.MAX_SAFE_INTEGER,h+x);return this.dropped=Math.min(Number.MAX_SAFE_INTEGER,this.dropped+Math.max(0,_-m)),this.upstreamDropped.set(s,Math.max(m,_)),this.upstreamDropped.size>32&&this.upstreamDropped.delete(this.upstreamDropped.keys().next().value),this.upstreamTruncated||=i.truncated===!0||x>0,u}catch{return this.dropped++,!1}}resetDocumentProgress(){this.progress.clear(),this.progressSources.clear(),this.progressLoss.clear(),this.progressBytes=0,this.progressDropped=0,this.open.clear(),this.completedSpans.clear()}retainRunner(t){if(!this.retainedRunners.has(t)&&this.retainedRunners.size>=Z)return this.markProgressDropped(t),()=>{};this.retainedRunners.set(t,(this.retainedRunners.get(t)??0)+1);let e=!1;return()=>{if(e)return;e=!0;const r=(this.retainedRunners.get(t)??1)-1;r?this.retainedRunners.set(t,r):this.retainedRunners.delete(t)}}snapshot(t={}){const e=[...this.progress.values()].filter(d=>{const s=d.slots.values().next().value;return!t.runnerId||!s.runnerId||s.runnerId===t.runnerId}).map(d=>{const s=[...d.slots.values()],{realm:m,sourceId:h,timeOriginMs:x,documentBootId:_,artifactId:n,runnerId:c,workerGeneration:f,sessionGeneration:y,startupAttempt:w}=s[0];return{context:{realm:m,sourceId:h,timeOriginMs:x,documentBootId:_,artifactId:n,runnerId:c,workerGeneration:f,sessionGeneration:y,startupAttempt:w},records:s.map(({realm:P,sourceId:N,timeOriginMs:H,documentBootId:D,artifactId:o,runnerId:p,workerGeneration:g,sessionGeneration:b,startupAttempt:E,...k})=>k),lastSequence:d.lastSequence,coverage:d.coverage}}),r=t.runnerId?[...co(e,t.runnerId,this.context.documentBootId)].sort((d,s)=>+(s.context.runnerId===t.runnerId)-+(d.context.runnerId===t.runnerId)):e,l=[];let i=2,u=0;for(const d of r){const s=JSON.stringify(JSON.stringify(d)).length+1;if(i+s>to){u++;continue}i+=s,l.push(Object.freeze({...d,context:Object.freeze(d.context),records:Object.freeze(d.records.map(m=>Object.freeze(m)))}))}return Object.freeze({schemaVersion:1,observedRealms:Object.freeze([...this.observedRealms]),documentBootId:this.context.documentBootId,runnerId:t.runnerId,progress:Object.freeze(l),progressDropped:u+(t.runnerId?(this.progressLoss.get(t.runnerId)??0)+(this.progressLoss.get("")??0):this.progressDropped),records:Object.freeze(t.records===!1?[]:this.entries.map(d=>d.record)),openOperations:Object.freeze(t.records===!1?[]:[...this.open.values()]),dropped:this.dropped,truncated:this.dropped>0||this.upstreamTruncated})}markProgressDropped(t){this.progressDropped++;const e=t&&(this.progressLoss.has(t)||this.progressLoss.size<Z)?t:"";this.progressLoss.set(e,(this.progressLoss.get(e)??0)+1)}observeProgress(t,e,r){const l=qe(t);if(!l)return;const i=tt(t);let u=this.progress.get(i);const d=u?.slots.get(l);if(u&&(u.lastSequence=Math.max(u.lastSequence,t.sequence)),d&&l==="event_loop"&&(d.elapsedMs??0)-(d.budgetMs??0)>=(t.elapsedMs??0)-(t.budgetMs??0)||d&&(l==="first_fault"||He.has(l)?d.sequence<=t.sequence:d.sequence>=t.sequence))return;r??=JSON.stringify(t).length;const s=r-(d?JSON.stringify(d).length:0);for(;!u&&this.progress.size>=Z||this.progressBytes+s>Zn;){const m=[...this.progress].find(([h,x])=>{const _=x.slots.values().next().value.runnerId;return h!==i&&_&&!this.retainedRunners.has(_)});if(!m){this.markProgressDropped(t.runnerId),u&&(u.coverage="interrupted");return}this.progressBytes-=m[1].bytes,this.progress.delete(m[0]),this.markProgressDropped(m[1].slots.values().next().value.runnerId)}if(u||(u={slots:new Map,lastSequence:0,coverage:e,bytes:0},this.progress.set(i,u)),u.bytes+s>eo||!d&&u.slots.size>=Zt){this.markProgressDropped(t.runnerId),u.coverage="interrupted";return}u.slots.set(l,Object.freeze(t)),u.lastSequence=Math.max(u.lastSequence,t.sequence),e!=="complete"&&(u.coverage=e),u.bytes+=s,this.progressBytes+=s}mergeProgress(t,e){if(!t||typeof t!="object"){this.markProgressDropped();return}const r=t;if(!Array.isArray(r.records)||r.records.length===0||r.records.length>Zt||!Number.isSafeInteger(r.lastSequence)||r.lastSequence<0||!["complete","interrupted","unavailable"].includes(r.coverage??"")){this.markProgressDropped();return}const l=r.records.map(m=>Wt({...r.context,...m})),i=l[0];if(!i||l.some(m=>!m||tt(m)!==tt(i)||m.sequence>r.lastSequence||!qe(m))){this.markProgressDropped();return}const u=this.progress.get(tt(i));if(u&&r.lastSequence<u.lastSequence)return;const d=this.progressDropped;for(let m=0;m<l.length;m++)this.observeProgress(ee(l[m],r.records[m],e),r.coverage);const s=this.progress.get(tt(i));s&&(s.lastSequence=Math.max(s.lastSequence,r.lastSequence),s.coverage=this.progressDropped===d?r.coverage:"interrupted")}observeSpan(t){if(t.spanId!==void 0){const e=\`\${tt(t)}:\${t.spanId}\`;if(t.phase==="begin"){if((this.completedSpans.get(e)??-1)>=t.sequence||(this.open.get(e)?.sequence??-1)>=t.sequence)return;this.open.has(e)||this.open.size<Mt?this.open.set(e,Object.freeze(t)):this.dropped++}else(t.phase==="returned"||t.phase==="threw")&&(this.open.delete(e),this.completedSpans.set(e,t.sequence),this.completedSpans.size>ut&&this.completedSpans.delete(this.completedSpans.keys().next().value))}}retain(t,e){const r=JSON.stringify(t).length;this.observeProgress(t,e,r),this.observedRealms.add(t.realm),this.observeSpan(t);const l=this.entries.length<8||t.fault!==void 0&&!this.entries.some(i=>i.record.fault);for(;this.entries.length>=ut||this.bytes+r>Yn;){const i=this.entries.findIndex(u=>!u.pinned);if(i<0){this.dropped++;return}this.bytes-=this.entries[i].bytes,this.entries.splice(i,1),this.dropped++}this.entries.push({record:Object.freeze(t),bytes:r,pinned:l}),this.bytes+=r}forward(t){if(this.emit){if(this.emitted++>=Te+1){this.dropped++;return}try{this.emit(t)}catch{this.dropped++}}}}function co(a,t,e){const r=a.filter(({context:s})=>(!t||!s.runnerId||s.runnerId===t)&&(!e||!s.documentBootId||s.documentBootId===e)),l=r.map(s=>s.context).filter(s=>s.runnerId===t),i=Math.max(-1,...l.map(s=>s.workerGeneration??-1)),u=Math.max(-1,...l.filter(s=>s.workerGeneration===i).map(s=>s.sessionGeneration??-1)),d=Math.max(-1,...l.filter(s=>s.workerGeneration===i&&s.sessionGeneration===u).map(s=>s.startupAttempt??-1));return r.filter(({context:s})=>(s.workerGeneration===void 0||s.workerGeneration===i)&&(s.sessionGeneration===void 0||s.sessionGeneration===u)&&(s.startupAttempt===void 0||s.startupAttempt===d))}const po=performance.now(),at=new Map;let lt,Q;dt(globalThis,"message",Ke),dt(globalThis,"error",a=>{const t=a;Q?.record("error","reported_error",{error:t.error??t.message,reason:"uncaught_error"})}),dt(globalThis,"unhandledrejection",a=>{Q?.record("error","rejected",{error:a.reason,reason:"unhandled_rejection"})});function Ke(a){if(lt||a.ports.length!==1||!Gn(a.data))return;Me(globalThis,"message",Ke);const t=a.ports[0];Q=Je(a.data.diagnostics,t),Q?.record("worker_module","returned",{elapsedMs:Q.now()-po}),Q?.record("worker_control","received");try{X(Q,"harden_worker",_o),dt(t,"message",mo),t.start(),lt=t,Q?.record("worker_control","returned")}catch(e){throw Q?.fault("worker_control",e),t.close(),e}}function _o(){const a=()=>{throw new Error("DIL policy blocked dynamic code evaluation")},t=[Function.prototype,Object.getPrototypeOf(async function(){}),Object.getPrototypeOf(function*(){}),Object.getPrototypeOf(async function*(){})];for(const l of t)Object.defineProperty(l,"constructor",{configurable:!1,enumerable:!1,value:a,writable:!1});globalThis.eval=a;const e=Object.getPrototypeOf(globalThis),r=EventTarget.prototype;for(let l=e;l!==null&&l!==r;l=Object.getPrototypeOf(l))for(const i of Reflect.ownKeys(l)){if(i==="constructor"||Reflect.deleteProperty(l,i))continue;const u=Reflect.get(l,i,globalThis);if(typeof u=="function"||typeof u=="object"&&u!==null)throw new Error(\`Failed to remove browser capability "\${String(i)}"\`)}for(const l of Reflect.ownKeys(r))l!=="constructor"&&Object.defineProperty(e,l,{configurable:!0,value:void 0});Cn.hardenSandboxGlobal(globalThis,!0)}function mo(a){if(ho(a.data)){const l=a.data.runnerId,i=typeof l=="string"&&l.length<=128?at.get(l):void 0,u=i?.diagnostics;lt?.postMessage({__oaiDilWorker:!0,kind:"healthy",requestId:a.data.requestId,...typeof l=="string"&&l.length<=128?{target:{...Q?.context,...u?.context,runnerId:l,present:i!==void 0,workerReadySent:i?.workerReadySent}}:{},...u?{diagnostics:u.snapshot({runnerId:l,records:!1})}:{}}),Q?.record("health_probe","sent",{requestId:a.data.requestId});return}if(zn(a.data)){const l=at.get(a.data.runnerId);l&&(at.delete(a.data.runnerId),ct(a.data.runnerId,()=>X(l.diagnostics,"runner_dispose",l.dispose)));return}if(a.ports.length!==1||!On(a.data))return;const t=a.data,e=at.get(t.runnerId);e&&(at.delete(t.runnerId),ct(t.runnerId,()=>X(e.diagnostics,"runner_dispose",e.dispose)));const r=Je(t.diagnosticContext,lt);r?.record("runner_create","received"),ct(t.runnerId,()=>{X(r,"runner_create",()=>fo(t,a.ports[0],r))})}function fo(a,t,e){const r=new Map;let l,i=null,u=0;const s=Object.fromEntries(Object.entries({registerMessengerTransport:({channelId:n})=>{r.get(n)?.();const c={command:(f,y)=>m.commands.invokeMessengerCommand({channelId:n,data:y,type:f}),event:(f,y)=>{m.emit("messengerEvent",{channelId:n,data:y,type:f})}};r.set(n,_().registerDilMessengerTransport(n,c))},setCompiledDil:({compiledDil:n,data:c})=>{_().updateSource(n,c)},setData:({data:n})=>{_().setData(n)},setStateSnapshot:({snapshot:n,widgetId:c})=>{_().setStateSnapshot(n,c)},trigger:n=>{const c=l;l=n.interactionCapability;try{const f=Number(n.id.slice(9));if(!Number.isSafeInteger(f))throw new Error(\`Unknown DIL callback "\${n.id}"\`);return _().invokeFunction(f,n.args,n.propagateErrors)}finally{l=c}},unregisterMessengerTransport:({channelId:n})=>{r.get(n)?.(),r.delete(n)}}).map(([n,c])=>[n,f=>ct(a.runnerId,()=>c(f))])),m=new Un({handlers:{...s,[An]:()=>{}},port:t,diagnostics:e}),h=qn(a,m,()=>l),x={diagnostics:e,workerReadySent:!1,dispose(){h.dispose();for(const n of r.values())n();r.clear(),i?.dispose(),m.dispose()}};at.set(a.runnerId,x),m.emit("lifecycle",{kind:"worker_ready"}),x.workerReadySent=!0,e?.record("worker_ready","sent");try{const n=X(e,"decode_globals",()=>We(a.globals,(y,w)=>m.commands.invokeGlobal({args:w,id:y,...l==null?{}:{interactionCapability:l}}))),c=a.statePersistence,f=c?X(e,"decode_persistence",()=>We({persistState:c.persistState},(y,w)=>m.commands.invokeGlobal({args:w,id:y})).persistState):void 0;if(c&&typeof f!="function")throw new Error("DIL state persistence is not available");i=X(e,"unsafe_runner",()=>new Dn(a.compiledDil,{...h.options,data:a.data,dilComponents:a.dilComponents,globals:n,onError:y=>{u+=1,e?.record("error","reported_error",{error:y,snapshotVersion:u}),X(e,"snapshot_post",()=>m.emit("snapshot",{error:Jt(y),version:u})),e?.record("snapshot_post","sent",{snapshotVersion:u,hasError:!0})},onOperations:y=>{u+=1,X(e,"snapshot_post",()=>m.emit("snapshot",{error:null,operations:y,version:u})),e?.record("snapshot_post","sent",{snapshotVersion:u,hasError:!1})},...e?{trace:(y,w)=>{const P=go(y);return P?e.trace(P,w):w()}}:{},runWithExecutionAttribution:y=>ct(a.runnerId,y),...c&&typeof f=="function"?{onStateChange:(y,w)=>{Promise.resolve(X(e,"persist_state",()=>f(y,w))).catch(()=>{})},stateSnapshot:c.snapshot,widgetStateSnapshots:c.widgetSnapshots}:{}}))}catch(n){e?.record("runner_create","reported_error",{error:n}),m.emit("lifecycle",{kind:"failure",stage:"runtime_error"}),X(e,"snapshot_post",()=>m.emit("snapshot",{error:Jt(n),version:u+1})),e?.record("snapshot_post","sent",{snapshotVersion:u+1,hasError:!0})}function _(){if(!i)throw new Error("DIL frame runner is not initialized");return i}}function ct(a,t){lt?.postMessage({__oaiDilWorker:!0,kind:"executionStarted",runnerId:a});try{return t()}finally{lt?.postMessage({__oaiDilWorker:!0,kind:"executionFinished",runnerId:a})}}function ho(a){return a!=null&&typeof a=="object"&&a.__oaiDilWorker===!0&&a.kind==="healthCheck"&&typeof a.requestId=="string"}function Je(a,t){if(!(!a||!t))return new uo({realm:"worker",context:a,emit:e=>{t.postMessage({__oaiDilWorker:!0,kind:"diagnostic",record:e})}})}function X(a,t,e){return a?a.trace(t,e):e()}function go(a){switch(a){case"DILRenderer.compileJS":return"compile";case"DILRenderer.evaluateJS":return"evaluate";case"DILRenderer.render":return"render";case"runtime_construct":case"seed_runtime":case"hydrate_state":case"prepare_source":case"update_source":case"render_operations":case"commit_state":case"flush":case"flush_render":case"flush_effects":case"restore_source":return a;default:return}}})();
`,F=typeof self<"u"&&self.Blob&&new Blob(["(self.URL || self.webkitURL).revokeObjectURL(self.location.href);",B],{type:"text/javascript;charset=utf-8"});function Re(r){let e;try{if(e=F&&(self.URL||self.webkitURL).createObjectURL(F),!e)throw"";const t=new Worker(e,{name:r?.name});return t.addEventListener("error",()=>{(self.URL||self.webkitURL).revokeObjectURL(e)}),t}catch{return new Worker("data:text/javascript;charset=utf-8,"+encodeURIComponent(B),{name:r?.name})}}function Ce(){return new Re}const we=/^runner-([A-Za-z0-9_-]{8,64})\.js$/.exec(new URL(import.meta.url).pathname.split("/").at(-1)??"")?.[1],ke=new URLSearchParams(location.hash.slice(1)).get("dil-diagnostics")==="1",g=ke?new fe({realm:"iframe",context:{artifactId:we,documentBootId:window.__oaiDilBootstrap?.documentBootId??`${Date.now().toString(36)}-${Math.random().toString(36).slice(2)}`},emit:r=>window.parent.postMessage({__oaiDilFrame:!0,kind:"diagnostic",protocolVersion:b,record:r},"*")}):void 0;g?.record("module_entry","returned");const S=new Ie({createWorker:Ce,diagnostics:g});window.addEventListener("message",Se);window.addEventListener("pagehide",r=>{r.persisted||S.dispose()});const Ee={__oaiDilFrame:!0,kind:"ready",protocolVersion:b};window.parent.postMessage(Ee,"*");g?.record("frame_ready","sent");function Se(r){if(r.source!==window.parent)return;const e=r.data;if(g&&e&&typeof e=="object"&&"__oaiDilFrame"in e&&e.__oaiDilFrame===!0&&"kind"in e&&e.kind==="diagnosticProbe"&&"protocolVersion"in e&&e.protocolVersion===b&&"requestId"in e&&typeof e.requestId=="string"&&e.requestId.length<=128){const t="runnerId"in e&&typeof e.runnerId=="string"&&e.runnerId.length<=128?e.runnerId:void 0;g.record("frame_probe","received",{requestId:e.requestId,runnerId:t}),S.probeTarget(t,()=>window.parent.postMessage({__oaiDilFrame:!0,kind:"diagnosticSnapshot",protocolVersion:b,requestId:e.requestId,documentBootId:g.context.documentBootId,diagnostics:g.snapshot({runnerId:t,records:!1})},"*"));return}if(Q(r.data)){if(r.ports.length!==1)return;g?.record("runner_create","received",{runnerId:r.data.runnerId}),S.createRunner(r.data,r.ports[0]);return}X(r.data)&&(g?.record("runner_dispose","received",{runnerId:r.data.runnerId}),S.disposeRunner(r.data.runnerId))}
