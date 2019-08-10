# -*- coding:UTF-8 -*-
from selenium import webdriver
import unittest
from page.omsPage.login import *
"""测试固件分离"""

class Init(unittest.TestCase, ReadXML):
    """setUpClass()/tearDownClass() 测试固件同一个类中不用每个用例都执行"""
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        cls.driver = webdriver.Chrome(options=option)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get(cls.getXMLDataCls('omsurl'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
