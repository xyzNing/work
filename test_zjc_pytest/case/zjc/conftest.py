import pytest
from pageObject.zjc import loginPage
url=''


@pytest.fixture()
def login_pur(driver,user='',psw=''):
    login_page=loginPage.LoginPage(driver)
    login_page.pur_login(user,psw)


@pytest.fixture()
def login_sup(driver,user='',psw=''):
    login_page=loginPage.LoginPage(driver)
    login_page.sup_login(user,psw)


@pytest.fixture()
def login_cus(driver,user='c',psw=''):
    login_page=loginPage.LoginPage(driver)
    login_page.custom_login(user,psw)


@pytest.fixture()
def start_page(driver):
    driver.get(url)
    driver.delete_all_cookies()
    driver.refresh()
