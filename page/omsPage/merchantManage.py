# -*-coding:UTF-8-*-
# __author__ = 'gao'
"""品智客户运维系统->客户管理"""
from base.basePage import *
from selenium.webdriver.common.by import By
import time


class MerchantManage(WebDriver):
    """客户管理页面"""
    merchant_manage_loc = (By.XPATH, '//*[@id="DH"]/li[2]/a')  # 客户管理
    add_loc = (By.ID, 'addBtn')  # 添加按钮
    merchant_loc = (By.ID, 'keywords')  # 商户（查询）
    search_loc = (By.ID, 'btnSearch')  # 查询
    change_loc = (By.NAME, 'btnChg')  # 修改
    del_loc = (By.NAME, 'btnDelete')  # 删除
    synchron_loc = (By.NAME, 'synchronizationData')  # 同步操作
    synbaseinfo_loc = (By.NAME, 'btnSyncBaseinfo')  # 初始化商户库基本信息
    confirmYes_loc = (By.ID, 'btnConfirmYes')  # 您确定重置吗-是
    confirmNo_loc = (By.ID, 'btnConfirmNo')  # 您确定重置吗-否

    """添加商户界面"""
    merchant_name_loc = (By.ID, 'merchantname')  # 商户名称
    address_loc = (By.ID, 'address')  # 地址
    contact_loc = (By.ID, 'contact')  # 联系人
    server_ip_loc = (By.ID, 'servip')  # 服务器IP
    server_user_loc = (By.ID, 'username')  # 服务器用户名
    server_password_loc = (By.ID, 'password')  # 服务器密码
    save_loc = (By.ID, 'btnSave')  # 保存
    """div弹出消息，如保存、删除等成功消息"""
    divMsg_loc = (By.XPATH, '//*[@id="loadingDiv"]')

    """进入商户管理界面"""
    def enter_merchant_manage(self):
        self.findElement(*self.merchant_manage_loc).click()

    """添加商户"""
    def add_merchant(self):
        self.findElement(*self.add_loc).click()
        time.sleep(2)
        self.findElement(*self.merchant_name_loc).send_keys("test_merchant")
        self.findElement(*self.address_loc).send_keys("address")
        self.findElement(*self.contact_loc).send_keys("pinzhi")
        self.findElement(*self.server_ip_loc).send_keys("127.0.0.1")
        self.findElement(*self.server_user_loc).send_keys("pinzhi")
        self.findElement(*self.server_password_loc).send_keys("password")
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """查询商户-根据商户ID/名称"""
    def search_merchantByName(self, merchantName):
        self.findElement(*self.merchant_loc).clear()
        self.findElement(*self.merchant_loc).send_keys(merchantName)
        self.findElement(*self.search_loc).click()
        time.sleep(3)

    """查询商户-根据服务器"""
    def search_merchantByServer(self):
        # value="0" ，选择第一个服务器类型
        js = 'var q=document.getElementsByName("servertype")[0].value="0"'
        self.driver.execute_script(js)
        self.findElement(*self.search_loc).click()
        time.sleep(5)

    """修改-地址"""
    def change_merchant(self):
        self.findElement(*self.change_loc).click()
        self.findElement(*self.address_loc).clear()
        self.findElement(*self.address_loc).send_keys("newAddress")
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """删除"""
    def delete_merchant(self):
        self.findElement(*self.del_loc).click()
        # 确定要删除此项？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """同步操作"""
    def syn_merchant(self):
        self.findElement(*self.synchron_loc).click()
        # 确定要删除此项？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """初始化商户库基本信息"""
    def synbaseinfo_merchant(self):
        self.findElement(*self.synbaseinfo_loc).click()
        # 确定要删除此项？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

