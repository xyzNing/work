from public.basePage import BasePage
from selenium.webdriver.common.by import By
import time
zjc_login_url = ""
custom_login_url=""


class LoginPage(BasePage):
    selector_user = (By.ID,"user")
    selector_pw = (By.ID,"pass")
    selector_submit = (By.ID,"login")
    selector_login_custom=(By.ID,"submit_")
    selector_supply=(By.XPATH,"//li[@id='2']")
    selector_pur=(By.XPATH,"//p[@class='index-login__p']")
    selector_text=(By.XPATH,"//p[@class='index-login__p']")
    selector_dialog=(By.XPATH,"//div[@class='dialog__content-layout']")

    def u_input(self,username):
        self.send_keys(self.selector_user,username)

    def p_input(self,password):
        self.send_keys(self.selector_pw,password)

    def l_login(self):
        self.click(self.selector_submit)

    def pur_login(self,username,password):
        self.open(zjc_login_url)
        self.u_input(username)
        self.p_input(password)
        self.l_login()

# 供应商登录
    def sup_login(self,username,password):
        self.open(zjc_login_url)
        self.click(self.selector_supply)
        self.u_input(username)
        self.p_input(password)
        self.l_login()
        time.sleep(2)

# 客服登录
    def custom_login(self,username,password):
        self.open(custom_login_url)
        self.u_input(username)
        self.p_input(password)
        self.click(self.selector_login_custom)

    def get_text(self):
        return self.element_text(self.selector_text)

    def is_text(self,text):
        return self.text_in_element(self.selector_text,text)

    def alert_text(self,text):
        return self.text_in_element(self.selector_dialog,text)







