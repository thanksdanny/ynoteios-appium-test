/* zepto.js  + underscore.js */
!function(){function a(b,c,d){if(b===c)return 0!==b||1/b==1/c;if(null==b||null==c)return b===c;if(b._chain&&(b=b._wrapped),c._chain&&(c=c._wrapped),x.isFunction(b.isEqual))return b.isEqual(c);if(x.isFunction(c.isEqual))return c.isEqual(b);var e=typeof b;if(e!=typeof c)return!1;if(!b!=!c)return!1;if(x.isNaN(b))return x.isNaN(c);var f=x.isString(b),g=x.isString(c);if(f||g)return f&&g&&String(b)==String(c);var h=x.isNumber(b),i=x.isNumber(c);if(h||i)return h&&i&&+b==+c;var j=x.isBoolean(b),l=x.isBoolean(c);if(j||l)return j&&l&&+b==+c;var m=x.isDate(b),n=x.isDate(c);if(m||n)return m&&n&&b.getTime()==c.getTime();var o=x.isRegExp(b),p=x.isRegExp(c);if(o||p)return o&&p&&b.source==c.source&&b.global==c.global&&b.multiline==c.multiline&&b.ignoreCase==c.ignoreCase;if("object"!=e)return!1;if(b.length!==c.length)return!1;if(b.constructor!==c.constructor)return!1;for(var q=d.length;q--;)if(d[q]==b)return!0;d.push(b);var r=0,s=!0;for(var t in b)if(k.call(b,t)&&(r++,!(s=k.call(c,t)&&a(b[t],c[t],d))))break;if(s){for(t in c)if(k.call(c,t)&&!r--)break;s=!r}return d.pop(),s}var b=this,c=b._,d={},e=Array.prototype,f=Object.prototype,g=Function.prototype,h=e.slice,i=e.unshift,j=f.toString,k=f.hasOwnProperty,l=e.forEach,m=e.map,n=e.reduce,o=e.reduceRight,p=e.filter,q=e.every,r=e.some,s=e.indexOf,t=e.lastIndexOf,u=Array.isArray,v=Object.keys,w=g.bind,x=function(a){return new C(a)};"undefined"!=typeof exports?("undefined"!=typeof module&&module.exports&&(exports=module.exports=x),exports._=x):"function"==typeof define&&define.amd?define("underscore",function(){return x}):b._=x,x.VERSION="1.2.1";var y=x.each=x.forEach=function(a,b,c){if(null!=a)if(l&&a.forEach===l)a.forEach(b,c);else if(a.length===+a.length){for(var e=0,f=a.length;f>e;e++)if(e in a&&b.call(c,a[e],e,a)===d)return}else for(var g in a)if(k.call(a,g)&&b.call(c,a[g],g,a)===d)return};x.map=function(a,b,c){var d=[];return null==a?d:m&&a.map===m?a.map(b,c):(y(a,function(a,e,f){d[d.length]=b.call(c,a,e,f)}),d)},x.reduce=x.foldl=x.inject=function(a,b,c,d){var e=void 0!==c;if(null==a&&(a=[]),n&&a.reduce===n)return d&&(b=x.bind(b,d)),e?a.reduce(b,c):a.reduce(b);if(y(a,function(a,f,g){e?c=b.call(d,c,a,f,g):(c=a,e=!0)}),!e)throw new TypeError("Reduce of empty array with no initial value");return c},x.reduceRight=x.foldr=function(a,b,c,d){if(null==a&&(a=[]),o&&a.reduceRight===o)return d&&(b=x.bind(b,d)),void 0!==c?a.reduceRight(b,c):a.reduceRight(b);var e=(x.isArray(a)?a.slice():x.toArray(a)).reverse();return x.reduce(e,b,c,d)},x.find=x.detect=function(a,b,c){var d;return z(a,function(a,e,f){return b.call(c,a,e,f)?(d=a,!0):void 0}),d},x.filter=x.select=function(a,b,c){var d=[];return null==a?d:p&&a.filter===p?a.filter(b,c):(y(a,function(a,e,f){b.call(c,a,e,f)&&(d[d.length]=a)}),d)},x.reject=function(a,b,c){var d=[];return null==a?d:(y(a,function(a,e,f){b.call(c,a,e,f)||(d[d.length]=a)}),d)},x.every=x.all=function(a,b,c){var e=!0;return null==a?e:q&&a.every===q?a.every(b,c):(y(a,function(a,f,g){return(e=e&&b.call(c,a,f,g))?void 0:d}),e)};var z=x.some=x.any=function(a,b,c){b=b||x.identity;var e=!1;return null==a?e:r&&a.some===r?a.some(b,c):(y(a,function(a,f,g){return(e|=b.call(c,a,f,g))?d:void 0}),!!e)};x.include=x.contains=function(a,b){var c=!1;return null==a?c:s&&a.indexOf===s?-1!=a.indexOf(b):c=z(a,function(a){return a===b?!0:void 0})},x.invoke=function(a,b){var c=h.call(arguments,2);return x.map(a,function(a){return(b.call?b||a:a[b]).apply(a,c)})},x.pluck=function(a,b){return x.map(a,function(a){return a[b]})},x.max=function(a,b,c){if(!b&&x.isArray(a))return Math.max.apply(Math,a);if(!b&&x.isEmpty(a))return-(1/0);var d={computed:-(1/0)};return y(a,function(a,e,f){var g=b?b.call(c,a,e,f):a;g>=d.computed&&(d={value:a,computed:g})}),d.value},x.min=function(a,b,c){if(!b&&x.isArray(a))return Math.min.apply(Math,a);if(!b&&x.isEmpty(a))return 1/0;var d={computed:1/0};return y(a,function(a,e,f){var g=b?b.call(c,a,e,f):a;g<d.computed&&(d={value:a,computed:g})}),d.value},x.shuffle=function(a){var b,c=[];return y(a,function(a,d,e){0==d?c[0]=a:(b=Math.floor(Math.random()*(d+1)),c[d]=c[b],c[b]=a)}),c},x.sortBy=function(a,b,c){return x.pluck(x.map(a,function(a,d,e){return{value:a,criteria:b.call(c,a,d,e)}}).sort(function(a,b){var c=a.criteria,d=b.criteria;return d>c?-1:c>d?1:0}),"value")},x.groupBy=function(a,b){var c={},d=x.isFunction(b)?b:function(a){return a[b]};return y(a,function(a,b){var e=d(a,b);(c[e]||(c[e]=[])).push(a)}),c},x.sortedIndex=function(a,b,c){c||(c=x.identity);for(var d=0,e=a.length;e>d;){var f=d+e>>1;c(a[f])<c(b)?d=f+1:e=f}return d},x.toArray=function(a){return a?a.toArray?a.toArray():x.isArray(a)?h.call(a):x.isArguments(a)?h.call(a):x.values(a):[]},x.size=function(a){return x.toArray(a).length},x.first=x.head=function(a,b,c){return null==b||c?a[0]:h.call(a,0,b)},x.initial=function(a,b,c){return h.call(a,0,a.length-(null==b||c?1:b))},x.last=function(a,b,c){return null==b||c?a[a.length-1]:h.call(a,a.length-b)},x.rest=x.tail=function(a,b,c){return h.call(a,null==b||c?1:b)},x.compact=function(a){return x.filter(a,function(a){return!!a})},x.flatten=function(a,b){return x.reduce(a,function(a,c){return x.isArray(c)?a.concat(b?c:x.flatten(c)):(a[a.length]=c,a)},[])},x.without=function(a){return x.difference(a,h.call(arguments,1))},x.uniq=x.unique=function(a,b,c){var d=c?x.map(a,c):a,e=[];return x.reduce(d,function(c,d,f){return 0!=f&&(b===!0?x.last(c)==d:x.include(c,d))||(c[c.length]=d,e[e.length]=a[f]),c},[]),e},x.union=function(){return x.uniq(x.flatten(arguments,!0))},x.intersection=x.intersect=function(a){var b=h.call(arguments,1);return x.filter(x.uniq(a),function(a){return x.every(b,function(b){return x.indexOf(b,a)>=0})})},x.difference=function(a,b){return x.filter(a,function(a){return!x.include(b,a)})},x.zip=function(){for(var a=h.call(arguments),b=x.max(x.pluck(a,"length")),c=new Array(b),d=0;b>d;d++)c[d]=x.pluck(a,""+d);return c},x.indexOf=function(a,b,c){if(null==a)return-1;var d,e;if(c)return d=x.sortedIndex(a,b),a[d]===b?d:-1;if(s&&a.indexOf===s)return a.indexOf(b);for(d=0,e=a.length;e>d;d++)if(a[d]===b)return d;return-1},x.lastIndexOf=function(a,b){if(null==a)return-1;if(t&&a.lastIndexOf===t)return a.lastIndexOf(b);for(var c=a.length;c--;)if(a[c]===b)return c;return-1},x.range=function(a,b,c){arguments.length<=1&&(b=a||0,a=0),c=arguments[2]||1;for(var d=Math.max(Math.ceil((b-a)/c),0),e=0,f=new Array(d);d>e;)f[e++]=a,a+=c;return f};var A=function(){};x.bind=function(a,b){var c,d;if(a.bind===w&&w)return w.apply(a,h.call(arguments,1));if(!x.isFunction(a))throw new TypeError;return d=h.call(arguments,2),c=function(){if(!(this instanceof c))return a.apply(b,d.concat(h.call(arguments)));A.prototype=a.prototype;var e=new A,f=a.apply(e,d.concat(h.call(arguments)));return Object(f)===f?f:e}},x.bindAll=function(a){var b=h.call(arguments,1);return 0==b.length&&(b=x.functions(a)),y(b,function(b){a[b]=x.bind(a[b],a)}),a},x.memoize=function(a,b){var c={};return b||(b=x.identity),function(){var d=b.apply(this,arguments);return k.call(c,d)?c[d]:c[d]=a.apply(this,arguments)}},x.delay=function(a,b){var c=h.call(arguments,2);return setTimeout(function(){return a.apply(a,c)},b)},x.defer=function(a){return x.delay.apply(x,[a,1].concat(h.call(arguments,1)))},x.throttle=function(a,b){var c,d,e,f,g;return g=x.debounce(function(){f=!1},b),function(){d=this,e=arguments;var h=function(){c=null,a.apply(d,e),g()};c||(c=setTimeout(h,b)),f||a.apply(d,e),g&&g(),f=!0}},x.debounce=function(a,b){var c;return function(){var d=this,e=arguments,f=function(){c=null,a.apply(d,e)};clearTimeout(c),c=setTimeout(f,b)}},x.once=function(a){var b,c=!1;return function(){return c?b:(c=!0,b=a.apply(this,arguments))}},x.wrap=function(a,b){return function(){var c=[a].concat(h.call(arguments));return b.apply(this,c)}},x.compose=function(){var a=h.call(arguments);return function(){for(var b=h.call(arguments),c=a.length-1;c>=0;c--)b=[a[c].apply(this,b)];return b[0]}},x.after=function(a,b){return function(){return--a<1?b.apply(this,arguments):void 0}},x.keys=v||function(a){if(a!==Object(a))throw new TypeError("Invalid object");var b=[];for(var c in a)k.call(a,c)&&(b[b.length]=c);return b},x.values=function(a){return x.map(a,x.identity)},x.functions=x.methods=function(a){var b=[];for(var c in a)x.isFunction(a[c])&&b.push(c);return b.sort()},x.extend=function(a){return y(h.call(arguments,1),function(b){for(var c in b)void 0!==b[c]&&(a[c]=b[c])}),a},x.defaults=function(a){return y(h.call(arguments,1),function(b){for(var c in b)null==a[c]&&(a[c]=b[c])}),a},x.clone=function(a){return x.isObject(a)?x.isArray(a)?a.slice():x.extend({},a):a},x.tap=function(a,b){return b(a),a},x.isEqual=function(b,c){return a(b,c,[])},x.isEmpty=function(a){if(x.isArray(a)||x.isString(a))return 0===a.length;for(var b in a)if(k.call(a,b))return!1;return!0},x.isElement=function(a){return!(!a||1!=a.nodeType)},x.isArray=u||function(a){return"[object Array]"==j.call(a)},x.isObject=function(a){return a===Object(a)},"[object Arguments]"==j.call(arguments)?x.isArguments=function(a){return"[object Arguments]"==j.call(a)}:x.isArguments=function(a){return!(!a||!k.call(a,"callee"))},x.isFunction=function(a){return"[object Function]"==j.call(a)},x.isString=function(a){return"[object String]"==j.call(a)},x.isNumber=function(a){return"[object Number]"==j.call(a)},x.isNaN=function(a){return a!==a},x.isBoolean=function(a){return a===!0||a===!1||"[object Boolean]"==j.call(a)},x.isDate=function(a){return"[object Date]"==j.call(a)},x.isRegExp=function(a){return"[object RegExp]"==j.call(a)},x.isNull=function(a){return null===a},x.isUndefined=function(a){return void 0===a},x.noConflict=function(){return b._=c,this},x.identity=function(a){return a},x.times=function(a,b,c){for(var d=0;a>d;d++)b.call(c,d)},x.escape=function(a){return(""+a).replace(/&(?!\w+;|#\d+;|#x[\da-f]+;)/gi,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;").replace(/\//g,"&#x2F;")},x.mixin=function(a){y(x.functions(a),function(b){E(b,x[b]=a[b])})};var B=0;x.uniqueId=function(a){var b=B++;return a?a+b:b},x.templateSettings={evaluate:/<%([\s\S]+?)%>/g,interpolate:/<%=([\s\S]+?)%>/g,escape:/<%-([\s\S]+?)%>/g},x.template=function(a,b){var c=x.templateSettings,d="var __p=[],print=function(){__p.push.apply(__p,arguments);};with(obj||{}){__p.push('"+a.replace(/\\/g,"\\\\").replace(/'/g,"\\'").replace(c.escape,function(a,b){return"',_.escape("+b.replace(/\\'/g,"'")+"),'"}).replace(c.interpolate,function(a,b){return"',"+b.replace(/\\'/g,"'")+",'"}).replace(c.evaluate||null,function(a,b){return"');"+b.replace(/\\'/g,"'").replace(/[\r\n\t]/g," ")+"__p.push('"}).replace(/\r/g,"\\r").replace(/\n/g,"\\n").replace(/\t/g,"\\t")+"');}return __p.join('');",e=new Function("obj",d);return b?e(b):e};var C=function(a){this._wrapped=a};x.prototype=C.prototype;var D=function(a,b){return b?x(a).chain():a},E=function(a,b){C.prototype[a]=function(){var a=h.call(arguments);return i.call(a,this._wrapped),D(b.apply(x,a),this._chain)}};x.mixin(x),y(["pop","push","reverse","shift","sort","splice","unshift"],function(a){var b=e[a];C.prototype[a]=function(){return b.apply(this._wrapped,arguments),D(this._wrapped,this._chain)}}),y(["concat","join","slice"],function(a){var b=e[a];C.prototype[a]=function(){return D(b.apply(this._wrapped,arguments),this._chain)}}),C.prototype.chain=function(){return this._chain=!0,this},C.prototype.value=function(){return this._wrapped}}(),function(a){String.prototype.trim===a&&(String.prototype.trim=function(){return this.replace(/^\s+/,"").replace(/\s+$/,"")}),Array.prototype.reduce===a&&(Array.prototype.reduce=function(b){if(void 0===this||null===this)throw new TypeError;var c,d=Object(this),e=d.length>>>0,f=0;if("function"!=typeof b)throw new TypeError;if(0==e&&1==arguments.length)throw new TypeError;if(arguments.length>=2)c=arguments[1];else for(;;){if(f in d){c=d[f++];break}if(++f>=e)throw new TypeError}for(;e>f;)f in d&&(c=b.call(a,c,d[f],f,d)),f++;return c})}();var Zepto=function(){function a(a){return"[object Function]"==M.call(a)}function b(a){return a instanceof Object}function c(b){var c,d;if("[object Object]"!==M.call(b))return!1;if(d=a(b.constructor)&&b.constructor.prototype,!d||!hasOwnProperty.call(d,"isPrototypeOf"))return!1;for(c in b);return c===p||hasOwnProperty.call(b,c)}function d(a){return a instanceof Array}function e(a){return"number"==typeof a.length}function f(a){return a.filter(function(a){return a!==p&&null!==a})}function g(a){return a.length>0?[].concat.apply([],a):a}function h(a){return a.replace(/::/g,"/").replace(/([A-Z]+)([A-Z][a-z])/g,"$1_$2").replace(/([a-z\d])([A-Z])/g,"$1_$2").replace(/_/g,"-").toLowerCase()}function i(a){return a in z?z[a]:z[a]=new RegExp("(^|\\s)"+a+"(\\s|$)")}function j(a,b){return"number"!=typeof b||B[h(a)]?b:b+"px"}function k(a){var b,c;return y[a]||(b=x.createElement(a),x.body.appendChild(b),c=A(b,"").getPropertyValue("display"),b.parentNode.removeChild(b),"none"==c&&(c="block"),y[a]=c),y[a]}function l(a,b){return b===p?r(a):r(a).filter(b)}function m(b,c,d,e){return a(c)?c.call(b,d,e):c}function n(a,b,c){var d=a%2?b:b.parentNode;d?d.insertBefore(c,a?1==a?d.firstChild:2==a?b:null:b.nextSibling):r(c).remove()}function o(a,b){b(a);for(var c in a.childNodes)o(a.childNodes[c],b)}var p,q,r,s,t,u,v=[],w=v.slice,x=window.document,y={},z={},A=x.defaultView.getComputedStyle,B={"column-count":1,columns:1,"font-weight":1,"line-height":1,opacity:1,"z-index":1,zoom:1},C=/^\s*<(\w+|!)[^>]*>/,D=[1,3,8,9,11],E=["after","prepend","before","append"],F=x.createElement("table"),G=x.createElement("tr"),H={tr:x.createElement("tbody"),tbody:F,thead:F,tfoot:F,td:G,th:G,"*":x.createElement("div")},I=/complete|loaded|interactive/,J=/^\.([\w-]+)$/,K=/^#([\w-]+)$/,L=/^[\w-]+$/,M={}.toString,N={},O=x.createElement("div");return N.matches=function(a,b){if(!a||1!==a.nodeType)return!1;var c=a.webkitMatchesSelector||a.mozMatchesSelector||a.oMatchesSelector||a.matchesSelector;if(c)return c.call(a,b);var d,e=a.parentNode,f=!e;return f&&(e=O).appendChild(a),d=~N.qsa(e,b).indexOf(a),f&&O.removeChild(a),d},t=function(a){return a.replace(/-+(.)?/g,function(a,b){return b?b.toUpperCase():""})},u=function(a){return a.filter(function(b,c){return a.indexOf(b)==c})},N.fragment=function(a,b){b===p&&(b=C.test(a)&&RegExp.$1),b in H||(b="*");var c=H[b];return c.innerHTML=""+a,r.each(w.call(c.childNodes),function(){c.removeChild(this)})},N.Z=function(a,b){return a=a||[],a.__proto__=arguments.callee.prototype,a.selector=b||"",a},N.isZ=function(a){return a instanceof N.Z},N.init=function(b,e){if(b){if(a(b))return r(x).ready(b);if(N.isZ(b))return b;var g;if(d(b))g=f(b);else if(c(b))g=[r.extend({},b)],b=null;else if(D.indexOf(b.nodeType)>=0||b===window)g=[b],b=null;else if(C.test(b))g=N.fragment(b.trim(),RegExp.$1),b=null;else{if(e!==p)return r(e).find(b);g=N.qsa(x,b)}return N.Z(g,b)}return N.Z()},r=function(a,b){return N.init(a,b)},r.extend=function(a){return w.call(arguments,1).forEach(function(b){for(q in b)b[q]!==p&&(a[q]=b[q])}),a},N.qsa=function(a,b){var c;return a===x&&K.test(b)?(c=a.getElementById(RegExp.$1))?[c]:v:1!==a.nodeType&&9!==a.nodeType?v:w.call(J.test(b)?a.getElementsByClassName(RegExp.$1):L.test(b)?a.getElementsByTagName(b):a.querySelectorAll(b))},r.isFunction=a,r.isObject=b,r.isArray=d,r.isPlainObject=c,r.inArray=function(a,b,c){return v.indexOf.call(b,a,c)},r.trim=function(a){return a.trim()},r.uuid=0,r.map=function(a,b){var c,d,f,h=[];if(e(a))for(d=0;d<a.length;d++)c=b(a[d],d),null!=c&&h.push(c);else for(f in a)c=b(a[f],f),null!=c&&h.push(c);return g(h)},r.each=function(a,b){var c,d;if(e(a)){for(c=0;c<a.length;c++)if(b.call(a[c],c,a[c])===!1)return a}else for(d in a)if(b.call(a[d],d,a[d])===!1)return a;return a},r.fn={forEach:v.forEach,reduce:v.reduce,push:v.push,indexOf:v.indexOf,concat:v.concat,map:function(a){return r.map(this,function(b,c){return a.call(b,c,b)})},slice:function(){return r(w.apply(this,arguments))},ready:function(a){return I.test(x.readyState)?a(r):x.addEventListener("DOMContentLoaded",function(){a(r)},!1),this},get:function(a){return a===p?w.call(this):this[a]},toArray:function(){return this.get()},size:function(){return this.length},remove:function(){return this.each(function(){null!=this.parentNode&&this.parentNode.removeChild(this)})},each:function(a){return this.forEach(function(b,c){a.call(b,c,b)}),this},filter:function(a){return r([].filter.call(this,function(b){return N.matches(b,a)}))},add:function(a,b){return r(u(this.concat(r(a,b))))},is:function(a){return this.length>0&&N.matches(this[0],a)},not:function(b){var c=[];if(a(b)&&b.call!==p)this.each(function(a){b.call(this,a)||c.push(this)});else{var d="string"==typeof b?this.filter(b):e(b)&&a(b.item)?w.call(b):r(b);this.forEach(function(a){d.indexOf(a)<0&&c.push(a)})}return r(c)},eq:function(a){return-1===a?this.slice(a):this.slice(a,+a+1)},first:function(){var a=this[0];return a&&!b(a)?a:r(a)},last:function(){var a=this[this.length-1];return a&&!b(a)?a:r(a)},find:function(a){var b;return b=1==this.length?N.qsa(this[0],a):this.map(function(){return N.qsa(this,a)}),r(b)},closest:function(a,b){for(var c=this[0];c&&!N.matches(c,a);)c=c!==b&&c!==x&&c.parentNode;return r(c)},parents:function(a){for(var b=[],c=this;c.length>0;)c=r.map(c,function(a){return(a=a.parentNode)&&a!==x&&b.indexOf(a)<0?(b.push(a),a):void 0});return l(b,a)},parent:function(a){return l(u(this.pluck("parentNode")),a)},children:function(a){return l(this.map(function(){return w.call(this.children)}),a)},siblings:function(a){return l(this.map(function(a,b){return w.call(b.parentNode.children).filter(function(a){return a!==b})}),a)},empty:function(){return this.each(function(){this.innerHTML=""})},pluck:function(a){return this.map(function(){return this[a]})},show:function(){return this.each(function(){"none"==this.style.display&&(this.style.display=null),"none"==A(this,"").getPropertyValue("display")&&(this.style.display=k(this.nodeName))})},replaceWith:function(a){return this.before(a).remove()},wrap:function(a){return this.each(function(){r(this).wrapAll(r(a)[0].cloneNode(!1))})},wrapAll:function(a){return this[0]&&(r(this[0]).before(a=r(a)),a.append(this)),this},unwrap:function(){return this.parent().each(function(){r(this).replaceWith(r(this).children())}),this},clone:function(){return r(this.map(function(){return this.cloneNode(!0)}))},hide:function(){return this.css("display","none")},toggle:function(a){return(a===p?"none"==this.css("display"):a)?this.show():this.hide()},prev:function(){return r(this.pluck("previousElementSibling"))},next:function(){return r(this.pluck("nextElementSibling"))},html:function(a){return a===p?this.length>0?this[0].innerHTML:null:this.each(function(b){var c=this.innerHTML;r(this).empty().append(m(this,a,b,c))})},text:function(a){return a===p?this.length>0?this[0].textContent:null:this.each(function(){this.textContent=a})},attr:function(a,c){var d;return"string"==typeof a&&c===p?0==this.length||1!==this[0].nodeType?p:"value"==a&&"INPUT"==this[0].nodeName?this.val():!(d=this[0].getAttribute(a))&&a in this[0]?this[0][a]:d:this.each(function(d){if(1===this.nodeType)if(b(a))for(q in a)this.setAttribute(q,a[q]);else this.setAttribute(a,m(this,c,d,this.getAttribute(a)))})},removeAttr:function(a){return this.each(function(){1===this.nodeType&&this.removeAttribute(a)})},prop:function(a,b){return b===p?this[0]?this[0][a]:p:this.each(function(c){this[a]=m(this,b,c,this[a])})},data:function(a,b){var c=this.attr("data-"+h(a),b);return null!==c?c:p},val:function(a){return a===p?this.length>0?this[0].value:p:this.each(function(b){this.value=m(this,a,b,this.value)})},offset:function(){if(0==this.length)return null;var a=this[0].getBoundingClientRect();return{left:a.left+window.pageXOffset,top:a.top+window.pageYOffset,width:a.width,height:a.height}},css:function(a,b){if(b===p&&"string"==typeof a)return 0==this.length?p:this[0].style[t(a)]||A(this[0],"").getPropertyValue(a);var c="";for(q in a)"string"==typeof a[q]&&""==a[q]?this.each(function(){this.style.removeProperty(h(q))}):c+=h(q)+":"+j(q,a[q])+";";return"string"==typeof a&&(""==b?this.each(function(){this.style.removeProperty(h(a))}):c=h(a)+":"+j(a,b)),this.each(function(){this.style.cssText+=";"+c})},index:function(a){return a?this.indexOf(r(a)[0]):this.parent().children().indexOf(this[0])},hasClass:function(a){return this.length<1?!1:i(a).test(this[0].className)},addClass:function(a){return this.each(function(b){s=[];var c=this.className,d=m(this,a,b,c);d.split(/\s+/g).forEach(function(a){r(this).hasClass(a)||s.push(a)},this),s.length&&(this.className+=(c?" ":"")+s.join(" "))})},removeClass:function(a){return this.each(function(b){return a===p?this.className="":(s=this.className,m(this,a,b,s).split(/\s+/g).forEach(function(a){s=s.replace(i(a)," ")}),void(this.className=s.trim()))})},toggleClass:function(a,b){return this.each(function(c){var d=m(this,a,c,this.className);(b===p?!r(this).hasClass(d):b)?r(this).addClass(d):r(this).removeClass(d)})}},["width","height"].forEach(function(a){r.fn[a]=function(b){var c,d=a.replace(/./,function(a){return a[0].toUpperCase()});return b===p?this[0]==window?window["inner"+d]:this[0]==x?x.documentElement["offset"+d]:(c=this.offset())&&c[a]:this.each(function(c){var d=r(this);d.css(a,m(this,b,c,d[a]()))})}}),E.forEach(function(a,c){r.fn[a]=function(){var a=r.map(arguments,function(a){return b(a)?a:N.fragment(a)});if(a.length<1)return this;var d=this.length,e=d>1,f=2>c;return this.each(function(b,g){for(var h=0;h<a.length;h++){var i=a[f?a.length-h-1:h];o(i,function(a){null==a.nodeName||"SCRIPT"!==a.nodeName.toUpperCase()||a.type&&"text/javascript"!==a.type||window.eval.call(window,a.innerHTML)}),e&&d-1>b&&(i=i.cloneNode(!0)),n(c,g,i)}})},r.fn[c%2?a+"To":"insert"+(c?"Before":"After")]=function(b){return r(b)[a](this),this}}),N.Z.prototype=r.fn,N.camelize=t,N.uniq=u,r.zepto=N,r}();window.Zepto=Zepto,"$"in window||(window.$=Zepto),function(a){function b(a){return a._zid||(a._zid=l++)}function c(a,c,f,g){if(c=d(c),c.ns)var h=e(c.ns);return(k[b(a)]||[]).filter(function(a){return a&&(!c.e||a.e==c.e)&&(!c.ns||h.test(a.ns))&&(!f||b(a.fn)===b(f))&&(!g||a.sel==g)})}function d(a){var b=(""+a).split(".");return{e:b[0],ns:b.slice(1).sort().join(" ")}}function e(a){return new RegExp("(?:^| )"+a.replace(" "," .* ?")+"(?: |$)")}function f(b,c,d){a.isObject(b)?a.each(b,d):b.split(/\s/).forEach(function(a){d(a,c)})}function g(c,e,g,h,i,j){j=!!j;var l=b(c),m=k[l]||(k[l]=[]);f(e,g,function(b,e){var f=i&&i(e,b),g=f||e,k=function(a){var b=g.apply(c,[a].concat(a.data));return b===!1&&a.preventDefault(),b},l=a.extend(d(b),{fn:e,proxy:k,sel:h,del:f,i:m.length});m.push(l),c.addEventListener(l.e,k,j)})}function h(a,d,e,g){var h=b(a);f(d||"",e,function(b,d){c(a,b,d,g).forEach(function(b){delete k[h][b.i],a.removeEventListener(b.e,b.proxy,!1)})})}function i(b){var c=a.extend({originalEvent:b},b);return a.each(p,function(a,d){c[a]=function(){return this[d]=n,b[a].apply(b,arguments)},c[d]=o}),c}function j(a){if(!("defaultPrevented"in a)){a.defaultPrevented=!1;var b=a.preventDefault;a.preventDefault=function(){this.defaultPrevented=!0,b.call(this)}}}var k=(a.zepto.qsa,{}),l=1,m={};m.click=m.mousedown=m.mouseup=m.mousemove="MouseEvents",a.event={add:g,remove:h},a.proxy=function(c,d){if(a.isFunction(c)){var e=function(){return c.apply(d,arguments)};return e._zid=b(c),e}if("string"==typeof d)return a.proxy(c[d],c);throw new TypeError("expected function")},a.fn.bind=function(a,b){return this.each(function(){g(this,a,b)})},a.fn.unbind=function(a,b){return this.each(function(){h(this,a,b)})},a.fn.one=function(a,b){return this.each(function(c,d){g(this,a,b,null,function(a,b){return function(){var c=a.apply(d,arguments);return h(d,b,a),c}})})};var n=function(){return!0},o=function(){return!1},p={preventDefault:"isDefaultPrevented",stopImmediatePropagation:"isImmediatePropagationStopped",stopPropagation:"isPropagationStopped"};a.fn.delegate=function(b,c,d){var e=!1;return("blur"==c||"focus"==c)&&(a.iswebkit?c="blur"==c?"focusout":"focus"==c?"focusin":c:e=!0),this.each(function(f,h){g(h,c,d,b,function(c){return function(d){var e,f=a(d.target).closest(b,h).get(0);return f?(e=a.extend(i(d),{currentTarget:f,liveFired:h}),c.apply(f,[e].concat([].slice.call(arguments,1)))):void 0}},e)})},a.fn.undelegate=function(a,b,c){return this.each(function(){h(this,b,c,a)})},a.fn.live=function(b,c){return a(document.body).delegate(this.selector,b,c),this},a.fn.die=function(b,c){return a(document.body).undelegate(this.selector,b,c),this},a.fn.on=function(b,c,d){return void 0==c||a.isFunction(c)?this.bind(b,c):this.delegate(c,b,d)},a.fn.off=function(b,c,d){return void 0==c||a.isFunction(c)?this.unbind(b,c):this.undelegate(c,b,d)},a.fn.trigger=function(b,c){return"string"==typeof b&&(b=a.Event(b)),j(b),b.data=c,this.each(function(){"dispatchEvent"in this&&this.dispatchEvent(b)})},a.fn.triggerHandler=function(b,d){var e,f;return this.each(function(g,h){e=i("string"==typeof b?a.Event(b):b),e.data=d,e.target=h,a.each(c(h,b.type||b),function(a,b){return f=b.proxy(e),e.isImmediatePropagationStopped()?!1:void 0})}),f},"focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout change select keydown keypress keyup error".split(" ").forEach(function(b){a.fn[b]=function(a){return this.bind(b,a)}}),["focus","blur"].forEach(function(b){a.fn[b]=function(a){if(a)this.bind(b,a);else if(this.length)try{this.get(0)[b]()}catch(c){}return this}}),a.Event=function(a,b){var c=document.createEvent(m[a]||"Events"),d=!0;if(b)for(var e in b)"bubbles"==e?d=!!b[e]:c[e]=b[e];return c.initEvent(a,d,!0,null,null,null,null,null,null,null,null,null,null,null,null),c}}(Zepto),function(a){function b(a){var b=this.os={},c=this.browser={},d=a.match(/WebKit\/([\d.]+)/),e=a.match(/(Android)\s+([\d.]+)/),f=a.match(/(iPad).*OS\s([\d_]+)/),g=!f&&a.match(/(iPhone\sOS)\s([\d_]+)/),h=a.match(/(webOS|hpwOS)[\s\/]([\d.]+)/),i=h&&a.match(/TouchPad/),j=a.match(/Kindle\/([\d.]+)/),k=a.match(/Silk\/([\d._]+)/),l=a.match(/(BlackBerry).*Version\/([\d.]+)/);(c.webkit=!!d)&&(c.version=d[1]),e&&(b.android=!0,b.version=e[2]),g&&(b.ios=b.iphone=!0,b.version=g[2].replace(/_/g,".")),f&&(b.ios=b.ipad=!0,b.version=f[2].replace(/_/g,".")),h&&(b.webos=!0,b.version=h[2]),i&&(b.touchpad=!0),l&&(b.blackberry=!0,b.version=l[2]),j&&(b.kindle=!0,b.version=j[1]),k&&(c.silk=!0,c.version=k[1]),!k&&b.android&&a.match(/Kindle Fire/)&&(c.silk=!0)}b.call(a,navigator.userAgent),a.__detect=b}(Zepto),function(a,b){function c(a){return a.toLowerCase()}function d(a){return e?e+a:c(a)}var e,f="",g={Webkit:"webkit",Moz:"",O:"o",ms:"MS"},h=window.document,i=h.createElement("div"),j=/^((translate|rotate|scale)(X|Y|Z|3d)?|matrix(3d)?|perspective|skew(X|Y)?)$/i,k={};a.each(g,function(a,d){return i.style[a+"TransitionProperty"]!==b?(f="-"+c(a)+"-",e=d,!1):void 0}),k[f+"transition-property"]=k[f+"transition-duration"]=k[f+"transition-timing-function"]=k[f+"animation-name"]=k[f+"animation-duration"]="",a.fx={off:e===b&&i.style.transitionProperty===b,cssPrefix:f,transitionEnd:d("TransitionEnd"),animationEnd:d("AnimationEnd")},a.fn.animate=function(b,c,d,e){return a.isObject(c)&&(d=c.easing,e=c.complete,c=c.duration),c&&(c/=1e3),this.anim(b,c,d,e)},a.fn.anim=function(c,d,e,g){var h,i,l,m={},n=this,o=a.fx.transitionEnd;if(d===b&&(d=.4),a.fx.off&&(d=0),"string"==typeof c)m[f+"animation-name"]=c,m[f+"animation-duration"]=d+"s",o=a.fx.animationEnd;else{for(i in c)j.test(i)?(h||(h=[]),h.push(i+"("+c[i]+")")):m[i]=c[i];h&&(m[f+"transform"]=h.join(" ")),a.fx.off||"object"!=typeof c||(m[f+"transition-property"]=Object.keys(c).join(", "),m[f+"transition-duration"]=d+"s",m[f+"transition-timing-function"]=e||"linear")}return l=function(b){if("undefined"!=typeof b){if(b.target!==b.currentTarget)return;a(b.target).unbind(o,arguments.callee)}a(this).css(k),g&&g.call(this)},d>0&&this.bind(o,l),setTimeout(function(){n.css(m),0>=d&&setTimeout(function(){n.each(function(){l.call(this)})},0)},0),this},i=null}(Zepto),function(a){function b(b,c,d){var e=a.Event(c);return a(b).trigger(e,d),!e.defaultPrevented}function c(a,c,d,e){return a.global?b(c||s,d,e):void 0}function d(b){b.global&&0===a.active++&&c(b,null,"ajaxStart")}function e(b){b.global&&!--a.active&&c(b,null,"ajaxStop")}function f(a,b){var d=b.context;return b.beforeSend.call(d,a,b)===!1||c(b,d,"ajaxBeforeSend",[a,b])===!1?!1:void c(b,d,"ajaxSend",[a,b])}function g(a,b,d){var e=d.context,f="success";d.success.call(e,a,f,b),c(d,e,"ajaxSuccess",[b,d,a]),i(f,b,d)}function h(a,b,d,e){var f=e.context;e.error.call(f,d,b,a),c(e,f,"ajaxError",[d,e,a]),i(b,d,e)}function i(a,b,d){var f=d.context;d.complete.call(f,b,a),c(d,f,"ajaxComplete",[b,d]),e(d)}function j(){}function k(a){return a&&(a==x?"html":a==w?"json":u.test(a)?"script":v.test(a)&&"xml")||"text"}function l(a,b){return(a+"&"+b).replace(/[&?]{1,2}/,"?")}function m(b){r(b.data)&&(b.data=a.param(b.data)),!b.data||b.type&&"GET"!=b.type.toUpperCase()||(b.url=l(b.url,b.data))}function n(b,c,d,e){var f=a.isArray(c);a.each(c,function(c,g){e&&(c=d?e:e+"["+(f?"":c)+"]"),!e&&f?b.add(g.name,g.value):(d?a.isArray(g):r(g))?n(b,g,d,c):b.add(c,g)})}var o,p,q=0,r=a.isObject,s=window.document,t=/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,u=/^(?:text|application)\/javascript/i,v=/^(?:text|application)\/xml/i,w="application/json",x="text/html",y=/^\s*$/;a.active=0,a.ajaxJSONP=function(b){var c,d="jsonp"+ ++q,e=s.createElement("script"),f=function(){a(e).remove(),d in window&&(window[d]=j),i("abort",h,b)},h={abort:f};return b.error&&(e.onerror=function(){h.abort(),b.error()}),window[d]=function(f){clearTimeout(c),a(e).remove(),delete window[d],g(f,h,b)},m(b),e.src=b.url.replace(/=\?/,"="+d),a("head").append(e),b.timeout>0&&(c=setTimeout(function(){h.abort(),i("timeout",h,b)},b.timeout)),h},a.ajaxSettings={type:"GET",beforeSend:j,success:j,error:j,complete:j,context:null,global:!0,xhr:function(){return new window.XMLHttpRequest},accepts:{script:"text/javascript, application/javascript",json:w,xml:"application/xml, text/xml",html:x,text:"text/plain"},crossDomain:!1,timeout:0},a.ajax=function(b){var c=a.extend({},b||{});for(o in a.ajaxSettings)void 0===c[o]&&(c[o]=a.ajaxSettings[o]);d(c),c.crossDomain||(c.crossDomain=/^([\w-]+:)?\/\/([^\/]+)/.test(c.url)&&RegExp.$2!=window.location.host);var e=c.dataType,i=/=\?/.test(c.url);if("jsonp"==e||i)return i||(c.url=l(c.url,"callback=?")),a.ajaxJSONP(c);c.url||(c.url=window.location.toString()),m(c);var n,q=c.accepts[e],r={},s=/^([\w-]+:)\/\//.test(c.url)?RegExp.$1:window.location.protocol,t=a.ajaxSettings.xhr();c.crossDomain||(r["X-Requested-With"]="XMLHttpRequest"),q&&(r.Accept=q,q.indexOf(",")>-1&&(q=q.split(",",2)[0]),t.overrideMimeType&&t.overrideMimeType(q)),(c.contentType||c.data&&"GET"!=c.type.toUpperCase())&&(r["Content-Type"]=c.contentType||"application/x-www-form-urlencoded"),c.headers=a.extend(r,c.headers||{}),t.onreadystatechange=function(){if(4==t.readyState){clearTimeout(n);var a,b=!1;if(t.status>=200&&t.status<300||304==t.status||0==t.status&&"file:"==s){e=e||k(t.getResponseHeader("content-type")),a=t.responseText;try{"script"==e?(1,eval)(a):"xml"==e?a=t.responseXML:"json"==e&&(a=y.test(a)?null:JSON.parse(a))}catch(d){b=d}b?h(b,"parsererror",t,c):g(a,t,c)}else h(null,"error",t,c)}};var u="async"in c?c.async:!0;t.open(c.type,c.url,u);for(p in c.headers)t.setRequestHeader(p,c.headers[p]);return f(t,c)===!1?(t.abort(),!1):(c.timeout>0&&(n=setTimeout(function(){t.onreadystatechange=j,t.abort(),h(null,"timeout",t,c)},c.timeout)),t.send(c.data?c.data:null),t)},a.get=function(b,c){return a.ajax({url:b,success:c})},a.post=function(b,c,d,e){return a.isFunction(c)&&(e=e||d,d=c,c=null),a.ajax({type:"POST",url:b,data:c,success:d,dataType:e})},a.getJSON=function(b,c){return a.ajax({url:b,success:c,dataType:"json"})},a.fn.load=function(b,c){if(!this.length)return this;var d,e=this,f=b.split(/\s/);return f.length>1&&(b=f[0],d=f[1]),a.get(b,function(b){e.html(d?a(s.createElement("div")).html(b.replace(t,"")).find(d).html():b),c&&c.call(e)}),
this};var z=encodeURIComponent;a.param=function(a,b){var c=[];return c.add=function(a,b){this.push(z(a)+"="+z(b))},n(c,a,b),c.join("&").replace("%20","+")}}(Zepto),function(a){a.fn.serializeArray=function(){var b,c=[];return a(Array.prototype.slice.call(this.get(0).elements)).each(function(){b=a(this);var d=b.attr("type");"fieldset"!=this.nodeName.toLowerCase()&&!this.disabled&&"submit"!=d&&"reset"!=d&&"button"!=d&&("radio"!=d&&"checkbox"!=d||this.checked)&&c.push({name:b.attr("name"),value:b.val()})}),c},a.fn.serialize=function(){var a=[];return this.serializeArray().forEach(function(b){a.push(encodeURIComponent(b.name)+"="+encodeURIComponent(b.value))}),a.join("&")},a.fn.submit=function(b){if(b)this.bind("submit",b);else if(this.length){var c=a.Event("submit");this.eq(0).trigger(c),c.defaultPrevented||this.get(0).submit()}return this}}(Zepto),function(a){function b(a){return"tagName"in a?a:a.parentNode}function c(a,b,c,d){var e=Math.abs(a-b),f=Math.abs(c-d);return e>=f?a-b>0?"Left":"Right":c-d>0?"Up":"Down"}function d(){g=null,h.last&&(h.el.trigger("longTap"),h={})}function e(){g&&clearTimeout(g),g=null}var f,g,h={},i=750;a(document).ready(function(){var j,k;a(document.body).bind("touchstart",function(c){j=Date.now(),k=j-(h.last||j),h.el=a(b(c.touches[0].target)),f&&clearTimeout(f),h.x1=c.touches[0].pageX,h.y1=c.touches[0].pageY,k>0&&250>=k&&(h.isDoubleTap=!0),h.last=j,g=setTimeout(d,i)}).bind("touchmove",function(a){e(),h.x2=a.touches[0].pageX,h.y2=a.touches[0].pageY}).bind("touchend",function(a){e(),h.isDoubleTap?(h.el.trigger("doubleTap"),h={}):h.x2&&Math.abs(h.x1-h.x2)>30||h.y2&&Math.abs(h.y1-h.y2)>30?(h.el.trigger("swipe")&&h.el.trigger("swipe"+c(h.x1,h.x2,h.y1,h.y2)),h={}):"last"in h&&(h.el.trigger("tap"),f=setTimeout(function(){f=null,h.el.trigger("singleTap"),h={}},250))}).bind("touchcancel",function(){f&&clearTimeout(f),g&&clearTimeout(g),g=f=null,h={}})}),["swipe","swipeLeft","swipeRight","swipeUp","swipeDown","doubleTap","tap","singleTap","longTap"].forEach(function(b){a.fn[b]=function(a){return this.bind(b,a)}})}(Zepto);