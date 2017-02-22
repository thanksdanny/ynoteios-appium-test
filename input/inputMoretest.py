#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest
import os
import time
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath(
            '/Users/wujia/Library/Developer/Xcode/DerivedData/YNote-ewvbkrazcxnhicayktmrgqqwzltv/Build/'
            'Products/Debug-iphonesimulator/有道云笔记.app')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.4',
                'deviceName': 'iPhone 5s',
                'automationName': 'XCUITest'
            })

        # self.driver.implicitly_wait(30)
        time.sleep(5)

    def tearDown(self):
        # 退出登陆todo
        self._login_out()
        time.sleep(3)
        self.driver.quit()

    def _login_out(self):
        time.sleep(5)
        # 点 用户头像
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAImage[2]').click()
        # 我的帐号页，点 退出登陆
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[2]').click()
        # 处理弹框，点 确认
        a = self.driver.switch_to_alert()
        a.accept()

    def _login_page(self):

        username = 'ynotetestui@163.com'
        password = 'abc123'

        usern = self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]')

        passw = self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASecureTextField[1]")

        login = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[2]")

        usern.clear()

        usern.send_keys(username)

        passw.send_keys(password)

        login.click()

        time.sleep(3)

        self.assertFalse(login.is_displayed(), "******login fail!*******")

    def _input_more(self):

        print "************  input method ***********"
        #点新建
        #newcreate = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        newcreate = self.driver.find_element_by_name('newNote\000normal')
        newcreate.click()
        # input
        str='abcdefghijklmnopqrstuvwxyz   abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz'
        inputview = self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]')
        for i in range(20):
            inputview.clear()
            inputview.send_keys(str)

            self.driver.find_element_by_name("unsort icon 0").click()
            self.driver.find_element_by_name("sort icon 0").click()
            self.driver.find_element_by_name("leftIndent icon 0").click()
            self.driver.find_element_by_name("rightIndent icon 0").click()
            self.driver.find_element_by_name("word icon 0").click()

            #标题
            title=self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]/UIATextField[1]")
            title.clear()
            title.send_keys("testing")

            print i
        #点 返回，生成笔记
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        return 0

    def test_inputmore(self):
        time.sleep(3)
        # 判断是否为首次使用应用，若打开应用直接跳到登录页，则直接 login,根据当前页面上是否包含 登录按扭来判断
        if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[2]'):
            self._login_page()
            print " ******非新安装的应用：login sucessful!"
            time.sleep(5)
            self._input_more()
        # 若当前打开不是登录页，则依次点 我的》登录，再进行login
        else:
            self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[5]').click()
            self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click()
            self._login_page()
            print "******新安装的应用：login sucessful!"
            time.sleep(5)
            self._input_more()


if __name__ == '__main__':
    unittest.main()
