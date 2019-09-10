from pageObject.zjc.accountManage import Account
from pageObject.zjc.purBackStage import BackStage
import pytest
import random
class TestAccount():

    def setup(self):
        self.name='ss'
        self.phone='13937949'+str(random.randint(1,1000))
        self.position='经理'
        self.dept='ceshi'
        self.password='zjc123456'
        self.password2='zjc123456'
        self.company_name='分公司1'

    @pytest.mark.usefixtures("login_pur")
    def test_create_group(self,driver):
        self.back_page=BackStage(driver)
        self.back_page.enter_setting()
        self.account_page=Account(driver)
        self.account_page.create_group_subaccount(self.name,self.phone,self.position,
                                                  self.dept,self.password,self.password2)

    def test_create_subunit(self,driver):
        self.account_page = Account(driver)
        self.account_page.create_subunit_subaccount(self.company_name,self.dept,self.phone,
                                                    self.password,self.password2)

if __name__ == '__main__':
    pytest.mian['-v','test_1_2_create_account.py']