from page.invoiceInfoPage import InvoiceInfoPage
import unittest
from datetime import datetime
class InvoiceInfo(unittest.TestCase):
    def setUp(self):
        self.title=datetime.strftime(datetime.now(),"%Y%m%d")
        self.invoiceInfo=InvoiceInfoPage()
        self.content=self.invoiceInfo.get_excel_value('invoiceInfo',1)[4]
    def tearDown(self):
       pass

    def test01(self):
        '''审核开票信息'''
        res = self.invoiceInfo.check_invoiceInfo(self.content)
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1]['code'], 1)

    def test02(self):
        '''删除开票信息'''
        res = self.invoiceInfo.del_invoiceInfo(self.content)
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1]['code'], 1)

    def test03(self):
        '''设置开票信息为默认'''
        res = self.invoiceInfo.set_invoiceInfo(self.content)
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1]['code'], 1)

if __name__ == '__main__':
    unittest.main()