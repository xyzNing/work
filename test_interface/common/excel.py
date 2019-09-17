import xlrd
from xlutils.copy import copy


class ExcelUtil():
    def __init__(self,path,sheet_name):
        self.path=path
        self.sheet_name=sheet_name
        self.wb=xlrd.open_workbook(path)
        self.sheet=self.wb.sheet_by_name(sheet_name)
        self.row=self.sheet.nrows
        self.col=self.sheet.ncols

    def get_value(self):
        list_value=[]
        i = 1
        for i in range(i,self.row):
            row_value=self.sheet.row_values(i)
            list_value.append(row_value)
        return list_value

    def write_excel(self,row,col,value):
        rb = xlrd.open_workbook(self.path)
        wb = copy(rb)
        sheet=wb.get_sheet(self.sheet_name)
        sheet.write(row,col,value)
        wb.save()


if __name__ == '__main__':
    excel=ExcelUtil(r'C:\Work\test_interface\testdata\case.xls', 'contract')
    print(excel.row)
    list1=excel.get_value()
    print(len(list1))
    print(list1)


