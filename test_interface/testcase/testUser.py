import unittest
import requests
from common.base import Base
from ddt import ddt,data,unpack
@ddt
class TestUesr(unittest.TestCase):
    def setUp(self):
        self.content='{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}'
        self.content2='{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/myAssets","company_id":"461","user_token":"d8865837e4c18a299cc44aa837dcc58b1538219212AAA"}'
    def tearDown(self):
        pass
    # @data('{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}',
    #       '{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"","page_name":"jf0461","user_token":""}',
    #       '{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"","type":"2002","password":"","page_name":"jf0461","user_token":""}')

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
    unittest.main

