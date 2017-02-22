#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》与我分享 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 与我分享》检验2

#检验1：与我分享 按扭存在
#检验2：与我分享列表不为空：第一条数据标题存在

common=Common_Util()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_forshare(self):
        print "************  mine for share  method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        # 检验 与我分享 按扭存在
        self.assertTrue(self.driver.find_element_by_name('与我分享').is_displayed(),'我的》与我分享 不存在！！')
        #open
        self.driver.find_element_by_name('与我分享').click()
        #检验与我分享列表不为空：第一条数据标题存在
        self.assertTrue(self.driver.find_elements_by_class_name('StaticText')[1].is_displayed(),'与我分享列表上 没有数据了！！')


if __name__ == '__main__':
    unittest.main()
