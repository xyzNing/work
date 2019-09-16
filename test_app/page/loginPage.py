from config.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class Login(BasePage):
    next=(By.ID,'com.zhujc.purchasedev:id/iv_next')
    click_login=(By.ID,'com.zhujc.purchasedev:id/riv_my_icon')
    login_user=(By.ID,'com.zhujc.purchasedev:id/et_login_name')
    login_passwd=(By.ID,'com.zhujc.purchasedev:id/et_login_pwd')
    login_confirm=(By.ID,'com.zhujc.purchasedev:id/bt_login_submit')
    login_company=(By.ID,"com.zhujc.purchasedev:id/tv_my_company")

    def login(self, user, passwd):
        # self.swipe_left()
        # time.sleep(5)
        # self.swipe_left()
        # self.click(self.next)
        self.click(self.click_login)
        self.send_text(self.login_user,user)
        self.send_text(self.login_passwd,passwd)
        self.click(self.login_confirm)

    def get_company_name(self):
        return self.get_ele_attribute(self.login_company,'text')
