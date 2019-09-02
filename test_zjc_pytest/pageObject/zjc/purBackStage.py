#coding=utf-8
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class BackStage(BasePage):
    selector_enter=(By.XPATH,"//a[@class='index-login__link mt16 goAdminPage']")#进入管理首页
    selector_pur_manage=(By.CSS_SELECTOR,"#n2>h3>span")#采购管理
    selector_project=(By.CSS_SELECTOR,"#n2-1>span")#项目管理
    selector_bid=(By.CSS_SELECTOR,"#n2-2>span")#招标管理
    selector_bid_self_build=(By.CSS_SELECTOR,"#n2-2-1>a")#自建项目
    selector_contract=(By.CSS_SELECTOR,"#n2-3>span") #合同管理

    select_instock=(By.CSS_SELECTOR,"#n2-5>span")   #入库管理
    select_instock_self=(By.XPATH,"//li[@id='n2-5-1']/a")
    selector_public_bid = (By.XPATH, ".//*[@id='main']/div[1]/p[2]/input[3]")
    selector_all_bidnames=(By.XPATH,"//tbody[@id='bidListMain']/tr[1]/td[2]")

    invoice_manage=(By.XPATH,"//li[@id='n2-6']/span")  #发票管理
    invoice_self=(By.XPATH,"//li[@id='n2-6-1']/a")   #自建项目
    invoice_other=(By.XPATH,"//li[@id='n2-6-2']/a")  #挂入项目
    invoice_add=(By.XPATH,"//input[@class='noborder opacity-btn add-btn cursor']") #新增发票
    invoice_hang=(By.XPATH,"//li[@id='n2-6-2']/a")   #挂入项目
    invoice_search_input=(By.XPATH,"//input[@id='searchInput']")  #输入需要搜索的内容
    invoice_search_button=(By.XPATH,"//input[@value='搜索']")  #搜索按钮
    invoice_ensure_button=(By.XPATH,"//p[@class='overhidden']/a")  #确认
    invoice_ensure=(By.XPATH,"//input[@value='确认发票']")
    invoice_dialog_comfirm=(By.XPATH,"//div[@class='dialog__footer']/a")

    def enter_project_manage(self):   #进入项目管理
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.selector_project)

    def bidSelf(self):
        self.click(self.selector_enter)
        self.click(self.selector_pur_manage)
        self.click(self.selector_bid)
        self.click(self.selector_bid_self_build)

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




