from pageObject.zjc.cusBackStage import CusBackStage
import pytest
class TestCheckContract():

    @pytest.mark.usefixtures("login_cus")
    def test_check_contract(self,driver):
        self.cus_page=CusBackStage(driver)
        contract_num = self.cus_page.read_excel('contract')
        for i in contract_num:
            if i =='':
                continue
            self.cus_page.check_contract(i)

if __name__ == '__main__':
    pytest.main(['-v','test_3_2_check_contract.py'])
