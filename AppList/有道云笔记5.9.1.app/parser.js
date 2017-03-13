/*jslint browser: true, vars: true, nomen: true, indent: 4, maxlen: 80, plusplus: true, sloppy: true*/
/*global define: true */
/**
 * 清除元素标签
 * @param  {[type]} el    [description]
 * @param  {[type]} tagSl [清除元素选择器]
 * @return {[type]}       [description]
 */
function cleanElements(el, tagSl){
    if (!tagSl) {
        console.log('tagSl is null');
        return;
    }
    var rmEls = el.querySelectorAll(tagSl);
    var i = 0;
    var len = rmEls.length;

    for (i = 0; i < len; i++) {
        rmEls[i].parentNode.removeChild(rmEls[i]);
    }
}

/**
 * 清除元素属性
 * @param  {[type]} el    [description]
 * @param  {[type]} attrs [清除属性列表]
 * @return {[type]}       [description]
 */
function cleanAttributes(el, attrs) {
    var els = el.getElementsByTagName('*');
    var i = 0;
    var j = 0;
    var len = els.length;
    var tmpEl = null;
    var attrsLen = attrs.length;

    for (i = 0; i < len; i++) {
        tmpEl = els[i];

        //清除attrs属性
        for(j = 0; j < attrsLen; j++) {
            tmpEl.removeAttribute(attrs[j]);
        }

        //清除链接脚本
        if (tmpEl.tagName === 'A' && /javascript:/i.test(tmpEl.href)) {
            tmpEl.href = '';
        }

        //设置图片最大宽度
        if (tmpEl.tagName === 'IMG') {
            tmpEl.style.maxWidth = '97%';
        }
    }
}

/**
 * 默认文档解析
 * @param  {[type]} str [description]
 * @return {[type]}     [description]
 */
function parserHtml(str) {
    //清除元素选择器
    var tagSl = 'script, style, link, iframe, form, input, select, textarea, button';
    var attrs =  ['style', //行内样式
            'id', // id 与 class
            'class',
            // DOM Level 1 与显示布局相关的属性
            'height', // width height
            'width',
            'size', // <font size="xxx" />
            'color', // <font color='xxx' />
            'bgcolor',
            'background'
            ];
    var wraper = document.createElement('div');
    wraper.innerHTML = str;
    cleanElements(wraper, tagSl);
    cleanAttributes(wraper, attrs);
    return wraper.innerHTML;
}

/**
 * Article文档解析
 * @param  {[type]} str [description]
 * @return {[type]}     [description]
 */
function parserArticle(str) {
        //清除元素选择器
    var tagSl = 'script, style, link, iframe, form, input, select, textarea, button';
    var attrs =  ['style', //行内样式
            'id', // id 与 class
            'class',
            // DOM Level 1 与显示布局相关的属性
            'height', // width height
            'width',
            'size', // <font size="xxx" />
            'color', // <font color='xxx' />
            'bgcolor',
            'background'
            ];
    var wraper = document.createElement('div');
    wraper.innerHTML = str;
    cleanElements(wraper, tagSl);
    cleanAttributes(wraper, attrs);
    //Title style
    var title = wraper.querySelector('h1 a');
    if (title) {
        title.style.cssText += 'color: black; text-decoration: none; font-size: 20px; font-weight: normal;'
    }
    return wraper.innerHTML;
}

function appendElementStyle(el, cssTxt) {
    el.style.cssText += cssTxt;
}

/**
 * 查词结果样式适配
 * @param  {[type]} el 
 * 适配样式
 *         .trans-container{
 *              border: 1px solid #e5e5e5;
 *              background-color: #fafafa;
 *              margin: 5px 0 5px 0;
 *              padding: 5px;
 *          }
 *          .secondary{
 *              color: #808080;
 *          }
 *          .col1.secondary{
 *              display: none;
 *          }
 *          .trans-container ul{
 *              list-style: decimal;
 *          }
 * @return {[type]}    [description]
 */
function appendWordStyle(el) {
    var config = {
        '.trans-container': 'border: 1px solid #e5e5e5; background-color: #fafafa; margin: 5px 0 5px 0; padding: 5px;',
        '.trans-container .secondary': 'color: #808080;',
        '.grey': 'color: #808080;',
        '.col1': 'display: none;',    // Todo remove
        '.trans-container ul': 'list-style: decimal;'
    };
    var it;
    var els;
    var i = 0;

    for (it in config){
        els = el.querySelectorAll(it);
        for (i = 0; i < els.length; i++) {
            appendElementStyle(els[i], config[it]);
        }
    }
}

function parserWordEl(el){
   var tagSl = 'script, style, link, iframe, form';
    var attrs =  ['style', //行内样式
            'id', // id 与 class
            //'class',
            // DOM Level 1 与显示布局相关的属性
            'height', // width height
            'width',
            'size', // <font size="xxx" />
            'color', // <font color='xxx' />
            'bgcolor',
            'background'
            ];
    cleanElements(el, tagSl);
    cleanAttributes(el, attrs);
    appendWordStyle(el);
}

/**
 * 词典Word Query文档解析
 * @param  {[type]} str  [description]
 * @param  {[type]} type [description]
 * @return {[type]}      [description]
 */
function parserWord(str) {
       //清除元素选择器
    var tagSl = 'script, style, link, iframe, form';
    var attrs =  ['style', //行内样式
            'id', // id 与 class
            //'class',
            // DOM Level 1 与显示布局相关的属性
            'height', // width height
            'width',
            'size', // <font size="xxx" />
            'color', // <font color='xxx' />
            'bgcolor',
            'background'
            ];
    var wraper = document.createElement('div');
    wraper.innerHTML = str;
    cleanElements(wraper, tagSl);
    cleanAttributes(wraper, attrs);
    appendWordStyle(wraper);
    return wraper.innerHTML;
}

function parser(str, type) {
    str = str || '';
    console.log('解析器执行html解析', str, type);
    var result = '';
    if (type === 'article') {
        result = parserArticle(str);
    } else if (type === 'word') {
        result = parserWord(str);
    } else {
        console.log('不支持类型, 使用默认解析');
        result = parserHtml(str);
    }
    return result;
}