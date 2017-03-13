#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.View_constant import ViewConstant

#查看旧笔记内容

#前提：已登陆
#步骤：
#1 打开应用》点击全部》打开文件夹
#2 输入阅读密码》打开
#3 检查当前页是否存在此文档，若存在，打开旧笔记》检验
#4 若不存在，往下滚一屏，再打开旧笔记》检验

#检验1：文字内容正常显示
#检验2：手写 正常显示
#检验3：图片 正常显示


common=Common_Util()
viewconstant=ViewConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_view_oldnote(self):
        print "************  view old note method ***********"

        #全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #打开分享文件夹
        self.driver.find_element_by_name(viewconstant.notebook_title).click()
        #input password
        self.driver.find_element_by_class_name('SecureTextField').send_keys(viewconstant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(1)

        #判断当前是否存在此文档
        common.exists(viewconstant.old_note_title)
        #open note
        self.driver.find_element_by_name(viewconstant.old_note_title).click()
        time.sleep(3)
        #check 第一段内容显示出来了
        self.assertTrue(unicode('旧笔记') in self.driver.find_element_by_class_name('StaticText').get_attribute('value'),'查看旧笔记内容失败！！')
        # check 语音附件出现
        self.assertTrue(self.driver.find_element_by_name('20170216-103626.m4a').is_displayed(),'查看旧笔记中的 语音附件失败！')
        #check 手写
        self.assertTrue(self.driver.find_elements_by_class_name('Image')[1].is_displayed(),'查看旧笔记中的 手写 失败')
        #check pic
        self.assertTrue(self.driver.find_elements_by_class_name('Image')[2].is_displayed(),'查看旧笔记中的 图片失败！')


if __name__ == '__main__':
    unittest.main()
