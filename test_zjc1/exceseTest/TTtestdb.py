import pymysql
import xlwt

conn=pymysql.connect(host='120.78.189.5',port=3306,user='jinfuuserdb',passwd='6lefDgZMlhb4RbgU',db='jinfu',charset='utf8')
cursor=conn.cursor()
sql='select * from fin_company'
cursor.execute(sql)
row1=cursor.fetchmany(5)
len=len(row1)
print(len)
print(row1)
cursor.close()
conn.close()
print("="*30)

# for index1,em in enumerate(row1):
#     for index2,y in enumerate(em):
#         print(index2,y)
excelbook=xlwt.Workbook(encoding='utf8')
excelsheet=excelbook.add_sheet('sheet1',cell_overwrite_ok=True)
for row, rowData in enumerate(row1):
        for col, value in enumerate(rowData):
            # 因为下标从0开始，所以要加1
            e=str(value)
            excelsheet.write(row+1, col+1,value )
        # e='ss'
excelbook.save(r'D:\test.xls')
