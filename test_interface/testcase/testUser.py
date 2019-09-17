import unittest
import requests
from common.base import Base
from ddt import ddt,data,unpack
@ddt
class TestUesr(unittest.TestCase):
    def setUp(self):
        self.content=''

    def tearDown(self):
        pass

    @data('')
    def test_Login(self):
        '''登陆'''
        # data=base.data_to_json(data1)
        # print(data)
        # r=requests.post(url=self.url1,data=data)
        # print(r.json())
        # res=base.send_post(self.url1,data1)
        # print(res)
        # print(res[0])
        # print(res[1])
        # token=res[1]['token']
        # data2={"content":self.content,
        #        "token":token}
        base=Base()
        res2=base.check_interface(self.content)
        self.assertEqual(res2[0],200)
        self.assertEqual(res2[1]['code'],1)


    # def test_Login1(self):
    #     # data=base.data_to_json(data1)
    #     # print(data)
    #     # r=requests.post(url=self.url1,data=data)
    #     # print(r.json())
    #     # res=base.send_post(self.url1,data1)
    #     # print(res)
    #     # print(res[0])
    #     # print(res[1])
    #     # token=res[1]['token']
    #     # data2={"content":self.content,
    #     #        "token":token}
    #     res2=check_interface(self.content2)
    #     if res2[0]==200 and res2[1]['code']==1:
    #         print("测试通过")
    #     else:
    #         print("测试失败")

if __name__ == '__main__':
    unittest.main()

