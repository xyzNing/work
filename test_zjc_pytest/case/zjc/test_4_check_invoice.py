from pageObject.zjc.cusBackStage import CusBackStage
import pytest
class TestCheckInvoice():
    @pytest.mark.usefixtures('login_cus')
    def test_check_invoice(self,driver):
        self.cus_page=CusBackStage(driver)
        self.cus_page.enter_invoice()
        self.invoice_list=self.cus_page.read_excel('invoice')
        for i in range(len(self.invoice_list)):
            if self.invoice_list[i]=='':
                continue
            self.cus_page.checkInvoice(self.invoice_list[i])

if __name__ == '__main__':
    pytest.main(['-v','test_4.check_invoice'])
