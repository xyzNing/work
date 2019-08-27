from configer.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class BidTenderPage(BasePage):
    bid_announcement=(By.XPATH,"//div[@class='clearfix']/a[2]")   #招标公告
    bid_search_input=(By.ID,"search-input")  #s搜索框
    bid_search_button=(By.ID,'search__btn') #查询按钮
    bid_tender_first=(By.XPATH,"//div[@class='bid-list__content-content']/ul/li[7]/div/p/a[2]") #我要投标
    bid_tender_second=(By.XPATH,"//div[@class='thod-btn']/a[2]")

    #报价须知页面
    quote_notice=(By.XPATH,"//div[@id='offerNoticeImg']/span/s[2]")  #勾选框
    quote_confirm=(By.XPATH,"//input[@id='offerNoticeBtn']") #确定

    #投标页面
    billing_information=(By.ID,"choseBillingBtn")  #开票信息
    billing_information_select=(By.XPATH,"//td[@class='w9']/i")   #选择开票信息
    billing_information_confirm=(By.XPATH,"//input[@id='selectBilling']")    #确定
    invoice_type=(By.ID,"//input[@id='selectBilling']")    #发票类型
    tax_rate=(By.ID,"taxRate")    #税率
    #报价单
    transportation1=(By.XPATH,"//div[@id='transportation1']/i[1]")  #是否已含运费  1 是 2否
    transportation2=(By.XPATH,"//div[@id='transportation2']/i[1]")    #是否已含税费和其他成本  1是 2否
    unit_price=(By.XPATH,"//input[@class='w75 mo-input itemPrice']")   #含税单价  多个
    actual_price=(By.ID,"money")    #实际报价
    business_man=(By.ID,"businessMan")   #业务联系人
    business_tel=(By.ID,'businessTel')   #联系人电话
    trading_rules=(By.XPATH,"//li[@id='theRules']/div/s[2]")    #交易细则
    submit_button=(By.XPATH,"//input[@id='modifyBtn']")      #提交
    alert_confirm=(By.XPATH,"//div[@class='dialog__footer']/a")  #弹框确定

    def bidTender(self,bid_number,rate,price1,price3,linkname,linkphone):
        # self.click(self.bid_announcement)

        self.send_keys(self.bid_search_input,bid_number)
        self.click(self.bid_search_button)
        self.click(self.bid_tender_first)
        self.switch_handel()
        self.click(self.bid_tender_second)
        self.move_to_element(self.quote_notice)
        self.click(self.quote_notice)
        sleep(1)
        self.click(self.quote_confirm)
        sleep(1)
        self.click(self.billing_information)
        print("222")
        sleep(1)
        self.click(self.billing_information_select)
        self.click(self.billing_information_confirm)
        self.send_keys(self.tax_rate,rate)
        self.click(self.transportation1)
        self.click(self.transportation2)
        self.send_keys_all(self.unit_price,price1)
        print('222')
        self.send_keys(self.actual_price,price3)
        self.send_keys(self.business_man,linkname)
        self.send_keys(self.business_tel,linkphone)
        self.click(self.trading_rules)
        self.click(self.submit_button)
        self.click(self.alert_confirm)


















