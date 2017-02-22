#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest
from Common.common import Common_Util

#创建 上传图片

#前提：已登陆
#步骤：
#1 打开应用》点击首页+号》点击 换到第二屏
#2 点击 上传图片》检验1
#3打开相册列表》选图》点 发送》检验2
#检验1：打开了系统相册
#检验2：首页列表上第一条数据的标题中包含.jpg

common=Common_Util()

class MyTestCase(unittest.TestCase):


    def setUp(self):
        # set up appium
        self.driver=common.setup_app()
        time.sleep(3)



    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



    def test_create_uploadpicword(self):

        print "************  create uploadpic word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        # 打开第二屏创建按钮上
        self.driver.find_elements_by_class_name('PageIndicator')[0].click()

        #上传图片
        self.driver.find_element_by_name('上传图片').click()
        time.sleep(2)

        #检验打开了系统相册
        self.assertTrue(self.driver.find_element_by_name('相册').is_displayed(),'上传图片时没有打开系统相册界面！')
        #打开相册
        self.driver.find_element_by_name('相机胶卷 (5)').click()

        #选图
        x1 = int(self.driver.get_window_size()['width'] * 0.13)
        y1 = int(self.driver.get_window_size()['height'] * 0.15)
        x2 = int(self.driver.get_window_size()['width'] * 0.26)
        self.driver.tap([(x1,y1),(x2,y1)],100)
        time.sleep(5)

        #点 发送
        self.driver.find_element_by_name('发送').click()
        time.sleep(2)

        # 检验生成了一个图片在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(('.jpg' in first_item.get_attribute('name')), '＊＊上传图片case失败！＊＊')

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
