#!/usr/bin/env python3
# coding=utf-8

#from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

import smtplib
import unittest
import time
import os


# =============发送邮件===================================
def sendReport(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = '*****@126.com'  # 发件地址
    msg['To'] = '*******@126.com;******@126.com'  # 收件人地址，多人以分号分隔

    smtp = smtplib.SMTP('smtp.126.com')
    smtp.set_debuglevel(1)
    smtp.login('username', 'password')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out!')


# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = 'E:\\workspace\\PythonLearn1\\autoTests'  # 测试用例所在目录
    test_report = 'E:\\workspace\\PythonLearn1\\report'  # 测试报告所在目录

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_baidu*.py')

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    filename = test_report + '\\' + now + 'result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()  # 这边曾错写成fp.close，导致发送邮件时正文怎么都发不出来

    new_report = newReport(test_report)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告

##################################test_baidu.py#####################
# !/usr/bin/env python3
# coding=utf-8

from selenium import webdriver
import unittest


class Baidu(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = 'https://www.baidu.com'

    def test_baidu_search(self):
        '''搜索关键字'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('HTML')
        driver.find_element_by_id('su').click()
        driver.quit()

    def tearDown(self):
        self.driver.quit()