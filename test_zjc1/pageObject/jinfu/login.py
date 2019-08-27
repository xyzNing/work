from selenium.webdriver.common.by import By
from configer.basePage import BasePage
class LoginJF(BasePage):
    loc_pur=(By.XPATH,"//li[@code='2001']")
    loc_sup=(By.XPATH,"//li[@code='2002']")
