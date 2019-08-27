import os
# from common.base import *
# print(os.path.abspath('.'))
# print(os.path.abspath(os.curdir))
# print(os.path.abspath('..'))
# a=[1,2,3,4]
# print("%s-%s-%s-%s"%(a[0],a[1],a[2],a[3]))
# dict1={"a":'1',"b":"{'a1':2}"}
# list1=['1','2','3']
# # for i in range(0,len(list1)):
# #     print(list1[i])
# sss1={"code":1,"message":"接口调用成功","data":{"data":[{"contract_id":442,"project_name":"0524测试项目","pur_name":"集团001","sup_name":"筑链智融供应商1","contractno":"HT190524010001","contract_number":"05241139","state":1,"entry_company":"集团001","source":1,"update_time":"2019-05-24 17:25:35","create_time":"2019-05-24 14:25:23","if_compile":0,"state_name":"平台审核中"}],"total_num":1,"page_number":1}}
# sss2={'code': 1, 'message': '接口调用成功', 'data': {'contract_id': '722'}}
# print(type(sss1))
# def get_value(data,name):
#     if isinstance(data,dict):
#         if name in data:
#             print(data[name])
#             # return L[key]
#         else:
#             for key in data.keys():
#                 newData=data[key]
#                 if isinstance(newData,dict):
#                     data=newData[key]
#                     get_value(data,key)
#                 if isinstance(newData,list):
#                     for i in range(len(newData)):
#                         tempdata=newData[i]
#                         get_value(tempdata,name)
#     if isinstance(data,list):
#         for i in range(len(data)):
#             tempdata = data[i]
#             get_value(tempdata, name)
#
#
# get_value(dict1,'a1')

# if 'a1' in {'a1': 2}:
#     print('3333')

# get_value(sss2,'contract_id')
# a1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}
# base=Base()
# ll=base.get_value(a1,'user_name')

import socket
hostman=socket.gethostname()
ipadd=socket.gethostbyname(hostman)
print(ipadd)
from datetime import datetime
time1=datetime.strftime(datetime.now(),"%Y%m%d%H%M")
print(time1)
