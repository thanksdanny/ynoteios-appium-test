import unittest
import os
import HTMLTestRunner
from sendEmailreport import SendEmail

email=SendEmail()

class runCase():
    # /Users/wujia/Documents/code/testing/ynoteios-appium-test

    cur_dir = os.path.abspath(os.curdir)
    #get caselist
    list=[]
    file=open(cur_dir+'/caseList.txt')

    for data in file:
        sdata=str(data).strip()
        if sdata != ' ' and not sdata.startswith("#"):
            list.append(sdata)

    testcase_dir_list = list
    start_dirs = []
    # collect all testcase dir
    for dir in testcase_dir_list:
        start_dir = cur_dir + dir
        start_dirs.append(start_dir)
        print start_dirs

    for sdir in start_dirs:
        # find all case
        suite = unittest.defaultTestLoader.discover(sdir, pattern='*_test.py')
        print ("================running %s=========================" % dir)
        # runner = unittest.TextTestRunner()
        # runner.run(suite)

        single_file = 'report.html'
        file_path = cur_dir + '/' + single_file
        print file_path
        fp = open(file_path, 'wb+')
        htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ynoteios appium result',
                                                   description='test result page on chrome')
        htmlrunner.run(suite)
        email.sendReportmail(file_path)




