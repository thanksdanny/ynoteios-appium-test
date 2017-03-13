#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》用户满意度调查 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 用户满意度调查》检验2

#检验1：用户满意度调查 按扭存在
#检验2：用户满意度调查 页面上右上角的 提交 键存在

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_forgroupbusiness(self):
        print "************  mine for groupbusiness method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        #检验当前页存在性
        #common.exists(self.driver.find_element_by_name('用户满意度调查'))
        self.driver.execute_script("mobile:scroll", {"direction": "down"})
        # 检验 用户满意度调查 按扭存在
        self.assertTrue(self.driver.find_element_by_name('用户满意度调查').is_displayed(),'我的>用户满意度调查 不存在！！')
        #open
        self.driver.find_element_by_name('用户满意度调查').click()
        #检验 用户满意度调查 页面上右上角的 提交 键存在
        self.assertTrue(self.driver.find_element_by_name('提交').is_displayed(),'用户满意度调查 列表 工打开失败！！')
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
