#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from Common.common import Common_Util

# 我的帐号页》修改昵称成功

#前提：已登陆
#步骤：
#1 打开应用》点击 头像》打开 我的帐号页
#2 点击昵称》进入编辑昵称页
#3 修改昵称后》返回 我的帐号页》检验

#检验：新昵称存在

nick =('noteUI') + str(int(time.time()))

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test__profile_nick(self):
        print "************ profile nick  method ***********"
        #头像
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)
        #profile,nick
        self.driver.find_element_by_name('昵称').click()
        #open nick edit page
        ele=self.driver.find_element_by_class_name('TextField')
        ele.clear()
        ele.send_keys(nick)

        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        #check 新昵称存在
        self.assertTrue(self.driver.find_element_by_name(nick).is_displayed(),'****我的帐号页：用户昵称修改失败！*****')


if __name__ == '__main__':
    unittest.main()
