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
    #get caselist
    list=[]
    file=open(cur_dir+'/caseList.txt')

    for data in file:
        sdata=str(data).strip()
        if sdata != '' and not sdata.startswith("#"):
            list.append(sdata)

            # find all case
    sdir=cur_dir+'/TestCase-note'+list[0]
    suite = unittest.defaultTestLoader.discover(sdir, pattern='*_test.py')
    print ("================running %s=========================" % sdir)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    single_file = 'report.html'
    file_path = cur_dir + '/' + single_file
    fp = open(file_path, 'wb+')
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ynoteios appium result',
                                                   description='test result page on chrome')
    htmlrunner.run(suite)

    print "running end !"
    # close appiumserver
    appiumserver.stopServer()










