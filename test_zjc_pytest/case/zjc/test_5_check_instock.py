import pytest
from pageObject.zjc.cusBackStage import CusBackStage
class TestCheckInstock():

    @pytest.mark.usefixtures("login_cus")
    def test_check_instock(self,driver):
        self.cus_page=CusBackStage(driver)
        self.cus_page.enter_instock()
        self.instock_nums = self.cus_page.read_excel('instock')
        for instock in self.instock_nums:
            if instock == '':
                continue
            self.cus_page.check_instock(instock)

if __name__ == '__main__':
    pytest.main(['-v','test_4_check_instock.py'])
