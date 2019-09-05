import pytest
from pageObject.zjc.invoiceManage import Invoice
from pageObject.zjc.purBackStage import BackStage
import time

class TestInvoice():
    @pytest.fixture(scope='function', autouse=True)
    def is_login(self, driver):
        driver.get("http://zjcbytest.zhutx.net/")
        driver.delete_all_cookies()
        driver.refresh()

    def setup(self):
        self.login_url = "http://zjcbytest.zhutx.net/"
        self.username = "a100048"
        self.password = "zjc123456789"
        self.htnumber = 'HT1902221289'
        self.htnumber1 = "HT1902221290"  # a00262下的合同
        self.htnumber2 = "HT1902281303"  # a00262下的合同
        self.htnumber3 = 'HT1902281304'
        self.list_num = []
        self.invoice_code1 = time.strftime("%Y%m%d%H%M")
        self.invoice_num1 = time.strftime("%Y%m%d%H%M")
        self.invoice_rate = "10"
        self.product = "a"
        self.rule = "a"
        self.unit = "a"
        self.num = 1
        self.price = 10000
        self.date = time.strftime("%Y-%m-%d")
        # self.file=r"‪C:\Users\Lee\Desktop\22.exe"

     # 新增多张发票
    @pytest.mark.usefixtures('login_pur')
    def test_01(self,driver):
        u'''新增发票'''
        self.back_page = BackStage(driver)
        self.back_page.enter_invoice_self()
        self.pur = Invoice(driver)
        contract_num=self.pur.read_excel('contract')[0]
        for i in range(0,1): #从1开始，不包含1
            self.invoice_code=self.invoice_code1+str(i)+"a"
            self.invoice_num=self.invoice_num1+str(i)+"b"
            self.pur.add_invoice(contract_num,self.invoice_code,self.invoice_num,self.date,self.invoice_rate,self.product,self.rule,
                               self.unit,self.num,self.price)
        time.sleep(1)
        self.list_num = self.pur.getInvoiceNumber()
        print(self.list_num)
        self.pur.write_excel(self.list_num, "invoice")

        # 新增单张发票
        # def test02(self):
        #     u'''新增发票'''
        #     self.pur = AddInvoice(self.driver)
        #     # self.pur.enter_invoice()
        #     self.invoice_code=self.invoice_code1+str(1)+"a"
        #     self.invoice_num=self.invoice_num1+str(1)+"b"
        #     self.pur.addInvoice(self.htnumber1,self.invoice_code,self.invoice_num,self.date,self.invoice_rate,self.product,self.rule,
        #                        self.unit,self.num,self.price,self.cmd)
        #     time.sleep(1)
        #     self.list_num=self.pur.getInvoiceNumber()
        #     print(self.list_num)
        #     self.pur.write_excel(self.list_num,"invoice")
if __name__ == '__main__':
    pytest.main(['-v','test_4_invoice.py'])


