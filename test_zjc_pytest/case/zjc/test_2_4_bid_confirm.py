from pageObject.zjc.bidManage import *
from pageObject.zjc.purBackStage import *
import pytest
class TestBIdConfirm():

    def setup(self):
        self.content="这家供应商真的很好"

    @pytest.mark.usefixtures("login_pur")
    def test_bid_confirm(self,driver):
        self.pur_page=BackStage(driver)
        self.pur_page.enter_bid_manage()
        self.bid_page=BidManage(driver)
        bid_number=self.bid_page.read_excel('bid')
        self.bid_page.bid_confirm(bid_number,self.content)

if __name__ == '__main__':
   pytest.main(['-v',"test_2_4_bid_confirm.py"])


