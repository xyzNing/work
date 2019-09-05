# conding=utf-8
from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time

class BidManage(BasePage):
    loc_bid_self=(By.XPATH,"//li[@id='n2-2-1']/a")  #自建项目
    loc_bid_other=(By.XPATH,"//li[@id='n2-2-2']/a")  #挂入项目
    location_public_bid = (By.XPATH,"//input[@value='发布标书']")
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
    location_material_name=(By.XPATH,"//tbody[@id='bidProductTbody']/tr/td[1]/input")
    location_model=(By.XPATH,"//tbody[@id='bidProductTbody']/tr/td[2]/input")
    location_uint=(By.XPATH,"//tbody[@id='bidProductTbody']/tr/td[6]/input")
    location_amount=(By.XPATH,"//tbody[@id='bidProductTbody']/tr/td[7]/input")
    location_price=(By.XPATH,"//tbody[@id='bidProductTbody']/tr/td[8]/input")
    # 输入物资第2行
    material_name2 = (By.XPATH,".//*[@id='bidProductTbody']/tr[2]/td[1]/input")
    model2 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[2]/input")
    unit2 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[6]/input")
    amount2= (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[7]/input")
    price2= (By.XPATH, ".//*[@id='bidProductTbody']/tr[2]/td[8]/input")
    # 输入物资第3行
    material_name3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[1]/input")
    model3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[2]/input")
    unit3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[6]/input")
    amount3 = (By.XPATH, ".//*[@id='productTbody']/tr[3]/td[7]/input")
    price3 = (By.XPATH, ".//*[@id='bidProductTbody']/tr[3]/td[8]/input")

    location_bid_content=(By.ID,"bidContent")
    location_first_next=(By.CSS_SELECTOR,".next-btn")
    #招标要求
    tender_closing_time=(By.ID,"endTime")
    calibration_date=(By.ID,'confirmTime')
    entry_data=(By.ID,'forecastTime')
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
    location_pay_day = (By.XPATH,".//*[@id='payDaysLi']/div/i[1]")  #付款天数
    location_pay_way = (By.ID,"payway")  #付款方式
    location_invoice_type = (By.XPATH,".//*[@id='invoice_type']/i[2]")   #发票要求
    location_is_deposit = (By.XPATH, "//li[@id='depositLi']/div/i[1]")  # 是否保证金   1不需要 2需要
    location_is_deposit2=(By.XPATH,"//li[@id='depositLi']/div/i[2]")  #是否保证金   1不需要 2需要
    location_money=(By.XPATH,"//li[@id='depositBox']/input")   #标书保证金金额
    location_second_next = (By.XPATH,"//input[@value='下一步']")   #下一步
    location_public_button=(By.XPATH,"//input[@value='发布标书']")
    public_tender = (By.ID,'addBidBtn')
    #选择金融产品
    financial_product=(By.XPATH,".//li[@id='260']//div[@class='poa cursor opens']")
    financia_day=(By.XPATH,".//li[@id='260']//input[@name='paydays']")
    public=(By.ID,"addBidBtn")
    confirm3=(By.XPATH,"//div[@class='btns-div']/input[4]")  #金融标书确认按钮，不管是否时金融标书

    #处理发布标书成功后的弹框
    loc_comfirm = (By.ID, 'noNeedCreateBid')  # 不需要并发布标书
    bid_success=(By.XPATH,"//div[@class='dialog__footer']/a")  #确定
    loc_state = (By.XPATH, "//li[@state='3']/a")   #
    loc_number = (By.XPATH, "//div[@class='textleft pl15']")  #标书编号
    #搜索相关
    loc_search_text=(By.ID,"searchInput")
    loc_search_button=(By.XPATH,"//p[@class='fr']/input[@value='搜索']")
    #定标相关
    loc_bid_confirm=(By.XPATH,"//a[text()='定标']")
    loc_select_suppier=(By.XPATH,"//input[@value='+选择供应商']")
    loc_suppier_name=(By.XPATH,"//td[@class='name']")  #选择中标的供应商
    loc_ensure=(By.XPATH,"//div[@class='btns-div']/input[@value='确定']")
    loc_next=(By.XPATH,"//input[@value='下一步']")
    loc_start1=(By.XPATH,"//ul[@class='judge-ul']/li[1]/ul/li[5]")  #服务态度
    loc_start2=(By.XPATH,"//ul[@class='judge-ul']/li[2]/ul/li[5]")   #价格合理度
    loc_start3 = (By.XPATH,"//ul[@class='judge-ul']/li[3]/ul/li[5]")   #公司资质
    loc_coment=(By.XPATH,"//ul[@class='judge-ul']/li[4]/textarea")   #总体评价
    loc_complete=(By.XPATH,"//input[@value='完成']")

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
        self.send_keys(self.location_material_name,materialname)
        self.send_keys(self.location_model, model)
        self.send_keys(self.location_uint, unit)
        self.send_keys(self.location_amount, amount)
        self.send_keys(self.location_price, price)
        # self.send_keys(self.material_name2,materialname)
        # self.send_keys(self.model2,model)
        # self.send_keys(self.unit2,unit)
        # self.send_keys(self.amount2,amount)
        # self.send_keys(self.price2,price)

    def input_bid_content(self,content):
        self.send_keys(self.location_bid_content,content)
        self.click(self.location_first_next)

    def input_date(self,date1,date2,date3):
        js1= 'document.getElementById("endTime").removeAttribute("readonly")'
        js2='document.getElementById("confirmTime").removeAttribute("readonly")'
        js3='document.getElementById("forecastTime").removeAttribute("readonly")'
        self.driver.execute_script(js1)
        self.driver.execute_script(js2)
        self.driver.execute_script(js3)
        self.send_keys(self.tender_closing_time,date1)
        self.send_keys(self.calibration_date,date2)
        self.send_keys(self.entry_data,date3)


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

    def base_info(self,bidname, linkname, linkphone, name, model, unit, amount, price, content):
        self.bid_project()
        self.bid_name(bidname)
        self.select_billing_info()
        self.input_linkman(linkname, linkphone)
        self.input_material(name,model,unit,amount,price)
        self.input_bid_content(content)

    def bid_require(self,date1,date2,date3,text):
        self.input_date(date1,date2,date3)
        self.click(self.sent_sample)
        self.click(self.sent_product)
        self.click(self.quote_type)
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

    def get_bid_number(self):
        '''
       获取标书编号，目前返回的时当前页面所有的标书编号
       :return: 标书编号
        '''
        number = self.element_texts(self.loc_number)
        return number

    def click_submit(self):
        self.click(self.location_public_button)
        time.sleep(5)
        self.click(self.loc_comfirm)
        time.sleep(1)
        self.click(self.bid_success)

    def search_bid(self,number):
        '''
        根据输入的标书编号，名称等搜索标书
        :param number:
        :return:
        '''
        self.send_keys(self.loc_search_text,number)
        self.click(self.loc_search_button)
        time.sleep(1)

    def bid_confirm(self,number,text):
        '''
        定标流程，单个供应商中标
        :param text: 评价供应商的内容
        :return:
        '''
        self.click(self.loc_bid_self)
        self.search_bid(number)
        self.click(self.loc_bid_confirm)
        self.click(self.loc_select_suppier)
        self.click(self.loc_suppier_name)
        self.click(self.loc_ensure)
        self.click(self.loc_next)
        self.click(self.loc_start1)
        self.click(self.loc_start2)
        self.click(self.loc_start3)
        self.send_keys(self.loc_coment,text)
        self.click(self.loc_complete)
        self.click(self.bid_success)















