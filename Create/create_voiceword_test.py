#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import unittest

from Common.common import Common_Util

#创建录音笔记

#前提：已登陆
#步骤：
#1 打开应用》点击首页+号》点击 新建笔记
#2 点击 滑到第二屏》点击录音笔记》检验1
#3 点击停止录音》检验2，3
#4 点击返回》检验4

#检验1：录音按扭显示，正在录音
#检验2：当前标题为 录音笔记
#检验3：录音按扭消失
#检验4：首页列表上，最新一条笔记的标题是以 录音笔记开头的

common=Common_Util()

class MyTestCase(unittest.TestCase):


    def setUp(self):
        # set up appium
        self.driver=common.setup_app()
        time.sleep(3)



    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



    def test_create_voiceword(self):

        print "************  create voice word note method ***********"

        #点新建
        self.driver.find_element_by_name('newNote normal').click()

        #打开第二屏创建按钮上
        self.driver.find_elements_by_class_name('PageIndicator')[0].click()

        #录音笔记
        self.driver.find_elements_by_class_name('Button')[3].click()
        time.sleep(3)
        #检验录音按扭存在，表示正在录音
        self.assertTrue(self.driver.find_element_by_name('RecordPause').is_displayed(),'创建录音笔记失败，没有在录音！！')

        #点 停止录音
        self.driver.find_element_by_name('RecordStop').click()
        self.driver.hide_keyboard()

        #检验标题存在
        self.assertTrue(self.driver.find_element_by_name('录音笔记').is_displayed(),'创建录音笔记失败！')
        #检验录音按扭消失
        self.assertFalse(self.driver.find_elements_by_name('RecordPause'),'创建录音笔记失败！')

        #back
        self.driver.find_element_by_name('返回').click()
        time.sleep(2)

        # 检验生成了一篇录音笔记在列表上
        first_item = self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(first_item.get_attribute('name').startswith(unicode("录音笔记")), '＊＊录音笔记创建case失败！＊＊')

if __name__ == '__main__':
    unittest.main()
