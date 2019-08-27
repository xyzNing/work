#  -*-coding=utf-8-*-
from pageObject.loginPage import LoginPage
from configer.basePage import browser
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.login_url = "http://zjcbytest.zhutx.net/"
        self.username_pur='A00262'  #采购商
        self.password_pur='zjc123456'
        self.text="范氏集团"
        self.username_sup='13937949014'  #供应商
        self.password_sup="12345678"
        self.username_cus="custom228"
        self.password_cus="123456"
        self.driver = browser()
        self.login = LoginPage(self.driver)

    def tearDown(self):
       self.driver.quit()


    def test_pur_login(self):
        u'''采购商登录功能'''
        self.login.open(self.login_url)
        self.login.pur_login(self.username_pur, self.password_pur)
        # get_text=self.login.get_text()
        # print(get_text)
        # self.assertIn(self.assert_text,get_text,msg="原因")
        self.assertTrue(self.login.is_text(self.text))

        # self.assertTrue(act_result)

    # def test_sup_login(self):
    #     self.login = LoginPage(self.driver)
    #     self.login.sup_login(self.username_sup,self.password_sup)

    # def test_cus_login(self):
    #     '''客服登录'''
    #     self.login.custom_login(self.username_cus,self.password_cus)


if __name__=="__main__":
    unittest.main()

