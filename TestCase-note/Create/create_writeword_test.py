#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import unittest

reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util
from Constant.create_constant import Create_Constant

#创建手写笔记

#前提：已登陆
#步骤：
# 1打开应用》点击首页+号》点击 换到第二屏
# 2点击 手写笔记》检验1
# 3输入5次手写内容》输入标题
# 4点 完成》点返回》检验2
#检验1：检验手写输入界面出现
#检验2：首页上出现的第一条记录的标题是以 手写 开头的

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



    def test_create_writeword(self):

        print "************  create write word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        # 打开第二屏创建按钮上
        self.driver.find_elements_by_class_name('PageIndicator')[0].click()

        #手写笔记
        self.driver.find_elements_by_class_name('Button')[2].click()
        time.sleep(3)

        #检验手写输入界面出现
        self.assertTrue(self.driver.find_element_by_name('handWriteMizige').is_displayed())
        #input
        x1 = int(self.driver.get_window_size()['width'] * 0.25)
        y1 = int(self.driver.get_window_size()['height'] * 0.75)
        x2 = int(self.driver.get_window_size()['width'] * 0.75)
        i=1
        for i in range(1,6):
            self.driver.swipe(x1, y1, x2, y1, 100)
            i=i+1

        time.sleep(2)
        #title
        self.driver.find_element_by_class_name('TextField').send_keys(create_constant.write_title)
        #finish
        self.driver.find_element_by_name('完成').click()
        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)
        # 检验生成了一篇手写笔记在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(first_item.get_attribute('name').startswith(create_constant.write_title), '＊＊手写笔记创建case失败！＊＊')

if __name__ == '__main__':
    unittest.main()
