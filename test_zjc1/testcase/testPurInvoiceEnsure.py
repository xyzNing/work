from configer.basePage import browser
from pageObject.backStage import BackStage
from pageObject.loginPage import LoginPage
import unittest
class TestPurInvoiceEnsure(unittest.TestCase):
    def setUp(self):
        self.username="a100048"   #a00276  凡是分公司
        self.passwd="zjc123456789"
        self.list_invoice=[]
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.open("http://zjcbytest.zhutx.net")
        self.login.pur_login(self.username,self.passwd)


    def tearDown(self):
        self.driver.quit()

    def test_invoice_comfirm(self):
        self.backstage=BackStage(self.driver)
        self.list_invoice=self.backstage.read_excel("invoice")
        print(self.list_invoice)
        self.backstage.enter_invoice()
        for num in self.list_invoice:
            print(num)
            if num=="":
                continue
            else:
                self.backstage.invoiceEnsure(num)

if __name__ == '__main__':
    unittest()
