import unittest
import os
import HTMLTestRunner
from sendEmailreport import SendEmail
from AppiumServer import appiumServer

#根据需要，运行所有的用例
#用例集目录在  项目》TestCase-note
#遍历下面所有用例，并执行



email=SendEmail()
appiumserver=appiumServer()

class runCase():

    # /~/Documents/code/testing/ynoteios-appium-test

    cur_dir = os.path.abspath(os.curdir)
    print cur_dir
    #collect all case
    suite= unittest.defaultTestLoader.discover(cur_dir+'/TestCase-note', pattern='*_test.py')

    single_file = 'report.html'
    file_path = cur_dir + '/' + single_file
    fp = open(file_path, 'wb+')
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ynoteios appium result',
                                               description='test result page on chrome')


    htmlrunner.run(suite)

    print "running allcase end !"

    appiumServer.stopServer()










