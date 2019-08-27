#  -*-coding=utf-8-*-
from pageObject.backStage import BackStage
from pageObject.loginPage import LoginPage
from pageObject.publicBidPage import PublicBid
from configer.basePage import browser
import unittest
import datetime
import time

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = browser()
        self.login_url = "http://zjcbytest.zhutx.net/"
        self.username='a100073'  #a100048  a100073
        self.password='zjc123456'
        self.bidname1 = '普通标书'
        self.bidname2 ='金融标书'
        self.bidname3 = '保证金标书'
        self.link_name='sss'
        self.linkphone = '13526954101'
        self.name='三级螺纹钢'
        self.model='a'
        self.unit='s'
        self.amount=100
        self.price=1000
        self.content="biaoshu1"
        self.date1=(datetime.datetime.now()+datetime.timedelta(days=6)).strftime("%Y-%m-%d-%H-%M-%S")
        self.date2=(datetime.datetime.now()+datetime.timedelta(days=10 )).strftime("%Y-%m-%d-%H-%M-%S")
        self.address='ccc'
        self.text='xianjin'
        self.money=3000
        self.day=120
        self.login = LoginPage(self.driver)
        self.login.open(self.login_url)
        self.login.pur_login(self.username, self.password)

    def tearDown(self):

      self.driver.quit()

    # 测试发布普通标书
    def test_bid(self):
        u'''发布普通标书'''
        self.bidname=self.bidname1+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.bidname=self.bidname1+time.strftime("%Y-%m-%d-%H-%M-%S")
        self.backStage=BackStage(self.driver)
        self.backStage.bidSelf()
        self.publicBid=PublicBid(self.driver)
        self.publicBid.base_info(self.bidname,self.link_name,self.linkphone,self.name,self.model,self.unit,
                                  self.amount,self.price, self.content)
        self.publicBid.bid_request(self.date1,self.date2,self.address,self.text)
        self.publicBid.click_submit()
    # 测试发布金融标书
    # def test_fbid(self):
    #     u'''发布金融标书'''
    #     # for i in range(1,11):
    #     # self.bidname = self.bidname2+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #     self.bidname = self.bidname2 + time.strftime("%Y-%m-%d-%H-%M-%S")
    #     self.backStage = BackStage(self.driver)
    #     self.backStage.bidSelf()
    #     self.publicBid = PublicBid(self.driver)
    #     self.publicBid.base_info(self.bidname, self.link_name, self.linkphone, self.name, self.model, self.unit,
    #                              self.amount, self.price, self.content)
    #     self.publicBid.bid_request(self.date1, self.date2, self.address, self.text)
    #     self.publicBid.select_fproduct(self.day)
    #     self.publicBid.click_submit()
    #需要保证金的标书
    # def test_bid3(self):
    #     u'''发布需要保证金的普通标书'''
    #     # self.bidname=self.bidname3+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #     self.backStage=BackStage(self.driver)
    #     self.backStage.bidSelf()
    #     self.publicBid=PublicBid(self.driver)
    #
    #     self.bidname3 = self.bidname3 + time.strftime("%Y-%m-%d-%H-%M-%S")
    #     i=0
    #     while i<10:
    #
    #         self.publicBid.base_info(self.bidname3,self.link_name,self.linkphone,self.name,self.model,self.unit,
    #                                   self.amount,self.price, self.content)
    #         self.publicBid.bid_request1(self.date1,self.date2,self.text,self.money)
    #         i+=1

if __name__=="__main__":
    unittest.main()