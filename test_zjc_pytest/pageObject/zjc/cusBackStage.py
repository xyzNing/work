#-*- coding=utf-8 -*-
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class CusBackStage(BasePage):
    user_manage=(By.XPATH,"//h3[@headerindex='0h']")
    billing_manage=(By.XPATH,"//h3[@headerindex='1h']")
    billing_pur=(By.XPATH,"//a[text()='开票信息']")
    billing_search_text=(By.ID,"txtname")
    billing_search_button=(By.ID,"search_button")
    billing_check=(By.XPATH,"//a[text()='审核']")
    billing_check_select=(By.ID,"checkopt")

    billing_save=(By.ID,"submit_button")

    bid_tend_manage=(By.XPATH,"//h3[@headerindex='2h']")
    bid_public_check=(By.XPATH,"//a[@title=审核']")
    bid_search_input=(By.XPATH,"//input[@id='txtname']")
    bid_search=(By.ID,'search_button')
    bid_check_button=( By.XPATH,"//div[@class='piaofu']/")
    bid_delete=(By.XPATH,"//tbody[@id='product']/tr[3]//a")
    bid_modify_reason=(By.ID,'draft_remark')
    bid_select_check=(By.ID,'author_0')
    bid_save=(By.XPATH,"//div[@class='out_right']/a[2]")

    margin_manage=(By.XPATH,"//h3[@headerindex='3h']")

    contract_manage=(By.XPATH,"//h3[@headerindex='4h']")
    contract_view=(By.XPATH,"//a[text()='查看']")
    contract_txt=(By.ID,"txtname")
    contract_search_button=(By.ID,"search_button")
    contract_check=(By.XPATH,"//a[@title='审核']")

    contract_select=(By.ID,"shstate")

    contract_confirm=(By.ID,"btn_submit")

    order_manage=(By.XPATH,"//h3[@headerindex='5h']")

    instock_manage_content=(By.XPATH,"//h3[@headerindex='6h']")
    instock_manage=(By.XPATH,"//a[@title='管理']")
    instokc_search_input=(By.ID,"txtname")
    instock_search=(By.ID,"search_button")
    instock_check=(By.XPATH,"//a[@title='审核']")
    instock_check_select=(By.ID,"checkopt")

    instock_save=(By.ID,"submit_button")

    invoice_manage_content=(By.XPATH,"//h3[@headerindex='7h']")
    invoice_manage=(By.XPATH,"//a[@title='管理']")
    invoice_state=(By.ID,"state")
    invoice_search_input=(By.ID,"txtname")
    invoice_search=(By.ID,"search_button")
    invoice_check=(By.XPATH,"//a[@title='审核']")
    invoice_check_select=(By.ID,"checkopt")

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

    def check_instock(self,instock_number):
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

    def check_invoice(self,invoice_code):
        self.send_keys(self.invoice_search_input,invoice_code)
        self.click(self.invoice_search)
        self.click(self.invoice_check)
        self.select_by_value(self.invoice_check_select,"1")
        self.click(self.invoice_submit)
        time.sleep(1)
        self.accept()







