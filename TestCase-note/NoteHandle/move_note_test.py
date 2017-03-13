#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.noteHandle_constant import NoteHandle_constant

#移动笔记

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹》输入阅读密码》打开
# 2检查当前页是否存在此文档，若存在，打开新笔记
# 3若不存在，往下滚一屏，再打开笔记
# 4点击笔记下方 移动 按扭》打开移动界面》检验

#检验：打开了全部文件界面，移动到此处 按扭存在

common=Common_Util()
notehandle_constant=NoteHandle_constant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_move_note(self):
        print "************ move note method ***********"

        #全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #打开分享文件夹
        self.driver.find_element_by_name(notehandle_constant.notebook_title).click()
        #input password
        self.driver.find_element_by_class_name('SecureTextField').send_keys(notehandle_constant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(1)

        #判断当前是否存在此文档
        common.exists(notehandle_constant.note)
        #open note
        self.driver.find_element_by_name(notehandle_constant.note).click()
        time.sleep(1)
        #click
        self.driver.find_element_by_name('移动').click()
        #chcek 打开全部文件界面
        self.assertTrue(self.driver.find_element_by_name('全部文件').is_displayed(),'移动笔记：失败！')
        #移动到此处 按扭存在
        self.assertTrue(self.driver.find_element_by_name('移动到此处').is_displayed(),'移动笔记：失败！')



if __name__ == '__main__':
    unittest.main()
