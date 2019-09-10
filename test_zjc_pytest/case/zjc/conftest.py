import pytest
from pageObject.zjc import loginPage
@pytest.fixture()
def login_pur(driver,user='a100048',psw='zjc123456789'):
    login_page=loginPage.LoginPage(driver)
    login_page.pur_login(user,psw)

@pytest.fixture()
def login_sup(driver,user='b01158',psw='zjc123456'):
    login_page=loginPage.LoginPage(driver)
    login_page.sup_login(user,psw)

@pytest.fixture()
def login_cus(driver,user='custom232',psw='123456'):
    login_page=loginPage.LoginPage(driver)
    login_page.custom_login(user,psw)

@pytest.fixture()
def start_page(driver):
    driver.get("http://zjcbytest.zhutx.net/")
    driver.delete_all_cookies()
    driver.refresh()
