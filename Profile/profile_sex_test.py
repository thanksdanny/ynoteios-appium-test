#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time
import random

from Common.common import Common_Util

# 我的帐号页》修改性别成功

#前提：已登陆
#步骤：
#1 打开应用》点击 头像》打开 我的帐号页
#2 点击性别》进入编辑性别页
#3 修改性别后》返回 我的帐号页》检验

#检验：旧性别不存在


common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test__profile_sex(self):
        print "************ profile sex  method ***********"

        #头像
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)

        #根据当前性别来更换为另一性别

        ele=self.driver.find_element_by_name('性别')

        if self.driver.find_elements_by_name('女'):
            print "!!!!!!女！！！！！！"
            currentsex = '女'
            # 选个男
            ele.click()
            time.sleep(1)
            self.driver.find_element_by_name('男').click()

        elif self.driver.find_elements_by_name('男'):
            print "!!!!!!男！！！！！！"
            currentsex='男'
            #选个女
            ele.click()
            time.sleep(1)
            self.driver.find_element_by_name('女').click()
        else:

            currentsex='未设置'
            #随机选一个性别
            ele.click()
            time.sleep(2)
            sex=random.choice(['男','女'])
            self.driver.find_element_by_name(sex)

        # back
        time.sleep(2)
        #check 旧性别不存在
        self.assertFalse(self.driver.find_elements_by_name(currentsex),'****我的帐号页：用户性别修改失败！*****')


if __name__ == '__main__':
    unittest.main()
