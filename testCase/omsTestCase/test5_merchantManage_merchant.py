# -*-coding:UTF-8-*-
# __author__ = 'gao'
from page.omsPage.merchantManage import *
from page.omsPage.init import *


class TestOperatorManage(Init, Login, MerchantManage):
    """用例：商户管理-添加商户"""
    def test01_addMerchant(self):
        # 登录，为使此py可单独运行
        self.username = self.getXMLData('omsUsername')
        self.pwd = self.getXMLData('omsPwd')
        self.login(self.username, self.pwd)
        time.sleep(2)

        self.enter_operatorManage()
        # 添加新用户
        msg = self.add_operator()
        self.assertEqual('保存成功！', msg, "保存成功断言")
        time.sleep(2)

        # 登录，为使此py可单独运行
        # self.logout
        # time.sleep(2)
        # 登录运营商账号，才能创建商户
        self.login("888888", "999999")
        time.sleep(5)

        self.enter_merchant_manage()
        # 添加新用户
        msg = self.add_merchant()
        self.assertEqual('保存成功！', msg, "保存成功断言")
        time.sleep(2)

    """用例：根据商户名称查询用户"""
    def test02_search(self):
        self.search_merchantByName("test_merchant")

    """用例：根据服务器名称查询用户"""
    def test03_search(self):
        self.search_merchantByServer()

    """用例：修改用户"""
    def test04_change(self):
        self.search_merchantByName("test_merchant")
        msg = self.change_merchant()
        self.assertEqual("保存成功！", msg, "修改后保存成功断言")

    """用例:同步操作"""
    def test05_syn_merchant(self):
        self.search_merchantByName("test_merchant")
        time.sleep(2)
        msg = self.syn_merchant()
        self.assertEqual("同步成功！", msg, "是否同步成功断言")

    """用例:删除商户"""
    def test06_delete_user(self):
        self.search_merchantByName("test_merchant")
        time.sleep(2)
        msg = self.delete_merchant()
        self.assertEqual("删除成功！", msg, "是否删除成功断言")


if __name__ == '__main__':
    unittest.main(verbosity=2)


