#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util
from Constant.login_constant import LoginConstant

#登录126帐号成功

#前提：未登录（被注销＼从未登录过）
#步骤：
# 1判断当前是否登录页
# 2若是，则直接输入帐号密码，点登录》检验
# 3若不是，先点 我的，点此登录》开登录页，输入帐号密码，点登录》检验
#检验：当前界面为最新页


common=Common_Util()
loginconstant=LoginConstant()


@unittest.skip('')
class MyTestCase(unittest.TestCase):

    def setUp(self):
        # set up appium
        #不登录
        self.driver = common.setup_app(0)
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login126(self):
        print "************  login 126 user method ***********"
        #判断当前是否为 登录页
        if self.driver.find_elements_by_name('注册网易通行证'):
            #login page
            self.login_in()
        else:
            #当前是首页，则依次点击我的》点此登录》打开登录页
            self.driver.find_element_by_name('我的').click()
            time.sleep(2)
            self.driver.find_element_by_name('点此登录').click()
            #login page
            self.login_in()

    def login_in(self):

        # login page
        self.driver.find_element_by_class_name('TextField').clear()
        self.driver.find_element_by_class_name('TextField').send_keys(loginconstant.user126[0])
        self.driver.find_element_by_class_name('SecureTextField').send_keys(loginconstant.user126[1])

        self.driver.find_elements_by_name('登录')[2].click()
        time.sleep(3)
        #检验登录完成，跳转至了 最新 页
        self.assertTrue(self.driver.find_element_by_name('最新').is_displayed(),'＊＊＊＊126号：登录失败了！！＊＊＊')
        print '＊＊＊＊126号：登录成功！！＊＊＊'


if __name__ == '__main__':
    unittest.main()
