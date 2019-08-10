# -*-coding:UTF-8-*-
# __author__ = 'gao'
# 品智客户运维系统-用户管理-运营商用户管理
from page.omsPage.userManage import *
from page.omsPage.init import *
import time


class TestOperatorUserManager(Init, Login, UserManage):
    # 类变量,调用类方法
    newUser = ReadXML.getXMLDataCls('omsNewOperatorUser')
    newUserNo = ReadXML.getXMLDataCls('omsNewOperatorNo')

    """用例：添加运营商用户-保存"""
    def test01_addOperatorUser(self):
        # 登录，为使此py可单独运行
        self.username = self.getXMLData('omsUsername')
        self.pwd = self.getXMLData('omsPwd')
        self.login(self.username, self.pwd)
        time.sleep(2)

        self.enter_opertor()
        # 查询用户，如果存在先删除
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        if result != "表中数据为空":
            self.delete_user()

        # 添加新用户
        msg = self.add_operator(self.newUserNo, self.newUser)
        self.assertEqual('保存成功！', msg, "保存成功断言")
        time.sleep(2)

    """用例：根据用户名查询用户"""
    def test02_searchUser(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")

    """用例：重置密码-是"""
    def test03_resetPwd(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        msg = self.reset_password()
        self.assertEqual("重置成功！", msg, "重置成功断言")
        time.sleep(2)

    """用例：重置密码-否"""
    def test04_resetPwd_no(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        self.reset_password_no()
        time.sleep(1)

    """用例:修改用户-保存"""
    def test05_change_user(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        msg = self.change_user("changeName")
        self.assertEqual("保存成功！", msg, "修改后保存成功断言")
        time.sleep(2)

        # 搜索修改后用户名
        result = self.search_by_username("changeName")
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        # 修改为初始用户名
        msg = self.change_user(self.newUser)
        self.assertEqual("保存成功！", msg, "修改后保存成功断言")
        time.sleep(2)

    """用例:修改用户-放弃"""
    def test06_change_user_abandon(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        self.change_user_abandon("changeName")

        # 搜索修改后用户名，数据为空才正确
        result = self.search_by_username("changeName")
        time.sleep(3)
        self.assertEqual("表中数据为空", result, "是否搜索到数据断言")

    """用例：停用用户"""
    def test07_disable_user(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        # 停用
        disable_msg = self.disable_user()
        self.assertEqual("停用成功！", disable_msg, "是否停用成功断言")
        time.sleep(2)
        # 返回所有列表界面，此时需要重新选择用户
        self.search_by_username(self.newUser)
        time.sleep(2)
        state1 = self.get_state()
        self.assertEqual("已停用", state1, "用户状态应为已停用断言")

    """用例：启用-选择不启用用户"""
    def test08_enable_userNo(self):
        self.enable_user_no()
        time.sleep(2)
        # 返回所有列表界面，此时需要重新选择用户
        self.search_by_username(self.newUser)
        time.sleep(2)
        state = self.get_state()
        self.assertEqual("已停用", state, "用户状态应为已停用断言")

    """用例：启用用户"""
    def test09_enable_user(self):
        # 启用
        enable_msg = self.enable_user()
        self.assertEqual("启用成功！", enable_msg, "是否启用成功断言")
        # 返回所有列表界面，此时需要重新选择用户
        self.search_by_username(self.newUser)
        time.sleep(2)
        state = self.get_state()
        self.assertEqual("正常", state, "不停用用户状态应为正常断言")

    """用例：停用-选择不停用用户"""
    def test10_disable_userNo(self):
        self.disable_user_no()
        state = self.get_state()
        self.assertEqual("正常", state, "不停用用户状态应为正常断言")

    """**用例：删除用户"""
    def test11_delUser(self):
        # 查询用户
        result = self.search_by_username(self.newUser)
        time.sleep(3)
        self.assertNotEqual("表中数据为空", result, "是否搜索到数据断言")
        msg = self.delete_user()
        self.assertEqual("删除成功！", msg, "删除成功断言")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

