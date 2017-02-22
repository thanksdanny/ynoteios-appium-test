#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》设置 正常显示

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 点击设置按扭》检验2

#检验1：设置 按扭 存在
#检验2：设置页面，意见反馈按扭存在

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_setting(self):
        print "************  mine setting method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 设置 存在
        self.assertTrue(self.driver.find_element_by_name('设置').is_displayed(),'我的>设置  按扭 不存在！！')
        # click
        self.driver.find_element_by_name('设置').click()
        #检验 设置页面，意见反馈按扭存在
        self.assertTrue(self.driver.find_element_by_name('意见反馈').is_displayed(),'我的》设置 页，打开失败！')

if __name__ == '__main__':
    unittest.main()
