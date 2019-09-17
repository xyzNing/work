from page.contractPage import ContractPage
import unittest
from datetime import datetime


class TestContract(unittest.TestCase):
    def setUp(self):
        self.contract_page = ContractPage()
        self.time=datetime.strftime(datetime.now(),"%Y%m%d%H%M")
        self.content=self.contract_page.get_excel_value('contract',1)[4]
        self.content2 = self.contract_page.get_excel_value('contract', 2)[4]


    def tearDown(self):
        '''
        unittest提供了一些跳过指定用例的方法
        @unittest.skip(reason)：强制跳转。reason是跳转原因
        @unittest.skipIf(condition, reason)：condition为True的时候跳转
        @unittest.skipUnless(condition, reason)：condition为False的时候跳转
        @unittest.expectedFailure：如果test失败了，这个test不计入失败的case数目
        :return:
        '''
        pass

    # @unittest.skipIf(3==2,'条件为真时执行')
    def test01(self):
        '''新增合同存草稿后删除合同'''
        res=self.contract_page.del_contract(self.content)
        self.assertEqual(res[0],200) and self.assertEqual(res[1]['code'],'1')

    # @unittest.skip('条件为真时执行')
    def test_02(self):
        '''新增合同审核不通过后编辑合同审核通过'''
        res=self.contract_page.edict_contract(self.content2)
        self.assertEqual(res[0], 200) and self.assertEqual(res[1]['code'], '1')


    def test_03(self):
        '''编辑合同附件审核通过'''
        res=self.contract_page.edict_attach(self.content2)
        res_code=res[0]
        res_code1=res[1]['code']
        print(type(res_code))
        print(type(res_code1))
        self.assertEqual(res_code,200,"res_code=200")
        self.assertEqual(res_code1,1,"res_code1=1")


    # def test04(self):
    #     self.assertEqual(200,200,"200=200")

if __name__ == '__main__':
    unittest.main()

