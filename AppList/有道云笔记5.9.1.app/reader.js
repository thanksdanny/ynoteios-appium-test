/*
 * reader.js
 * author: suzy (suzy@rd.netease.com)
 *         tangqiao (tangqiao@rd.netease.com)
 * description: the imgs will be clickable if this js is loaded.
 *     the click will start load an url as "app:imgclicked:xxx"
 */

var allImgs;
var originalImgs;
// 鼠标点击位置
var mousePos = {};
//是否是视网膜屏
var IS_RETINA  =  window.devicePixelRatio >= 2,
    UNKOWN_PNG = 'unknown-media-type' + (IS_RETINA ? '@2x' : '') + '.png',
    UNKOWN_WIDTH = 303,
    UNKOWN_HEIGHT = 62;

// --------------------- Click Response Functions ---------------------
function imgClicked(img) {
    if (img.getAttribute("path")) {
        if (img.getAttribute("title") == null) {
            img.setAttribute("title", "没有title??");
        }
        loadURL("app:att:"+img.getAttribute("path")+"/"+img.getAttribute("title"));
    } else {
        //this is an attach image
        //get original thumbnail src first
        img = img.firstChild;
        var order = img.name;
        var spaceIndex = order.indexOf(" ");
        var orderNumber = order.substring(spaceIndex+1);
        var index = parseInt(orderNumber);
        loadURL("app:img:"+originalImgs[index].src);
    }
}

// 通知iphone web view加载url对应的资源
function loadURL(url) {
    var iFrame;
    iFrame= document.createElement("iframe");
    iFrame.setAttribute("src", url);
    iFrame.style.display = 'none';
    document.body.appendChild(iFrame); 
    iFrame.parentNode.removeChild(iFrame);
    iFrame = null;
}

// 附件被点击，通知app下载附件
function attachmentClicked(span) {
    var images = span.getElementsByTagName("img");
    var theImg = images[0];
    imgClicked(theImg);
}

// 检查该附件，将大小和path传给后台，后台根据下载情况将附件改成已下载或启动自动下载(大小<500K)
function checkAttachment(index) {
    loadURL("app:check:" + index);
}

function attDownloadFinished(index) {
    var id = "attachImageSpan " + index;
    var aDiv = document.getElementById(id);
    aDiv.className = "rborder_done";
    var aTable = aDiv.getElementsByTagName('table');
    aTable[0].rows[1].cells[1].innerHTML = '';
}

function attDownloading(index, percent) {
    var id = "attachImageSpan " + index;
    var aDiv = document.getElementById(id);
    aDiv.className = "rborder_loading";
    // TODO: add percent text
    var aTable = aDiv.getElementsByTagName('table');
    aTable[0].rows[1].cells[1].innerHTML = '&nbsp;&nbsp;' +  percent + '%';
}

// --------------------- script initialize ---------------------

// 恢复成以前的html标签
function recoverOriginalContent() {
    allImgs = document.body.getElementsByTagName('img');
    for (var i = allImgs.length - 1 ; i >= 0;  i--) {
        if (!allImgs[i] || allImgs[i].className === 'arrow') {
            continue;
        }
        var father = allImgs[i].parentNode;
        var nodeType = father.tagName.toLowerCase();
        if ( nodeType === 'div') {
            father.insertAdjacentElement("afterEnd", originalImgs[i]);
            father.parentNode.removeChild(father);
        } else if (nodeType === 'td') {
            var child = null;
            while (nodeType !== 'div' && nodeType !== 'p') {
                child = father;
                father = father.parentNode;
                nodeType = father.tagName.toLowerCase();
            }
            // 如果是p，则表示在编辑模式下，div被替换成了p了
            if (nodeType === 'p') {
                father = child;
            }
            father.insertAdjacentElement("afterEnd", originalImgs[i]);
            father.parentNode.removeChild(father);
        }
    }
    return "recover Succeed";
}

// 图片的缩略图下载成功时的回调函数
function handleDownloadFinished(i, imageSrcAdd) {
    allImgs[i].src = imageSrcAdd;
}

/**
 * 截取固定长度字符串
 */
function shortString(str, len, flag) {
    var strLen = str.replace(/[\u4e00-\u9fa5\s]/g , "**").length, newStr = [], totalCount = 0;
    
    if( strLen <=  len ) {
        return str;
    } else {
        for(var i = 0; i < strLen; i++ ) {
            var nowValue = str.charAt( i );
            if ( /[^\x00-\xff]/.test( nowValue ) ) {
                totalCount += 2;
            } else {
                totalCount +=1;
            }
            newStr.push(nowValue);
            if( totalCount >= len ) {
                break;
            }
        }
        if( flag ) {
            return newStr.join("");
        } else {
            return newStr.join("") + "...";
        }
    }
};

// 类似Java的String.endWith(subStr)方法
function stringEndWith(str, endStr) {
    var pos = str.lastIndexOf(endStr);
    return pos + endStr.length === str.length;
}

