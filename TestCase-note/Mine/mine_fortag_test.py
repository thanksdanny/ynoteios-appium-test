#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.share_constant import ShareConstant

# 我的》我的标签 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 我的标签》检验2

#检验1：我的标签 按扭存在
#检验2：我的标签 列表右上角的 编辑 按扭出现

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_fortag(self):
        print "************  mine for tag  method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 我的标签 按扭存在
        self.assertTrue(self.driver.find_element_by_name('我的标签').is_displayed(),'我的>我的标签 不存在！！')
        #open
        self.driver.find_element_by_name('我的标签').click()
        #检验 我的标签 列表右上角的 编辑 按扭出现
        self.assertTrue(self.driver.find_element_by_name('编辑').is_displayed(),'我的标签 列表 工打开失败！！')

if __name__ == '__main__':
    unittest.main()
