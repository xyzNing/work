from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class ContractPage(BasePage):
    loc_contract_self=(By.XPATH,"//li[@id='n2-3-1']/a")
    loc_contract_other=(By.XPATH,"//li[@id='n2-3-2']/a")
    loc_search_text=(By.ID,"searchInput")
    loc_search_button=(By.XPATH,"//p[@class='fr']/input[2]")
    loc_entry=(By.XPATH,"//a[@class='cff8d08']")  #录入合同按钮
    loc_traditional=(By.ID,"traditionContract")
    loc_electronic=(By.ID,"electronContract")
    #录入合同详情页内容
    loc_sign_date=(By.ID,"signTime")
    loc_icon1=(By.XPATH,"//div[@id='replenishType']/i[1]")   #合同实际编号，默认选中
    loc_icon2=(By.XPATH,"//div[@id='replenishType']/i[2]")   #合同实际名称
    loc_text=(By.XPATH,"//input[@id='replenishText']")
    loc_upload_button=(By.ID,"selectfiles1")
    loc_confirm=(By.XPATH,"//div[@class='btns-div']/input[2]")   #确定
    loc_success=(By.XPATH,"//div[@class='dialog__footer']/a")   #录入成功弹框的确定

    loc_traditional_div=(By.XPATH,"//li[@type='1']")  #传统合同标签
    loc_state1=(By.XPATH,"//ul[@id='traditionTab']//a[@state='4']")  #待审核
    loc_state2 = (By.XPATH, "//ul[@id='traditionTab']//a[@state='5']")  # 审核未通过
    loc_state3 = (By.XPATH, "//ul[@id='traditionTab']//a[@state='3']")  # 异议
    loc_contract_number=(By.XPATH,"//div[@class='textleft pl10']")   #合同编号

    def get_number(self):
        '''
        获取合同编号
        :return:
        '''
        time.sleep(1)
        self.click(self.loc_traditional_div)
        self.click(self.loc_state1)
        time.sleep(1)
        list_number=self.element_texts(self.loc_contract_number)
        contract_number=self.arr_sort(list_number)
        return contract_number

    def search_contract(self,number):
        '''
        传入number，查找对应的合同
        :param number:
        :return:
        '''
        self.click(self.loc_contract_self)
        self.send_keys(self.loc_search_text,number)
        self.click(self.loc_search_button)

    def create_contract(self,date,text):
        '''
        创建传统合同
        :param date: 日期
        :param text: 合同实际编号
        :return:
        '''
        self.click(self.loc_entry)
        self.click(self.loc_traditional)
        self.send_date(self.loc_sign_date,date)
        self.send_keys(self.loc_text,text)
        self.upload_pictures(self.loc_upload_button)
        self.click(self.loc_confirm)
        self.click(self.loc_success)
        time.sleep(1)


