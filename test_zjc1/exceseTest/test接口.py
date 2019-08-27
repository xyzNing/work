import requests
url="http://localhost:8080/jenkins/j_acegi_security_check"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
date={
    "from":"/jenkins/",
    "j_password":"123456",
    "j_username":"admin",
    "Submit":"Sign in"
}
s=requests.session()
r=s.post(url,headers=header,data=date)
print(r.content)