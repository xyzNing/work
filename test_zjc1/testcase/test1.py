import os,xlrd
def read_data(type):
    file = os.path.dirname(os.getcwd()) + r"\Date\casedata.xlsx"
    print(file)
    book = xlrd.open_workbook(file)
    sheet1 = book.sheet_by_name(type)
    # sheet2 = book.sheet_by_name("invoice")
    row1 = book.sheet_by_name(type).nrows
    col1 = book.sheet_by_name(type).ncols
    print(row1, col1)
    # row2 = book.sheet_by_name("invoice").nrows
    # mylog.info("开始读" + type + "信息")
    # data1 = sheet1.row_values(row1 )
    # mylog.info("读取" + type + "完成")
    # return data1
read_data('login')

def test():
    try:
        a=3
    except:
        raise Exception('aa')






