from public.basePage import BasePage
from selenium.webdriver.common.by import By
import os,time
class Invoice(BasePage):
    enter_manage=(By.XPATH,"//a[@class='index-login__link mt16 goAdminPage']")  #进入管理首页
    pur_manage = (By.CSS_SELECTOR, "#n2>h3>span")  # 采购管理
    invoice_manage=(By.XPATH,"//li[@id='n2-6']/span")   #发票管理
    invoice_self=(By.XPATH,"//li[@id='n2-6-1']/a[1]") #自建项目

    loc_add_invoice=(By.XPATH,"//input[@value='新增发票']")  #新增发票
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

    invoice_hang = (By.XPATH, "//li[@id='n2-6-2']/a")  # 挂入项目
    invoice_search_input = (By.XPATH, "//input[@id='searchInput']")  # 输入需要搜索的内容
    invoice_search_button = (By.XPATH, "//input[@value='搜索']")  # 搜索按钮
    invoice_ensure_button = (By.XPATH, "//p[@class='overhidden']/a")  # 确认
    invoice_ensure = (By.XPATH, "//input[@value='确认发票']")
    invoice_dialog_comfirm = (By.XPATH, "//div[@class='dialog__footer']/a")

    #新增发票
    def add_invoice(self,text,code,number,date,rate,product,rule,unit,num,price,):
        '''
        新增发票
        :param text: 合同编号，通过合同编号搜索到该合同
        :param code:发票代码
        :param number:发票号码
        :param date:开票日期
        :param rate:税率
        :param product:货物或应税劳务、服务名称
        :param rule:规则型号
        :param unit:单位
        :param num:数量
        :param price:单价
        :param cmd:
        :return:
        '''
        # self.click(self.enter_manage)
        # self.click(self.pur_manage)
        # self.click(self.invoice_manage)
        # self.click(self.invoice_self)
        self.click(self.loc_add_invoice)
        self.click(self.select_contract)
        self.send_keys(self.search_input,text)
        self.click(self.search_button)
        time.sleep(2)
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
        self.upload_pictures(self.invoice_attach)
        self.click(self.attach_submit)
        self.click(self.alert_comfirm)
        self.click(self.success_confirm)

    def getInvoiceNumber(self):
        '''
        获取发票的编号，写入excel，后面用来客服审核
        :return:
        '''
        self.click(self.invoice_state)
        time.sleep(1)
        text=self.element_texts_all()
        return text
    #
    # def enter_invoice(self):
    #     self.click(self.enter_manage)
    #     self.click(self.pur_manage)
    #     self.click(self.invoice_manage)
    #     self.click(self.invoice_self)

    #确认发票
    def ensure_invoice(self, text):
        '''
        确认发票，传入发票的编号
        :param text: 发标编号
        :return:
        '''
        self.send_keys(self.invoice_search_input, text)
        self.click(self.invoice_search_button)
        time.sleep(1)
        self.click(self.invoice_ensure_button)
        self.click(self.invoice_ensure)
        self.click(self.invoice_dialog_comfirm)













