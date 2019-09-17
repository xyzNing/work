from public.basePage import BasePage
from selenium.webdriver.common.by import  By
import os
import time
class Instock(BasePage):
    loc_add_instock=(By.XPATH,"//input[@value='单']")
    loc_select_contract=(By.XPATH,"//input[@value='同']")
    loc_input_search=(By.XPATH,"//input[@id='archInput1']")
    loc_search=(By.XPATH,"//div[@id='chosontract']//div[@class='modal-search-right fr']//input[@value='搜索']")
    loc_select_button=(By.XPATH,"//i[@css='icon radio radio-no']")
    loc_enter=(By.XPATH,"//div[@id='chosentract']//div[@class='btns-div']//input[@value='确定']")
    loc_materials_name=(By.XPATH,"//ody[@id='pductTbody2']/tr/td[1]/input")
    loc_amount=(By.XPATH,"//tbody[@id='produTbody2']/tr/td[6]/input")
    loc_unit=(By.XPATH,"//tbody[@id='producbody2']/tr/td[7]/input")
    loc_price=(By.XPATH,"//tbody[@id='pucbody2']/tr/td[8]/input")
    loc_sum_money=(By.XPATH,"//tbody[@id='productTbody2']/tr/td[9]/input")
    loc_instock_time2 = (By.ID, "to")
    loc_pay_time=(By.ID,"prePayDate")
    loc_operator=(By.XPATH,"//input[@id='opera']")
    loc_upload_attachment=(By.XPATH,"//button[@id='sefiles1']")
    loc_submit=(By.XPATH,"//input[@value='提交']")
    loc_dialog_enter=(By.XPATH,"//a")

    loc_instock_num=(By.XPATH,"//div[@class='teft pl15']")

    def selectContract(self,htnumber):
        self.click(self.loc_add_instock)
        self.click(self.loc_select_contract)
        self.send_keys(self.loc_input_search,htnumber)
        self.click(self.loc_search)
        time.sleep(1)
        self.click(self.loc_select_button)
        self.click(self.loc_enter)

    def inputMaterials(self,name,model,amount,unit,price):
        self.send_keys(self.loc_materials_name,name)
        self.send_keys(self.loc_models,model)
        self.send_keys(self.loc_amount,amount)
        self.send_keys(self.loc_unit,unit)
        self.send_keys(self.loc_price,price)

    def public_instock(self,htnumber,name,model,amount,unit,price,time1,time2,paytime,operator):
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

    def get_instock_number(self):
        self.click(self.loc_audit)
        time.sleep(2)
        number_list=self.element_texts(self.loc_instock_num)
        new_list=self.arr_sort(number_list)
        return new_list





