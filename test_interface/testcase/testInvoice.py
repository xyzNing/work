#coding=utf-8
from page.invoicePage import InovicePage
import unittest
class Invoice(unittest.TestCase):
    def setUp(self):
        self.sheet_name='invoice'
        self.invocie=InovicePage()
        self.content =self.invocie.get_excel_value('invoice',1)[4]

    def tearDown(self):
        pass

    def test01(self):
        '''审核发票'''
        res=self.invocie.check_invoice(self.content)
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1]['code'], 1)
        print('111')
        self.invocie.write_excel(self.sheet_name,1, 7, res[0])
        self.invocie.write_excel(self.sheet_name,1, 8, res[1]['code'])
        self.invocie.write_excel(self.sheet_name,1, 9, str(res[1]))
        print('222')

if __name__ == '__main__':
    unittest.main()