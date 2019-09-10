import pytest
import datetime
from pageObject.zjc.purBackStage import *
from pageObject.zjc.bidManage import *
class  TestPubBid():
    def setup(self):
        self.username = 'a100073'  # a100048  a100073
        self.password = 'zjc123456'
        self.bidname1 = '普通标书'
        self.bidname2 = '金融标书'
        self.bidname3 = '保证金标书'
        self.link_name = 'sss'
        self.linkphone = '13526954101'
        self.name = 'a'
        self.model = 'a'
        self.unit = 's'
        self.amount = '100'
        self.price = '1000'
        self.content = "biaoshu1"
        self.date1 = (datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y-%m-%d-%H-%M-%S")
        self.date2 = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
        self.address = 'ccc'
        self.text = 'xianjin'
        self.money = '3000'
        self.day = '120'

    # 测试发布普通标书
    @pytest.mark.usefixtures("login_pur")
    def test_ordinary_bid(self,driver):
        u'''发布普通标书'''
        self.backStage = BackStage(driver)
        self.backStage.enter_bid_manage()
        self.bidname = self.bidname1 + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.publicBid = BidManage(driver)
        self.publicBid.base_info(self.bidname, self.link_name, self.linkphone, self.name, self.model, self.unit,
                                 self.amount, self.price, self.content)
        self.publicBid.bid_require(self.date1, self.date2, self.date2,self.text)
        self.publicBid.click_submit()
        num=self.publicBid.get_bid_number()
        self.publicBid.write_excel(num[0:1],'bid')


    # 测试发布金融标书
    # def test_finance_bid(self):
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

    # 需要保证金的标书
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

if __name__ == "__main__":
    pytest.main(['-v','test_2_1_public_bid.py'])
