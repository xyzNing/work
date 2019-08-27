import pymysql
con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='zjc',charset='utf8')
cursor=con.cursor()
sql="select * from zjc_bid"
cursor.execute(sql)
row=cursor.fetchmany(5)
len=len(row)
print(row)
print(len)
for i  in range(len):
    print(row[i])
cursor.close()
con.close()