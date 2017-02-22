#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util
from Constant.create_constant import Create_Constant

#创建英文笔记

#前提：已登陆
#步骤：
# 1打开应用》点击首页+号》点击 新建笔记
# 2输入标题》输入英文内容
# 3点 完成 》点返回
#检验：首页列表上刚创建的笔记标题 存在

common=Common_Util()
create_constant=Create_Constant()

class MyTestCase(unittest.TestCase):


    def setUp(self):
        # set up appium
        self.driver=common.setup_app()
        time.sleep(3)



    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



    def test_create_noteword(self):

        print "************  create english word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        self.driver.find_element_by_name('新建笔记').click()
        time.sleep(3)
        # zhi zhang try
        if  self.driver.find_elements_by_name('取消'):
            self.driver.find_element_by_name('取消').click()

        # title
        self.driver.find_element_by_class_name('TextField').send_keys(create_constant.english_title)
        # article
        self.driver.find_element_by_class_name('TextView').send_keys(create_constant.english_article)
        #finish
        self.driver.find_element_by_name('完成').click()
        # back
        self.driver.find_element_by_name('返回').click()

        time.sleep(10)

        # 检验生成了一篇英文笔记在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(first_item.get_attribute('name').startswith(create_constant.english_title), '＊＊英文笔记创建case失败！＊＊')

        time.sleep(3)
        #检验数据库中状态，sqlite3



if __name__ == '__main__':
    unittest.main()