// 根据文件类型来设置icon
function getAttachmentIcon(filename) {
    filename = filename.toLocaleLowerCase();
    if (stringEndWith(filename, 'txt')) {
        return 'txt.png';
    }
    if (stringEndWith(filename, 'doc') || stringEndWith(filename, 'docx')) {
        return 'word.png';
    }
    if (stringEndWith(filename, 'ppt') || stringEndWith(filename, 'pptx')) {
        return 'powerpoint.png';
    }
    if (stringEndWith(filename, 'xls') || stringEndWith(filename, 'xlsx')) {
        return 'excel.png';
    }
    if (stringEndWith(filename, 'pdf')) {
        return 'pdf64.png';
    }
    if (stringEndWith(filename, 'txt')) {
        return 'txt.png';
    }
    var audio = ['mp3','aac','ogg','wav','flac','m4a','ape','amr'];
    for (var i = 0; i < audio.length; ++i) {
        if (stringEndWith(filename, audio[i])) {
            return 'audio.png';
        }
    }
    var video = ['rm','rmvb','avi','mkv','mpg','mpeg','wmv','ts','m4v','mp4','wma'];
    for (var i = 0; i < video.length; ++i) {
        if (stringEndWith(filename, video[i])) {
            return 'video.png';
        }
    }
    var picture = ['jpg','jpeg','gif','png','bmp','psd','ia'];
    for (var i = 0; i < picture.length; ++i) {
        if (stringEndWith(filename, picture[i])) {
            return 'picture.png';
        }
    }
    var rar = ['zip','rar','7zp'];
    for (var i = 0; i < rar.length; ++i) {
        if (stringEndWith(filename, rar[i])) {
            return 'rar.png';
        }
    }
    var html = ['html','htm','mht'];
    for (var i = 0; i < html.length; ++i) {
        if (stringEndWith(filename, html[i])) {
            return 'html.png';
        }
    }
    var swf = ['swf','flv'];
    for (var i = 0; i < swf.length; ++i) {
        if (stringEndWith(filename, swf[i])) {
            return 'swf.png';
        }
    }
    return 'other_type.png';
}


// 将自定义的img标签替换成更好的显示方式
function initClickResponse() {
    var body = document.body;
    if (!body) {
        //alert("no body!");
        return "document Error: No Body.";
    }
    
    allImgs = document.body.getElementsByTagName('img'); 
    originalImgs = new Array();
    for(i = 0; i < allImgs.length; i++)
    {
        originalImgs[i] = allImgs[i].cloneNode(true);
        if (allImgs[i].className === 'arrow') {
            continue;
        }
        //判断是否是 未知类型的
        //see Editor src/IPhone/Filter/ImageUnknownSetFilter.js
        //use getAttribute NOT dataset
        //for ios4 don't support dataset
        var type = (allImgs[i].getAttribute('data-media-type') || 'image').toLowerCase();
        var known = ['image', 'attachment', 'handwrite', 'crypt'];
        // for test
        //var known = ['image', 'attachment', 'crypt']
        var isUnknown = known.indexOf(type) == -1;
        if (isUnknown) {
            allImgs[i].src = UNKOWN_PNG;
            allImgs[i].style.width = UNKOWN_WIDTH + 'px';
            allImgs[i].style.height = UNKOWN_HEIGHT + 'px';
            continue;
        }

        //
        allImgs[i].name = "imagename " + i;
        //如果有filename但没有title,就把title设置成filename
        if (allImgs[i].getAttribute("filename") && !allImgs[i].title) {
            allImgs[i].setAttribute("title", allImgs[i].getAttribute("filename"));
        }
        //用一个带有id的div包围图片，防止被编辑
        var aDiv = document.createElement("div");
        aDiv.id = "attachImageSpan " + i;
        //开始分类处理, 一共分3类：内部图片、内部附件、外部图片
        //内部图片要显示缩略图，内部附件要显示附件大小（小于500K)自动下载，外部图片不管
        var attPath = allImgs[i].getAttribute("path");
        var attSrc = allImgs[i].getAttribute("src");
        var pos = attSrc.indexOf("note.youdao.com");

        if (pos == -1) {
            pos = attSrc.indexOf(".corp.youdao.com");
        }
        if (pos == -1) {
            if (attSrc[0] === '/') {
                pos = 0;
            }
        }
        if (pos != -1) {
            // 内部图片
            if (!attPath) {
                allImgs[i].insertAdjacentElement("afterEnd", aDiv);
                aDiv.insertAdjacentElement("beforeEnd", allImgs[i]);
                aDiv.onclick = function() {
                    return imgClicked(this);
                };
                //此处如果使用removeAttribute而不是setAttribute
                //则会发生style/height/width删不掉的问题，而且代码会挂，执行不到后面请求缩略图的部分
                if (allImgs[i].getAttribute("style")) {
                    allImgs[i].setAttribute("style", "");
                }
                if (allImgs[i].getAttribute("height")) {
                    allImgs[i].setAttribute("height", "");
                }
                if (allImgs[i].getAttribute("width")) {
                    allImgs[i].setAttribute("width", "");
                }
                //图片类需要改url为本地图片，并发起后台下载
                var theSrc = allImgs[i].src;
                loadURL("app:attachthumb:"+theSrc+":"+i);
            } else { // 内部附件
                // 增加圆角样式
                aDiv.className = "rborder";
                // 计算大小
                var len = allImgs[i].getAttribute("filelength");
                var contentSize;
                if (len) {
                    if (len < 1024) {
                        contentSize = len + "B";
                    } else if (len >= 1024 && len < 1048576) {
                        contentSize = (len / 1024).toFixed(2) + "KB";
                    } else {
                        contentSize = (len / 1048576).toFixed(2) + "MB";
                    }
                }
                // 加入table
                var table = document.createElement('table');
                table.innerHTML = '<tr style="color:gray">'
                +   '<td width="35px" rowspan=2></td>'
                +   '<td width="200px" colspan=2>name</td>'
                +   '<td width="50px" rowspan=2><div class="att_bg"><img class="loadingPic" src="loading.gif" /></div>  </td> '
                + '</tr>' 
                + '<tr style="color:gray">'
                +   '<td width="50px">size</td>'
                +   '<td width="150px"></td>'
                +   '</tr>';
                aDiv.appendChild(table);
                //table.rows[0].cells[1].innerHTML = shortString(allImgs[i].title, 22);
                table.rows[0].cells[1].innerHTML = '<div class="ynote-reader-title">' + allImgs[i].title +'</div>';
                table.rows[1].cells[0].innerHTML = contentSize;
                // 先将aDiv放在图片下面，然后再将图片放进table里
                allImgs[i].className = 'attachicon';
                allImgs[i].src = getAttachmentIcon(allImgs[i].title);
                allImgs[i].insertAdjacentElement("afterEnd", aDiv);
                table.rows[0].cells[0].insertAdjacentElement("beforeEnd", allImgs[i]);
                aDiv.onclick = function() {
                    return attachmentClicked(this);
                };
                checkAttachment(i, allImgs[i].getAttribute("path"), len);
            }
        }
    }
    return "init Succeed";
}


