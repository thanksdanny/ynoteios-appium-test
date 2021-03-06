#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.share_constant import ShareConstant

#分享新笔记

#前提：已登陆
#步骤：
#1 打开应用》点击全部
#2 打开分享文件夹》输入阅读密码》打开
#3 打开新笔记》点击分享按扭》检验1
#4 点击复制分享链接》检验2

#检验1：分享界面显示出来了
#检验2：分享成功提示出现

common=Common_Util()
share_constant=ShareConstant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_share_newnote(self):
        print "************ share new note method ***********"

        #全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #打开分享文件夹
        self.driver.find_element_by_name(share_constant.notebook_title).click()
        #input password
        self.driver.find_element_by_class_name('SecureTextField').send_keys(share_constant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(2)
        #判断当前页上有此文档
        common.exists(share_constant.newnote_title)
        #open note
        self.driver.find_element_by_name(share_constant.newnote_title).click()
        time.sleep(2)
        #click share button
        self.driver.find_element_by_name('viewModButtonShare').click()
        #检验分享界面显示出来了
        self.assertTrue(self.driver.find_elements_by_name('取消')[0].is_displayed(),'点击分享后，弹框失败！')
        #点击 获取分享链接
        self.driver.find_element_by_name('copyShareLink').click()
        time.sleep(5)
        #检验 分享成功提示出现
        self.assertTrue(self.driver.find_elements_by_name('链接复制成功')[0].is_displayed(),'分享新笔记失败！')



if __name__ == '__main__':
    unittest.main()
