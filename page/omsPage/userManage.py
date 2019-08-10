# -*-coding:UTF-8-*-
# __author__ = 'gao'
from base.basePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class UserManage(WebDriver):
    # 用户管理
    userManage_loc = (By.XPATH, '//*[@id="DH"]/li[1]/a')
    # 运营商用户管理
    operatorUserManage_loc = (By.XPATH, '//*[@id="headingcarrierusers"]/h4/a')
    operatorUserManage2_loc = (By.XPATH, '//*[@id="collapsecarrierusers"]/div/a')

    """品智用户管理界面"""
    username_loc = (By.ID, 'username')  # 用户名（查询）
    authority_loc = (By.ID, 'privilege')  # 权限（查询）
    search_loc = (By.ID, 'btnSearch')  # 查询按钮
    searchResult_loc = (By.CSS_SELECTOR, '#user > tbody > tr > td')  # 查询的结果
    addUser_loc = (By.ID, 'addBtn')  # 添加品智用户+
    reset_loc = (By.NAME, 'btnReset')  # 重置密码
    change_loc = (By.NAME, 'btnChg')  # 修改
    disable_loc = (By.NAME, 'btnDisable')  # 停用
    enable_loc = (By.NAME, 'btnEnable')  # 启用
    delete_loc = (By.NAME, 'btnDelete')  # 删除
    confirmYes_loc = (By.ID, 'btnConfirmYes')  # 您确定重置吗-是
    confirmNo_loc = (By.ID, 'btnConfirmNo')  # 您确定重置吗-否
    """div弹出消息，如保存、删除等成功消息"""
    divMsg_loc = (By.XPATH, '//*[@id="loadingDiv"]')
    state_loc = (By.XPATH, '//*[@id="user"]/tbody/tr/td[5]')  # 用户状态

    """获取用户表格中状态"""
    def get_state(self):
        state = self.findElement(*self.state_loc).text
        return state

    """选择要查询的权限，下拉框"""
    def selectAuthority(self, authority):
        self.select_element = self.findElement(*self.authority_loc)
        self.select = Select(self.select_element)
        self.select.select_by_visible_text(authority)

    """重置密码"""
    def reset_password(self):
        self.findElement(*self.reset_loc).click()
        time.sleep(2)
        # 确定要重置密码？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(6)
        return msg

    """重置密码-否"""
    def reset_password_no(self):
        self.findElement(*self.reset_loc).click()
        time.sleep(2)
        # 确定要重置密码？弹框点否
        self.findElement(*self.confirmNo_loc).click()

    """修改用户信息"""
    def change_user(self, userName):
        self.findElement(*self.change_loc).click()
        time.sleep(2)
        self.findElement(*self.userName_loc).clear()  # 先清空用户名
        self.findElement(*self.userName_loc).send_keys(userName)
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """修改用户信息-放弃"""
    def change_user_abandon(self, userName):
        self.findElement(*self.change_loc).click()
        time.sleep(2)
        self.findElement(*self.userName_loc).clear()  # 先清空用户名
        self.findElement(*self.userName_loc).send_keys(userName)
        self.findElement(*self.abandon_loc).click()

    """停用"""
    def disable_user(self):
        self.findElement(*self.disable_loc).click()
        # 您确定停用吗？-是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(6)
        return msg

    """停用-否"""
    def disable_user_no(self):
        self.findElement(*self.disable_loc).click()
        # 您确定停用吗？-否
        self.findElement(*self.confirmNo_loc).click()

    """启用用户"""
    def enable_user(self):
        self.findElement(*self.enable_loc).click()
        # 确定要启用此项?-是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(6)
        return msg

    """启用用户-否"""
    def enable_user_no(self):
        self.findElement(*self.enable_loc).click()
        # 确定要启用此项?-否
        self.findElement(*self.confirmNo_loc).click()

    """删除用户"""
    def delete_user(self):
        self.findElement(*self.delete_loc).click()
        # 确定要删除此项？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """按用户名查询search_user"""
    def search_by_username(self, username):
        self.findElement(*self.username_loc).send_keys(username)
        self.findElement(*self.search_loc).click()
        time.sleep(3)
        rel = self.findElement(*self.searchResult_loc).text
        self.findElement(*self.username_loc).clear()
        return rel

    # """查询用户名+权限功能"""
    # def searchUser(self, username, authority):
    #     self.findElement(*self.username_loc).send_keys(username)
    #     self.selectAuthority(authority)
    #     self.findElement(*self.search_loc).click()
    #     rel = self.findElement(*self.searchResult_loc).text
    #     return rel

    """添加品智用户界面"""
    userNumber_loc = (By.ID, 'epno')  # 输入工号
    userName_loc = (By.ID, 'epname')  # 输入用户名
    userEmail_loc = (By.ID, 'epmail')  # 邮箱
    selectAuth_loc = (By.XPATH, '//*[@id="_easyui_tree_1"]/span[3]')  #全部权限
    save_loc = (By.ID, 'btnSave')  # 保存按钮
    abandon_loc = (By.ID, 'btnBack')  # 放弃按钮

    """添加用户"""
    def addUser(self, userNumber='123456', userName='autoTest'):
        self.findElement(*self.addUser_loc).click()
        time.sleep(2)
        self.findElement(*self.userNumber_loc).send_keys(userNumber)
        self.findElement(*self.userName_loc).send_keys(userName)
        self.findElement(*self.selectAuth_loc).click()
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """添加运营商用户界面"""
    selectOperator1_loc = (By.XPATH, '//*[@id="userForm"]/div[1]/div/div/button/span')  #选择运营商span
    selectOperator2_loc = (By.XPATH, '//*[@id="operatorid"]')  # 选择运营商select
    selectbyindex1_loc = (By.XPATH, '//*[@id="userForm"]/div[1]/div/div/div/ul/li[1]/label/span')

    """进入运营商用户管理界面"""
    def enter_opertor(self):
        self.findElement(*self.userManage_loc).click()
        time.sleep(1)
        self.findElement(*self.operatorUserManage_loc).click()
        time.sleep(1)
        self.findElement(*self.operatorUserManage2_loc).click()
        time.sleep(1)

    """添加运营商"""
    def add_operator(self, user_no, user_name):
        self.findElement(*self.addUser_loc).click()
        time.sleep(2)
        self.findElement(*self.selectOperator1_loc).click()
        time.sleep(2)
        # 选择第一个运营商
        self.findElement(*self.selectbyindex1_loc).click()
        time.sleep(3)

        # select方式此处不可用提示Element is not currently visible and may not be manipulated
        # select_element = self.findElement(*self.selectOperator2_loc)
        # time.sleep(1)
        # select = Select(select_element)
        # # select.select_by_visible_text(operator)  # 根据运营商名称选择
        # select.select_by_index(0)
        self.findElement(*self.userNumber_loc).send_keys(user_no)
        time.sleep(2)
        self.findElement(*self.userName_loc).send_keys(user_name)
        time.sleep(2)
        self.findElement(*self.selectAuth_loc).click()
        time.sleep(2)
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg












