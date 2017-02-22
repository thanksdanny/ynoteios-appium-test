#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#帐号 ynotetestui@163.com/abc123
#测试目录 全部>EditorTool Test

import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class EditorConstant():

    localtime = time.strftime('%Y-%M-%d %H-%M-%S', time.localtime())

    notebook_title='EditorTool Test'
    #无序笔记的标题和内容
    unsort=['unsort'+localtime,  unicode('测试无序笔记内容')+'unsort'+'\n']
    #有序笔记的标题和内容
    sort=['sort'+localtime,  unicode('测试有序笔记内容')+'sort'+'\n']
    #左缩进笔记的标题和内容
    leftIndent = ['leftIndent' + localtime, unicode('测试缩进笔记内容') + 'leftIndent' + '\n']
    #右缩进笔记的标题和内容
    rightIndent=['rightIndent'+localtime,  unicode('测试缩进笔记内容')+'rightIndent'+'\n']


    #加粗笔记的标题和内容
    bold=['bold'+localtime,  unicode('测试加粗笔记内容')+'bold'+'\n']
    #斜体笔记的标题和内容
    italic=['italic'+localtime,  unicode('测试斜体笔记内容')+'italic'+'\n']
    #下划线笔记的标题和内容
    underline = ['underline' + localtime, unicode('测试下划线笔记内容') + 'underline' + '\n']
    #删除线笔记的标题和内容
    strike = ['strike' + localtime, unicode('测试删除线笔记内容') + 'strike' + '\n']
    # 背景色笔记的标题和内容
    bgcolor = ['bgcolor' + localtime, unicode('测试删除线笔记内容') + 'bgcolor' + '\n']


    # 左对齐笔记的标题和内容
    leftalign = ['leftalign' + localtime, unicode('测试左对齐笔记内容') + 'leftalign' + '\n']
    # 居中对齐笔记的标题和内容
    textcenter = ['textcenter' + localtime, unicode('测试居中对齐笔记内容') + 'textcenter' + '\n']
    # 右对齐笔记的标题和内容
    rightalign = ['bgcolor' + localtime, unicode('测试右对齐笔记内容') + 'rightalign' + '\n']

    # 大字号笔记的标题和内容
    sizeincrease = ['sizeincrease' + localtime, unicode('测试大字号笔记内容') + 'sizeincrease' + '\n']
    # 小字号笔记的标题和内容
    sizeminus = ['sizeminus' + localtime, unicode('测试小字号笔记内容') + 'sizeminus' + '\n']


    # 带字色笔记的标题和内容
    colorlist=['color gray ','color red','color blue','color green','color orange']
    color = ['color' + localtime, unicode('测试字色笔记内容') + 'color' + '\n']




