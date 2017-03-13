#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from Common.common import Common_Util

# 我的》签到 正常

#前提：已登陆
#步骤：
#1 打开应用》点击 我的》检验1
#2 打开 签到》检验2

#检验1：签到 按扭存在
#检验2：签到 页面标题为 会员

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_mine_checkin(self):
        print "************  mine checkin method ***********"
        #wo de
        self.driver.find_element_by_name('tabbar_my').click()
        time.sleep(2)
        #判断是否签过到
        if self.driver.find_elements_by_name('签到 签到获取更多空间'):

            print '去签到！！！'
            #签到按扭在，没签过到
            self.driver.find_element_by_name('签到 签到获取更多空间').click
            # 检验 签到成功
            self.assertTrue(self.driver.find_element_by_name('签到成功').is_displayed(), '我的》签到 点击失败！！')
        else:
            #签过到
            self.driver.find_element_by_name('已签到 签到获取更多空间').click()
            # 检验 提示已签到成功
            self.assertTrue(self.driver.find_element_by_name('今日已签到').is_displayed(), '我的》已签到 点击失败！！')

if __name__ == '__main__':
    unittest.main()
