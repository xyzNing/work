from pageObject.jinfu.assetCenter import AssetCenter
import datetime
import pytest
class TestAssertCenter():
    def setup(self):
        self.url="http://paybytest.zhutx.net/index/my_asset/asset"
        self.htnumber='HT190808010021'
        self.code=str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y%m%d"))+"a"
        self.num=str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y%m%d"))+"b"
        self.tax="10"
        self.name="a"
        self.model="s"
        self.unit="s"
        self.amount="10"
        self.sum="10"
        # self.date1=  (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.date1 = (datetime.datetime.now()).strftime("%Y-%m-%d")
        self.opetaror='s'

    def teardown(self):
        pass

    @pytest.mark.skip('not zjc')
    def test_addInstock(self):
        n=0
        self.pur = AssetCenter(self.driver)
        while n<1:
            self.pur.open(self.url)
            self.pur.add_instock(self.htnumber,self.date1,self.date1,self.opetaror)
            n+=1

    @pytest.mark.skip('not zjc')
    def test_addInvoice(self,driver):
        self.assert_center_page=AssetCenter(driver)
        n = 0
        while n < 1:
            self.assert_center_page.open(self.url)
            self.code = str((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d%H%M")) + "a"
            self.num = str((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d%H%M")) + "b"
            self.code+=str(n)
            self.num+=str(n)
            self.assert_center_page.add_invoice(self.htnumber,self.code,self.num,self.date1,self.tax,
                                 self.name,self.sum)
            n += 1

if __name__ == '__main__':
    pytest.main(['-v','-m','jinfu','test_assert_center'])