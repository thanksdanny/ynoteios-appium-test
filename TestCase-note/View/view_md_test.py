#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.View_constant import ViewConstant

#查看md内容

#前提：已登陆
#步骤：
#1 打开应用》点击全部》打开文件夹》输入阅读密码》打开
#2 检查当前页是否存在此文档，若存在，打开md》检验
#3 若不存在，往下滚一屏 再打开md》检验

#检验：检验md显示出来了

common=Common_Util()
viewconstant=ViewConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_view_md(self):
        print "************  view md method ***********"

        #全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #打开分享文件夹
        self.driver.find_element_by_name(viewconstant.notebook_title).click()
        #input password
        self.driver.find_element_by_class_name('SecureTextField').send_keys(viewconstant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(1)

        #判断当前是否存在此文档
        common.exists(viewconstant.md_title)
        #open md
        self.driver.find_element_by_name(viewconstant.md_title).click()
        time.sleep(2)
        #check 第一行内容为 markdonw 文章
        self.assertTrue(self.driver.find_element_by_name('markdonw 文章').is_displayed(),'查看md内容失败！！')

if __name__ == '__main__':
    unittest.main()
