import pytest
from pageObject.zjc.InstockPage import Instock
from pageObject.zjc.purBackStage import BackStage
import datetime
class TestInstock():

    def setup(self):
        self.htnumber='HT1902221289'
        self.htnumber1="HT1902221290"  #a00262下的合同
        self.htnumber2 = "HT1902281303"  # a00262下的合同
        self.htnumber3 = 'HT1902281304'
        self.materials='wuzi1'
        self.model='guige'
        self.amount=3
        self.unit='t'
        self.price=11000
        self.time1=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.time2=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.operator='sss'
        self.n=1

    @pytest.mark.usefixtures("login_pur")
    def test_add_instock(self,driver):
        u'''新增入库单'''
        self.backstage = BackStage(driver)
        self.backstage.instockSelf()
        self.bid_page = Instock(driver)
        contract_number=self.bid_page.read_excel('contract')[0]
        for i in range(self.n):
            self.bid_page.public_instock(contract_number, self.materials, self.model, self.amount, self.unit,
                                                  self.price, self.time1, self.time1,self.time2,self.operator)
        List_num= self.bid_page.get_instock_number()[0:self.n]
        print(List_num)
        self.bid_page.write_excel(List_num,"instock")


if __name__ == '__main__':
  pytest.main(['-s','test_4_create_Instock.py'])

  # pytest - -html = report.html  生成测试报告

#第一步
  # pytest - s - q - -alluredir指定 report路径
#第二步
  # allure generate directory-with-results/ -o directory-with-reportdirectory
  # with-results 是 alluredir 生成的 xml 目录，
  # directory -with-report 是最终生成 html 的目录