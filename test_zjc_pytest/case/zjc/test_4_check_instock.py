import pytest
from pageObject.zjc.cusBackStage import CusBackStage
class TestCheckInstock():

    @pytest.mark.usefixtures('login_cus')
    def test_check_instock(self,driver):
        self.cus_page=CusBackStage(driver)
        self.cus_page.enter_instock()
        self.instock_nums = self.cus_page.read_excel('instock')
        for i in range(len(self.instock_nums)):
            if self.instock_nums[i] == '':
                continue
            self.cus_page.checkInstock(self.instock_nums[i])

if __name__ == '__main__':
    pytest.main(['-v','test_4_check_instock'])