function handleClick(e) {
    if (!isPhoneMode) {
        handleTouchEnd(e);
    }
}

function handleTouchEnd(e) {
    var target = e.target || e.srcElement || document;
    // show web trans page
    if (target.nodeType === Node.TEXT_NODE) {
        target = target.parentNode;
    }
    var offsetX = window.scrollX? window.scrollX : 0;
    var offsetY = window.scrollY? window.scrollY : 0;
    var eventDefX = e.touches && e.touches.length > 0? e.touches[0].pageX : (e.changedTouches && e.changedTouches.length > 0? e.changedTouches[0].pageX : e.pageX);
    var eventDefY = e.touches && e.touches.length > 0? e.touches[0].pageY : (e.changedTouches && e.changedTouches.length > 0? e.changedTouches[0].pageY : e.pageY);
    var eventClientX = eventDefX - offsetX;
    var eventClientY = eventDefY - offsetY;
    if (mousePos.x && mousePos.y) {
        var xx = mousePos.x;
        var yy = mousePos.y;
        var diff = {};
        diff.x = xx - parseInt(eventClientX);
        diff.y = yy - parseInt(eventClientY);
        diff.dis = diff.x * diff.x + diff.y * diff.y;
        mousePos = {};
        if (diff.dis > 900) {
            // The moving action with more than 30 pixels is justified as dragging.
            return;
        }
    }
    var clientX = (e.touches && e.touches.length > 0)? e.touches[0].clientX : (e.changedTouches && e.changedTouches.length > 0? e.changedTouches[0].clientX : e.clientX);
    var clientY = (e.touches && e.touches.length > 0)? e.touches[0].clientY : (e.changedTouches && e.changedTouches.length > 0? e.changedTouches[0].clientY : e.clientY);
    mousePos.x = clientX;
    mousePos.y = clientY;
}

function handleTouchStart(e) {
    // Notice: mousePos is the client coordinate of the start of touch.
    // The page/client/screen coordinates on iOS are all the same as the page one, which seems to be a bug.
    // However, we could solve it in this way: change the page(x, y) to client(x, y) by subtracting window.scroll(x, y)
    isPhoneMode = true;
    var offsetX = window.scrollX? window.scrollX : 0;
    var offsetY = window.scrollY? window.scrollY : 0;
    if (e.touches && e.touches.length > 0) {
        mousePos.x = e.touches[0].pageX - offsetX;
        mousePos.y = e.touches[0].pageY - offsetY;
    } else if (e.changedTouches && e.changedTouches.length > 0) {
        mousePos.x = e.changedTouches[0].pageX - offsetX;
        mousePos.y = e.changedTouches[0].pageY - offsetY;
    }
}

function initYNoteEdit() {
    var body = document.body;
    if (!body) {
        document.addEventListener("DOMContentLoaded", initYNoteEdit, false);
        return;
    }
    body.addEventListener("click", handleClick, false);
    body.addEventListener("touchstart", handleTouchStart, false); // for mobile phones
    body.addEventListener("touchend", handleTouchEnd, false); // for mobile phones
}
initYNoteEdit();

////script start run from here.
document.addEventListener("DOMContentLoaded", initClickResponse, false);
