import smtplib
from email.mime.text import MIMEText
smtp=smtplib.SMTP()
port="smtp.163.com"
user="13937949082@163.com"
passwd="zjc123456"
msg=MIMEText("你好","plain","utf-8")
receive_to=["466268124xyz@2980.com","13937949082@163.com"]
server=smtplib.SMTP(port,25)
server.login(user,passwd)
server.sendmail(user,receive_to,msg.as_string())
server.quit()