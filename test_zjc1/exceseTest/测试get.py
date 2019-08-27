import requests
import requests.cookies
# s=requests.get('http://zjcbytest.zhutx.net/index.php/Home')
# print(s.status_code)
# print(s.text)
# print(s.headers)
# # print(s.json())
# print('--'*20)
# print(s.cookies)
heads={
'Connection':'keep-alive',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests':'1',
'User-AgenT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'http://zjcbytest.zhutx.net/index.php/Home'
}
url='http://zjcbytest.zhutx.net/index.php/Home'
s=requests.session()
# s.headers.update(heads)
r=s.get(url,headers=heads,verify=False)
print(s.cookies)
c=requests.cookies.RequestsCookieJar()
c.set('zhujc.tokenstr','d309091f1cc42dd4102b1f73f11c9a7f')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','uid=2075')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','username=a00241')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','listname=%E4%BA%8C%E5%8F%B7%E6%B5%8B%E8%AF%95%E9%9B%86%E5%9B%A2')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','companytype=5')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','companyname=%E4%BA%8C%E5%8F%B7%E6%B5%8B%E8%AF%95%E9%9B%86%E5%9B%A2')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','companystate=2')
c.set('	d309091f1cc42dd4102b1f73f11c9a7f','adminflag=1')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','autharr=')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','phone=')
c.set('d309091f1cc42dd4102b1f73f11c9a7f','isfinancing=1')
s.cookies.update(c)
print(s.cookies)
print(r.text)
r1=s.get('http://zjcbytest.zhutx.net/index.php/Purchaser/Bid/bidCreate',headers=heads)








