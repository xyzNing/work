from public.basePage import BasePage
from selenium.webdriver.common.by import By
class Account(BasePage):
    loc_subaccount_manage=(By.XPATH,"//li[@id='n5-3']/a")
    loc_add_account=(By.XPATH,"//input[@value='新增子账号']")
    loc_account_type=(By.XPATH,"//i[@state='2']")  #新增下属单位账号，默认为集团子账号
    loc_account_confirm=(By.XPATH,"//div[@class='modal-input-div']/input")  #确定
    #集团子账号下新增页面元素
    loc_name=(By.ID,"name")
    loc_phone=(By.ID,"phone")   #可通用
    loc_phone_err=(By.ID,"phoneErr")
    loc_position=(By.ID,"position")
    loc_dept=(By.ID,"dept")
    loc_password=(By.ID,"password")
    loc_confirm_passwd=(By.ID,"confirmPassword")
    loc_account_auth=(By.XPATH,"//div[@id='authDiv']/i")  #账号权限
    loc_confirm=(By.XPATH,"//input[@value='新增']")
    loc_confirm2=(By.XPATH,"//div[@class='dialog__footer']/a[2]")  #弹框中确认并设置权限
    loc_add_auth=(By.XPATH,"//span[@id='noAuth']/a")  #新增权限
    loc_all_project=(By.XPATH,"//li[@id='allProject']/i")  #项目权限
    loc_self_auth=(By.XPATH,"//li[@id='project']//p[@authid='15']/i")  #自建项目只给了项目查看权限
    loc_other_auth=(By.XPATH,"//li[@authid='18']/i[1]")  #挂入项目项目审核
    loc_auth_confirm=(By.XPATH,"//div[@class='chose-auth modal']//input[@value='确定']")
    loc_confirm_modify=(By.XPATH,"//input[@value='确认修改']")
    #下属单位子账号新增页面元素页面
    loc_company_name=(By.ID,"companyname")
    loc_manage_name=(By.ID,"listname")
    loc_submit=(By.ID,"addBtn")
    loc_success=(By.XPATH,"//div[@class='dialog__footer']/a")

    def create_group_subaccount(self,name,phone,position,dept,password,password2):
        '''
        新增集团子账号
        :param name: 姓名
        :param phone:手机号
        :param position:岗位名称
        :param dept:归属部门
        :param password:密码
        :param password2:确认密码
        :return:
        '''
        self.click(self.loc_subaccount_manage)
        self.click(self.loc_add_account)
        self.click(self.loc_account_confirm)
        self.send_keys(self.loc_name,name)
        self.send_keys(self.loc_phone,phone)
        while self.element_text(self.loc_phone_err)==u'该手机号已注册':
            self.send_keys(self.loc_phone)
        self.send_keys(self.loc_position,position)
        self.send_keys(self.loc_dept,dept)
        self.send_keys(self.loc_password,password)
        self.send_keys(self.loc_confirm_passwd,password2)
        self.click(self.loc_confirm)
        self.click(self.loc_confirm2)
        self.click(self.loc_add_auth)
        self.click(self.loc_all_project)
        self.click(self.loc_self_auth)
        self.click(self.loc_other_auth)
        self.click(self.loc_auth_confirm)
        self.click(self.loc_confirm_modify)
        self.click(self.loc_success)

    def create_subunit_subaccount(self,company_name,manage_name,phone,password,password2):
        '''
        新增下属单位子账号
        :param company_name: 公司名称
        :param manage_name: 管理人姓名
        :param phone:手机号
        :param password:密码
        :param password2:确认密码
        :return:
        '''
        self.click(self.loc_subaccount_manage)
        self.click(self.loc_add_account)
        self.click(self.loc_account_type)
        self.click(self.loc_account_confirm)
        self.send_keys(self.loc_company_name,company_name)
        self.send_keys(self.loc_manage_name,manage_name)
        self.send_keys(self.loc_phone,phone)
        self.send_keys(self.loc_password,password)
        self.send_keys(self.loc_confirm_passwd,password2)
        self.click(self.loc_submit)
        self.click(self.loc_success)









