#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.editor_constant import EditorConstant

#创建小字号的中英文笔记

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹Editor Test
# 2点＋号》选择 新建笔记 按扭》进入新建笔记界面
# 3点击 工具条上，word图标》再选中 字号 －按扭 点击
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

    def test_sizeminus_note(self):
        print "************ size minus note method ***********"

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
        #点 字号的－号 按扭，减小字号为12
        self.driver.find_element_by_name('size minus').click()
        #点编辑区，进入编辑模式
        self.driver.find_element_by_class_name('TextView').click()

        #输入5行内容
        for i in range(1,6):
            self.driver.find_element_by_class_name('TextView').send_keys(editorconstant.sizeminus[1])

        #finish
        self.driver.find_element_by_name('完成').click()
        #title
        self.driver.find_element_by_class_name('TextField').send_keys(editorconstant.sizeminus[0])
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        #检验 在列表上笔记创建成功
        self.assertTrue(self.driver.find_element_by_name(editorconstant.sizeminus[0]).is_displayed(),'＊＊*小字号笔记创建失败！＊＊＊')

if __name__ == '__main__':
    unittest.main()
