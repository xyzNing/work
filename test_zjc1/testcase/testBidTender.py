from pageObject.bidTenderPage import BidTenderPage
from pageObject.loginPage import LoginPage
from configer.basePage import browser,BasePage
import unittest,time
class TestBidTender(unittest.TestCase):
    def setUp(self):
        self.username='13937949015'
        self.password='zjc123456'
        self.bid_number='ZB190122005'
        self.rate='10'
        self.price1='1000'
        self.price3='100000'
        self.linkphone='13937949014'
        self.linkname='sss'
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.sup_login(self.username,self.password)


    def tearDown(self):
        self.driver.quit()

    def test01(self):

        self.bid_Tender=BidTenderPage(self.driver)
        self.bid_Tender.bidTender(self.bid_number,self.rate,self.price1,self.price3,self.linkname,self.linkphone)

if __name__ == '__main__':
    unittest()