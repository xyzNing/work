from pageObject.jinfu.assertCenter import Assert_Center
from configer.basePage import browser
import datetime
import unittest
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.url="http://zlzrtest.zhutx.net/index/my_asset/asset"
        self.htnumber='HT190725010001'
        self.code=str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y%m%d"))+"a"
        self.num=str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y%m%d"))+"b"
        self.tax="10"
        self.name="a"
        self.model="s"
        self.unit="s"
        self.amount="10"
        self.sum="10"
        # self.date1=  (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.date1 = (datetime.datetime.now()).strftime("%Y-%m-%d")
        self.opetaror='s'
        self.driver=browser()

    def teardown(self):
        pass

    # def test_addInstokc(self):
    #     n=0
    #     while n<1:
    #         self.driver.get(self.url)
    #         self.pur=Assert_Center(self.driver)
    #         self.pur.add_instock(self.htnumber,self.date1,self.date1,self.opetaror)
    #         n+=1

    def test_addInvoice(self):
        n = 0
        while n < 5:
            self.driver.get(self.url)
            self.pur = Assert_Center(self.driver)
            self.code = str((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d%H%M")) + "a"
            self.num = str((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d%H%M")) + "b"
            self.code+=str(n)
            self.num+=str(n)
            self.pur.add_invoice(self.htnumber,self.code,self.num,self.date1,self.tax,
                                 self.name,self.sum)
            n += 1

if __name__ == '__main__':
    unittest.main