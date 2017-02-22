#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util

# 我的》云协作企业版 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 云协作企业版》检验2

#检验1：云协作企业版 按扭存在
#检验2：云协作企业版 页面上标题正常显示

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
        # 检验 云协作企业版 按扭存在
        self.assertTrue(self.driver.find_element_by_name('云协作企业版').is_displayed(),'我的>云协作企业版 不存在！！')
        #open
        self.driver.find_element_by_name('云协作企业版').click()
        time.sleep(2)
        #检验 云协作企业版 页面上标题正常显示
        self.assertTrue(self.driver.find_element_by_name('有道云协作企业版').is_displayed(),'云协作企业版 列表 打开失败！！')

if __name__ == '__main__':
    unittest.main()
