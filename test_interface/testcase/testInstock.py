from page.instkockPage import InstockPage
import unittest
class TestInstock(unittest.TestCase):
    def setUp(self):
        self.instock=InstockPage()
        self.content=self.instock.get_excel_value('instock',1)[4]

    def tearDown(self):
        pass

    # @unittest.skip("跳过")
    def test01(self):
        '''审核入库单'''
        res = self.instock.check_instock(self.content)
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1]['code'], 1)

    def test02(self):
        '''审核入库单附件'''
        res=self.instock.check_attach(self.content)
        self.assertEqual(res[0],200)
        self.assertEqual(res[1]['code'],1)

if __name__ == '__main__':
    unittest.main()