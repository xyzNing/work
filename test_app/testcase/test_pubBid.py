from page.purchase.purchasePage import PurchasePage
from page.purchase.pubBid import PubBid
from page.myPage import MyPage
from config.basePage import *
import unittest
class TestPublicBid(unittest.TestCase):
    def setUp(self):
        self.username='a00247'
        self.passwd='123456'
        self.bid_name='BID'
        self.content='ASD'
        self.name='computer'
        self.model='15'
        self.brand='lenevo'
        self.place='china'
        self.price='10000'
        self.unit='tai'
        self.count='3'
        self.paycontent='xianjin'
        self.linkname='asd'
        self.phone='13937949012'
        self.driver = get_driver('Android', 'c2f8b612', '5.0', 'com.zhujc.purchasedev',
                                 'com.zhujc.purchase.activity.splash.SplashActivity')
        self.login=MyPage(self.driver)
        self.login.login(self.username,self.passwd)
    def tearDown(self):
        pass

    def test_pub_bid(self):
        self.purchase=PurchasePage(self.driver)
        self.purchase.enter_purchase()
        self.purchase.start_pub_bid()
        self.pubbid=PubBid(self.driver)
        self.pubbid.pub_bid(self.bid_name,self.content,self.name,self.model,self.brand,self.place,self.price,self.unit,self.count,self.paycontent,self.linkname,self.phone)
if __name__ == '__main__':
    unittest()