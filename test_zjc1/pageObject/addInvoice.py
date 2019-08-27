from configer.basePage import BasePage
from selenium.webdriver.common.by import By
import os,time
class AddInvoice(BasePage):
    enter_manage=(By.XPATH,"//a[@class='index-login__link mt16 goAdminPage']")  #进入管理首页
    pur_manage = (By.CSS_SELECTOR, "#n2>h3>span")  # 采购管理
    invoice_manage=(By.XPATH,"//li[@id='n2-6']/span")   #发票管理
    invoice_self=(By.XPATH,"//li[@id='n2-6-1']/a[1]") #自建项目
    add_invoice=(By.XPATH,"//input[@value='新增发票']")  #新增发票
    #新增发票页面元素
    select_contract=(By.XPATH,"//input[@value='选择合同']")
    search_input=(By.XPATH,"//div[@class='modal-search-right fr']/input[1]")  #搜索框
    search_button=(By.XPATH,"//input[@value='搜索']")  #搜索按钮
    select_e=(By.XPATH,"//a[@class='ml10 c48cead']")  #选中
    #select_confirm=(By.XPATH,"//a[@href='#']")
    invoice_type=(By.XPATH,"//div[@id='transportation1']/i[2]")   #发票方式
    invoice_code=(By.XPATH,"//input[@id='code0']")  #发票代码
    invoice_number=(By.XPATH,"//input[@id='code1']")   #发票号码
    invoice_date=(By.ID,"invoiceDate")
    invoice_rate=(By.XPATH,"//input[@id='taxRate3']")
    invoice_products=(By.XPATH,"//tbody[@id='invoiceTbody3']/tr/td[1]/input")
    invoice_rules=(By.XPATH,"//tbody[@id='invoiceTbody3']/tr/td[2]/input")
    invoice_unit=(By.XPATH,"//tbody[@id='invoiceTbody3']/tr/td[3]/input")
    invoice_num=(By.XPATH,"//tbody[@id='invoiceTbody3']/tr/td[4]/input")
    invoice_price=(By.XPATH,"//tbody[@id='invoiceTbody3']/tr/td[5]/input")

    invoice_attach=(By.XPATH,"//button[@id='selectfiles1']")
    # attach_form=(By.NAME,"kindeditor_upload_iframe_1523602709522")
    # attach_scan=(By.XPATH,"//form/div/div")
    attach_submit=(By.XPATH,"//input[@value='确定']")
    alert_comfirm=(By.XPATH,"//div[@class='dialog__footer']/a[2]")
    success_confirm=(By.XPATH,"//div[@class='dialog__footer']/a")

    invoice_state=(By.XPATH,"//a[@status='6']")
    loc_invoice_num=(By.XPATH,"//table[@class='list-table list-table-cover']/tbody/tr[%s]/td/div[@class='textleft pl15']")
    #新增发票
    def addInvoice(self,text,code,number,date,rate,product,rule,unit,num,price,cmd):
        self.click(self.enter_manage)
        self.click(self.pur_manage)
        self.click(self.invoice_manage)
        self.click(self.invoice_self)
        self.click(self.add_invoice)
        self.click(self.select_contract)
        self.send_keys(self.search_input,text)
        self.click(self.search_button)
        time.sleep(3)
        self.click(self.select_e)
        time.sleep(2)
        self.move_to_element(self.invoice_type)
        self.click(self.invoice_type)
        self.send_keys(self.invoice_code,code)
        self.send_keys(self.invoice_number,number)
        self.send_date(self.invoice_date, date)
        self.send_keys(self.invoice_rate,rate)
        self.send_keys(self.invoice_products,product)
        self.send_keys(self.invoice_rules,rule)
        self.send_keys(self.invoice_unit,unit)
        self.send_keys(self.invoice_num,num)
        self.send_keys(self.invoice_price,price)
        self.click(self.invoice_attach)
        # self.switch_to_frame(self.attach_form)
        # self.click(self.attach_scan)
        time.sleep(2)
        os.system(cmd)
        # js1 = 'document.getElementByName("localUrl").removeAttribute("readonly")'
        # self.driver.execute_script(js1)
        # self.send_keys(self.attach_url,attach_url)
        self.click(self.attach_submit)
        self.click(self.alert_comfirm)
        self.click(self.success_confirm)

    def getInvoiceNumber(self):
        self.click(self.invoice_state)
        text=self.element_texts_all()
        return text

    def enter_invoice(self):
        self.click(self.enter_manage)
        self.click(self.pur_manage)
        self.click(self.invoice_manage)
        self.click(self.invoice_self)












