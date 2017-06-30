// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
require({cache:{"url:esri/dijit/LayerList/templates/LayerList.html":'\x3cdiv class\x3d"${theme}" role\x3d"presentation"\x3e\r\n  \x3cdiv role\x3d"menu" data-dojo-attach-point\x3d"_container" class\x3d"${css.container}"\x3e\r\n    \x3cul role\x3d"group" class\x3d"${css.list}" data-dojo-attach-point\x3d"_layersNode"\x3e\x3c/ul\x3e\r\n    \x3cdiv class\x3d"${css.noLayersText}" data-dojo-attach-point\x3d"_noLayersNode"\x3e\x3c/div\x3e\r\n  \x3c/div\x3e\r\n\x3c/div\x3e'}});
define("esri/dijit/LayerList","dojo/_base/array dojo/_base/declare dojo/_base/lang dojo/_base/kernel ../kernel dojo/uacss dojo/Deferred dojo/on dojo/query dojo/dom-class dojo/dom-style dojo/dom-construct dojo/dom-attr dojo/i18n!../nls/jsapi dijit/a11yclick dijit/_WidgetBase dijit/_TemplatedMixin ../promiseList ../layerUtils dojo/text!./LayerList/templates/LayerList.html".split(" "),function(n,v,m,K,L,M,C,q,F,g,D,k,l,x,E,N,O,P,Q,R){var S=n.some(["ar","he"],function(a){return-1!==K.locale.indexOf(a)});
v=v([N,O],{templateString:R,defaults:{theme:"esriLayerList",map:null,layers:null,showSubLayers:!0,showOpacitySlider:!1,showLegend:!1,removeUnderscores:!0,visible:!0},constructor:function(a){a=m.mixin({},this.defaults,a);this.set(a);this.css={container:"esriContainer",noLayers:"esriNoLayers",noLayersText:"esriNoLayersText",slider:"esriSlider",sliderLabels:"esriSliderLabels",legend:"esriLegend",tabContainer:"esriTabContainer",tabs:"esriTabs",tabMenu:"esriTabMenu",tabMenuItem:"esriTabMenuItem",tabMenuSelected:"esriTabMenuSelected",
tabMenuVisible:"esriTabMenuVisible",tab:"esriTab",tabSelected:"esriTabSelected",toggleButton:"esriToggleButton",iconCollapse:"esri-icon-down",iconExpand:S?"esri-icon-left":"esri-icon-right",list:"esriList",listExpand:"esriListExpand",subListExpand:"esriSubListExpand",listVisible:"esriListVisible",subList:"esriSubList",hasSubList:"esriHasSubList",hasButton:"esriHasButton",hasTabContent:"esriHasTabContent",subListLayer:"esriSubListLayer",layer:"esriLayer",layerScaleInvisible:"esriScaleInvisible",title:"esriTitle",
titleContainer:"esriTitleContainer",checkbox:"esriCheckbox",label:"esriLabel",button:"esriButton",content:"esriContent",clearFix:"esriClearFix",clear:"esriClear"}},postCreate:function(){this.inherited(arguments);var a=this;this.own(q(this._layersNode,q.selector("."+this.css.checkbox,"change"),function(){var c,b;c=l.get(this,"data-layer-index");b=l.get(this,"data-sublayer-index");a._toggleLayer(c,b);a._toggleState(c,b)}));this.own(q(this._layersNode,q.selector("."+this.css.tabMenuItem,E.press),function(){var c=
l.get(this,"data-layer-index"),b=l.get(this,"data-tab-id");a._toggleTab(c,b)}));this.own(q(this._layersNode,q.selector("."+this.css.toggleButton,E.press),function(){var c=l.get(this,"data-layer-index");a._toggleExpand(c)}))},startup:function(){this.inherited(arguments);this._mapLoaded(this.map).then(m.hitch(this,this._init))},destroy:function(){this._removeEvents();this.inherited(arguments)},refresh:function(){var a=this.layers;this._nodes=[];var c=[];if(a&&a.length)for(var b=0;b<a.length;b++)c.push(this._layerLoaded(b));
return P(c).always(m.hitch(this,function(a){this._loadedLayers=a;this._removeEvents();this._createLayerNodes();this._setLayerEvents();this.emit("refresh")}))},_mapLoaded:function(a){var c=new C;if(a)if(a.loaded)c.resolve();else q.once(a,"load",m.hitch(this,function(){c.resolve()}));else c.resolve();return c.promise},_toggleExpand:function(a){a=parseInt(a,10);if(a=this._nodes[a]){var c=a.layer;g.toggle(c,this.css.listExpand);c=g.contains(c,this.css.listExpand);l.set(a.toggle,"title",c?x.widgets.layerList.collapse:
x.widgets.layerList.expand);g.toggle(a.toggle,this.css.iconCollapse,c);g.toggle(a.toggle,this.css.iconExpand,!c)}},_toggleTab:function(a,c){a=parseInt(a,10);var b=this._nodes[a];if(b){var d=b.tabMenu,b=F("[data-tab-id]",b.tabs),d=F("[data-tab-id]",d),e;for(e=0;e<b.length;e++){var f=l.get(b[e],"data-tab-id");g.toggle(b[e],this.css.tabSelected,c===f)}for(e=0;e<d.length;e++)b=l.get(d[e],"data-tab-id"),g.toggle(d[e],this.css.tabMenuSelected,c===b)}},_layerLoaded:function(a){var c=this.layers[a],b=c.layer,
d={layer:b,layerInfo:c,layerIndex:a},e=new C;if(b)if(b.loaded)e.resolve(d);else if(b.loadError)e.reject(b.loadError);else{var f,h;f=q.once(b,"load",m.hitch(this,function(){h.remove();e.resolve(d)}));h=q.once(b,"error",m.hitch(this,function(a){f.remove();e.reject(a)}))}else e.resolve(d);return e.promise},_checkboxStatus:function(a){return!!a.visibility},_WMSVisible:function(a,c){var b=[];a&&a.layer&&(b=a.layer.visibleLayers);return-1<n.indexOf(b,c.name)},_subCheckboxStatus:function(a,c){var b;switch(a.layer.declaredClass){case "esri.layers.KMLLayer":b=
c.visible;break;case "esri.layers.WMSLayer":b=this._WMSVisible(a,c);break;default:b=c.defaultVisibility}return!!b},_getLayerTitle:function(a){var c="",b=a.layer;(a=a.layerInfo)&&a.title?c=a.title:b&&b.arcgisProps&&b.arcgisProps.title?c=b.arcgisProps.title:b&&b.name?c=b.name:a&&a.id?c=a.id:b&&b.id&&(c=b.id);return this.removeUnderscores?c.replace(/_/g," "):c},_showSublayers:function(a){return a.hasOwnProperty("showSubLayers")?a.showSubLayers:this.showSubLayers},_opacityChange:function(a){if(this.layer)this.layer.setOpacity(a);
else if(this.layers)for(var c=0;c<this.layers.length;c++)this.layers[c].layerObject&&this.layers[c].layerObject.setOpacity(a)},_legend:function(a,c,b){var d=k.create("div",{role:"tabpanel","data-tab-id":"legend",className:this.css.tab+" "+this.css.legend},a);require(["esri/dijit/Legend"],m.hitch(this,function(a){var e=[c];if(c&&c.featureCollection&&c.featureCollection.layers)for(var e=c.featureCollection.layers,h=0;h<e.length;h++)e[h].layer=e[h].layerObject;a=new a({map:this.map,layerInfos:e},k.create("div"));
k.place(a.domNode,d);a.startup();this._nodes[b].legend=a}))},_slider:function(a,c,b,d){a=k.create("div",{role:"tabpanel","data-tab-id":"opacity",className:this.css.tab+" "+this.css.slider},a);var e=k.create("div",{},a),f=k.create("div",{},a);require(["dijit/form/HorizontalSlider","dijit/form/HorizontalRuleLabels"],m.hitch(this,function(a,g){var h=new a({showButtons:!1,minimum:.1,maximum:1,layer:c,layers:b,discreteValues:.1,intermediateChanges:!0,value:d,onChange:this._opacityChange},e),k=new g({container:"bottomDecoration",
count:0,className:this.css.sliderLabels,labels:["0","50","100"]},f);h.startup();k.startup()}))},_createLayerNodes:function(){this._layersNode.innerHTML="";this._noLayersNode.innerHTML="";g.remove(this._container,this.css.noLayers);var a=this._loadedLayers;if(a&&a.length)for(var c=0;c<a.length;c++){var b=a[c];if(b){var d=b.layer,e=b.layerIndex,f=b.layerInfo;if(f){if(f.featureCollection&&!f.hasOwnProperty("visibility")){var h=f.featureCollection.layers[0];h&&h.layerObject&&(f.visibility=h.layerObject.visible)}d&&
!f.hasOwnProperty("visibility")&&(f.visibility=f.layer.visible);d&&!f.hasOwnProperty("id")&&(f.id=f.layer.id);var t,h=k.create("li",{role:"menuitem",className:this.css.layer});k.place(h,this._layersNode,"first");t=k.create("div",{className:this.css.title},h);var m=k.create("div",{className:this.css.tabContainer},h),n=k.create("ul",{role:"tablist",className:this.css.tabMenu+" "+this.css.clearFix},m),m=k.create("div",{className:this.css.tabs},m),q=[],y;d&&(y=d.declaredClass);var r=this._checkboxStatus(f),
u=k.create("div",{className:this.css.titleContainer},t),p=this.id+"_checkbox_"+e,z=k.create("input",{type:"checkbox",id:p,"data-layer-index":e,className:this.css.checkbox},u);l.set(z,"checked",r);d&&!d.visibleAtMapScale&&(g.add(h,this.css.layerScaleInvisible),l.set(h,"aria-disabled","true"),l.set(z,"disabled","disabled"));var w=k.create("div",{tabindex:0,role:"button","data-layer-index":e,title:x.widgets.layerList.expand,className:this.css.toggleButton+" "+this.css.iconExpand},u),v;f.button&&(v=f.button,
g.add(h,this.css.hasButton),g.add(v,this.css.button),k.place(v,u));b=this._getLayerTitle(b);b=k.create("label",{className:this.css.label,textContent:b},u);l.set(b,"for",p);var p=k.create("div",{className:this.css.clear},u),G;f.content&&(G=f.content,g.add(G,this.css.content),k.place(G,t));this._nodes[e]={checkbox:z,title:t,tabMenu:n,tabs:m,titleContainer:u,label:b,layer:h,toggle:w,clear:p,button:v,content:G,subNodes:q};g.toggle(h,this.css.listVisible,r);if(d&&(t=d.layerInfos,"esri.layers.KMLLayer"===
y&&(t=d.folders),u=this._showSublayers(f),"esri.layers.ArcGISTiledMapServiceLayer"!==y&&t&&t.length))if(u){k.create("li",{tabindex:0,"data-tab-id":"sublayers","data-layer-index":e,role:"tab",className:this.css.tabMenuItem,textContent:x.widgets.layerList.sublayers},n);g.add(h,this.css.hasSubList);g.toggle(h,this.css.subListExpand,r);for(var r=k.create("div",{className:this.css.tab,"data-tab-id":"sublayers",role:"tabpanel"},m),u=k.create("ul",{role:"group",className:this.css.subList},r),C,z=[],r=0;r<
t.length;r++){var b=t[r],A,p=-1,w=null;"esri.layers.ArcGISDynamicMapServiceLayer"===y?(A=b.id,p=b.parentLayerId,b.subLayerIds||(b.defaultVisibility=d&&d.visibleLayers&&-1!==d.visibleLayers.indexOf(b.id)?!0:!1)):"esri.layers.KMLLayer"===y?(A=b.id,p=b.parentFolderId):"esri.layers.WMSLayer"===y&&(A=b.name,p=-1);if(-1!==p)if(w=this._nodes[e].subNodes[p],z[p])w=z[p];else{var B=w.subLayer,w=k.create("ul",{role:"group",className:this.css.subList},B);g.add(B,this.css.hasSubList);g.toggle(B,[this.css.listVisible,
this.css.subListExpand],J);z[p]=w}var J=this._subCheckboxStatus(f,b);J&&!C&&(C=!0);var H=this.id+"_checkbox_sub_"+e+"_"+A,p=k.create("li",{role:"menuitem",className:this.css.subListLayer},w||u),B=k.create("div",{className:this.css.title},p),I=k.create("div",{className:this.css.titleContainer},B),D=k.create("input",{type:"checkbox",id:H,"data-layer-index":e,"data-sublayer-index":A,className:this.css.checkbox},I);l.set(D,"checked",J);b=k.create("label",{className:this.css.label,textContent:b.title||
b.name||""},I);l.set(b,"for",H);H=k.create("div",{className:this.css.clear},I);q[A]={subList:u,subSubList:w,subLayer:p,subTitle:B,subTitleContainer:I,subCheckbox:D,subLabel:b,subClear:H}}}else for(r=0;r<t.length;r++)b=t[r],p=-1,"esri.layers.ArcGISDynamicMapServiceLayer"===y&&(p=b.parentLayerId,b.subLayerIds||(b.defaultVisibility=d&&d.visibleLayers&&-1!==d.visibleLayers.indexOf(b.id)?!0:!1));if(f.hasOwnProperty("showLegend")?f.showLegend:this.showLegend)k.create("li",{tabindex:0,role:"tab",className:this.css.tabMenuItem,
"data-layer-index":e,"data-tab-id":"legend",textContent:x.widgets.layerList.legend},n),this._legend(m,f,e);if(f.hasOwnProperty("showOpacitySlider")?f.showOpacitySlider:this.showOpacitySlider){var E;!d&&f.featureCollection?(E=f.featureCollection.layers,f=f.featureCollection.layers[0].opacity):f=d.opacity;k.create("li",{tabindex:0,"data-tab-id":"opacity",role:"tab",className:this.css.tabMenuItem,"data-layer-index":e,textContent:x.widgets.layerList.opacity},n);this._slider(m,d,E,f)}d=F("."+this.css.tab,
m);if(e=d.length)g.add(h,[this.css.hasTabContent]),g.add(d[0],this.css.tabSelected);1<e&&(g.add(h,this.css.tabMenuVisible),h=F("li",n),h.length&&g.add(h[0],this.css.tabMenuSelected))}}}else g.add(this._container,this.css.noLayers),l.set(this._noLayersNode,"textContent",x.widgets.layerList.noLayers)},_removeEvents:function(){if(this._layerEvents&&this._layerEvents.length)for(var a=0;a<this._layerEvents.length;a++)this._layerEvents[a].remove();this._layerEvents=[]},_emitToggle:function(a,c,b){this.emit("toggle",
{layerIndex:a,subLayerIndex:c,visible:b})},_toggleVisible:function(a,c){var b=this._nodes[a].checkbox;g.toggle(this._nodes[a].layer,this.css.listVisible,c);var d=l.get(b,"checked");g.contains(this._nodes[a].layer,this.css.hasSubList)&&g.toggle(this._nodes[a].layer,this.css.subListExpand,d);d!==c&&(l.set(b,"checked",c),this._emitToggle(a,null,c))},_layerVisChangeEvent:function(a,c,b){b=c?a.layerInfo.featureCollection.layers[b].layer:a.layer;var d=q(b,"visibility-change",m.hitch(this,function(b){var d=
this.layers&&this.layers[a.layerIndex];d&&(d.visibility=b.visible);c?this._featureCollectionVisible(a.layerIndex,b.visible):this._toggleVisible(a.layerIndex,b.visible)}));this._layerEvents.push(d);c||(d=q(b,"scale-visibility-change",m.hitch(this,function(b){b=b.target.visibleAtMapScale;var c=this._nodes[a.layerIndex].checkbox,d=this._nodes[a.layerIndex].layer;g.toggle(d,this.css.layerScaleInvisible,!b);b?(l.remove(d,"aria-disabled"),l.remove(c,"disabled")):(l.set(d,"aria-disabled","true"),l.set(c,
"disabled","disabled"))})),this._layerEvents.push(d),"esri.layers.ArcGISDynamicMapServiceLayer"===b.declaredClass&&(b=q(this.map,"zoom-end",m.hitch(this,function(){this._subLayerScale(a)})),this._layerEvents.push(b),this._subLayerScale(a)))},_subLayerScale:function(a){var c=a.layer.createDynamicLayerInfosFromLayerInfos(),b=Q._getLayersForScale(this.map.getScale(),c);n.forEach(c,m.hitch(this,function(c){if(!c.subLayerIds){c=c.id;var d=this._nodes[a.layerIndex].subNodes[c];if(d){var f=d.subLayer,d=
d.subCheckbox,h=!1;-1===n.indexOf(b,c)&&(h=!0);g.toggle(f,this.css.layerScaleInvisible,h);h?(l.set(f,"aria-disabled","true"),l.set(d,"disabled","disabled")):(l.remove(f,"aria-disabled"),l.remove(d,"disabled"))}}}))},_layerEvent:function(a){var c=a.layerInfo;if(c.featureCollection&&c.featureCollection.layers&&c.featureCollection.layers.length){if((c=c.featureCollection.layers)&&c.length)for(var b=0;b<c.length;b++)this._layerVisChangeEvent(a,!0,b)}else this._layerVisChangeEvent(a)},_getVisibleLayers:function(a,
c){var b=a.layerInfos,d,e=[-1];"undefined"!==typeof c&&(b[c].defaultVisibility=!b[c].defaultVisibility);for(d=0;d<b.length;d++){var f=b[d];f.defaultVisibility&&(e.push(f.id),f=n.lastIndexOf(e,-1),-1!==f&&e.splice(f,1))}b=[];for(d=0;d<e.length;d++)f=e[d],this._allIdsPresent(a,f,e)&&b.push(f);d=[];for(e=0;e<b.length;e++)(f=this._getLayerInfo(a,b[e]))&&null===f.subLayerIds&&d.push(b[e]);d.length||(d=[-1]);return d},_toggleState:function(a,c){var b,d;a=parseInt(a,10);d=this._nodes[a];d.legend&&d.legend.refresh();
null!==c?(c=parseInt(c,10),b=d.subNodes[c].subLayer,d=d.subNodes[c].subCheckbox):(b=d.layer,d=d.checkbox);d=l.get(d,"checked");g.contains(b,this.css.hasSubList)&&g.toggle(b,this.css.subListExpand,d);g.toggle(b,this.css.listVisible,d)},_toggleLayer:function(a,c){if(this.layers&&this.layers.length){var b;a=parseInt(a,10);var d=this.layers[a],e=d.layer,f=e&&e.layerInfos,h;e&&(h=e.declaredClass);var g=d.featureCollection;if(g)for(b=!d.visibility,d.visibility=b,d=0;d<g.layers.length;d++)g.layers[d].layerObject.setVisibility(b);
else if(e)if(null!==c){if("esri.layers.ArcGISDynamicMapServiceLayer"===h)c=parseInt(c,10),g=this._getVisibleLayers(e,c),e.setVisibleLayers(g);else if("esri.layers.KMLLayer"===h)for(c=parseInt(c,10),g=e.folders,d=0;d<g.length;d++){if(h=g[d],h.id===c){e.setFolderVisibility(h,!h.visible);break}}else"esri.layers.WMSLayer"===h&&(g=e.visibleLayers,d=n.indexOf(g,c),-1===d?g.push(c):g.splice(d,1),e.setVisibleLayers(g));f&&(b=f[c].defaultVisibility)}else"esri.layers.ArcGISDynamicMapServiceLayer"===h&&(g=this._getVisibleLayers(e),
e.setVisibleLayers(g)),b=!e.visible,d.visibility=b,e.setVisibility(b);else b=!d.visible,d.setVisibility(b);this._emitToggle(a,c,b)}},_featureCollectionVisible:function(a,c){var b=this.layers[a],d=b.visibleLayers,e=b.featureCollection.layers;(d&&d.length?n.every(d,function(a){return e[a].layer.visible===c}):n.every(e,function(a){return a.layer.visible===c}))&&this._toggleVisible(a,c)},_setLayerEvents:function(){var a=this._loadedLayers;if(a&&a.length)for(var c=0;c<a.length;c++){var b=a[c];b.layer&&
this._layerEvent(b)}},_allIdsPresent:function(a,c,b){a=this._walkUpLayerIds(a,c);return n.every(a,function(a){return-1<n.indexOf(b,a)})},_walkUpLayerIds:function(a,c){var b=this._getLayerInfo(a,c),d=[];if(b)for(;-1!==b.parentLayerId;)(b=this._getLayerInfo(a,b.parentLayerId))&&d.push(b.id);return d},_getLayerInfo:function(a,c){for(var b,d=0;d<a.layerInfos.length;d++){var e=a.layerInfos[d];if(e.id===c){b=e;break}}return b},_isSupportedLayerType:function(a){return a&&!a._basemapGalleryLayerType||a&&
"basemap"!==a._basemapGalleryLayerType},_createLayerInfo:function(a){return{layer:a}},_updateAllMapLayers:function(){if(this.map&&(!this.layers||!this.layers.length)){var a=[];n.forEach(this.map.layerIds,function(c){c=this.map.getLayer(c);this._isSupportedLayerType(c)&&a.push(this._createLayerInfo(c))},this);n.forEach(this.map.graphicsLayerIds,function(c){c=this.map.getLayer(c);this._isSupportedLayerType(c)&&c._params&&c._params.drawMode&&a.push(this._createLayerInfo(c))},this);this._set("layers",
a)}},_init:function(){this._visible();this._updateAllMapLayers();this.refresh().always(m.hitch(this,function(){this.set("loaded",!0);this.emit("load")}))},_visible:function(){this.visible?D.set(this.domNode,"display","block"):D.set(this.domNode,"display","none")},_setThemeAttr:function(a){this.domNode&&(g.remove(this.domNode,this.theme),g.add(this.domNode,a));this._set("theme",a)},_setMapAttr:function(a){this._set("map",a);this._created&&this._mapLoaded(this.map).then(m.hitch(this,function(){this._updateAllMapLayers();
this.refresh()}))},_setLayersAttr:function(a){this._set("layers",a);this._created&&this.refresh()},_setRemoveUnderscoresAttr:function(a){this._set("removeUnderscores",a);this._created&&this.refresh()},_setShowSubLayersAttr:function(a){this._set("showSubLayers",a);this._created&&this.refresh()},_setShowOpacitySliderAttr:function(a){this._set("showOpacitySlider",a);this._created&&this.refresh()},_setShowLegendAttr:function(a){this._set("showLegend",a);this._created&&this.refresh()},_setVisibleAttr:function(a){this._set("visible",
a);this._created&&this._visible()}});M("extend-esri")&&m.setObject("dijit.LayerList",v,L);return v});