#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.noteHandle_constant import NoteHandle_constant

#笔记查看阅读模式

#前提：已登陆
#步骤：
# 1打开应用》点击全部》打开文件夹》输入阅读密码》打开
# 2检查当前页是否存在此文档，若存在，打开新笔记
# 3若不存在，往下滚一屏，再打开笔记
# 4点击笔记下方 阅读模式 按扭》打开阅读界面
# 5点击笔记标题位置》检验
#检验：弹出菜单中包含有 工具条 亮度 这一栏

common=Common_Util()
notehandle_constant=NoteHandle_constant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_readmodel_note(self):
        print "************ readmodel note method ***********"

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
        #
        self.driver.find_element_by_name('阅读模式').click()
        #点一下标题栏
        self.driver.find_element_by_name('All note').click()
        #检验 工具条出现了
        self.assertTrue(self.driver.find_element_by_name('亮度').is_displayed(),'笔记的阅读模式： 打开失败了！')
        #back
        self.driver.find_element_by_name('返回').click()




if __name__ == '__main__':
    unittest.main()
