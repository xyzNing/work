from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class AssetCenter(BasePage):
    loc_contract=(By.XPATH,"//div[@class='w100p acdata pa pb30  pt40']//a[contains(text(),'上传')]")

    loc_instock=(By.XPATH,"//div[@class='mt15 fl w40p']//a[contains(text(),'上传')]")
    sel_contract=(By.XPATH,"//input[@value='选择合同']")
    search_text=(By.ID,'searchInfo')
    search_button=(By.ID,'search')
    select_button=(By.XPATH,"//td[@class='left']/span/i[2]")
    ensure=(By.ID,'ensure')
    ins_materials=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]//input[@name='invocename']")
    ins_models=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]/td[1]")
    ins_unit=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]/td[6]")
    ins_number=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]/td[7]")
    ins_price=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]/td[8]")
    ins_date=(By.ID,'start_time')
    ins_pay_date=(By.ID,'end_time')
    ins_operarot=(By.ID,'arrangements_man')
    attach=(By.ID,'twoattach')
    submit=(By.ID,'submit')
    back = (By.XPATH, "//div[@class='dialog__footer']/a[1]")

    loc_invoice=(By.XPATH,"//div[@class='mt15 fr w40p']//a[contains(text(),'上传')]")
    invoice_code=(By.ID,'word')
    invoice_number=(By.ID,'code')
    invoice_date=(By.ID,'data')
    invoice_tax=(By.ID,'percentage')
    inv_sum=(By.XPATH,"//tbody[@id='productTbody2']/tr[1]//input[@name='invoiceSum']")

    def add_instock(self,htnum,date1,date2,operator):
        self.click(self.loc_instock)
        self.click(self.sel_contract)
        self.send_keys(self.search_text,htnum)
        self.click(self.search_button)
        time.sleep(1)
        self.click(self.select_button)
        time.sleep(1)
        self.click(self.ensure)
        # self.send_keys(self.ins_materials,name)
        # self.send_keys(self.ins_models,model)
        # self.send_keys(self.ins_unit,unit)
        # self.send_date(self.ins_number,amount)
        # self.send_keys(self.ins_price,price)
        self.send_date(self.ins_date,date1)
        self.send_date(self.ins_pay_date,date2)
        self.click(self.ins_operarot)
        self.send_keys(self.ins_operarot,operator)
        self.click(self.attach)
        self.send_pictures()
        self.click(self.submit)
        self.click(self.back)

    def add_invoice(self,htnum,code,number,date,tax,name,sum):
        self.click(self.loc_invoice)
        self.choose(self.sel_contract,self.search_text,htnum,self.search_button,self.select_button,self.ensure)
        self.send_keys(self.invoice_code,code)
        self.send_keys(self.invoice_number,number)
        self.send_date(self.invoice_date,date)
        self.send_keys(self.invoice_tax,tax)
        self.send_keys(self.ins_materials,name)
        self.send_keys(self.inv_sum,sum)
        self.click(self.attach)
        self.send_pictures()
        self.click(self.submit)
        self.click(self.back)
        time.sleep(2)




