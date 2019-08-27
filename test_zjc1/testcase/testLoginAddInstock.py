# -*- coding=utf-8 -*-
from pageObject.publicInstockPage import PublicInstock
from pageObject.loginPage import LoginPage
from configer.basePage import browser
from pageObject.backStage import BackStage
import unittest
import datetime
from selenium.webdriver.common.by import By

class InstockTest(unittest.TestCase):

    def setUp(self):
        self.driver=browser()
        self.login_url="http://zjcbytest.zhutx.net/"
        self.username="a100048"
        self.passwd="zjc123456789"
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
        self.login=LoginPage(self.driver)
        self.login.open(self.login_url)
        self.login.pur_login(self.username,self.passwd)

    def tearDown(self):
        self.driver.quit()

    def test_instock(self):
        u'''新增入库单'''
        self.backstage = BackStage(self.driver)
        self.backstage.instockSelf()
        self.public_instock = PublicInstock(self.driver)
        # self.driver.find_element_by_xpath("//a[@status='4']").click()
        # elements=self.driver.find_elements_by_xpath("//div[@class='textleft pl15']")
        # print(elements)
        #
        # for element in elements:
        #     print(element.text)
        n=0
        while n<2:
            self.public_instock = PublicInstock(self.driver)
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


if __name__=="__main__":
    unittest.main()
