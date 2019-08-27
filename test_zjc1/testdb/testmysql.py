import pymysql.cursors
connector=pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8'
)
cursor=connector.cursor()
#插入数据
sql="insert into t_company(type,name,linkman,linkphone,address,fund) values('%d','%s','%s','%s','%s','%s')"
date=(12001,'谷歌','SMR','1234567890','美国','1000')
cursor.execute(sql % date)
connector.commit()
print("成功插入",cursor.rowcount,'条数据')

#修改数据
sql="update t_company set linkphone=%s where company_id=%d"
date=('15201459999',1)
cursor.execute(sql % date)
connector.commit()
print('成功修改',cursor.rowcount,'条数据')

#查询数据
sql="select * from t_company where linkman= '%s'"
date=("李彦宏")
cursor.execute(sql % date)
connector.commit()
print("成功查询",cursor.rowcount,"条数据")





cursor.close()
connector.close()
