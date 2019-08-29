import pytest
from pageObject.zjc.InstockPage import PublicInstock
from pageObject.zjc.purBackStage import BackStage
import datetime
class TestInstock():
    @pytest.fixture(scope='function', autouse=True)
    def is_login(self, driver):
        driver.get("http://zjcbytest.zhutx.net/")
        driver.delete_all_cookies()
        driver.refresh()

    def setup(self):
        # self.login_url="http://zjcbytest.zhutx.net/"
        # self.username="a100048"
        # self.passwd="zjc123456789"
        self.htnumber='HT1902221289'
        self.htnumber1="HT1902221290"  #a00262下的合同
        self.htnumber2 = "HT1902281303"  # a00262下的合同
        self.htnumber3 = 'HT1902281304'
        self.materials='wuzi1'
        self.model='guige'
        self.amount=3
        self.unit='t'
        self.price=11000
        # self.total=100000
        self.time1=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d-%H-%M-%S")
        self.time2=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d-%H-%M-%S")
        self.operator='sss'

    @pytest.mark.usefixtures('login_pur')
    def test_add_instock(self,driver):
        u'''新增入库单'''
        self.backstage = BackStage(driver)
        self.backstage.instockSelf()
        self.public_instock = PublicInstock(driver)
        # self.driver.find_element_by_xpath("//a[@status='4']").click()
        # elements=self.driver.find_elements_by_xpath("//div[@class='textleft pl15']")
        # print(elements)
        #
        # for element in elements:
        #     print(element.text)
        n=1
        while n<5:
            self.public_instock.publicInstock(self.htnumber3, self.materials, self.model, self.amount, self.unit,
                                                  self.price, self.time1, self.time1,self.time2,self.operator)
            n+=1
        List_num= self.public_instock.getInstockNumber()
        print(List_num)
        self.public_instock.write_excel(List_num,"instock")
        # num_list=self.public_instock.getInstockNumber()
        # for i in num_list[:1]:
        #     with open("D:/Work/test_zjc/logs/instokc.txt","a+") as f:
        #         f.write(i)+" "

if __name__ == '__main__':
  pytest.main(['-s','test_3_Instock.py'])

  # pytest - -html = report.html  生成测试报告

#第一步
  # pytest - s - q - -alluredir指定 report路径
#第二步
  # allure generate directory-with-results/ -o directory-with-reportdirectory
  # with-results 是 alluredir 生成的 xml 目录，
  # directory -with-report 是最终生成 html 的目录