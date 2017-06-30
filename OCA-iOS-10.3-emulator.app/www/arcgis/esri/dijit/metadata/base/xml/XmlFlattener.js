// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
define("esri/dijit/metadata/base/xml/XmlFlattener","dojo/_base/declare dojo/_base/lang dojo/_base/array dojo/has ./xmlUtil ../../../../kernel".split(" "),function(g,k,h,m,l,n){g=g(null,{constructor:function(a){k.mixin(this,a)},flatten:function(a,b){var c={domIndex:{},domList:[],nNsPfx:0,nsPfxByUri:{},gxePfxByUri:{}};b&&(c.gxePfxByUri=this._makeGxePfxByUri(b));this._flattenDom({domData:c},a.documentElement,"");return{valuesByPath:c.domIndex,paths:c.domList,prefixesByUri:c.nsPfxByUri}},flattenNode:function(a,
b){var c={domIndex:{},domList:[],nNsPfx:0,nsPfxByUri:{},gxePfxByUri:b};this._flattenDom({domData:c},a,null);return c.domIndex},_flattenDom:function(a,b,c){var d=a.domData,e=l.nodeTypes.ELEMENT_NODE,f=this._flattenDomQN(d,b);null!=c&&(f=c+"/"+f);this._flattenDomValue(d,b,f);h.forEach(b.attributes,function(a){var b=this._flattenDomQN(d,a);this._flattenDomValue(d,a,f+"/@"+b)},this);h.forEach(b.childNodes,function(b){b.nodeType===e&&this._flattenDom(a,b,f)},this)},_flattenDomQN:function(a,b,c){var d=
c=b.localName,e=null;if(b=b.namespaceURI)b in a.gxePfxByUri?e=a.gxePfxByUri[b]:b in a.nsPfxByUri?e=a.nsPfxByUri[b]:(a.nNsPfx++,e="_"+a.nNsPfx,a.nsPfxByUri[b]=e),d=e+":"+c;return d},_flattenDomValue:function(a,b,c){b=this._getDomNodeText(b);c in a.domIndex?a.domIndex[c].push(b):(a.domIndex[c]=[b],a.domList.push(c))},_getDomNodeText:function(a){return l.getNodeText(a)},_makeGxePfxByUri:function(a){var b={};a&&h.forEach(a.getNamespaces(),function(a){a.prefix&&a.uri&&(b[a.uri]=a.prefix)});return b}});
m("extend-esri")&&k.setObject("dijit.metadata.base.xml.XmlFlattener",g,n);return g});