from page.loginPage import Login
from config.basePage import get_driver
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user=''
        self.passwd=''

        self.driver=get_driver('Android',"c2f8b612",'5.0','com.v','com.')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.mypage=Login(self.driver)
        self.mypage.login(self.user,self.passwd)
        company_name=self.mypage.get_company_name()
        self.assertEqual(company_name,"二号分公司")


if __name__ == '__main__':
    unittest.main()