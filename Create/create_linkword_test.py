#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import unittest

reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.create_constant import Create_Constant

#创建链接笔记

#前提：已登陆
#步骤：
# 1打开应用》点击首页+号》点击 换到第二屏
# 2点击 链接收藏》检验1
# 3输入url》点 确认》检验2
#检验1：弹框出现
#检验2：首页上出现的第一条记录的标题是以 百度 开头的

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



    def test_create_linkword(self):

        print "************  create link word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        # 打开第二屏创建按钮上
        self.driver.find_elements_by_class_name('PageIndicator')[0].click()

        #link笔记
        self.driver.find_element_by_name('链接收藏').click()
        time.sleep(3)

        #检验弹框存在
        self.assertTrue(self.driver.find_element_by_name('链接收藏').is_displayed(),'创建链接收藏的弹框没出现！')

        #输入url
        self.driver.find_element_by_class_name('TextView').send_keys(create_constant.link_url)

        #点 确认
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/'
                                           'XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/'
                                           'XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/'
                                           'XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/'
                                           'XCUIElementTypeOther[3]').click()



        time.sleep(5)

        # 检验生成了一篇笔记在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[3]
        self.assertTrue(first_item.get_attribute('name').startswith(unicode("百度")), '＊＊链接收藏创建case失败！＊＊')

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
