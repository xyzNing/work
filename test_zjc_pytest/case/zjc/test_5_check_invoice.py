from pageObject.zjc.cusBackStage import CusBackStage
import pytest
class TestCheckInvoice():

    @pytest.mark.usefixtures("login_cus")
    def test_check_invoice(self,driver):
        self.cus_page=CusBackStage(driver)
        self.cus_page.enter_invoice()
        self.invoice_list=self.cus_page.read_excel('invoice')
        for invoice in self.invoice_list:
            if invoice =='':
                continue
            self.cus_page.check_invoice(invoice)

if __name__ == '__main__':
    pytest.main(['-v','test_4.check_invoice'])
