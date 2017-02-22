#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Common.common import Common_Util
from Constant.View_constant import ViewConstant

#查看txt内容

#前提：已登陆
#步骤：
# 1打开应用》点击全部
# 2打开文件夹》输入阅读密码》打开
# 3检查当前页是否存在此文档，若存在，打开txt
# 4若不存在，往下滚一屏，再打开txt》检验

#检验：检验txt显示出来了

common=Common_Util()
viewconstant=ViewConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_view_txt(self):
        print "************  view txt method ***********"

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
        common.exists(viewconstant.txt_title)
        #open txt
        self.driver.find_element_by_name(viewconstant.txt_title).click()
        time.sleep(3)
        #check 内容中包含 某个字符串
        self.assertTrue(unicode('单项选择题') in self.driver.find_element_by_class_name('TextView').get_attribute('value'),'查看txt内容失败！！')

if __name__ == '__main__':
    unittest.main()
