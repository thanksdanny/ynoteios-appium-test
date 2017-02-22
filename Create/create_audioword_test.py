#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import unittest

reload(sys)
sys.setdefaultencoding('utf8')
from Common.common import Common_Util

#创建语音速记

#前提：已登陆
#步骤：
# 1打开应用》点击首页+号》点击 语音速记
# 2点击 分段》点击暂停》检验1
# 3点击停止》点击返回》检验2
#检验1：当前界面由录音变为普通，标题变为 语音速记
#检验2：最新列表上第一个item的标题以语音速记开头

common=Common_Util()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_create_audioword(self):
        print "************  create audio word note method ***********"

        # 点新建
        self.driver.find_element_by_name('newNote normal').click()

        self.driver.find_element_by_name('语音速记').click()
        time.sleep(3)
        # zhi zhang try
        if self.driver.find_elements_by_name('取消'):
            self.driver.find_element_by_name('取消').click()
        #pause
        self.driver.find_element_by_name('asr record btn').click()
        #分段
        self.driver.find_element_by_name('分段').click()
        #停止
        self.driver.find_element_by_name('停止').click()
        time.sleep(3)
        #检验标题变为 语音速记 了,表示停止录音了
        self.assertTrue(self.driver.find_element_by_name('语音速记').is_displayed())
        #back
        self.driver.find_element_by_name('navigationBack').click()
        #检验生成了一篇语音速记在列表上
        first_item=self.driver.find_elements_by_class_name('StaticText')[2]
        self.assertTrue(first_item.get_attribute('name').startswith(unicode("语音速记")),'＊＊语音速记创建case失败！＊＊')

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
