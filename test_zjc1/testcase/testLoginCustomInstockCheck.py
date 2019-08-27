from pageObject.cusBackStage import CusBackStage
from pageObject.loginPage import LoginPage
import  unittest
from configer import basePage
class TestInstockCheck(unittest.TestCase):
    def setUp(self):
        self.user="custom123"
        self.passwd="123456"
        self.instock_num=[]
        self.driver=basePage.browser()
        self.login=LoginPage(self.driver)
        self.login.custom_login(self.user,self.passwd)


    def tearDown(self):
        self.driver.quit()

    def test01(self):
        self.cusBackStage = CusBackStage(self.driver)
        self.instock_num=self.cusBackStage.read_excel("instock")
        print(self.instock_num)
        for num in self.instock_num:
            print(num)
            if num=='':
                continue
            else:
                self.cusBackStage.checkInstock(num)
if __name__ == '__main__':
    unittest.main()
