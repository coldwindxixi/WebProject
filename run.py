#new line
#new line
#new line
# -*- coding:UTF-8 -*-
import os
import time
import unittest
import HTMLTestRunner


def get_suite():
    """获取要执行的测试用例"""
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), 'testCase/omsTestCase'),
        pattern='test1_login.py',
        top_level_dir=None
    )
    return suite


def get_current_time():
    """获取当前时间"""
    return time.strftime("%Y-%m-%d %H_%M_%S")


def run():
    filename = os.path.join(os.path.dirname(__file__), 'report', get_current_time()+'_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="UI自动化测试报告",
        description="详细描述"
    )
    runner.run(get_suite())


if __name__ == '__main__':
    run()



