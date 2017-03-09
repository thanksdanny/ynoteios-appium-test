#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.noteHandle_constant import NoteHandle_constant

#查看笔记历史版本

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹》输入阅读密码》打开
# 2检查当前页是否存在此文档，若存在，打开新笔记
# 3若不存在，往下滚一屏，再打开笔记
# 4点击笔记下方 更多 按扭》打开 历史版本

#检验：

common=Common_Util()
notehandle_constant=NoteHandle_constant()
@unittest.skip
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_history_note(self):
        print "************ history note method ***********"

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
        self.driver.find_element_by_name('更多').click()
        #
        self.driver.find_element_by_name('历史版本').click()
        time.sleep(3)




if __name__ == '__main__':
    unittest.main()
