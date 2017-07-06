// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
define("esri/layers/vectorTiles/core/workers/JobProxy","require exports dojo/_base/kernel dojo/_base/lang dojo/_base/url dojo/Deferred ../../kernel ../../config ../../request ../Logger ../urlUtils ./WorkerFallbackImpl".split(" "),function(r,E,w,k,x,t,y,g,z,A,l,p){function B(){if(!C){var c=void 0;try{c=new Worker(m)}catch(h){n.warn("Failed to create Worker. Fallback to execute module in main thread",event),c=new p}return u(c)}if(!q){var c=new x(m),b=g.defaults?g.defaults.io.corsEnabledServers:g.request.corsEnabledServers;
-1===b.indexOf(c.host)&&b.push(c.host);q=z(m,{responseType:"text"})}return q.then(function(b){var c;try{c=new Worker(URL.createObjectURL(new Blob([b.data],{type:"text/javascript"})))}catch(a){n.warn("Failed to create Worker. Fallback to execute module in main thread",a),c=new p}return u(c)})}function u(c){function b(a){if(a&&a.data&&a.data.type)if(a=a.data.type,"\x3cworker-loaded\x3e"===a){a=c;var d;null!=g["default"]?(d=k.mixin({},g),delete d["default"],d=JSON.parse(JSON.stringify(d))):d=JSON.parse(JSON.stringify(g));
var e={async:!0,baseUrl:D,locale:w.locale,has:{},paths:{}};k.mixin(e,g.workers.loaderConfig);e.has=k.mixin({"esri-cors":1,"dojo-test-sniff":0,"config-deferredInstrumentation":0},e.has);e.paths=k.mixin({esri:"esri",dojo:"dojo",dojox:"dojox",dstore:"dstore",moment:"moment"},e.paths);a.postMessage({type:"\x3cconfigure\x3e",configure:{esriConfig:d,dojoConfig:e,loaderUrl:v}})}else"\x3cworker-configured\x3e"===a&&(c.removeEventListener("message",b),c.removeEventListener("error",h),f.resolve(c))}function h(a){a.preventDefault();
c.removeEventListener("message",b);c.removeEventListener("error",h);n.warn("Failed to create Worker. Fallback to execute module in main thread",a);c=new p;c.addEventListener("message",b);c.addEventListener("error",h)}var f=new t;c.addEventListener("message",b);c.addEventListener("error",h);return f.promise}var n=A.getLogger("esri.core.workers"),m=l.makeAbsolute(r.toUrl("./worker.js")),v=l.makeAbsolute(r.toUrl("./worker-init.js")),D=l.makeAbsolute("../../../../../../",v)+"/",C=!l.hasSameOrigin(m,location.href),
q=null;return function(){function c(b,c,f){var a=this;this.connections=b;this.index=c;this.workerInitCallback=f;this.msgCount=0;this.outgoingJobs={};this.incomingJobs={};this.incomingStaticJobs={};B().then(function(b){a.worker=b;a.worker.addEventListener("message",a.message.bind(a));a.worker.addEventListener("error",function(a){a.preventDefault();n.error(a)});a.workerInitCallback(a.index)})}c.prototype.terminate=function(){this.worker.terminate()};c.prototype.openConnection=function(b,c){return this.invoke("\x3copen-connection\x3e",
{path:b},void 0,c)};c.prototype.closeConnection=function(b){this.invoke("\x3cclose-connection\x3e",void 0,void 0,b)};c.prototype.invoke=function(b,c,f,a){var d=this,e=++this.msgCount,h=new t(function(b){d.worker.postMessage({type:"\x3ccancel\x3e",id:e,connection:a,data:{reason:b}});d.outgoingJobs[e]&&delete d.outgoingJobs[e]});this.outgoingJobs[e]=h;this.worker.postMessage({type:b,id:e,connection:a,data:c},f);return h.promise};c.prototype.message=function(b){var c=this;if(b&&b.data){var f=b.data.type;
if(f){var a=b.data,d=b.data.id;if("\x3cresponse\x3e"===f&&d){if(b=this.outgoingJobs[d])delete this.outgoingJobs[d],a.error?b.reject(a.error):b.resolve(a.data)}else if("\x3ccancel\x3e"===f&&d)(b=this.incomingJobs[d])&&b.cancel(a.data.reason),a.staticMsg&&(b=this.incomingStaticJobs[d])&&b.cancel(a.data.reason);else if("\x3cstatic-message\x3e"===f){var e=a.staticMsg;(b=y.workerMessages[e])&&"function"===typeof b?(a=b.call(this,a.data),this.incomingStaticJobs[d]=a,a.then(function(a){c.worker.postMessage({type:"\x3cstatic-message\x3e",
staticMsg:e,id:d,data:a.data},a.buffers)}).otherwise(function(a){a||(a="Error encountered at method"+e);a.dojoType&&"cancel"===a.dojoType||c.worker.postMessage({type:"\x3cstatic-message\x3e",staticMsg:e,id:d,error:a})}).always(function(){delete c.incomingStaticJobs[d]})):this.worker.postMessage({type:"\x3cstatic-message\x3e",staticMsg:e,id:d,error:b+" message type is not available on the kernel!"})}else{var g=a.connection;if(b=this.connections[g])if(b=b.client){var k=b[f];"function"===typeof k&&(a=
k.call(b,a.data),this.incomingJobs[d]=a,a.then(function(a){c.worker.postMessage({type:"\x3cresponse\x3e",id:d,connection:g,error:a.error,data:a.data},a.buffers)}).otherwise(function(a){a||(a="Error encountered at method"+f);a.dojoType&&"cancel"===a.dojoType||c.worker.postMessage({type:"\x3cresponse\x3e",id:d,connection:g,error:a})}).always(function(){delete c.incomingJobs[d]}))}}}}};return c}()});