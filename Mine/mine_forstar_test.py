#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》加星文档 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 加星文档》检验2

#检验1：加星文档 按扭存在
#检验2：加星文件 列表右上角的 more按扭出现

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_forstar(self):
        print "************  mine for star  method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 加星文件 按扭存在
        self.assertTrue(self.driver.find_element_by_name('加星文件').is_displayed(),'我的》加星文件 不存在！！')
        #open
        self.driver.find_element_by_name('加星文件').click()
        #检验 加星文件 列表右上角的 more按扭出现
        self.assertTrue(self.driver.find_element_by_name('more option').is_displayed(),'加星列表打开失败！！')
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
