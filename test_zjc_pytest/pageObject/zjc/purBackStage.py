#coding=utf-8
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class BackStage(BasePage):
    selector_enter=(By.XPATH,"//a[@class='index-goAdminPage']")
    selector_project=(By.CSS_SELECTOR,"#n2-1>san")
    selector_pur_manage=(By.CSS_SELECTOR,"#n2>h>span")
    selector_bid=(By.CSS_SELECTOR,"#n2-2>span")
    selector_bid_self_build=(By.CSS_SELECTOR,"#n2-2-1>a")
    selector_contract=(By.CSS_SELECTOR,"#n2-3>span") 
    select_instock=(By.CSS_SELECTOR,"#n2-5>span")
    select_instock_self=(By.XPATH,"//li[@id='n2-5-1']/a")
    invoice_manage=(By.XPATH,"//li[@id='n2']/span")
    invoice_self=(By.XPATH,"//li[@id='n2-6-]/a")
    invoice_other=(By.XPATH,"//li[@id='n2-2']/a")
    set_focus=(By.XPATH,"//div[@id='n5']/h/span")
    subaccount_manage=(By.XPATH,"//li[@id='n53']/a")
    billing_info=(By.XPATH,"//li[@id='n5-4']/a")

    def enter_project_manage(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.selector_project)

    def enter_bid_manage(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.selector_bid)

    def enter_contract_manage(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.selector_contract )

    def bid_name(self):
        self.element_text(self.selector_all_bidnames)

    def instockSelf(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.select_instock)
        self.click(self.select_instock_self)

    def enter_invoice(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.invoice_manage)

    def enter_invoice_self(self):
        self.enter_invoice()
        self.click(self.invoice_self)

    def enter_invoice_other(self):
        self.enter_invoice()
        self.click(self.invoice_other)

    def enter_setting(self):
        '''
        进入设置中心
        :return:
        '''
        self.click(self.selector_enter)
        self.click(self.set_focus)




