#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Common.common import Common_Util

# 我的帐号页》修改个人简介成功

#前提：已登陆(非会员)
#步骤：
#1 打开应用》点击 头像》打开 我的帐号页
#2 点击 个人简介》打开个人简介页
#3 修改简介》返回》检验

#检验：新简介内容存在

localtime = time.strftime('%Y-%M-%d %H-%M-%S', time.localtime())
resume = unicode('新个人简介') + localtime

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test__profile_resume(self):
        print "************ profile resume  method ***********"
        #头像
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)
        #profile,vip
        self.driver.find_element_by_name('个人简介').click()
        time.sleep(2)
        #open resume page
        ele=self.driver.find_element_by_class_name('TextView')
        ele.clear()
        ele.send_keys(resume)
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        #check  新简介存在
        self.assertTrue(self.driver.find_element_by_name(resume).is_displayed(),'****我的帐号页:修改个人简介失败！*****')


if __name__ == '__main__':
    unittest.main()
