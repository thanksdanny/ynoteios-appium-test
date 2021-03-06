#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import random

from Common.common import Common_Util
from Constant.editor_constant import EditorConstant

#创建带字色的中英文笔记

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹Editor Test
# 2点＋号》选择 新建笔记 按扭》进入新建笔记界面
# 3点击 工具条上，word图标》再随机选中 某字色  点击
# 4循环输入多次内容》完成》输入标题》返回》检验
#检验：创建笔记成功

common=Common_Util()
editorconstant=EditorConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_color_note(self):
        print "************ color note method ***********"

        #打开全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #open notebook
        self.driver.find_element_by_name(editorconstant.notebook_title).click()
        #new
        self.driver.find_element_by_name('newNote normal').click()
        self.driver.find_element_by_name('新建笔记').click()
        time.sleep(2)
        #edit page

        #edit
        #点 word 工具条
        self.driver.find_element_by_name('word icon').click()
        time.sleep(2)
        #随机选中某个字色
        color=editorconstant.colorlist[random.randint(0,4)]
        self.driver.find_element_by_name(color).click()

        #点编辑区，进入编辑模式
        self.driver.find_element_by_class_name('TextView').click()

        #输入5行内容
        for i in range(1,6):
            self.driver.find_element_by_class_name('TextView').send_keys(editorconstant.color[1])

        #finish
        self.driver.find_element_by_name('完成').click()
        #title
        self.driver.find_element_by_class_name('TextField').send_keys(editorconstant.color[0])
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        #检验 在列表上笔记创建成功
        self.assertTrue(self.driver.find_element_by_name(editorconstant.color[0]).is_displayed(),'＊＊*带字色笔记创建失败！＊＊＊')

if __name__ == '__main__':
    unittest.main()
