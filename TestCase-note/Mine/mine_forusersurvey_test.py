#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》有道云笔记用户调研 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 用户调研》检验2

#检验1：用户调研 按扭存在
#检验2：用户调研 列表右上角的 分享 按扭出现

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_forusersurvey(self):
        print "************  mine for usersurvey  method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        #判断当前页存在性
        common.exists('有道云笔记用户调研')
        # 检验 用户调研 按扭存在
        self.assertTrue(self.driver.find_element_by_name('有道云笔记用户调研').is_displayed(),'我的>用户调研 不存在！！')
        #open
        self.driver.find_element_by_name('有道云笔记用户调研').click()
        time.sleep(2)
        #检验 用户调研 列表右上角的 分享 按扭出现
        self.assertTrue(self.driver.find_element_by_name('viewModButtonShare').is_displayed(),'用户调研 列表 工打开失败！！')

if __name__ == '__main__':
    unittest.main()
