from selenium.webdriver.common.by import By
from config.basePage import BasePage
import random
import time
class PurchasePage(BasePage):
    purchase=(By.ID,'com.zhujc.purchasedev:id/ll_main_info')

    check_project=(By.ID,'com.zhujc.purchasedev:id/bt_cg_shxm')
    authorize_tender=(By.ID,'com.zhujc.purchasedev:id/bt_cg_sqbs')
    review_tender=(By.ID,'com.zhujc.purchasedev:id/bt_cg_fhbs')

    new_project=(By.ID,'com.zhujc.purchasedev:id/bt_cg_xjxm')
    issue_tender=(By.ID,'com.zhujc.purchasedev:id/bt_cg_fbbs')   #发布标书
    tender_discussion=(By.ID,'com.zhujc.purchasedev:id/bt_cg_yb')

    bid_confirm=(By.ID,'com.zhujc.purchasedev:id/bt_cg_db')
    contract_create=(By.ID,'com.zhujc.purchasedev:id/bt_cg_htlr')

    order_create=(By.ID,'com.zhujc.purchasedev:id/bt_cg_xzdd')
    instock_create=(By.ID,'com.zhujc.purchasedev:id/bt_cg_xzrk')
    invoice_create=(By.ID,'com.zhujc.purchasedev:id/bt_cg_xzfp')

    def enter_purchase(self):
        self.click(self.purchase)

    def start_pub_bid(self):
        self.click(self.issue_tender)

    def start_pub_project(self):
        self.click(self.new_project)