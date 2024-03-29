from page.loginPage import Login
from config.basePage import get_driver
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user='a00247'
        self.passwd='123456'
        # self.driver=get_driver('Android','GWY0217803001154','9','com.zhujc.purchasedev','com.zhujc.purchase.activity.splash.SplashActivity')
        self.driver=get_driver('Android',"c2f8b612",'5.0','com.zhujc.purchasedev','com.zhujc.purchase.activity.splash.SplashActivity')

    def tearDown(self):
        pass

    def test_login(self):
        self.mypage=Login(self.driver)
        self.mypage.login(self.user,self.passwd)
        size=self.mypage.get_size()
        print(size[0],size[1])

if __name__ == '__main__':
    unittest.main()