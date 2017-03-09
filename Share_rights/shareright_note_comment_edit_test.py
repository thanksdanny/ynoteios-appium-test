#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import unittest

from Common.common import Common_Util
from Constant.shareright_constant import Shareright_Constant

#笔记分享为可评论可编辑

#前提：已登陆
#步骤：
#1 打开应用》点击全部》打开分享文件夹》输入阅读密码
#2 打开文件》点分享》检验1
#3 点修改》检验2
#4 设置为可评论编辑》点完成》检验3

#检验1：分享界面显示出来了
#检验2：打开了分享权限设置页
#检验3：评论编辑权限设置成功

common=Common_Util()
shareright_constant=Shareright_Constant()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # set up appium
        self.driver = common.setup_app()

    def tearDown(self):
        self.driver.quit()

    def test_shareright_note_comment_edit(self):
        print "************  share right note comment_edit method ***********"

        #全部
        self.driver.find_element_by_name('全部').click()
        time.sleep(2)
        #打开分享文件夹
        self.driver.find_element_by_name(shareright_constant.notebook_title).click()
        #input password
        self.driver.find_element_by_class_name('SecureTextField').send_keys(shareright_constant.password)
        #open
        self.driver.find_element_by_name('打开').click()
        time.sleep(2)
        #open
        self.driver.find_element_by_name(shareright_constant.note_comment_edit_title).click()
        time.sleep(3)
        #click share button
        self.driver.find_element_by_name('viewModButtonShare').click()
        #检验分享界面显示出来了
        self.assertTrue(self.driver.find_elements_by_name('取消')[0].is_displayed(),'点击分享后，弹框失败！')
        #
        self.driver.find_element_by_name('修改').click()
        time.sleep(2)

        #check 打开了分享权限设置页
        self.assertTrue(self.driver.find_element_by_name('修改权限').is_displayed(),'笔记设置分享权限页打不开！！')

        #edit
        if self.driver.find_elements_by_class_name('Switch')[0].get_attribute('value'):
            # 已勾选过了,需要再点2次
            self.driver.find_elements_by_class_name('Switch')[0].click()
            self.driver.find_elements_by_class_name('Switch')[0].click()
        else:
            # 没有勾选过，只需要点1次
            self.driver.find_elements_by_class_name('Switch')[0].click()


        #comment
        if self.driver.find_elements_by_class_name('Switch')[1].get_attribute('value'):
            #已勾选过了,需要再点2次
            self.driver.find_elements_by_class_name('Switch')[1].click()
            self.driver.find_elements_by_class_name('Switch')[1].click()
        else:
            #没有勾选过，只需要点1次
            self.driver.find_elements_by_class_name('Switch')[1].click()

        #finish
        self.driver.find_element_by_name('完成').click()

        time.sleep(5)

        #check 权限设置成功
        self.assertTrue(self.driver.find_element_by_name('允许编辑，允许评论').is_displayed(),'笔记设置分享可评论可编辑失败！')

if __name__ == '__main__':
    unittest.main()
