from pageObject.zjc.billingInfoManage import BillingInfo
from pageObject.zjc.purBackStage import BackStage
import pytest
from datetime import datetime
class TestBillingInfo():
    def setup(self):
        self.title=str(datetime.now().strftime("%y%m%d%H%M"))+"title"
        self.address="sss"
        self.taxno='4464'
        self.telphone='13937949012'
        self.linkman='王先生'
        self.bank="工商银行"
        self.account="4456933"
        self.shottname=str(datetime.now().strftime("%y%m%d%H%M"))+"shortname"

    @pytest.mark.usefixtures("login_pur")
    def test_create_billing(self,driver):
        self.back_page=BackStage(driver)
        self.back_page.enter_setting()
        self.page=BillingInfo(driver)
        self.page.create_billing_info(self.title,self.address,self.taxno,self.telphone,self.linkman,
                                      self.bank,self.account,self.shottname)
        text=self.page.get_shortname()
        self.page.write_excel(text[0:1],'billingInfo')

if __name__ == '__main__':
    pytest.main(['-v','test_1_3_create_billing_info.py'])
