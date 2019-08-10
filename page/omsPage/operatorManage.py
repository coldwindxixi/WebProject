# -*-coding:UTF-8-*-
# __author__ = 'gao'
# 品智客户运维系统-运营商管理
from selenium import webdriver
from base.basePage import *
from selenium.webdriver.common.by import *
from selenium.webdriver.support.select import Select
import time
import execjs

class OperatorManage(WebDriver):
    """运营商管理页面"""
    operatorManage_loc = (By.XPATH, '//*[@id="DH"]/li[2]/a')  # 运营商管理
    addOperator_loc = (By.ID, 'addBtn')  # 添加+
    search_loc = (By.ID, 'btnSearch')  # 查询
    change_loc = (By.NAME, 'btnChg')  # 修改
    disable_loc = (By.NAME, 'btnDisable')  # 停用
    delete_loc = (By.NAME, 'btnDelete')  # 删除
    confirmYes_loc = (By.ID, 'btnConfirmYes')  # 您确定重置吗-是
    confirmNo_loc = (By.ID, 'btnConfirmNo')  # 您确定重置吗-否

    """添加运营商界面"""
    operatorName_loc = (By.ID, 'operatorname')  # 运营商名称
    taxno_loc = (By.ID, 'taxno')  # 税号
    address_loc = (By.ID, 'address')  # 地址
    contact1_loc = (By.ID, 'contact1')  # 联系人一
    phone1_loc = (By.ID, 'phone1')  # 电话
    save_loc = (By.ID, 'btnSave')  # 保存
    """div弹出消息，如保存、删除等成功消息"""
    divMsg_loc = (By.XPATH, '//*[@id="loadingDiv"]')

    """进入运营商管理"""
    def enter_operatorManage(self):
        self.findElement(*self.operatorManage_loc).click()
        time.sleep(1)

    """添加运营商"""
    def add_operator(self):
        # + 号添加
        self.findElement(*self.addOperator_loc).click()
        time.sleep(3)
        # 修改input属性， 选择省市
        js2 = "var q=document.getElementsByName('province')[0].value='北京市'"
        js3 = "var q=document.getElementsByName('city')[0].value='北京市'"
        self.driver.execute_script(js2)
        time.sleep(2)
        self.driver.execute_script(js3)
        time.sleep(2)
        # 运营商名称
        self.findElement(*self.operatorName_loc).send_keys("test_operator")
        # 税号
        self.findElement(*self.taxno_loc).send_keys("999999")
        # 地址
        self.findElement(*self.address_loc).send_keys("address")
        # 联系人一
        self.findElement(*self.contact1_loc).send_keys("高高")
        # 电话
        self.findElement(*self.phone1_loc).send_keys("15088889999")
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """查询运营商"""
    def search_by_cityAndOperator(self):
        # 修改input的value的值
        js2 = "var q=document.getElementsByName('city')[0].value='北京市'"
        js3 = "var q=document.getElementsByName('operatorname')[0].value='test_operator'"
        self.driver.execute_script(js2)
        time.sleep(3)
        self.driver.execute_script(js3)
        time.sleep(3)
        # 点击查询按钮
        self.findElement(*self.search_loc).click()
        time.sleep(5)

    """修改用户信息"""
    def change_user(self, address):
        self.findElement(*self.change_loc).click()  # 修改按钮
        time.sleep(2)
        # 修改input属性， 省市保留(历史bug)
        js2 = "var q=document.getElementsByName('province')[0].value='北京市'"
        js3 = "var q=document.getElementsByName('city')[0].value='北京市'"
        self.driver.execute_script(js2)
        time.sleep(2)
        self.driver.execute_script(js3)
        time.sleep(2)
        # 修改运营商名称
        self.findElement(*self.address_loc).clear()  # 先清空用户名
        self.findElement(*self.address_loc).send_keys(address)
        self.findElement(*self.save_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg

    """停用"""
    def disable_user(self):
        self.findElement(*self.disable_loc).click()
        # 您确定停用吗？-是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(6)
        return msg

    """删除用户"""
    def delete_user(self):
        self.findElement(*self.delete_loc).click()
        # 确定要删除此项？弹框点是
        self.findElement(*self.confirmYes_loc).click()
        msg = self.findElement(*self.divMsg_loc).text
        time.sleep(5)
        return msg







