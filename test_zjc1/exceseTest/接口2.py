import requests
import json
url_token="http://paybytest.zhutx.net/api.php/api/setToken"
url_interface="http://paybytest.zhutx.net/api.php/interfaceHandle"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
data_token={
    "content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}'
}
print(type(data_token))
s=requests.session()
response_token=s.post(url_token,headers=header,data=data_token)
token_json=response_token.content.decode("utf-8")
r=requests.post(url_token,headers=header,data=data_token)
print(r.json())
sss=r.json()
print(type(sss))
print(r.json()['token'])
print(type(r.json()['token']))
# print(json.load(sss)['token'])
print(token_json)
print(type(token_json))
token=json.loads(token_json)["token"]
print(type(token))
print(token)
data_data={
    "content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}',
    "token":token
}
r=s.post(url_interface,headers=header,data=data_data)
print(r.content.decode("utf-8"))
print(r.json())
user_token=json.loads(r.content.decode("utf-8"))["data"]["user_token"]
print(user_token)
content={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/unreadNews","user_id":"455","user_token":user_token}
content1=json.dumps(content,separators=(",",":"))
data1={"content":content1}
r1=s.post(url_token,headers=header,data=data1)
token1=json.loads(r1.content.decode("utf-8"))["token"]
print(token1)
data_11={"content":content1,
        "token":token1}
r11=s.post(url_interface,headers=header,data=data_11)
print(r11.content.decode("utf-8"))

# print(response_token.content.decode("utf-8"))
# print(type(response_token.content.decode("utf-8")))
# token=json.loads(response_token.content.decode("utf-8"))["token"]
# print(token)
# print(type(token))
# date_inertface={
# "content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"123456","page_name":"jf0461","user_token":""}',
# "token":token
# }
# response_interface=s.post(url_interface,headers=header,data=date_inertface)
# print(response_interface.content.decode("utf-8"))
# print(type(response_interface.content.decode("utf-8")))
# L=[{"user":"jf0461","password":"123456"}]
# content_dict={
#     'pname':'web','sn':'d41d8cd98f00b204e9800998ecf8427e','interface_name':'HomeUserAccount/login','user_name':L[0]['user'],'type':'2002','password':L[0]['password'],'page_name':'jf0461','user_token':''}
# data_token={
#     "content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"123456","page_name":"jf0461","user_token":""}'
# }
# data_11=json.dumps(content_dict,separators=(",",":"))
# data={"content":data_11}
# print("-"*20)
# print(content_dict)
# print(str(content_dict))
# print("data=%s"%data)
# s=requests.session()
# response=s.post(url_token,headers=header,data=data)
# print(response.content)
# data_data= {"content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"123456","page_name":"jf0461","user_token":""}'}
# data_token={"content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"123456","page_name":"jf0461","user_token":""}'}
# response1=requests.post(url_token,headers=header,data=data_data)
# print(response1.content)
# data_1= {"content":'{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"HomeUserAccount/login","user_name":"jf0461","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}'}
#

{"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Performance/contractList","company_id":"46","type":"2002","password":"zjc123456","page_name":"jf0461","user_token":""}