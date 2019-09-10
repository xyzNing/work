#-*- coding=utf-8 -*-
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class CusBackStage(BasePage):
    user_manage=(By.XPATH,"//h3[@headerindex='0h']")   #用户管理
    billing_manage=(By.XPATH,"//h3[@headerindex='1h']")   #开票管理
    billing_pur=(By.XPATH,"//a[text()='采购商开票信息']")
    billing_search_text=(By.ID,"txtname")
    billing_search_button=(By.ID,"search_button")
    billing_check=(By.XPATH,"//a[text()='审核']")
    billing_check_select=(By.ID,"checkopt")
    #value=1 审核通过 value=2  审核不通过
    billing_save=(By.ID,"submit_button")

    bid_tend_manage=(By.XPATH,"//h3[@headerindex='2h']")   #招投标管理
    bid_public_check=(By.XPATH,"//a[@title='招标发布一次审核']")
    bid_search_input=(By.XPATH,"//input[@id='txtname']")  #搜索框
    bid_search=(By.ID,'search_button')  #搜索按钮
    bid_check_button=( By.XPATH,"//div[@class='piaofu']//a[2]")  #审核按钮
    bid_delete=(By.XPATH,"//tbody[@id='product']/tr[3]/td[11]/a") #物资删除，发布的标书因数据问题第2行没有物资数量和单价
    bid_modify_reason=(By.ID,'draft_remark')  #标书修改原因
    bid_select_check=(By.ID,'author_0')   #审核操作  0 待审核 1审核通过 2审核未通过
    bid_save=(By.XPATH,"//div[@class='out_right']/a[2]")  #保存

    margin_manage=(By.XPATH,"//h3[@headerindex='3h']")     #保证金管理
    #合同相关页面元素
    contract_manage=(By.XPATH,"//h3[@headerindex='4h']")   #合同管理
    contract_view=(By.XPATH,"//a[text()='合同查看']")
    contract_txt=(By.ID,"txtname")
    contract_search_button=(By.ID,"search_button")
    contract_check=(By.XPATH,"//a[@title='审核']")
    #合同审核详情页
    contract_select=(By.ID,"shstate")   #审核选项
    #value=1 审核通过  value=2 审核不通过  默认审核通过，可不选
    contract_confirm=(By.ID,"btn_submit")

    order_manage=(By.XPATH,"//h3[@headerindex='5h']")     #订单管理

    instock_manage_content=(By.XPATH,"//h3[@headerindex='6h']")   #入库管理
    instock_manage=(By.XPATH,"//a[@title='入库管理']")
    instokc_search_input=(By.ID,"txtname")  #搜索框
    instock_search=(By.ID,"search_button")   #搜索按钮
    instock_check=(By.XPATH,"//a[@title='审核']")
    instock_check_select=(By.ID,"checkopt")
    #value=1  审核通过   value=5 审核未通过
    instock_save=(By.ID,"submit_button")

    invoice_manage_content=(By.XPATH,"//h3[@headerindex='7h']")   #发票管理
    invoice_manage=(By.XPATH,"//a[@title='发票管理']")
    invoice_state=(By.ID,"state")
    invoice_search_input=(By.ID,"txtname")
    invoice_search=(By.ID,"search_button")
    invoice_check=(By.XPATH,"//a[@title='审核']")
    invoice_check_select=(By.ID,"checkopt")
    #value=1 审核通过  value=7 审核未通过
    invoice_submit=(By.ID,"submit_button")

    def check_billing(self,number):
        self.click(self.billing_manage)
        self.click(self.billing_pur)
        self.send_keys(self.billing_search_text,number)
        self.click(self.billing_search_button)
        self.click(self.billing_check)
        self.select_by_value(self.billing_check_select,"1")
        self.click(self.billing_save)
        time.sleep(2)
        self.accept()

    def check_bid(self,bid_number,bid_reason='审核通过'):
        self.click(self.bid_tend_manage)
        self.click(self.bid_public_check)
        self.send_keys(self.bid_search_input,bid_number)
        self.click(self.bid_search)
        time.sleep(1)
        self.click(self.bid_check_button)
        self.click(self.bid_delete)
        self.send_keys(self.bid_modify_reason,bid_reason)
        self.select_by_value(self.bid_select_check,'1')
        self.click(self.bid_save)
        time.sleep(2)
        self.accept()

    def enter_instock(self):
        self.click(self.instock_manage_content)
        self.click(self.instock_manage)

    def check_instock(self,instock_number):    #审核入库单
        self.send_keys(self.instokc_search_input,instock_number)
        self.click(self.instock_search)
        time.sleep(2)
        self.click(self.instock_check)
        self.select_by_value(self.instock_check_select,"1")
        self.click(self.instock_save)
        time.sleep(2)
        self.accept()

    def check_contract(self,number):

        self.click(self.contract_manage)
        self.click(self.contract_view)
        self.send_keys(self.contract_txt,number)
        self.click(self.contract_search_button)
        self.click(self.contract_check)
        self.scroll()
        time.sleep(2)
        self.click(self.contract_confirm)
        time.sleep(2)
        self.accept()

    def enter_invoice(self):
        self.click(self.invoice_manage_content)
        self.click(self.invoice_manage)

    def check_invoice(self,invoice_code):    #审核发票
        self.send_keys(self.invoice_search_input,invoice_code)
        self.click(self.invoice_search)
        self.click(self.invoice_check)
        self.select_by_value(self.invoice_check_select,"1")
        self.click(self.invoice_submit)
        time.sleep(1)
        self.accept()







