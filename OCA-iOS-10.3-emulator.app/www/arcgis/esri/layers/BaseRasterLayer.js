// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
define("esri/layers/BaseRasterLayer","dojo/_base/declare dojo/_base/lang dojo/_base/connect dojo/_base/array dojo/sniff dojo/dom-construct dojo/dom-style dojox/gfx/matrix ../kernel ../config ../lang ../domUtils ../geometry/Point ./layer".split(" "),function(p,q,g,r,t,h,f,k,e,u,v,m,w,x){var y=u.defaults.map.zoomDuration;return p([x],{declaredClass:"esri.layers.BaseRasterLayer",managedSuspension:!0,opacity:1,constructor:function(a,b){this.drawMode=b&&void 0!==b.drawMode?b.drawMode:!0;this.drawType=
b&&b.drawType?b.drawType:"2d";this.pixelData=null;this._initialize(a,b)},setDrawMode:function(a){this.drawMode=a},setOpacity:function(a){this.opacity!==a&&(this.opacity=a,this.onOpacityChange(a))},onOpacityChange:function(){},refresh:function(){if(!this._canDraw()||10>t("ie"))this.onError(Error("Unable to refresh. This layer is not supported in the current browser."));else this._map&&this._extentChangeHandler(this._map.extent)},clear:function(){this._canDraw()&&"2d"===this.drawType&&this._context.clearRect(0,
0,this._mapWidth,this._mapHeight)},getContext:function(){return this._context},onResume:function(){this.inherited(arguments);this._toggleTime();if("css-transforms"===this._map.navigationMode){var a=this._map.__visibleDelta;this._left=this._tdx=a.x;this._top=this._tdy=a.y;f.set(this._div,e._css.names.transform,e._css.translate(this._left,this._top))}this._displayTimer=this._displayTimer||setTimeout(q.hitch(this,function(){this._extentChangeHandler(this._map.extent,null,!0)}),0)},onSuspend:function(){this.inherited(arguments);
this._toggleTime();clearTimeout(this._displayTimer);this._displayTimer=null},redraw:function(){this.hasDataChanged=!1;this._setPixelData(this.originalPixelData)},getCurrentResolution:function(){var a=this._map.extent;return new w((a.xmax-a.xmin)/this._map.width,(a.ymax-a.ymin)/this._map.height,a.spatialReference)},setPixelFilter:function(a,b){this.pixelFilter=a;b||this.redraw()},_toggleTime:function(){},_setMap:function(a,b){this.inherited(arguments);this._dragOrigin={x:0,y:0};var c=this._div=h.create("div",
null,b),d={width:a.width+"px",height:a.height+"px",position:"absolute"};"css-transforms"===a.navigationMode?(d[e._css.names.transform]=e._css.translate(a.__visibleDelta.x,a.__visibleDelta.y),this._left=a.__visibleDelta.x,this._top=a.__visibleDelta.y):this._left=this._top=0;f.set(c,d);this._canvas=h.create("canvas",{id:"canvas",width:a.width+"px",height:a.height+"px",style:"position: absolute;"},c);v.isDefined(this.opacity)&&f.set(c,"opacity",this.opacity);(this._context=this._canvas.getContext(this.drawType))||
console.error("Unable to create the context. This browser might not support \x3ccanvas\x3e elements.");this._mapWidth=a.width;this._mapHeight=a.height;this._connects=[];this._connects.push(g.connect(a,"onPan",this,this._panHandler));this._connects.push(g.connect(a,"onPanEnd",this,this._panEndHandler));"css-transforms"===a.navigationMode?this._connects.push(g.connect(a,"onScale",this,this._onScaleHandler)):(this._connects.push(g.connect(a,"onZoom",this,this._onZoomHandler)),this._connects.push(g.connect(a,
"onZoomEnd",this,this._onZoomEndHandler)));this._connects.push(g.connect(a,"onResize",this,this._onResizeHandler));this._connects.push(g.connect(a,"onExtentChange",this,this._extentChangeHandler));this._connects.push(g.connect(this,"onVisibilityChange",this,this._visibilityChangeHandler));this._connects.push(g.connect(this,"onOpacityChange",this,this._opacityChangeHandler));this._startRect={left:0,top:0,width:a.width,height:a.height};this.evaluateSuspension();if(this.suspended&&!a.loaded)var n=g.connect(a,
"onLoad",this,function(){g.disconnect(n);n=null;this.evaluateSuspension()});return c},_unsetMap:function(a,b){r.forEach(this._connects,g.disconnect,this);var c=this._div;c&&(b.removeChild(c),h.destroy(c));this._map=this._canvas=this._context=this.data=this._connects=null;clearTimeout(this._displayTimer);this._displayTimer=null;this.inherited(arguments)},_canDraw:function(){return!!(this._map&&this._canvas&&this._context)},_requestDataErrorHandler:function(a){"CancelError"!==a.name&&(this.clear(),
this.onError(a))},_drawPixelData:function(){this._startRect={left:0,top:0,width:this._map.width,height:this._map.height};var a=this._useBrowserDecoding();!a&&this.drawMode||"css-transforms"!==this._map.navigationMode||(this._tdx=this._left,this._tdy=this._top,this._multiply=null,f.set(this._div,e._css.names.transform,e._css.translate(this._left,this._top)),f.set(this._canvas,e._css.names.transform,e._css.translate(-this._left,-this._top)),this._dragOrigin={x:0,y:0});if(this._canDraw&&this.drawMode)if(a)this._fireUpdateEnd();
else if(this.drawMode)if(this.pixelData&&this.pixelData.pixelBlock){var a=this.pixelData.pixelBlock,b=this._context,c=b.createImageData(a.width,a.height);c.data.set(a.getAsRGBA());var d=this.pixelData.extent,g=this._map.extent,l=this.getCurrentResolution(),h=0,k=0;Math.abs(d.xmin-g.xmin)>l.x&&(h=Math.round((d.xmin-g.xmin)/l.x));Math.abs(g.ymax-d.ymax)>l.y&&(k=Math.round((g.ymax-d.ymax)/l.y));this.clear();"css-transforms"===this._map.navigationMode?(this._tdx=this._left,this._tdy=this._top,this._multiply=
null,f.set(this._div,e._css.names.transform,e._css.translate(this._left,this._top)),f.set(this._canvas,e._css.names.transform,e._css.translate(-this._left,-this._top))):(f.set(this._div,{left:"0px",top:"0px",width:this._map.width+"px",height:this._map.height+"px"}),f.set(this._canvas,{left:"0px",top:"0px",width:this._map.width+"px",height:this._map.height+"px"}));this._dragOrigin={x:0,y:0};b.putImageData(c,h,k,0,0,a.width,a.height);this._fireUpdateEnd()}else this.clear()},_panHandler:function(a,b){"css-transforms"===
this._map.navigationMode?(this._left=this._map.__visibleDelta.x+b.x,this._top=this._map.__visibleDelta.y+b.y,f.set(this._div,e._css.names.transform,e._css.translate(this._left,this._top))):f.set(this._div,{left:this._startRect.left+b.x+"px",top:this._startRect.top+b.y+"px"})},_panEndHandler:function(a,b){b&&(this._startRect.left+=b.x,this._startRect.top+=b.y)},_onScaleHandler:function(a,b){var c={},d=e._css.names;f.set(this._canvas,d.transition,b?"none":d.transformName+" "+y+"ms ease");this._matrix=
a;a=this._multiply?k.multiply(a,this._multiply):a;if(this._tdx||this._tdy)a=k.multiply(a,{xx:1,xy:0,yx:0,yy:1,dx:-this._tdx,dy:-this._tdy});c[d.transform]=e._css.matrix(a);f.set(this._canvas,c)},_onZoomHandler:function(a,b,c){var d=this._startRect;a=d.width*b;b*=d.height;var e=d.left-(a-d.width)*(c.x-d.left)/d.width;c=d.top-(b-d.height)*(c.y-d.top)/d.height;f.set(this._canvas,{left:e+"px",top:c+"px",width:a+"px",height:b+"px"});this._endRect={left:e,top:c,width:a,height:b}},_onZoomEndHandler:function(){this._endRect&&
(this._startRect=this._endRect)},_onResizeHandler:function(a,b,c){f.set(this._div,{width:b+"px",height:c+"px"});f.set(this._canvas,{width:b+"px",height:c+"px"});this._startRect.width=this._canvas.width=b;this._startRect.height=this._canvas.height=c},_extentChangeHandler:function(a,b,c,d){this.suspended||b&&0===b.x&&0===b.y&&!c||("css-transforms"===this._map.navigationMode&&(b&&(this._dragOrigin.x+=b.x,this._dragOrigin.y+=b.y),c||(this._left=this._map.__visibleDelta.x,this._top=this._map.__visibleDelta.y,
f.set(this._div,e._css.names.transform,e._css.translate(this._left,this._top))),c&&(f.set(this._canvas,e._css.names.transition,"none"),this._multiply=this._multiply?k.multiply(this._matrix,this._multiply):this._matrix)),this._fireUpdateStart(),a=this._map,this._requestData(a.extent,a.width,a.height))},_visibilityChangeHandler:function(a){a?m.show(this._div):m.hide(this._div)},_opacityChangeHandler:function(a){f.set(this._div,"opacity",a)}})});