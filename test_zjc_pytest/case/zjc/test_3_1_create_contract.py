from pageObject.zjc.contractMange import ContractPage
from pageObject.zjc.purBackStage import BackStage
import pytest
from datetime import datetime
class TestContract():

    def setup(self):
        self.date=datetime.now().strftime("%Y-%m-%d")
        self.text=str(datetime.now().strftime("%Y%m%d%H%M"))

    @pytest.mark.usefixtures("login_pur")
    def test_create_contract(self,driver):
        self.back_page=BackStage(driver)
        self.back_page.enter_contract_manage()
        self.contract_page=ContractPage(driver)
        bid_number=self.contract_page.read_excel('bid')
        self.contract_page.search_contract(bid_number)
        self.contract_page.create_contract(self.date,self.text)
        contract_number=self.contract_page.get_number()[0:1]
        self.contract_page.write_excel(contract_number,'contract')



if __name__ == '__main__':
    pytest.main(['-v','test_3_1_create_contract.py'])
