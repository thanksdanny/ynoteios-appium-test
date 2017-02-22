#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.editor_constant import EditorConstant

#创建无序列表中英文笔记

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹Editor Test
# 2点＋号》选择 新建笔记 按扭》进入新建笔记界面
# 3点击 工具条上，无序按扭
# 4循环输入多次内容》完成》输入标题》返回
# 5再次打开笔记》进入编辑模式》检验
#检验：工具条上的unsort元素的 value值为true（被选中）

common=Common_Util()
editorconstant=EditorConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_unorder_note(self):
        print "************ unorder note method ***********"

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
        #点 无序工具条
        self.driver.find_element_by_name('unsort icon').click()
        #输入5行内容
        for i in range(1,6):
            self.driver.find_element_by_class_name('TextView').send_keys(editorconstant.unsort[1])

        #finish
        self.driver.find_element_by_name('完成').click()
        #title
        self.driver.find_element_by_class_name('TextField').send_keys(editorconstant.unsort[0])
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)

        #check无序
        #再次打开此笔记
        self.driver.find_element_by_name(editorconstant.unsort[0]).click()
        time.sleep(2)
        #点编辑区，进入编辑模式
        self.driver.find_element_by_class_name('TextView').click()
        time.sleep(2)
        #检验 unsort的工具条元素的 value值为true
        self.assertTrue(self.driver.find_element_by_name('unsort icon').get_attribute('value'),'＊＊无序中英文笔记创建失败！＊＊')




if __name__ == '__main__':
    unittest.main()
