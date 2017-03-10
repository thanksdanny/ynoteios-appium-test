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


    start_dirs = []
    # collect all list
    for dir in list:
        start_dir = cur_dir + dir
        start_dirs.append(start_dir)

    single_file = 'report.html'
    file_path = cur_dir + '/' + single_file
    fp = open(file_path, 'wb+')
    for sdir in start_dirs:
        # find all case
        suite = unittest.defaultTestLoader.discover(sdir, pattern='*_test.py')
        print ("================running %s=========================" % dir)
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ynoteios appium result',
                                                   description='test result page on chrome')
        htmlrunner.run(suite)

        print "running end !"
        #close appiumserver
        appiumserver.stopServer()







