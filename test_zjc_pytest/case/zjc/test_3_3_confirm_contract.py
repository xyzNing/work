from pageObject.zjc.supContractManage import SupContract
import pytest
class TestContract():
    def start(self, driver):
        driver.get("http://zjcbytest.zhutx.net/index.php")
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.usefixtures('login_sup')
    def test_confirm_contract(self,driver):
        self.sup_page=SupContract(driver)
        number=self.sup_page.read_excel('contract')
        self.sup_page.confirm_contract(number[0])

if __name__ == '__main__':
    pytest.main(['-v','test_3_3_confirm_contract.py'])


