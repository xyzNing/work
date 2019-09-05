from pageObject.zjc.bidManage import *
from pageObject.zjc.purBackStage import *
import pytest
class TestBIdConfirm():
    def start(self,driver):
        driver.get("http://zjcbytest.zhutx.net/")
        driver.delete_all_cookies()
        driver.refresh()

    def setup(self):
        self.coment="这家供应商真的很好"

    @pytest.mark.usefixtures('login_pur')
    def test_bid_confirm(self,driver):
        self.pur_page=BackStage(driver)
        self.pur_page.enter_bid_manage()
        self.bid_page=BidManage(driver)
        bid_number=self.bid_page.read_excel('bid')
        self.bid_page.bid_confirm(bid_number,self.coment)

if __name__ == '__main__':
   pytest.main(['-v',"test_2_4_bid_confirm.py"])


