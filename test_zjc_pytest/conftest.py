import pytest
from selenium import webdriver
from public.log import Logger

mylog=Logger(logger="conf").getlog()
@pytest.fixture(scope='module')
def driver(request,browser='Firefox'):
    try:
        if browser=='Firefox':
            profile_dir=r"C:\Users\ning\AppData\Roaming\Mozilla\Firefox\Profiles\vug7kmnt.default-1558406072358"
            profile=webdriver.FirefoxProfile(profile_dir)
            driver=webdriver.Firefox(profile)
            mylog.info("打开火狐浏览器")
        elif browser=='Chrome':
            driver=webdriver.Chrome()
            mylog.info("打开谷歌浏览器")
        elif browser=='Ie':
            driver=webdriver.Ie()
            mylog.info("打开ie浏览器")
        else:
            print(u"请重新选择浏览器")
    except Exception as msg:
        print('%s' %msg)
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver
