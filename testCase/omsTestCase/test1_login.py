# -*-coding:UTF-8-*-
# __author__ = 'gao'
from page.omsPage.login import *
from page.omsPage.init import *
import time


class TestLogin(Init, Login):
    """登录相关的测试用例"""
    """用例：登录成功。输入xml文件中用户名密码登录成功"""
    def test1_login_success(self):
        self.username = self.getXMLData('omsUsername')
        self.pwd = self.getXMLData('omsPwd')
        self.login(self.username, self.pwd)
        time.sleep(3)
        self.exceptUrl = self.getXMLData('omsAfterLoginUrl')
        self.assertEqual(self.driver.current_url, self.exceptUrl, '登录后url断言失败!')
        self.logout
        time.sleep(2)

    """用例：输入错误的用户名密码"""
    def test2_login_wrong_both(self):
        self.login('notExist', 'notExist')
        time.sleep(2)
        self.loginMSG = self.getLoginMSG()
        self.assertEqual("用户名或密码错误!", self.loginMSG, '用户名或密码错误提示断言失败！')
        self.clearLogin()
        time.sleep(2)

    """用例：输入错误的用户名"""
    def test3_login_wrong_username(self):
        self.login('notExist', '123456')
        time.sleep(2)
        self.loginMSG = self.getLoginMSG()
        self.assertEqual("用户名或密码错误!", self.loginMSG, '用户名错误提示断言失败！')
        self.clearLogin()
        time.sleep(2)

    """用例：输入错误的密码"""
    def test4_login_wrong_pwd(self):
        self.login('admin', 'notExist')
        time.sleep(2)
        self.loginMSG = self.getLoginMSG()
        self.assertEqual("用户名或密码错误!", self.loginMSG, "密码错误提示断言失败")
        self.clearLogin()
        time.sleep(2)

    """用例：用户名密码输入为空"""
    def test5_login_null_both(self):
        self.login('', '')
        time.sleep(2)
        self.loginMsg1 = self.getUsernameNullMsg()
        self.loginMsg2 = self.getPasswordNullMsg()
        self.assertEqual("必填", self.loginMsg1, "全部为空时用户名为空断言失败")
        self.assertEqual("必填", self.loginMsg2, "全部为空时密码为空断言失败")

    """用例：用户名输入为空"""
    def test6_login_null_username(self):
        self.login('', '123')
        time.sleep(2)
        self.loginMsg = self.getUsernameNullMsg()
        self.assertEqual("必填", self.loginMsg, "用户名为空断言失败")
        self.clearLogin()
        time.sleep(2)

    """用例：密码输入为空"""
    def test7_login_null_pwd(self):
        self.login('admin', '')
        time.sleep(2)
        self.loginMsg = self.getPasswordNullMsg()
        self.assertEqual("必填", self.loginMsg, "密码为空断言失败")
        self.clearLogin()
        time.sleep(2)

    """用例：勾选记住登录用户并登录成功"""
    def test8_login_remember(self):
        self.username = self.getXMLData('omsUsername')
        self.pwd = self.getXMLData('omsPwd')
        self.login_remember(self.username, self.pwd)
        time.sleep(3)
        self.exceptUrl = self.getXMLData('omsAfterLoginUrl')
        self.assertEqual(self.driver.current_url, self.exceptUrl, '勾选记住用户登录后url断言失败!')
        self.logout
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
