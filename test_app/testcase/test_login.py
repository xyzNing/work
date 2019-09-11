from page.myPage import MyPage
from config.basePage import get_driver
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user='a00247'
        self.passwd='123456'
        self.driver=get_driver('Android','c2f8b612','5.0','com.zhujc.purchasedev','com.zhujc.purchase.activity.splash.SplashActivity')
    def tearDown(self):
        pass

    def test_login(self):
        self.mypage=MyPage(self.driver)
        self.mypage.login(self.user,self.passwd)

if __name__ == '__main__':
    unittest()