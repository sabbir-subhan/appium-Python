//>>built
define("dgrid1/util/misc",["dojo/has"],function(l){l.add("dom-contains",function(f,a,c){return!!c.contains});var d=[],a,k,h,m=/([^A-Za-z0-9_\u00A0-\uFFFF-])/g,g={defaultDelay:15,throttle:function(f,a,c){var b=!1;c=c||g.defaultDelay;return function(){b||(b=!0,f.apply(a,arguments),setTimeout(function(){b=!1},c))}},throttleDelayed:function(f,a,c){var b=!1;c=c||g.defaultDelay;return function(){if(!b){b=!0;var e=arguments;setTimeout(function(){b=!1;f.apply(a,e)},c)}}},debounce:function(f,a,c){var b;c=
c||g.defaultDelay;return function(){b&&(clearTimeout(b),b=null);var e=arguments;b=setTimeout(function(){f.apply(a,e)},c)}},each:function(a,d,c){var b,e;if(a)if("number"===typeof a.length)for(b=0,e=a.length;b<e;b++)d.call(c,a[b],b,a);else for(b in a)d.call(c,a[b],b,a)},addCssRule:function(f,g){a||(a=document.createElement("style"),document.getElementsByTagName("head")[0].appendChild(a),a=a.sheet||a.styleSheet,k=a.deleteRule?"deleteRule":"removeRule",h=a.cssRules?"cssRules":"rules");var c=d.length;
d[c]=(a.cssRules||a.rules).length;a.addRule?a.addRule(f,g):a.insertRule(f+"{"+g+"}",d[c]);return{get:function(b){return a[h][d[c]].style[b]},set:function(b,e){"undefined"!==typeof d[c]&&(a[h][d[c]].style[b]=e)},remove:function(){var b=d[c],e,f;if(void 0!==b)for(a[k](b),d[c]=void 0,e=c+1,f=d.length;e<f;e++)d[e]>b&&d[e]--}}},escapeCssIdentifier:function(a,d){return"string"===typeof a?a.replace(m,d||"\\$1"):a}};return g});