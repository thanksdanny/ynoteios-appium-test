/** This file is automatically generated by BulbEditor builder **/

define(function () {
    return {

/*********************./src/iphone/io/editorApi.js START *********************/


        /**
        * @param {String} content
        * @param {Boolean} isHtml
        */
        setEditorContent: function(content, isHtml){
        },

        setEditorText: function(text){
        },

        /**
        * @param {Boolean} isHtml
        * @return {String}
        */
        getEditorContent: function(isHtml){
        },

        focusEditor: function(){
        },

        /**
        * @param {String} cmd.name
        * @param {Object} cmd.args
        */
        exeCmd: function(cmd){
        },

        /**
        * @param {String} orgSrc
        * @param {Object} info
        * @param {String} info.url 图片缩略图地址
        */
        replaceImageByOrigSrc: function(orgSrc, info){
        },

        /**
        * @param {String} resource
        * @param {String} distSrc
        */
        setAttachmentState: function(resource, distSrc){
        },

        /**
        * @param {String} info.type
        * @param {Object} info.data
        */
        doPaste: function(info){
        },

        /**
        * @param {String} uid
        */
        getDataByUID: function(uid){
        },

        getEditorFirstLineTextContent: function(){
        },

        /**
        * get editor plain text which is used for iphone to generate
        * summary info
        * @param {Boolean} ignoreTable -- whether ignore the table info
        */
        getEditorTextContent: function(ignoreTable){
        },

        /**
        * set the view port height when the keyboard is shown
        * @param {Integer} height
        */
        setEditorInnerHeight: function(height){
        },

        setEditorFullHeight: function(height){
        },

        setTextEditMenuState: function(isActive){
        },

        /**
        * @param {Boolean} readOnly
        */
        setReadOnlyMode: function(readOnly){
        },

        updateImages: function(imageInfos){
        },

        /**
        * 设置表格中某一项的内容
        * @param {JSON对象} cellInfo
        * cellInfo = {
        *      stringValue: 'insert', //插入值
        *      tableId: 23222, //表格块id
        uid: cellId_128, //所在单元格ID
        moveToNext: true or false // 是否移到下面的单元格
        * }
        */
        setCellValue: function(cellInfo){
        },

        /** 高亮文本
        * @param {Array<String>} words
        */
        highlight: function(words){
        },

        removeHighlight: function(){
        },

        /**
        * 为字数统计提供的接口
        */
        countWords: function(){
        },

        /**
        * 设置编辑器的左右填充空白宽度
        * @param {Integer} value 宽度
        */
        setPaddingLeftAndRight: function(value){
        },

        /**
        * @return {Integer}
        * @see https://developer.mozilla.org/en-US/docs/DOM/window.scrollY
        */
        getCurrentPosition: function(){
        },

        /**
        * 设置当前的位置, 在setEditorContent()之后调用
        * @param {Integer}  percentage number working with RATIO
        * @see https://developer.mozilla.org/en-US/docs/DOM/window.scrollTo
        */
        setCurrentPosition: function(y){
        },

        /**
        * @param {Integer} mode
        *     mode = 1 : 无键盘弹出或者无外接硬键盘状态
        *     mode = 2 : 普通/手写键盘弹出或者有外接硬键盘状态
        * @see ../../mobile/util/keyboardMode.js
        */
        setKeyboardMode: function(mode){
        },

/*********************./src/iphone/io/editorApi.js END *********************/

    };
});