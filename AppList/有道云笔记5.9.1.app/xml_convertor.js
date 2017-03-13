(function(){
    window.xml2html = function(data) {
        var xmls = jsonParse(decode(data)),
            result = [];

        for(var i=0, len = xmls.length; i<len; i++) {
            result.push(convertXml2Html(xmls[i]));
        }

        return jsonStringify({
            result: result
        });
    };

    function convertXml2Html(xml) {
        var html = '';
        try {
            html = BulbEditor.xml2html(xml);
        } catch(e) {
            console.error('xml转换失败');
        } finally {
            return html;
        }
    }

    function jsonParse(str) {
        var json = null;
        try {
            json = JSON.parse(str);
        } catch(e) {
            console.error('JSON parse失败');
        } finally {
            return json;
        }
    }

    function jsonStringify(json) {
        var str = '';
        try {
            str = JSON.stringify(json);
        } catch(e) {
            console.error('JSON stringify失败');
        } finally {
            return str;
        }
    }

    function encode(str) {
        try {
            return window.btoa(window.unescape(encodeURIComponent(str)));
        } catch(e) {
            console.error('encode error');
        }
    }

    function decode(str) {
        try {
            return decodeURIComponent(window.escape(window.atob(str)));
        } catch(e) {
            console.error('decode error');
        }
    }

    //Ready
    (function(){
        execIframe = document.createElement('iframe');
        execIframe.style.display = 'none';
        execIframe.src = 'async:Ready';
        document.documentElement.appendChild(execIframe);
        execIframe.parentNode.removeChild(execIframe);
        execIframe = null;
    })();
})();