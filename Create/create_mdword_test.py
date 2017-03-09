#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util
from Constant.create_constant import Create_Constant

#创建markdown笔记

#前提：已登陆
#步骤：
# 1打开应用》点击首页+号》点击 新建笔记
# 2点击 markdown》检验1
# 3输入标题》输入内容》预览》返回》检验2
#检验1：当前界面上工具条出现
#检验2：首页上刚创建的md的标题所在的item存在

common=Common_Util()
create_constant=Create_Constant()

class MyTestCase(unittest.TestCase):


    def setUp(self):
        # set up appium
        self.driver=common.setup_app()



    def tearDown(self):
        self.driver.quit()



    def test_create_markdownword(self):

        print "************  create markdown word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        #markdown笔记
        self.driver.find_element_by_name('Markdown').click()
        time.sleep(3)

        #检验工具条出现
        self.assertTrue(self.driver.find_element_by_name('throughLine').is_displayed(),'markdown创建失败了！')


        #article
        self.driver.find_element_by_name('throughLine').click()
        self.driver.find_element_by_class_name('WebView').send_keys('a\n')

        self.driver.find_element_by_name('boldFont').click()
        self.driver.find_element_by_class_name('WebView').send_keys('b\n')


        #self.driver.find_element_by_class_name('insertLink')
        #self.driver.find_element_by_class_name('WebView').send_keys('a')

        self.driver.find_element_by_name('styleH1').click()
        self.driver.find_element_by_class_name('WebView').send_keys('c\n')

        self.driver.find_element_by_name('styleQuote').click()
        self.driver.find_element_by_class_name('WebView').send_keys('d\r')

        self.driver.find_element_by_name('styleList').click()
        self.driver.find_element_by_class_name('WebView').send_keys('e\n')

        self.driver.find_element_by_name('editModButtonHideKeyboard').click()
        self.driver.find_element_by_class_name('WebView').send_keys('f\n')

        # title
        self.driver.find_element_by_class_name('TextField').send_keys(create_constant.markdown_title)


        time.sleep(3)

        #preview
        self.driver.find_element_by_name('预览').click()
        #输入内容存在
        self.assertTrue(self.driver.find_element_by_class_name('StaticText').is_displayed(),'markdown内容保存失败')

        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)

        #检验列表上标题存在 *.md
        self.assertTrue(self.driver.find_element_by_name(create_constant.markdown_title+'.md').is_displayed())

if __name__ == '__main__':
    unittest.main()
