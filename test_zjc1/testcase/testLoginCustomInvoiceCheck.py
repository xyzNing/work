from configer.basePage import browser
from pageObject.cusBackStage import CusBackStage
from pageObject.loginPage import LoginPage
import unittest

class TestInvoiceCheck(unittest.TestCase):
    def setUp(self):
        self.username="custom123"
        self.passwd="123456"
        self.list_invoice=[]
        self.invoice_value="1"
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.custom_login(self.username,self.passwd)


    def tearDown(self):
        self.driver.quit()

    def test01(self):
        self.cus = CusBackStage(self.driver)
        self.list_invoice=self.cus.read_excel("invoice")
        print(self.list_invoice)
        for invoice in self.list_invoice:
            if invoice=="":
                continue
            else:
                self.cus.checkInvoice(invoice)
                print('check'+invoice)
        # self.cus.checkInvoice(self.invoiceCode, self.invoice_value)
if __name__ == '__main__':
    unittest.main()


