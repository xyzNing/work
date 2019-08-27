import pytest
from pageObject.zjc.purBackStage import BackStage
from pageObject.zjc.purInvoice import Invoice
class TestEnsureInvoice():

    @pytest.mark.usefixtures('login_pur')
    def test_ensure_Invoice(self,driver):
        self.back_page = BackStage(driver)
        self.back_page.enter_invoice_other()
        self.invoice=Invoice(driver)
        self.invoice_list=self.invoice.read_excel('invoice')
        for i in range(len(self.invoice_list)):
            if self.invoice_list[i]=='':
                continue
            self.invoice.ensure_invoice(self.invoice_list[i])

if __name__ == '__main__':
    pytest.main(['-v',''])

