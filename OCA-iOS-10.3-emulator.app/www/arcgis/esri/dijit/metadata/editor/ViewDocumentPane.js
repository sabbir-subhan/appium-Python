// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
require({cache:{"url:esri/dijit/metadata/editor/templates/ViewDocumentPane.html":'\x3cdiv class\x3d"gxeViewDocumentPane"\x3e\r\n  \x3cdiv class\x3d"gxeMessage" data-dojo-attach-point\x3d"messageNode" style\x3d"display:none"\x3e\x3c/div\x3e\r\n  \x3cdiv data-dojo-attach-point\x3d"containerNode,rootContainer"\x3e\x3c/div\x3e\r\n\x3c/div\x3e'}});
define("esri/dijit/metadata/editor/ViewDocumentPane","dojo/_base/declare dojo/_base/lang dojo/dom-style dojo/has ../base/Templated dojo/text!./templates/ViewDocumentPane.html ../../../kernel".split(" "),function(a,c,b,d,e,f,g){a=a([e],{gxeDocument:null,templateString:f,xmlString:null,postCreate:function(){this.inherited(arguments)},hideMessage:function(){this.messageNode.innerHTML="";b.set(this.messageNode,"display","none")},showMessage:function(a){this.setNodeText(this.messageNode,a);b.set(this.messageNode,
"display","")}});d("extend-esri")&&c.setObject("dijit.metadata.editor.ViewDocumentPane",a,g);return a});