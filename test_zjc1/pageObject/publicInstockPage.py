from configer.basePage import BasePage
from selenium.webdriver.common.by import  By
import os
import time
class PublicInstock(BasePage):
    loc_add_instock=(By.XPATH,"//input[@value='新增入库单']")
    loc_select_contract=(By.XPATH,"//input[@value='选择合同']")
    loc_input_search=(By.XPATH,"//input[@id='searchInput1']")
    loc_search=(By.XPATH,"//div[@id='choseContract']//div[@class='modal-search-right fr']//input[@value='搜索']")
    loc_select_button=(By.XPATH,"//i[@class='icon radio radio-no']")
    loc_enter=(By.XPATH,"//div[@id='choseContract']//div[@class='btns-div']//input[@value='确定']")
    loc_materials_name=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[1]/input")  #物资名称
    loc_models=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[2]/input")   #规则型号
    loc_amount=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[6]/input")   #数量
    loc_unit=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[7]/input")     #单位
    loc_price=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[8]/input")    #单价
    loc_sum_money=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[9]/input")   #金额
    loc_instock_time1=(By.ID,"from")
    loc_instock_time2 = (By.ID, "to")
    loc_pay_time=(By.ID,"prePayDate")
    loc_operator=(By.XPATH,"//input[@id='operator']")
    loc_upload_attachment=(By.XPATH,"//button[@id='selectfiles1']")
    loc_submit=(By.XPATH,"//input[@value='提交']")
    loc_dialog_enter=(By.XPATH,"//div[@class='dialog__footer']/a")

    loc_audit=(By.XPATH,"//a[@status='4']")   #待审核列表   0 全部 4待审核 5 审核未通过 1入库待评价 2已评价
    loc_instock_num=(By.XPATH,"//div[@class='textleft pl15']")
#选择合同
    def selectContract(self,htnumber):
        self.click(self.loc_add_instock)
        self.click(self.loc_select_contract)
        self.send_keys(self.loc_input_search,htnumber)
        self.click(self.loc_search)
        time.sleep(1)
        self.click(self.loc_select_button)
        self.click(self.loc_enter)
#收入物资
    def inputMaterials(self,name,model,amount,unit,price):
        self.send_keys(self.loc_materials_name,name)
        self.send_keys(self.loc_models,model)
        self.send_keys(self.loc_amount,amount)
        self.send_keys(self.loc_unit,unit)
        self.send_keys(self.loc_price,price)
        # self.send_keys(self.loc_sum_money)
#新增入库单
    def publicInstock(self,htnumber,name,model,amount,unit,price,time1,time2,paytime,operator):
        self.selectContract(htnumber)

        self.inputMaterials(name,model,amount,unit,price)
        self.send_date(self.loc_instock_time1,time1)
        self.send_date(self.loc_instock_time2,time2)
        self.send_date(self.loc_pay_time,paytime)
        self.send_keys(self.loc_operator,operator)
        self.click(self.loc_upload_attachment)
        os.system(r"C:\Users\ning\Desktop\SendPhoto.exe")
        self.click(self.loc_submit)
        self.click(self.loc_dialog_enter)

    def getInstockNumber(self):
        self.click(self.loc_audit)
        text=self.element_texts(self.loc_instock_num)
        return text





