// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
define("esri/dijit/metadata/types/arcgis/base/conditionals/FGDC_Reports","dojo/_base/declare dojo/_base/lang dojo/_base/array dojo/topic dojo/has ../../../../../../kernel dojo/i18n!../../../../nls/i18nArcGIS ../../../../base/Conditional ../../../../base/etc/docUtil".split(" "),function(d,h,e,f,k,l,m,n,p){d=d(n,{key:"FGDC_Reports",postCreate:function(){this.inherited(arguments);var b=this;this.own(f.subscribe("gxe/interaction-occurred",function(a){try{b.parentXNode&&a&&a.inputWidget&&a.inputWidget.parentXNode&&
"/metadata/dqInfo/report/@type"===a.inputWidget.parentXNode.gxePath&&b.emitInteractionOccurred()}catch(c){console.error(c)}}));this.own(f.subscribe("gxe/after-xnode-destroyed",function(a){try{b.parentXNode&&a&&a.xnode&&"report"===a.xnode.target&&b.emitInteractionOccurred()}catch(c){console.error(c)}}))},ensureFocus:function(){p.ensureVisibility(this.parentXNode);e.some(this.parentXNode.getChildren(),function(b){if(b._isGxeTabs)return e.some(b.getChildren(),function(a){if(a.isReportSection)return b.ensureActiveTab(a),
!0}),!0})},validateConditionals:function(b){var a=this.newStatus({message:m.conditionals[this.key]}),c=!0,d=this.parentXNode.domNode,g,e=!1,f=!1;this.isXNodeOff(this.parentXNode)||(c=!1,this.forActiveXNodes("/metadata/dqInfo/report/@type",d,function(a){a&&a.inputWidget&&(g=a.inputWidget.getInputValue(),"DQCompOm"===g?e=!0:"DQConcConsis"===g&&(f=!0));if(e&&f)return c=!0}));a.isValid=c;this.track(a,b);return a}});k("extend-esri")&&h.setObject("dijit.metadata.types.arcgis.base.conditionals.FGDC_Reports",
d,l);return d});