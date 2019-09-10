from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class BillingInfo(BasePage):
    loc_bill_info=(By.XPATH,"//li[@id='n5-4']/a")
    loc_add_bill=(By.XPATH,"//input[@value='新增开票信息']")
    #新增开票信息页面元素
    loc_title=(By.ID,"title")
    loc_province = (By.ID, "province")
    loc_province_info = (By.XPATH, "//li[@code='11']")  # 北京
    loc_city = (By.ID, "city")
    loc_city_info = (By.XPATH, "//li[@code='1101']")  # 市辖区
    loc_area = (By.ID, "area")
    loc_area_info = (By.XPATH, "//li[@code='110101']")  # code=110101  东城区
    loc_addr = (By.ID, "address")
    loc_postcode=(By.ID,"postcode")   #邮政编号，非必填
    loc_taxno=(By.ID,"taxno")
    loc_financetel2=(By.ID,"financetel2")
    loc_linkman=(By.ID,"linkman")
    loc_bank=(By.ID,"bank")
    loc_account=(By.ID,"account")
    loc_shortname=(By.ID,"shortname")
    loc_submit=(By.XPATH,"//input[@value='提交']")
    loc_success=(By.XPATH,"//div[@class='dialog__footer']/a")
    loc_shortname_text=(By.XPATH,"//div[@class='textleft pl15']")

    def create_billing_info(self,title,address,taxno,telphone,linkman,bank,account,shortname):
        self.click(self.loc_bill_info)
        self.click(self.loc_add_bill)
        self.send_keys(self.loc_title,title)
        self.click(self.loc_province)
        self.click(self.loc_province_info)
        self.click(self.loc_city)
        self.click(self.loc_city_info)
        self.click(self.loc_area)
        self.click(self.loc_area_info)
        self.send_keys(self.loc_addr,address)
        self.send_keys(self.loc_taxno,taxno)
        self.send_keys(self.loc_financetel2,telphone)
        self.send_keys(self.loc_linkman,linkman)
        self.send_keys(self.loc_bank,bank)
        self.send_keys(self.loc_account,account)
        self.send_keys(self.loc_shortname,shortname)
        self.click(self.loc_submit)
        self.click(self.loc_success)
        time.sleep(1)

    def get_shortname(self):
        text_list=self.element_texts(self.loc_shortname_text)
        return text_list



