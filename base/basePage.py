# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        """单个定位元素的方法"""
        try:
            element = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*loc))
            return element
        except NoSuchElementException as e:
            print("Error Details {0}".format(e.args[0]))

    def findElements(self, *loc):
        """多个定位元素的方法"""
        try:
            element = WebDriverWait(self.driver, 20).util(lambda x: x.find_elements(*loc))
            return element
        except NoSuchElementException as e:
            print("Error Details {0}".format(e.args[0]))

