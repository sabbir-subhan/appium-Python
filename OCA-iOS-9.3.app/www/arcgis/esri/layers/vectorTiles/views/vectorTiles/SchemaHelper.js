// All material copyright ESRI, All Rights Reserved, unless otherwise specified.
// See http://js.arcgis.com/3.20/esri/copyright.txt for details.
//>>built
define("esri/layers/vectorTiles/views/vectorTiles/SchemaHelper",["require","exports","../../core/Error"],function(q,r,e){return function(){function b(a){this.lockedSchemaPixelSize=a}b.prototype.getCompatibleLevelRowCol=function(a){var c=a[0],d=a[1];a=a[2];if(256===this.lockedSchemaPixelSize&&0<c)c--,d>>=1,a>>=1;else if(0!==c&&512!==this.lockedSchemaPixelSize)throw new e("Cannot get a compatible tile key for the locked tiling scheme!");return[c,d,a]};b.prototype.getSchemaShift=function(a,c){var d=
0,b=0;256===this.lockedSchemaPixelSize&&(a[2]%2&&(d=2*c),a[1]%2&&(b=2*c));return[d,b]};b.prototype.adjustLevel=function(a){return 256===this.lockedSchemaPixelSize?0<a?a-1:0:a};b.create256x256CompatibleTileInfo=function(a){if(!a)return null;if(256===a.rows&&256===a.cols)return a;for(var c=a.format,b=a.compressionQuality,e=a.dpi,m=a.origin,n=a.spatialReference,h=[],k,l,p=a.lods.length,f=0;f<p;f++){var g=a.lods[f];k=g.scale;l=2*g.resolution;h.push({level:g.level,scale:k,resolution:l})}return{rows:256,
cols:256,dpi:e,format:c,compressionQuality:b,origin:m,spatialReference:n,lods:h}};return b}()});