import requests
import json
from common.log import log
import xlrd
from xlutils.copy import copy
url1 = ""
url2 = ""


class Base(object):
    case_pass = 0
    case_fail = 0

    def send_post(self, url, parm=None):
        r = requests.post(url, data=parm)
        response_code = r.status_code
        log.info('返回的code为：%s' % response_code)
        try:
            if response_code == 200:
                response_json = r.json()
                log.info('返回的json为：%s' % response_json)
                return response_code, response_json
            else:
               raise Exception('接口错误')
        except:
            raise Exception('接口错误')

    def check_interface(self, content):
        try:
            if isinstance(content,dict):
                if 'interface_name' in content:
                    log.info("正在测试接口：%s"%content['interface_name'])
                    log.info("请求的参数为：%s" % str(content))
                    data1={"content":json.dumps(content)}
                    res=self.send_post(url1,data1)
                    token=res[1]['token']
                    data2={"content":json.dumps(content),"token":token}
                    res2=self.send_post(url2,data2)
                    return res2
            else:
                content_dict=eval(content)
                if 'interface_name' in content_dict:
                    log.info("正在测试接口：%s"%content_dict['interface_name'])
                    log.info("请求的参数为：%s" % content)
                    data1={"content":json.dumps(content_dict)}
                    res=self.send_post(url1,data1)
                    token=res[1]['token']
                    data2={"content":json.dumps(content_dict),"token":token}
                    res2=self.send_post(url2,data2)
                    return res2
        except Exception as msg:
            log.error("错误信息是：%s"%msg)
            raise

    def send_get(self):
        pass

    def get_token(self,response_json):
        token=response_json['token']
        return token

    def get_value(self,data_value, name):
        if isinstance(data_value, dict):
            if name in data_value:
                # print(data[name])
                return data_value[name]
            else:
                for key in data_value.keys():
                    newData = data_value[key]
                    if isinstance(newData, dict):
                        # data1 = newData[key]
                        result=self.get_value(newData,name)
                        return result
                    if isinstance(newData, list):
                        for i in range(len(newData)):
                            tempdata = newData[i]
                            result=self.get_value(tempdata, name)
                            return result
        if isinstance(data_value, list):
            for i in range(len(data_value)):
                tempdata = data_value[i]
                result=self.get_value(tempdata, name)
                return  result

    def data_to_json(self,data):
        dict_json=json.dumps(data)
        return  dict_json

    def json_to_dict(self,data):
        if isinstance(data,str):
            data_dict=eval(data)
            json_data=json.loads(data_dict)
        else:
            json_data=json.loads(data)
        return json_data

    def get_excel(self):    #返回行和列
        file=r'C:\Work\test_interface\testdata\case.xls'
        workbook=xlrd.open_workbook(file)
        sheet=workbook.sheet_by_name("case")
        rows=sheet.nrows
        cols=sheet.ncols
        return rows,cols

    def get_excel_value(self,sheet_name):
        list_sheet=[]
        rows,cols=self.get_excel()
        file = r'C:\Work\test_interface\testdata\case.xls'
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheet_by_name(sheet_name)
        # cell_value=sheet.cell(row,1).value  #获取单个单元格的值
        i=1
        for i in range(i,rows):
            cell_value=sheet.row_values(rows)
            list_sheet.append(cell_value)
        return  list_sheet

    def write_excel(self,sheet_name,row,col,value):
        file=r'C:\Work\test_interface\testdata\case.xls'
        read_book=xlrd.open_workbook(file)
        write_book=copy(read_book)
        # sheet=wbook.get_sheet(0)
        sheet = write_book.get_sheet(sheet_name)
        sheet.write(row,col,value)
        write_book.save(file)

    # def  test(self):
    #      num=self.get_excel()
    #      print(num[0],num[1])
    #      value = self.get_excel_value('case')
    #      print(value)
    #      for i in range(1,num[0]):
    #          log.info("用例id：%s--用户类型；%s--接口名称：%s--请求方式：%s"%(value[i][0],value[i][1],value[i][2],value[i][3]))
    #          res=self.check_interface(value[i][4])
    #          if isinstance(res,tuple):
    #              self.write_excel('case',i,7,res[0])
    #              self.write_excel('case',i,8,res[1]['code'])
    #              self.write_excel('case',i,9,str(res[1]))
    #          else:
    #             self.write_excel(i,7,res)
    #          new_value=self.get_excel_value(i)
    #          if new_value[5]==new_value[7] and new_value[6]==new_value[8]:
    #             self.write_excel(i,10,'Pass')
    #             self.case_pass+=1
    #          else:
    #             self.write_excel(i,10,'fail')
    #             self.case_fail+=1
    #     print(self.case_pass)
    #     print(self.case_fail)


if __name__ == '__main__':
    # base=Base()
    # base.test()
    pass






