from pageObject.zjc.cusBackStage import CusBackStage
import pytest
class TestCheckBillingInfo():

    @pytest.mark.usefixtures('login_cus')
    def test_check_billing(self,driver):
        self.page=CusBackStage(driver)
        text_list=self.page.read_excel("billingInfo")
        for text in text_list:
            self.page.check_billing(text)

if __name__ == '__main__':
    pytest.main(['-v','test_1_4_check_billing.py'])
