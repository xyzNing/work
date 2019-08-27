#  -*-coding=utf-8-*-
from pageObject.addInvoice import AddInvoice
from configer.basePage import browser
from pageObject.loginPage import LoginPage
import  unittest
import time


class AddInvoiceTest(unittest.TestCase):
    def setUp(self):
        self.login_url = "http://zjcbytest.zhutx.net/"
        self.username="a100048"
        self.password="zjc123456789"
        self.htnumber = 'HT1902221289'
        self.htnumber1 = "HT1902221290"  # a00262下的合同
        self.htnumber2 = "HT1902281303"  # a00262下的合同
        self.htnumber3 = 'HT1902281304'
        self.list_num=[]
        self.invoice_code1=time.strftime("%Y%m%d%H%M")
        self.invoice_num1=time.strftime("%Y%m%d%H%M")
        self.invoice_rate="10"
        self.product="a"
        self.rule="a"
        self.unit="a"
        self.num=1
        self.price=10000
        self.cmd=r"C:\Users\ning\Desktop\SendPhoto.exe"
        self.date=time.strftime("%Y-%m-%d")
        # self.file=r"‪C:\Users\Lee\Desktop\22.exe"
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.open(self.login_url)
        self.login.pur_login(self.username,self.password)

    #新增多张发票
    def test01(self):
        u'''新增发票'''
        self.pur = AddInvoice(self.driver)
        self.pur.enter_invoice()
        # for i in range(0,1): #从1开始，不包含2
        #     self.invoice_code=self.invoice_code1+str(i)+"a"
        #     self.invoice_num=self.invoice_num1+str(i)+"b"
        #     self.pur.addInvoice(self.htnumber3,self.invoice_code,self.invoice_num,self.date,self.invoice_rate,self.product,self.rule,
        #                        self.unit,self.num,self.price,self.cmd)
        time.sleep(1)
        self.list_num=self.pur.getInvoiceNumber()
        print(self.list_num)
        self.pur.write_excel(self.list_num,"invoice")

    #新增单张发票
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

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
