from pageObject.zjc.supTenderBid import *
import pytest
import time
class TestBidTender():

    def setup(self):
        self.rax="10"
        self.price1='10000'
        self.price2='10000'
        self.linkman='ss'
        self.phone='13937949012'

    @pytest.mark.usefixtures("login_sup")
    def test_bid_tender(self,driver):
        time.sleep(5)
        self.sup_page=BidTenderPage(driver)
        bid_num=self.sup_page.read_excel('bid')
        for i in range(len(bid_num)):
            self.sup_page.bid_tender(bid_num[i],self.rax,self.price1,self.price2,self.linkman,self.phone)

if __name__ == '__main__':
    pytest.main(['-v','test_2_3_bid_tender.py'])
