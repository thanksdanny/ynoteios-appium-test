#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.View_constant import ViewConstant

#查看图片内容

#前提：已登陆
#步骤：
# 1打开应用》点击全部
# 2打开文件夹》输入阅读密码》打开
# 3检查当前页是否存在此文档，若存在，打开图片
# 4若不存在，往下滚一屏，再打开图片》检验

#检验：检验图片显示出来了

common=Common_Util()
viewconstant=ViewConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_view_pic(self):
        print "************  view pic method ***********"

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
        common.exists(viewconstant.pic_title)
        #open pic
        self.driver.find_element_by_name(viewconstant.pic_title).click()
        time.sleep(2)
        #check
        self.assertTrue(self.driver.find_element_by_class_name('Image').is_displayed(),'查看图片内容失败！！')

if __name__ == '__main__':
    unittest.main()
