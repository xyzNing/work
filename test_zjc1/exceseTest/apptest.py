from appium import webdriver
import time
desired_caps={
'platformName': 'Android',
                'platformVersion': '5.0',
                'deviceName': 'c2f8b612',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id("com.tencent.mm:id/iq").click()
# 输入内容搜索
time.sleep(3)
driver.find
driver.find_element_by_id('com.tencent.mm:id/hx').send_keys("yoyoketang")
# 点开公众号
time.sleep(3)
driver.find_element_by_id('com.tencent.mm:id/l7').click()

# 点公众号菜单-精品分类
time.sleep(3)
driver.find_elements_by_id('com.tencent.mm:id/aaq')[0].click()