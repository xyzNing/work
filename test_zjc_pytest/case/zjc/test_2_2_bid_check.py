from pageObject.zjc.cusBackStage import *
import pytest
class TestCheckBid():

    @pytest.mark.usefixtures("login_cus")
    def test_check_bid(self,driver):
        self.cus_page=CusBackStage(driver)
        num=self.cus_page.read_excel('bid')
        for i in range(len(num)):
            self.cus_page.check_bid(num[i])

if __name__ == '__main__':
    pytest.main(['-m','test_2_2_bid_check.py'])


