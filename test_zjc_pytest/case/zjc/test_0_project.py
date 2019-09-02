from pageObject.zjc.projectManagePage import ProjectPage
from pageObject.zjc.purBackStage import BackStage
import pytest
from datetime import datetime
class TestProject():
    def setup(self):
        self.name=str(datetime.now().strftime("%Y%m%d%H%M"))+'项目'
        self.desc='test'
        self.addr='1号'
        self.manager='s'
        self.phone='13937949012'
        self.type='自建'
        self.area=1000
        self.money=10000

    # def start(self,driver):
    #     self.back_page=BackStage(driver)
    #     self.back_page.enter_project_manage()

    @pytest.mark.usefixtures('login_pur')
    def test_create_project(self,driver):
        self.back_page = BackStage(driver)
        self.back_page.enter_project_manage()
        self.project_page = ProjectPage(driver)
        self.project_page.public_project(self.name,self.desc,self.addr,self.manager,self.phone,self.type,self.area,self.money)
        number=self.project_page.get_project_number()
        self.project_page.write_excel(number[0],'project')


    def test_check_project(self,driver):
        # self.back_page = BackStage(driver)
        # self.back_page.enter_project_manage()
        self.project_page = ProjectPage(driver)
        num= self.project_page.read_excel('project')
        self.project_page.check_project(num)

if __name__ == '__main__':
    pytest.main(['-v','test_0_project.py'])


