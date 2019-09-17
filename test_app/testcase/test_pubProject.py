from page.purchase.pubProject import PubProject
from page.purchase.purchasePage import PurchasePage
from page.loginPage import Login
from config.basePage import get_driver
import unittest
class TestPubProject(unittest.TestCase):
    def setUp(self):
        self.username = 'a00247'
        self.passwd = '123456'
        self.pro_name='新建项目'
        self.pro_type='随便'
        self.pro_manage='张三'
        self.phone='13937949044'
        self.pro_money='1000000'
        self.pro_area1='10000'
        self.pro_area2='10000'
        self.pro_cycle='12个月'
        self.pro_address='111号'
        self.pro_desc='测试项目'
        self.driver=get_driver('Android',"c2f8b612",'5.0','com','com')
        self.login = Login(self.driver)
        self.login.login(self.username, self.passwd)

    def tearDown(self):
        pass

    def test_pub_project(self):
        self.purchase=PurchasePage(self.driver)
        self.purchase.enter_purchase()
        self.purchase.start_pub_project()
        self.pubProject=PubProject(self.driver)
        self.pubProject.pub_project(self.pro_name,self.pro_type,self.pro_manage,self.phone,self.pro_money,
                                    self.pro_area1,self.pro_area2,self.pro_cycle,self.pro_address,self.pro_desc)


if __name__ == '__main__':
    unittest.main()
