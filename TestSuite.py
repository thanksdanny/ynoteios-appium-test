import unittest
import os
class testSuite():
    #/Users/wujia/Documents/code/testing/ynoteios-appium-test
    #start_dir=os.path.abspath(os.curdir)

    testcase_dir_list=['/Create','/EditorTool','/Login','/Mine','/NoteHandle','/Profile','/Share','/Share_rights','/View']
    suites=[]
    cur_dir=os.path.abspath(os.curdir)

    for dir in testcase_dir_list:

        start_dir=cur_dir + dir
        #找到所有case
        suite = unittest.defaultTestLoader.discover(start_dir, pattern='*_test.py')
        suites.append(suite)


    runner=unittest.TextTestRunner()
    runner.run(suites)

