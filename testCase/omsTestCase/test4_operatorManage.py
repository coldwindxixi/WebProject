# -*-coding:UTF-8-*-
# __author__ = 'gao'
from page.omsPage.operatorManage import *
from page.omsPage.init import *


class TestOperatorManage(Init, Login, OperatorManage):
    """用例：添加运营商用户-保存"""
    def test01_addOperatorUser(self):
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

    """用例：查询用户"""
    def test02_search(self):
        self.search_by_cityAndOperator()

    """用例：修改用户"""
    def test03_change(self):
        self.search_by_cityAndOperator()
        msg = self.change_user("newAddress")
        self.assertEqual("保存成功！", msg, "修改后保存成功断言")

    """用例：停用用户"""
    def test04_disable_user(self):
        # 查询用户
        self.search_by_cityAndOperator()
        time.sleep(3)
        # 停用
        disable_msg = self.disable_user()
        self.assertEqual("停用成功！", disable_msg, "是否停用成功断言")

    """用例：删除运营商"""
    def test05_delete_user(self):
        self.search_by_cityAndOperator()
        time.sleep(2)
        msg = self.delete_user()
        self.assertEqual("删除成功！", msg, "是否删除成功断言")


if __name__ == '__main__':
    unittest.main(verbosity=2)

