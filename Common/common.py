#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file common

import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#默认登录帐号
up = ['163', 'ynotetestui@163.com', 'abc123']
# 引导页数量
N = 2
i = 1
direction=['up','down','left','right']
#是否需要登录，1是需要去登录，0是不需要走登录
login=0|1

class Common_Util():

    def setup_app(self,login=1):
        app = os.path.abspath(
            '/Users/wujia/Library/Developer/Xcode/DerivedData/YNote-ewvbkrazcxnhicayktmrgqqwzltv/Build/'
            'Products/Debug-iphonesimulator/有道云笔记.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.2',
                'deviceName': 'iPhone 6',
                'automationName': 'XCUITest',
                'autoAcceptAlerts':'true'
            })
        #self.intro_take(N)
        self.comment_take()
        self.login_take(login)
        time.sleep(3)
        return self.driver


    def intro_take(self,N):
         # 处理引导页,滑动，再点 立即体验
         if N == 1:
             pass
         else:
             for i in range(1, N):
                 print "*****引导页处理*******"
                 self.driver.execute_script("mobile:scroll",{"direction":"right"})
                 i = i + 1
         if self.driver.find_elements_by_name('立即体验'):
             self.driver.find_element_by_name('立即体验').click()

    def comment_take(self):
        # 评价弹框 处理
        if self.driver.find_elements_by_name('残忍滴拒绝'):
            print "*******处理评论弹框！************"
            self.driver.find_elements_by_name('残忍滴拒绝')[0].click()
        else:
            print "*******评论弹框 木出现！************"
            pass

    def login_take(self,login):
        # 处理登录问题
        # 判断是否已登录
        # 判断头像处的VIP小图标是否存在，存在表示登录过了
        if self.driver.find_elements_by_name('headernonVip.png'):
            #如果已登录上了
            if login==1:
                pass
                print "******登录过了 ynotetestui@163.com*****"
            else:
                #将登录的号注销掉
                print "******登录过了,去注销帐号！*****"
                self.login_out()

        else:
            #如果没登录
            if login==1:
                print "******重新去登录 ynotetestui@163.com*****"
                self.login_in(up[1], up[2])
            else:
                pass
                print "*******启动后应用是：未登录状态********"


    def login_in(self,user,password):

        # wo de
        self.driver.find_element_by_name('tabbar_my').click()

        self.driver.find_element_by_name('点此登录').click()
        time.sleep(2)

        # login page
        self.driver.find_element_by_class_name('TextField').send_keys(user)
        self.driver.find_element_by_class_name('SecureTextField').send_keys(password)
        self.driver.find_elements_by_name('登录')[2].click()

    def login_out(self):

        # user logo
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)
        #往上滑动
        self.driver.execute_script("mobile:scroll", {"direction": "down"})
        # 退出登录
        self.driver.find_element_by_name('退出登录').click()
        # 确定
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeOther[1]/'
                                          'XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/'
                                          'XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/'
                                          'XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/'
                                          'XCUIElementTypeOther[3]').click()

    #此方法用于在列表上查找文档
    #判断当前页是否存在此文档，若存在，则继续，若不存在，则往下滚一屏
    def exists(self,elename):
        if self.driver.find_element_by_name(elename).is_displayed():
            print '当前页上有此元素，不滚动查找'
            pass
        else:
            # 当前页不存在，则往下滚一屏
            print '当前页上无此元素，先滚动一屏'
            self.driver.execute_script("mobile:scroll",{"direction":"down"})
            time.sleep(2)
            pass










