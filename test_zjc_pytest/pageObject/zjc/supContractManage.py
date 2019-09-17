from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class SupContract(BasePage):
    loc_enter_home=(By.XPATH,"//div[@class='index-login__content']/a")
    loc_sup_manage=(By.XPATH,"//div[@id='n2']/h3/span")
    loc_contract_manage=(By.XPATH,"//li[@id='n2-2']/a")
    loc_tradiction=(By.XPATH,"//li[@type='1']")   #传统合同
    loc_eletronic=(By.XPATH,"//li[@type='2']")  #电子合同
    loc_search=(By.ID,"searchInput")
    loc_search_button=(By.ID,"searchBtn")
    loc_confirm=(By.XPATH,"//a[text()='确认']")
    #确认页面元素
    loc_agree =(By.ID,"confirm")
    loc_refuse=(By.XPATH,"//input[@value='异议']")
    loc_refuse_reason=(By.ID,"reason")
    loc_refuse_confirm=(By.XPATH,"//div[@id='refuseModal']//input")
    loc_success=(By.XPATH,"//div[@class='dialog__footer']/a")  #提交成功的确定

    def confirm_contract(self,number):
        '''
        供应商确认合同，先通过搜索功能找到对应合同，然后确认
        :param number: 合同编号
        :return:
        '''
        self.click(self.loc_enter_home)
        time.sleep(2)
        self.click(self.loc_sup_manage)
        self.click(self.loc_contract_manage)
        self.send_keys(self.loc_search,number)
        self.click(self.loc_search_button)
        time.sleep(1)
        self.click(self.loc_confirm)
        self.scroll()
        time.sleep(1)
        self.click(self.loc_agree)
        self.click(self.loc_success)

