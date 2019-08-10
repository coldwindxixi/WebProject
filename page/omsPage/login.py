# -*-coding:UTF-8-*-
# __author__ = 'gao'
from base.basePage import *
from selenium.webdriver.common.by import By
from utils.readXML import *


class Login(WebDriver, ReadXML):
    """请输入用户名属性"""
    username_loc = (By.ID, 'username')
    """请输入密码属性"""
    pwd_loc = (By.ID, 'password')
    """登录按钮属性"""
    btnLogin_loc = (By.ID, 'btnLogin')
    """用户名密码错误提示控件属性"""
    loginMSG_loc = (By.CLASS_NAME, 'loginMSG')
    """用户名为空属性"""
    usernameNull_loc = (By.ID, 'username-error')
    """密码为空属性"""
    pwdNull_loc = (By.ID, 'password-error')
    """记住登录用户"""
    remember_loc = (By.ID, 'rememberMe')
    """退出"""
    logOut_loc = (By.ID, 'logout')

    """输入用户名"""
    def typeUsername(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    """输入密码"""
    def typePassword(self, pwd):
        self.findElement(*self.pwd_loc).send_keys(pwd)

    """清空用户名密码"""
    def clearLogin(self):
        self.findElement(*self.username_loc).clear()
        self.findElement(*self.pwd_loc).clear()

    """勾选记住登录用户"""
    def check_remember(self):
        self.findElement(*self.remember_loc).click()

    "点击登录"
    @property
    def clickLogin(self):
        self.findElement(*self.btnLogin_loc).click()

    """退出"""
    @property
    def logout(self):
        self.findElement(*self.logOut_loc).click()

    """获取登录报错信息"""
    def getLoginMSG(self):
        return(self.findElement(*self.loginMSG_loc).text)

    """获取用户名为空提示信息"""
    def getUsernameNullMsg(self):
        return (self.findElement(*self.usernameNull_loc).text)

    """获取密码为空提示信息"""
    def getPasswordNullMsg(self):
        return (self.findElement(*self.pwdNull_loc).text)

    """登录业务"""
    def login(self, username='', pwd=''):
        self.typeUsername(username)
        self.typePassword(pwd)
        self.clickLogin

    """登录并勾选记住登录用户"""
    def login_remember(self, username, pwd):
        self.typeUsername(username)
        self.typePassword(pwd)
        self.check_remember()
        self.clickLogin
