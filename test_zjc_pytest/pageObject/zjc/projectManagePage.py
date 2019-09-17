from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class ProjectPage( BasePage):

    loc_project_self=(By.XPATH,"//li[@id='n2-1-1']/a")
    loc_project_other=(By.XPATH,"//li[@id='n2-1-2']/a")
    loc_public_project=(By.XPATH,"//input[@value='发布项目']")
    loc_project_name=(By.ID,"projectName")
    loc_project_desc=(By.ID,'projectDescription')
    loc_project_province=(By.ID,"projectProvince")
    loc_province=(By.XPATH,"//li[@code='11']")
    loc_project_city=(By.ID,"projectCity")
    loc_city=(By.XPATH,"//li[@code='1101']")
    loc_project_area=(By.ID,"projectArea")
    loc_area=(By.XPATH,"//li[@code='110101']")
    loc_project_addr=(By.ID,"projectAddress")
    loc_project_manager=(By.ID,"projectManager")
    loc_project_contract=(By.ID,"projectContact")
    loc_manage_unit=(By.ID,"administration")
    loc_unit=(By.XPATH,"//ul[@id='administrationList']/li[1]")
    loc_project_type=(By.ID,"projectType")
    loc_total_area=(By.ID,"totalSpace")
    loc_user_area=(By.ID,"useSpace")
    loc_project_cycle=(By.ID,"projectTime")  #非必填
    loc_select_picture=(By.ID,"selectfiles")
    loc_project_state=(By.ID,"projectState")
    # state=1 进行中 state=2 已结束 state=3 未进行
    loc_state=(By.XPATH,"//ul[@id='statusList']/li[1]")
    loc_project_money=(By.ID,"projectMoney")
    loc_submit=(By.XPATH,"//input[@value='提交']")
    loc_success=(By.XPATH,"//div[@class='dialog__footer']/a")

    loc_number=(By.XPATH,"//div[@class='textleft pl15']")   #项目编号
    loc_search_input=(By.ID,"searchInput")
    loc_search=(By.ID,'searchBtn')
    loc_check_state=(By.XPATH,"//a[@value='2']")
    loc_check=(By.XPATH,"//a[text()='审核']")
    loc_confirm=(By.XPATH,"//input[@value='确认']")


    def public_project(self,name,desc,addr,manager,phone,type,space,money):
        self.click(self.loc_project_self)
        self.click(self.loc_public_project)
        self.send_keys(self.loc_project_name,name)
        self.send_keys(self.loc_project_desc,desc)
        self.click(self.loc_project_province)
        self.click(self.loc_province)
        self.click(self.loc_project_city)
        self.click(self.loc_city)
        self.click(self.loc_project_area)
        self.click(self.loc_area)
        self.send_keys(self.loc_project_addr,addr)
        self.send_keys(self.loc_project_manager,manager)
        self.send_keys(self.loc_project_contract,phone)
        self.click(self.loc_manage_unit)
        self.click(self.loc_unit)
        self.send_keys(self.loc_project_type,type)
        self.send_keys(self.loc_user_area,space)
        self.upload_pictures(self.loc_select_picture)
        self.click(self.loc_project_state)
        self.click(self.loc_state)
        self.send_keys(self.loc_project_money,money)
        self.click(self.loc_submit)
        self.click(self.loc_success)

    def get_project_number(self):
        self.click(self.loc_check_state)
        number=self.element_texts(self.loc_number)
        return number

    def check_project(self,number):
        self.click(self.loc_project_other)
        self.send_keys(self.loc_search_input,number)
        self.click(self.loc_search)
        self.click(self.loc_check)
        self.click(self.loc_confirm)
        self.click(self.loc_success)
        time.sleep(1)












