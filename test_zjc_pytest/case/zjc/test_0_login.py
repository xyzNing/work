import pytest
from pageObject.zjc.loginPage import LoginPage
import time
class TestLogin():
    @pytest.fixture(scope='function',autouse=True)
    def start_page(self,driver):
        driver.get("http://zjcbytest.zhutx.net/")
        driver.delete_all_cookies()
        driver.refresh()

    def setup(self,):
        self.user1='a100048'
        self.pas1='123456'
        self.pas2='zjc123456789'
        self.text=u'你好，阳哥'
        self.text1=u'密码错误'

    def test_login(self,driver):
        self.login_page = LoginPage(driver)
        self.login_page.pur_login(self.user1,self.pas2)
        result=self.login_page.is_text(self.text)
        print(result)
        assert result


    def test_login1(self,driver):
        self.login_page = LoginPage(driver)
        self.login_page.pur_login(self.user1,self.pas1)
        time.sleep(2)
        result=self.login_page.alert_text(self.text1)
        print(result)
        assert result



if __name__ == '__main__':
   pytest.main(['-v','test_0_login.py'])
