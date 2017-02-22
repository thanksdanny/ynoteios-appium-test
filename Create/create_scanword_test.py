#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util
from Constant.create_constant import Create_Constant

#创建scan文件

#前提：已登陆
#步骤：打开应用》点击首页+号》点击 新建笔记 》点击 文档扫描》
#检验1：当前界面上工具条出现
#检验2：首页上刚创建的md的标题所在的item存在

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



    def test_create_scanword(self):

        print "************  create scan word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        #scan笔记
        self.driver.find_element_by_name('文档扫描').click()
        time.sleep(3)

        #模拟器上没有摄相头的弹框处理
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/'
                                           'XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/'
                                           'XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/'
                                           'XCUIElementTypeOther[1]').click()

        #检验拍摄工具条出现
        self.assertTrue(self.driver.find_element_by_name('scan take photo').is_displayed(),'scan创建失败了！')


        #pic
        self.driver.find_element_by_name('scan upload').click()
        self.driver.find_element_by_name('相机胶卷 (5)').click()
        #choose pic
        self.driver.tap((30,30),10)
        #insert pic
        self.driver.find_elements_by_class_name('Button')[2].click()
        time.sleep(5)

        #finish
        self.driver.find_element_by_name('scan ok').click()

        # 检验生成了一篇scan笔记在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(first_item.get_attribute('name').startswith(create_constant.scan_title), '＊＊文档扫描创建case失败！＊＊')

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
