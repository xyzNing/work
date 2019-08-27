from pageObject.cusBackStage import CusBackStage
from pageObject.loginPage import LoginPage
from configer.basePage import BasePage,browser
import unittest
class TestCusBidCheck(unittest.TestCase):
    def setUp(self):
        self.username='custom231'
        self.passwd='123456'
        self.bid_number='ZB190122005'
        self.bid_reason=u"审核通过"
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.custom_login(self.username,self.passwd)

    def tearDown(self):
        self.driver.quit()

    def testCheck(self):
        self.cusBackStage=CusBackStage(self.driver)
        self.cusBackStage.checkBid(self.bid_number,self.bid_reason)

if __name__ == '__main__':
    unittest()