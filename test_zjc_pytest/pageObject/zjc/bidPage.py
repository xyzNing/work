# conding=utf-8
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class PublicBid(BasePage):
    location_public_bid = (By.XPATH,"//p[@class='fr']/input[3]")
    #标书基本信息
    location_bid_type = (By.ID, "//div[@id='bidType'/i[1]")
    location_bid_project = (By.ID,"bidProject")
    location_project = (By.XPATH,"//ul[@id='bidProjectList']/li[1]")
    location_bid_name = (By.ID,"bidName")

    location_bid_method = (By.XPATH,".//*[@id='bidWay']/i[1]")
    #  askSupplier=(By.ID,"askSupplierButton")
    location_billing_info=(By.XPATH,"//input[@class='selectBtn w6 fl']")  #开票信息
    location_select_billing_info=(By.XPATH,".//*[@id='billingItem']/tr[1]/td[1]/i")  #选择开票信息
    location_billing_confirm =(By.XPATH,".//*[@id='choseBilling']/div[2]/div/input")
    location_link_name = (By.ID,'linkman')
    location_mobile_phone= (By.ID,'linkmanmob')
    location_select_material=(By.ID,"selectMaterialBtn")
    location_category_Ⅰ = (By.CSS_SELECTOR,".on>span")
    location_category_Ⅱ = (By.XPATH,".//*[@id='material-box']/div[2]/ul[2]/li[1]")
    location_is_category_Ⅱ=(By.XPATH,".//*[@id='material-box']/div[2]/ul[2]/li[1]/label/i")
    location_material_confirm = (By.XPATH,".//*[@id='material-box']/div[4]/button")
    # 输入物资第1行
    location_material_name=(By.CSS_SELECTOR,".w100.textleft")
    location_model=(By.XPATH,".//*[@id='bidProductTbody']/tr/td[2]/input")
    location_uint=(By.XPATH,".//*[@id='bidProductTbody']/tr/td[6]/input")
    location_amount=(By.XPATH,".//*[@id='bidProductTbody']/tr/td[7]/input")
    location_price=(By.XPATH,".//*[@id='bidProductTbody']/tr/td[8]/input")
    # 输入物资第2行
    material_name2 = (By.XPATH,".//*[@id='bidProductTbody']/tr[2]/td[1]/input")
    model2 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[2]/input")
    uint2 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[6]/input")
    amount2= (By.XPATH, ".//*[@id='productTbody']/tr[2]/td[7]/input")
    price2= (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[8]/input")
    # 输入物资第3行
    material_name3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[1]/input")
    model3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[2]/input")
    uint3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[6]/input")
    amount3 = (By.XPATH, ".//*[@id='productTbody']/tr[3]/td[7]/input")
    price3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[8]/input")

    location_bid_content=(By.ID,"bidContent")
    location_first_next=(By.CSS_SELECTOR,".next-btn")
    #招标要求
    tender_closing_time=(By.ID,"endTime")
    calibration_date=(By.ID,'confirmTime')
    sent_sample=(By.XPATH,".//*[@id='sentSampleLi']/div/i[1]")
    sent_product=(By.XPATH,".//*[@id='sentProductLi']/div/i[1]")

    province = (By.ID,"province")
    select_province = (By.XPATH,".//*[@id='addressLi']/div[1]/ul/li[1]")
    city = (By.ID,"city")
    select_city = (By.XPATH,".//*[@id='addressLi']/div[2]/ul/li[1]")
    area = (By.ID,"area")
    select_area = (By.XPATH,".//*[@id='addressLi']/div[3]/ul/li[1]")
    address = (By.ID,"address")

    quote_type = (By.XPATH,".//*[@id='quoteTypeLi']/div/i[1]")
    location_pay_day = (By.XPATH,".//*[@id='payDaysLi']/div/i[1]")
    location_pay_way = (By.ID,"payway")
    location_invoice_type = (By.XPATH,".//*[@id='invoice_type']/i[2]")   #发票要求
    location_is_deposit = (By.XPATH, "//li[@id='depositLi']/div/i[1]")  # 是否保证金   1不需要 2需要
    location_is_deposit2=(By.XPATH,"//li[@id='depositLi']/div/i[2]")  #是否保证金   1不需要 2需要
    location_money=(By.XPATH,"//li[@id='depositBox']/input")   #标书保证金金额
    location_second_next = (By.XPATH,"//*[@id='step2']/div[2]/input[3]")   #下一步
    location_public_button=(By.XPATH,"//input[@value='发布标书']")
    public_tender = (By.ID,'addBidBtn')
    #选择金融产品
    financial_product=(By.XPATH,".//li[@id='260']//div[@class='poa cursor opens']")
    financia_day=(By.XPATH,".//li[@id='260']//input[@name='paydays']")
    public=(By.ID,"addBidBtn")
    confirm3=(By.LINK_TEXT,"确认")

    #处理发布标书成功后的弹框
    bid_success=(By.XPATH,".//div[@class='dialog__footer']/a")

    # def public_bid(self):
    #     self.click(self.selector_public_bid)

    def bid_project(self):
        self.click(self.location_public_bid)
        self.click(self.location_bid_project)
        self.click(self.location_project)

    def bid_name(self, bidname ):
        self.send_keys(self.location_bid_name, bidname)
        # self.click(self.location_bid_type)
        self.click(self.location_bid_method)

    def select_billing_info(self):
        self.click(self.location_billing_info)
        self.click(self.location_select_billing_info)
        self.click(self.location_billing_confirm)

    def input_linkman(self, linkname , linkphone):
        self.send_keys(self.location_link_name,linkname)
        self.send_keys(self.location_mobile_phone,linkphone)

    def input_material(self, materialname, model, unit, amount, price):
        self.click(self.location_select_material)
        time.sleep(2)
        self.move_to_element(self.location_category_Ⅰ)
        time.sleep(2)
        self.move_to_element(self.location_category_Ⅱ)
        self.click(self.location_is_category_Ⅱ)
        self.click(self.location_material_confirm)

#         self.send_keys(self.materialName,name2)
#         self.send_keys(self.material1Model,model)
#         self.send_keys(self.uint,unit)
#         self.send_keys(self.amount,amount)
#         self.send_keys(self.price,price)
#
#         self.send_keys(self.materialName2, name3)
#         self.send_keys(self.material1Model2, model)
#         self.send_keys(self.uint2, unit)
#         self.send_keys(self.amount2, amount)
#         self.send_keys(self.price, price)

        self.send_keys(self.location_material_name,materialname)
        self.send_keys(self.location_model, model)
        self.send_keys(self.location_uint, unit)
        self.send_keys(self.location_amount, amount)
        self.send_keys(self.location_price, price)

    def input_bid_content(self,content):
        self.send_keys(self.location_bid_content,content)
        self.click(self.location_first_next)

    def input_date(self,date1,date2):
        js1= 'document.getElementById("endTime").removeAttribute("readonly")'
        js2='document.getElementById("confirmTime").removeAttribute("readonly")'
        self.driver.execute_script(js1)
        self.driver.execute_script(js2)

        self.send_keys(self.tender_closing_time,date1)
        self.send_keys(self.calibration_date,date2)

    def input_address(self,address):
        self.click(self.provice)
        self.click(self.provice1)
        self.click(self.city)
        self.click(self.city1)
        self.click(self.area)
        self.click(self.area1)
        self.send_keys(self.address,address)

    def pay_way(self,text):
        self.send_keys(self.location_pay_way,text)

    def invoice_type_money(self,money):
        self.click(self.location_invoice_type)
        self.click(self.location_is_deposit2)
        self.send_keys(self.location_money,money)


    def invoice_type(self):
        self.click(self.location_invoice_type)
        self.click(self.location_is_deposit)
        self.click(self.location_second_next)

    def click_submit(self):
        self.click(self.public_tender)
        self.click(self.bid_success)

    def base_info(self,bidname, linkname, linkphone, name, model, unit, amount, price, content):

        self.bid_project()
        self.bid_name(bidname)
        self.select_billing_info()
        self.input_linkman(linkname, linkphone)
        self.input_material(name,model,unit,amount,price)
        self.input_bid_content(content)

    def bid_request(self,date1,date2,text):
        self.input_date(date1,date2)
        self.click(self.sent_sample)
        self.click(self.sent_product)
        # self.input_address(address)
        self.click(self.quote_type)
        self.click(self.location_pay_day)
        self.pay_way(text)
        self.invoice_type()

    def bid_request1(self, date1, date2, text,money):
        self.input_date(date1, date2)
        self.click(self.sent_sample)
        self.click(self.sent_product)
        # self.input_address(address)
        self.click(self.quote_type)
        self.click(self.location_pay_day)
        self.pay_way(text)
        self.invoice_type_money(money)
        self.click(self.location_public_button)
        self.click(self.bid_success)


#选择金融产品并提交
    def select_fproduct(self,day):
        self.click(self.financial_product)
        self.send_keys(self.financia_day,day)
        self.click(self.public)
        self.click(self.bid_success)

    # def alert_accept(self):
    #     self.accept(self.bid_success)















