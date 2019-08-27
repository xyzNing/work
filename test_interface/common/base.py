import requests
import json
from common.log import log
import xlrd
from xlutils.copy import copy
url1 = "http://paybytest.zhutx.net/api.php/api/setToken"
url2 = "http://paybytest.zhutx.net/api.php/interfaceHandle"


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
             # new_value=self.get_excel_value(i)
             # if new_value[5]==new_value[7] and new_value[6]==new_value[8]:
             #    self.write_excel(i,10,'Pass')
             #    self.case_pass+=1
             # else:
             #    self.write_excel(i,10,'fail')
             #    self.case_fail+=1
         # print(self.case_pass)
         # print(self.case_fail)
if __name__ == '__main__':
    # base=Base()
    # base.test()
    null=""
    a1 = {"code":1,"message":"接口调用成功","data":{"data":[{"number":"RK190528003","instock_id":1382,"contract_id":598,"project_name":"筑集采项目","sup_name":"一只小小鸟","contractno":"HT1905281361","state":3,"entry_company":"集团001","arrangements_man":"A","source":3,"update_time":"2019-06-21 15:42:02","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"},{"number":"RK190621004","instock_id":1387,"contract_id":599,"project_name":"筑集采项目","sup_name":"测试1","contractno":"HT190621001","state":3,"entry_company":"集团001","arrangements_man":"aaa","source":3,"update_time":"2019-06-21 16:27:03","attach_state":null,"entry_company_id":674,"if_compile":1,"state_name":"审核通过"},{"number":"RK190621002","instock_id":1383,"contract_id":599,"project_name":"筑集采项目","sup_name":"测试1","contractno":"HT190621001","state":3,"entry_company":"集团001","arrangements_man":"a","source":3,"update_time":"2019-06-21 15:42:02","attach_state":null,"entry_company_id":674,"if_compile":1,"state_name":"审核通过"},{"number":"RK190528001","instock_id":1380,"contract_id":598,"project_name":"筑集采项目","sup_name":"一只小小鸟","contractno":"HT1905281361","state":3,"entry_company":"集团001","arrangements_man":"AA","source":3,"update_time":"2019-06-21 15:42:02","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"},{"number":"RK190621003","instock_id":1385,"contract_id":599,"project_name":"筑集采项目","sup_name":"测试1","contractno":"HT190621001","state":3,"entry_company":"集团001","arrangements_man":"aa","source":3,"update_time":"2019-06-21 16:07:02","attach_state":null,"entry_company_id":674,"if_compile":1,"state_name":"审核通过"},{"number":"RK190528002","instock_id":1381,"contract_id":598,"project_name":"筑集采项目","sup_name":"一只小小鸟","contractno":"HT1905281361","state":3,"entry_company":"集团001","arrangements_man":"aa","source":3,"update_time":"2019-06-21 15:42:02","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"},{"number":"RK190527010002","instock_id":1180,"contract_id":453,"project_name":"05261407项目","sup_name":"筑链智融供应商1","contractno":"HT190526010007","state":1,"entry_company":"集团001","arrangements_man":"aaa","source":1,"update_time":"2019-05-27 14:31:44","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190527010004","instock_id":1182,"contract_id":446,"project_name":"0527项目1401","sup_name":"随便投投有限公司","contractno":"HT190524010005","state":2,"entry_company":"集团001","arrangements_man":"aaaa","source":1,"update_time":"2019-05-27 14:44:50","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核不通过"},{"number":"RK190527010001","instock_id":1179,"contract_id":447,"project_name":"0526","sup_name":"筑链智融供应商1","contractno":"HT190526010001","state":1,"entry_company":"集团001","arrangements_man":"a","source":1,"update_time":"2019-05-27 15:45:15","attach_state":"","entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190527010008","instock_id":1186,"contract_id":453,"project_name":"05261407项目","sup_name":"筑链智融供应商1","contractno":"HT190526010007","state":1,"entry_company":"集团001","arrangements_man":"AAA","source":1,"update_time":"2019-05-27 15:51:02","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"}],"total_num":90,"page_number":1}}
    a2={"code":1,"message":"接口调用成功","data":{"data":[{"number":"RK190806010003","instock_id":1589,"contract_id":442,"project_name":"0524测试项目","sup_name":"筑链智融供应商1","contractno":"HT190524010001","state":1,"entry_company":"集团001","arrangements_man":"11","source":1,"update_time":"2019-08-06 14:28:23","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190806010002","instock_id":1588,"contract_id":442,"project_name":"0524测试项目","sup_name":"筑链智融供应商1","contractno":"HT190524010001","state":1,"entry_company":"集团001","arrangements_man":"11","source":1,"update_time":"2019-08-06 14:27:04","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190806010001","instock_id":1587,"contract_id":442,"project_name":"0524测试项目","sup_name":"筑链智融供应商1","contractno":"HT190524010001","state":1,"entry_company":"集团001","arrangements_man":"11","source":1,"update_time":"2019-08-06 14:25:37","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190701010007","instock_id":1445,"contract_id":446,"project_name":"0527项目1401","sup_name":"随便投投有限公司","contractno":"HT190524010005","state":2,"entry_company":"集团001","arrangements_man":"a","source":1,"update_time":"2019-07-01 10:38:15","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核不通过"},{"number":"RK190701010004","instock_id":1442,"contract_id":446,"project_name":"0527项目1401","sup_name":"随便投投有限公司","contractno":"HT190524010005","state":3,"entry_company":"集团001","arrangements_man":"aa","source":1,"update_time":"2019-07-01 10:29:19","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"},{"number":"RK190627010013","instock_id":1427,"contract_id":656,"project_name":"0627sss","sup_name":"中建UAT2","contractno":"HT190627010009","state":3,"entry_company":"集团001","arrangements_man":"a","source":1,"update_time":"2019-06-27 15:08:31","attach_state":null,"entry_company_id":674,"if_compile":1,"state_name":"审核通过"},{"number":"RK190627010012","instock_id":1426,"contract_id":655,"project_name":"fudong","sup_name":"中建UAT2","contractno":"HT190627010008","state":3,"entry_company":"集团001","arrangements_man":"a","source":1,"update_time":"2019-06-27 14:00:23","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"},{"number":"RK190627010011","instock_id":1425,"contract_id":655,"project_name":"fudong","sup_name":"中建UAT2","contractno":"HT190627010008","state":1,"entry_company":"集团001","arrangements_man":"a","source":1,"update_time":"2019-06-27 11:47:09","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"平台审核中"},{"number":"RK190627010010","instock_id":1424,"contract_id":649,"project_name":"0627yanz1","sup_name":"中建UAT2","contractno":"HT190627010002","state":3,"entry_company":"集团001","arrangements_man":"ss","source":1,"update_time":"2019-06-27 10:19:10","attach_state":null,"entry_company_id":674,"if_compile":1,"state_name":"审核通过"},{"number":"RK190626010005","instock_id":1413,"contract_id":645,"project_name":"0626qingkuian","sup_name":"筑链智融供应商1","contractno":"HT190626010008","state":3,"entry_company":"集团001","arrangements_man":"aa","source":1,"update_time":"2019-06-26 14:53:22","attach_state":null,"entry_company_id":674,"if_compile":0,"state_name":"审核通过"}],"total_num":90,"page_number":1}}
    base = Base()
    ll = base.get_value(a1, 'instock_id')
    kk=base.get_value(a2, 'instock_id')
    print(ll)
    print(kk)






