import xlwt
import os
import xlrd
from xlutils.copy import copy
def write_excel(List,type):
    file=os.path.dirname(os.getcwd())+"/date.xls"
    if os.path.exists(file):
        book=xlrd.open_workbook(file)
        row1=book.sheet_by_name("instock").nrows
        row2=book.sheet_by_name("invoice").nrows
        sheets=book.sheet_names()
        print(sheets)
        print(row1,row2)
        new_book=copy(book)
        sheet1=new_book.get_sheet(0)
        sheet2=new_book.get_sheet(1)
        if     type=="instock":
            print('1')
            for i in range(len(List)):
                sheet1.write(row1+1,i,List[i])
        elif  type=="invoice":
            for i in range(len(List)):
                sheet2.write(row2+1,i,List[i])
        new_book.save(file)
        print("ok")
    else:
        book=xlwt.Workbook(encoding="utf-8")
        sheet=book.add_sheet("instock")
        sheet2=book.add_sheet("invoice")
        for i in range(len(List)):
            sheet.write(1,i,List[i])
        book.save(file)

def read_excel(type):
    file = os.path.dirname(os.getcwd()) + "/date.xls"
    book=xlrd.open_workbook(file)
    sheet1=book.sheet_by_name("instock")
    sheet2=book.sheet_by_name("invoice")
    row1=book.sheet_by_name("instock").nrows
    row2=book.sheet_by_name("invoice").nrows
    if type.lower()=="instock":
        data1=sheet1.row_values(row1-1)
        return data1
    elif type.lower()=="invoice":
        data2=sheet2.row_values(row2-1)
        return data2





# write_excel(["1"],"invoice")
s=read_excel("instock")
print(s)