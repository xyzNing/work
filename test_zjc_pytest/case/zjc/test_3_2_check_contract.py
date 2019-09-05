from pageObject.zjc.cusBackStage import CusBackStage
import pytest
class TestCheckContract():
    def start(self, driver):
        driver.get("http://zjcbytest.zhutx.net/index.php/Custom")
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.usefixtures('login_cus')
    def test_check_contract(self,driver):
        self.cus_page=CusBackStage(driver)
        contract_num = self.cus_page.read_excel('contract')
        for i in range(len(contract_num)):
            self.cus_page.check_contract(contract_num[i])

if __name__ == '__main__':
    pytest.main(['-v','test_3_2_check_contract.py'])
