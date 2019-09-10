import pytest
from pageObject.zjc.purBackStage import BackStage
from pageObject.zjc.invoiceManage import Invoice
class TestEnsureInvoice():

    @pytest.mark.usefixtures("login_pur")
    def test_ensure_Invoice(self,driver):
        self.back_page = BackStage(driver)
        self.back_page.enter_invoice_other()
        self.invoice=Invoice(driver)
        self.invoice_list=self.invoice.read_excel('invoice')
        for invoice in self.invoice_list:
            if invoice =='':
                continue
            self.invoice.ensure_invoice(invoice)

if __name__ == '__main__':
    pytest.main(['-v',''])

