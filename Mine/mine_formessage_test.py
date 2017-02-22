#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》消息中心 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 消息中心》检验2

#检验1：消息中心 按扭存在
#检验2：我的 TAB消失了

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_formessage(self):
        print "************  mine for message method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 消息中心 按扭存在
        self.assertTrue(self.driver.find_element_by_name('消息中心').is_displayed(),'我的>消息中心 不存在！！')
        #open
        self.driver.find_element_by_name('消息中心').click()
        #检验 我的 TAB消失了
        self.assertFalse(self.driver.find_element_by_name('tabbar_my').is_displayed(),'消息中心 列表打开失败！！')
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
