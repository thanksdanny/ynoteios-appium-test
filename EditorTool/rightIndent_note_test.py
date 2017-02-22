#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.editor_constant import EditorConstant

#创建右缩进1位中英文笔记

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹Editor Test
# 2点＋号》选择 新建笔记 按扭》进入新建笔记界面
# 3点击 工具条上，左缩进按扭2次》右缩进1次
# 4循环输入多次内容》完成》输入标题》返回》检验
#检验：创建右缩进笔记成功

common=Common_Util()
editorconstant=EditorConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_rightIndent_note(self):
        print "************ rightIndent note method ***********"

        #打开全部
        self.driver.find_element_by_name('全部').click()
        #open notebook
        self.driver.find_element_by_name(editorconstant.notebook_title).click()
        #new
        self.driver.find_element_by_name('newNote normal').click()
        self.driver.find_element_by_name('新建笔记').click()
        time.sleep(2)
        #edit page

        #edit
        #点 leftIndent 工具条
        for i in range(1,3):
            self.driver.find_element_by_name('leftIndent icon').click()
        # 点 rightIndent 工具条
        for i in range(1,2):
            self.driver.find_element_by_name('rightIndent icon').click()
        #输入5行内容
        for i in range(1,6):
            self.driver.find_element_by_class_name('TextView').send_keys(editorconstant.rightIndent[1])

        #finish
        self.driver.find_element_by_name('完成').click()
        #title
        self.driver.find_element_by_class_name('TextField').send_keys(editorconstant.rightIndent[0])
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        #检验 在列表上笔记创建成功
        self.assertTrue(self.driver.find_element_by_name(editorconstant.rightIndent[0]).is_displayed(),'＊＊＊右缩进笔记创建失败！＊＊＊')

if __name__ == '__main__':
    unittest.main()
