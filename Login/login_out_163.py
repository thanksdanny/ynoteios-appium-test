#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util

#注销163帐号成功

#前提：已登录
#步骤：
# 1首页》点用户头像
# 2往上滑动》点 退出登录
# 3弹框确认》检验
#检验：进入登录页面，注销成功


common=Common_Util()
class MyTestCase(unittest.TestCase):

    def setUp(self):
        # set up appium
        #已登录
        self.driver = common.setup_app()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    @unittest.skip()
    def test_login_out_163(self):
        print "************  login out 163 user method ***********"
        #判断当前是否为 首页
        if self.driver.find_elements_by_name('最新'):

            print "*****开始注销帐号－－－！*******"

            # user logo
            self.driver.find_element_by_class_name('Image').click()
            time.sleep(2)
            # 往上滑动
            self.driver.execute_script("mobile:scroll", {"direction": "down"})
            # 退出登录
            self.driver.find_element_by_name('退出登录').click()
            # 确定
            self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeOther[1]/'
                                              'XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/'
                                              'XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/'
                                              'XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/'
                                              'XCUIElementTypeOther[3]').click()

            time.sleep(3)
            #检验注销成功，进入登录页面
            self.assertTrue(self.driver.find_element_by_name('注册网易通行证').is_displayed(),'＊＊＊163帐号：注销失败了＊＊＊')

            print "*****163帐号：注销成功！*******"
        else:
            pass
            print "******当前不在首页，无法注销帐号*********"


if __name__ == '__main__':
    unittest.main()
