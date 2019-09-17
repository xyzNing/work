import pytest
from pageObject.zjc.loginPage import LoginPage
import time
class TestLogin():

    def setup(self):
        self.user1=''
        self.pas1=''
        self.pas2=''
        self.text=u'你好，阳哥'
        self.text1=u'密码错误'

    @pytest.mark.usefixtures("start_page")
    def test_login(self,driver):
        self.login_page = LoginPage(driver)
        self.login_page.pur_login(self.user1,self.pas2)
        result=self.login_page.is_text(self.text)
        print(result)
        assert result

    @pytest.mark.usefixtures("start_page")
    def test_login1(self,driver):
        self.login_page = LoginPage(driver)
        self.login_page.pur_login(self.user1,self.pas1)
        time.sleep(2)
        result=self.login_page.alert_text(self.text1)
        print(result)
        assert result


if __name__ == '__main__':
    pytest.main(['-v','test_0_login.py'])

