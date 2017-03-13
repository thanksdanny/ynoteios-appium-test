/**
 * JS 实现接口
 * Native调用；JS实现
 */
var jsInterface = {
    /**
     * 设置解析内容
     * @param {[type]} bodyStr [解析内容]
     * @param {[type]} type    [解析类型 'article', 'word']
     */
    setBody: function (bodyStr, type) {
        console.log('setBody', arguments);
        //解析器执行解析
        var result = parser(bodyStr, type);
        //解析完成，发送解析结果
        console.log('parser result' + result);
        window.NativeApis.asyncSendBody(result, type);
        return result;
    }
};

/**
 * Native 实现的接口，
 * JS调用；Native实现
 */
var nativeInterface = {
    /**
     * 初始化完成
     */
    Ready: function () {
        console.log('ready', arguments);
        //document ready
        //call native to setBody
    },
    /**
     * 发送解析结果
     * @param {[type]} bodyStr [解析结果]
     * @param {[type]} type    [解析类型]
     */
    SendBody: function (bodyStr, type) {
        console.log('sendBody', arguments);
        //send innerHTML to native
    }
};

//JS端提供
window.Js = {};

/** 发布JS端实现接口 */
/**
 * [publicJsInterface description]
 * @param  {[type]} jsInterface [JsInterface 实现接口]
 * @return {[type]}             [description]
 */
function publicJsInterface(jsInterface) {
    var name;
    for (name in jsInterface) {
        window.Js[name] = (function(name, fn) {
            return function(jsonArgs) {
                console.log('native is calling jsInterface: ' + name);

                var args,
                    hasArgs = arguments.length > 0;
                //参数解码
                if (hasArgs) {
                    try {
                        //base64 解码参数
                        args = BASE64.decode(jsonArgs);
                    } catch (ex0) {
                        console.log(name + '-Js接口调用参数解析失败-base64');
                        return;
                    }
                    try {
                        //string args -> json array
                        args = window.JSON.parse(args);
                    } catch (ex1) {
                        console.log(name + '-Js接口调用参数解析失败-json parse');
                        return;
                    }                    
                }

                //方法调用
                try {
                    return fn.apply(null, args);
                } catch (ex2) {
                    console.log(name + '-Js接口调用失败');
                    return;
                }
                
            };
        })(name, jsInterface[name]);
    }
}

//Native端提供
/**
 * [publicNativeInterface 统一Native调用接口]
 * @param  {[type]} nativeInterface [Native接口]
 * @return {[type]}                 [description]
 */
function publicNativeInterface(nativeInterface){
    var name,
        nativeApis = window.NativeApis = {};
    for (name in nativeInterface) {
        nativeApis['async' + name] = (function(name, fn) {
            return function () {
                console.log('js is calling nativeInterface:' + name);

                var hasArgs = arguments.length > 0,
                    args = Array.prototype.slice.call(arguments, 0),
                    jsonArgs;
                //参数编码
                if (hasArgs) {
                    //json array -> string args
                    try {
                        jsonArgs = window.JSON.stringify(args);
                    } catch (ex0) {
                        console.log(name + '-Native接口调用参数编码失败-json-stringify');
                        return;
                    }
                    //base64 编码参数
                    try {
                        jsonArgs = BASE64.encode(jsonArgs);
                    } catch (ex1) {
                        console.log(name + '-Native接口调用参数编码失败-base64');
                        return;
                    }
                }
                try {
                    if (hasArgs) {
                        if (window.DEBUG === true) {
                            //DEBUG args参数
                            fn.apply(null, args);
                        } else {
                            //Native jsonArgs-base64参数
                            // window.Native[name](jsonArgs);
                            callNativeInterface(name, jsonArgs);
                        }                        
                    } else {
                        if (window.DEBUG === true) {
                            fn();
                        } else {
                            // window.Native[name]();
                            callNativeInterface(name, '');    
                        }                        
                    }
                } catch (ex2) {
                    console.log(name + '-Native接口调用失败');
                    return
                }      
            };
        })(name, nativeInterface[name]);
    }
}

/**
 * 通过 iframe 来调用Native方法
 * @param  {[type]} apiName        [Native方法名]
 * @param  {[type]} asyncParamsStr [参数]
 * @return {[type]}                [description]
 */
function callNativeInterface(name, asyncParamsStr) {
    console.log('js is calling nativeInterface:' + name);
    var iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    iframe.src = 'async:' + name + ':' + asyncParamsStr;
    document.body.appendChild(iframe);
    document.body.removeChild(iframe);
}

/**
 * 初始化jsInterface & nativeInterface
 * 通知Native Ready
 * @return {[type]} [description]
 */
(function init() {
    publicJsInterface(jsInterface);
    publicNativeInterface(nativeInterface);
    window.NativeApis.asyncReady();  
})();
