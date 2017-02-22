#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》用户信息（昵称）正常显示

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1

#检验1：昵称存在

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_foruserinfo(self):
        print "************  mine for userinfo  method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 userinfo 存在
        self.assertTrue(self.driver.find_element_by_name('ynotetestui').is_displayed(),'我的>用户昵称 不存在！！')
if __name__ == '__main__':
    unittest.main()
