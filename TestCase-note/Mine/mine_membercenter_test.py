#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.share_constant import ShareConstant

# 我的》升级为会员 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 升级为会员》检验2

#检验1：升级为会员 按扭存在
#检验2：升级为会员 页面标题为 会员

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_membercenter(self):
        print "************  mine membercenter method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 升级为会员 按扭存在
        self.assertTrue(self.driver.find_element_by_name('升级为会员 50G空间等更多会员特权').is_displayed(),'我的>升级为会员 不存在！！')
        #open
        self.driver.find_element_by_name('升级为会员 50G空间等更多会员特权').click()
        #检验 升级为会员 页面标题为 会员
        self.assertTrue(self.driver.find_element_by_name('会员').is_displayed(),'我的》升级为会员 页面打开失败！！')

if __name__ == '__main__':
    unittest.main()
