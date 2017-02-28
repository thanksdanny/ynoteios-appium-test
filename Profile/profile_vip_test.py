#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from Common.common import Common_Util

# 我的帐号页》点 开通会员

#前提：已登陆(非会员)
#步骤：
#1 打开应用》点击 头像》打开 我的帐号页
#3 点击 开通会员》检验

#检验：购买按扭存在

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test__profile_vip(self):
        print "************ profile vip  method ***********"
        #头像
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)
        #profile,vip
        self.driver.find_element_by_name('开通会员').click()
        time.sleep(2)
        #open vip page

        #check  购买 按扭存在
        self.assertTrue(self.driver.find_element_by_name('立即购买').is_displayed(),'****我的帐号页：点击 购买会员失败！*****')


if __name__ == '__main__':
    unittest.main()
