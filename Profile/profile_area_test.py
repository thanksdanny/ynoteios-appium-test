#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
import time
import random

from Common.common import Common_Util

# 我的帐号页》修改地区成功

#前提：已登陆
#步骤：
#1 打开应用》点击 头像》打开 我的帐号页
#2 点击地区》进入编辑地区页
#3 修改地区后》返回 我的帐号页》检验

#检验：新地区存在

citylist=['北京','上海','天津','重庆','浙江','广东','江苏','山东','福建']

common=Common_Util()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test__profile_cityarea(self):
        print "************ profile cityarea  method ***********"
        #头像
        self.driver.find_element_by_class_name('Image').click()
        time.sleep(2)
        #profile,area
        self.driver.find_element_by_name('地区').click()
        #open area edit page
        #city
        city=random.choice(citylist)
        self.driver.find_element_by_name(city).click()
        #area
        index=random.randint(1,3)
        ele=self.driver.find_elements_by_class_name('StaticText')[index]
        area=ele.get_attribute('value')
        self.ele.click()
        time.sleep(2)
        #back
        #check 帐号页上 新地区存在
        cityarea=city+''+area
        self.assertTrue(self.driver.find_element_by_name(cityarea).is_displayed(),'****我的帐号页：修改地区失败！*****')


if __name__ == '__main__':
    unittest.main()
