#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.noteHandle_constant import NoteHandle_constant

#新笔记加密成功

#前提：已登陆，已解密
#步骤：
# 1打开应用》点击全部》打开文件夹》输入阅读密码》打开
# 2检查当前页是否存在此文档，若存在，打开新笔记
# 3若不存在，往下滚一屏，再打开新笔记
# 4点击笔记下方 加密按扭
# 5返回列表》再次打开此笔记》检验
#检验：进入输密码页面

common=Common_Util()
notehandle_constant=NoteHandle_constant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        #清掉密码
        self.decode()
        self.driver.quit()

    def test_encrypt_note(self):
        print "************  encrypt new note method ***********"

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
        common.exists(notehandle_constant.new_note)
        #open note
        self.driver.find_element_by_name(notehandle_constant.new_note).click()

        time.sleep(1)
        #判断笔记是否已加过密了
        if self.driver.find_elements_by_name('忘记阅读密码？'):
            #已加密，先解密
            self.decode()
        else:
            #未加密
            pass
        time.sleep(2)
        # 加密按扭
        self.driver.find_element_by_name('加密').click()
        # check toast提示成功
        # todo
        #back
        self.driver.find_element_by_name('返回').click()
        #再次打开笔记
        self.driver.find_element_by_name(notehandle_constant.new_note).click()
        #check 出现输密码界面
        self.assertTrue(self.driver.find_element_by_name('忘记阅读密码？').is_displayed(),'新笔记加密失败！')


    def decode(self):
        # 输密码页面
        #在当前页上，输入密码，打开笔记正文
        self.driver.find_element_by_class_name('SecureTextField').send_keys(notehandle_constant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(2)
        #再点一下加密按扭，解除掉密码
        self.driver.find_element_by_name('加密').click()

if __name__ == '__main__':
    unittest.main()
