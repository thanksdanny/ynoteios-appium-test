import unittest
import os
import HTMLTestRunner
from sendEmailreport import SendEmail
from AppiumServer import appiumServer

email=SendEmail()
appiumserver=appiumServer()

class runCase():

    # /Users/wujia/Documents/code/testing/ynoteios-appium-test

    cur_dir = os.path.abspath(os.curdir)
    #collect all case
    suite= unittest.defaultTestLoader.discover(cur_dir+'/TestCase-note', pattern='*_test.py')

    single_file = 'report.html'
    file_path = cur_dir + '/' + single_file
    fp = open(file_path, 'wb+')
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ynoteios appium result',
                                               description='test result page on chrome')


    htmlrunner.run(suite)

    print "running allcase end !"










