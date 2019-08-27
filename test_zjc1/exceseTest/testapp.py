from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired={
    'platformName':'Android',
    'deviceName':'c2f8b612',
    'automationName': 'Uiautomator2',
    'platformVersion':'5.0',
    'appPackage':'com.zhujc.supplier',
    'appActivity':'com.zhuke.zjc.sup.splash.SplashActivity'
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired)
time.sleep(5)
locat=(By.ID,"com.zhujc.supplier:id/rb_mine")
element=WebDriverWait(driver,5).until(EC.presence_of_element_located(locat))
element.click()
# driver.find_element((By.ID,"com.zhujc.supplier:id/rb_mine"))
# driver.find_element_by_id('com.zhujc.supplier:id/rb_mine').click()
driver.find_element_by_id('com.zhujc.supplier:id/iv_avatar').click()
driver.find_element_by_id('com.zhujc.supplier:id/et_telephone').clear().send_keys('13937949014')
driver.find_element_by_id('com.zhujc.supplier:id/et_password').clear().send_keys('zjc123456')
driver.tap([(77,1009),(1003,1147)],500)
time.sleep(5)
driver.find_element_by_id('com.zhujc.supplier:id/cb_check').click()
driver.find_element_by_id('com.zhujc.supplier:id/tv_confirm').click()
