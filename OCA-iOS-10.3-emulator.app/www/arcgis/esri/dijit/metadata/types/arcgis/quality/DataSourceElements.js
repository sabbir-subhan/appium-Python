// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
require({cache:{"url:esri/dijit/metadata/types/arcgis/quality/templates/DataSourceElements.html":'\x3cdiv data-dojo-attach-point\x3d"containerNode"\x3e\r\n  \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Tabs"\x3e\r\n  \r\n    \x3c!-- source description --\x3e\r\n    \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Section"\r\n      data-dojo-props\x3d"showHeader:false,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.section.description}\'"\x3e          \r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/OpenElement"\r\n        data-dojo-props\x3d"target:\'srcDesc\',minOccurs:1,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.srcDesc}\'"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/InputTextArea"\x3e\x3c/div\x3e\r\n      \x3c/div\x3e\r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/OpenElement"\r\n        data-dojo-props\x3d"target:\'srcMedName\',minOccurs:0,label:\'${i18nArcGIS.codelist.MD_MediumNameCode}\'"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Element"\r\n          data-dojo-props\x3d"target:\'MedNameCd\',minOccurs:0,showHeader:false"\x3e\r\n          \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Attribute"\r\n            data-dojo-props\x3d"target:\'value\',minOccurs:0,showHeader:false"\x3e\r\n            \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/types/arcgis/form/InputSelectCode"\r\n              data-dojo-props\x3d"codelistType:\'MD_MediumNameCode\'"\x3e\r\n            \x3c/div\x3e\r\n          \x3c/div\x3e\r\n        \x3c/div\x3e\r\n      \x3c/div\x3e\r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Element"\r\n        data-dojo-props\x3d"target:\'srcScale\',minOccurs:0,showHeader:false"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/OpenElement"\r\n          data-dojo-props\x3d"target:\'rfDenom\',minOccurs:0,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.srcScale.rfDenom}\'"\x3e\r\n          \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/InputNumber"\r\n            data-dojo-props\x3d"minValue:0.0,minValueIsExclusive:true,hint:\'${i18nBase.hints.numberGreaterThanZero}\'"\x3e\r\n          \x3c/div\x3e\r\n        \x3c/div\x3e\r\n      \x3c/div\x3e\r\n    \x3c/div\x3e\r\n    \r\n    \x3c!-- source citation --\x3e\r\n    \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Section"\r\n      data-dojo-props\x3d"showHeader:false,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.section.srcCitatn}\'"\x3e\r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Element"\r\n        data-dojo-props\x3d"target:\'srcCitatn\',minOccurs:0,maxOccurs:\'unbounded\',label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.srcCitatn}\'"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/types/arcgis/citation/CitationElements"\x3e\x3c/div\x3e\r\n      \x3c/div\x3e\r\n    \x3c/div\x3e\r\n    \r\n    \x3c!-- source extent --\x3e\r\n    \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Section"\r\n      data-dojo-props\x3d"showHeader:false,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.section.srcExt}\'"\x3e\r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/types/arcgis/form/ExtentElement"\r\n        data-dojo-props\x3d"target:\'srcExt\',minOccurs:0,maxOccurs:\'unbounded\',label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.srcExt}\'"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/types/arcgis/extent/ExtentElements"\x3e\x3c/div\x3e\r\n      \x3c/div\x3e\r\n    \x3c/div\x3e\r\n    \r\n    \x3c!-- source reference system --\x3e\r\n    \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Section"\r\n      data-dojo-props\x3d"showHeader:false,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.section.srcRefSys}\'"\x3e\r\n      \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/form/Element"\r\n        data-dojo-props\x3d"target:\'srcRefSys\',minOccurs:0,label:\'${i18nArcGIS.dqInfo.dataLineage.dataSource.srcRefSys}\'"\x3e\r\n        \x3cdiv data-dojo-type\x3d"esri/dijit/metadata/types/arcgis/citation/CodeRefElements"\x3e\x3c/div\x3e\r\n      \x3c/div\x3e\r\n    \x3c/div\x3e\r\n    \r\n  \x3c/div\x3e\r\n\x3c/div\x3e'}});
define("esri/dijit/metadata/types/arcgis/quality/DataSourceElements","dojo/_base/declare dojo/_base/lang dojo/has ../../../../../kernel ../../../base/Descriptor dojo/text!./templates/DataSourceElements.html ../citation/CitationElements ../citation/CodeRefElements ../form/ExtentElement ../extent/ExtentElements".split(" "),function(a,b,c,d,e,f){a=a(e,{templateString:f});c("extend-esri")&&b.setObject("dijit.metadata.types.arcgis.quality.DataSourceElements",a,d);return a});