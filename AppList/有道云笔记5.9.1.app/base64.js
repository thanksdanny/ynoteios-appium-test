 /**
  * @class Base64 编码解码类，修复了 unicode 编码的问题
  * @name Base64
  */
 var BASE64 = {

     /**
      * @param {String} string
      * @returns {String}
      */
     encode: function(string) {
         return window.btoa(window.unescape(encodeURIComponent(string)));
     },
     /**
      * @param {String} string
      * @returns {String}
      */
     decode: function(string) {
         return decodeURIComponent(window.escape(window.atob(string)));
     }

 }
