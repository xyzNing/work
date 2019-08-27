from common.base import *
from datetime import datetime
from  common.log import log
class InstockPage(Base):
    def check_instock(self,content):
        '''
        新增入库单审核不通过再次编辑审核通过
        :param content:  传入搜索合同的参数
        :return:
        '''
        company_id = self.get_value(content, "company_id")
        log.info('搜索合同')
        res=self.check_interface(content)
        contract_id=self.get_value(res[1],"contract_id")
        content1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Performance/contractDetail","company_id":company_id,"contract_id":contract_id,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res1=self.check_interface(content1)
        log.info('合同详情页')
        contractno=self.get_value(res1[1],"contractno")
        print(contractno)
        project_name=self.get_value(res1[1],"project_name")
        sup_name=self.get_value(res1[1],"sup_name")
        instock_product_json='[{"id":"","instockId":"","name":"a","model":"s","para":"","brand":"","place":"","unit":"d","price":"1000","number":"10","remark":""}]'
        # print(type(instock_product_json))
        warehousing_date=datetime.strftime(datetime.now(),"%Y-%m-%d")
        estimated_paymen_date=datetime.strftime(datetime.now(),"%Y-%m-%d")
        # warehousing_date="2019-08-06 00:00:00"
        # estimated_paymen_date="2019-08-06 00:00:00"
        instock_price = self.get_value(eval(instock_product_json), 'price')
        instock_num = self.get_value(eval(instock_product_json), 'number')
        instock_money = str(int(instock_price) * int(instock_num))
        print(instock_money)
        content2={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Instock/updateInstock","company_id":company_id,"instock_id":"","contract_id":contract_id,"contract_number":contractno,"project_name":project_name,"sup_name":sup_name, "warehousing_date":warehousing_date,"estimated_paymen_date":estimated_paymen_date,
                  "arrangements_man":"ss","instock_product_json":instock_product_json,"source":1,"remark":"","attach_id":"12649","instock_money":instock_money,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res2=self.check_interface(content2)
        log.info('新入库单')
        content3={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Instock/instockList","company_id":company_id,"page_number":1,"anumber":10,"source":"","update_time_start":"","update_time_end":"","search":"","state":"","sort":1,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res3=self.check_interface(content3)
        log.info('入库单列表')
        instock_id=self.get_value(res3[1],"instock_id")
        content4={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInstock/checkInstock","customer_user_id":"36","check_state":2,"instock_id":instock_id,"reason":"6666","instock_money":instock_money,"user_token":""}
        res4=self.check_interface(content4)
        log.info('审核入库单不通过')
        content5 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e", "interface_name": "Instock/updateInstock",
                    "company_id": company_id, "instock_id": instock_id, "contract_id": contract_id,
                    "contract_number": contractno, "project_name": project_name, "sup_name": sup_name,
                    "warehousing_date": warehousing_date, "estimated_paymen_date": estimated_paymen_date,
                    "arrangements_man": "ss", "instock_product_json": instock_product_json, "source": 1, "remark": "",
                    "attach_id": "12649", "instock_money": instock_money,
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res5=self.check_interface(content5)
        log.info('编辑入库单')
        content6={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInstock/checkInstock","customer_user_id":"36","check_state":1,"instock_id":instock_id,"reason":"","instock_money":instock_money,"user_token":""}
        res6=self.check_interface(content6)
        log.info('审核通过入库单')
        return res6

    def check_attach(self,content):
        '''
        新增入库单审核通过编辑府入库单附件不通过后再次编辑入库单附件，审核通过
        :param content:
        :return:
        '''
        company_id = self.get_value(content, "company_id")
        res = self.check_interface(content)
        contract_id = self.get_value(res[1], "contract_id")
        content1 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "Performance/contractDetail", "company_id": company_id,
                    "contract_id": contract_id, "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res1 = self.check_interface(content1)
        contractno = self.get_value(res1[1], "contractno")
        project_name = self.get_value(res1[1], "project_name")
        sup_name = self.get_value(res1[1], "project_name")
        instock_product_json='[{"id":"","instockId":"","name":"a","model":"s","para":"","brand":"","place":"","unit":"d","price":"1000","number":"10","remark":""}]'
        warehousing_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
        estimated_paymen_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
        instock_price = self.get_value(eval(instock_product_json),'price')
        instock_num=self.get_value(eval(instock_product_json),'number')
        instock_money=str(int(instock_price)*int(instock_num))
        content2 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e", "interface_name": "Instock/updateInstock",
                    "company_id": company_id, "instock_id": "", "contract_id": contract_id, "contract_number": contractno,
                    "project_name": project_name, "sup_name": sup_name, "warehousing_date": warehousing_date,
                    "estimated_paymen_date": estimated_paymen_date,
                    "arrangements_man": "ss", "instock_product_json": instock_product_json, "source": 1, "remark": "",
                    "attach_id": "12650", "instock_money": instock_money,
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res2 = self.check_interface(content2)
        content3 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e", "interface_name": "Instock/instockList",
                    "company_id": company_id, "page_number": 1, "anumber": 10, "source": "", "update_time_start": "",
                    "update_time_end": "", "search": "", "state": "", "sort": 1,
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res3 = self.check_interface(content3)
        instock_id = self.get_value(res3[1], "instock_id")
        attach_id=self.get_value(res3[1],"attach_id")
        content4 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "CustomerInstock/checkInstock", "customer_user_id": "36", "check_state": 1,
                    "instock_id": instock_id, "reason": "", "instock_money": instock_money, "user_token": ""}
        res4 = self.check_interface(content4)
        content5={"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e", "interface_name": "Instock/updateInstockAttach",
                    "company_id": company_id, "instock_id": instock_id, "attach_id": "12650", "del_attach_id": "",
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res5=self.check_interface(content5)
        content6={"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "CustomerInstock/checkInstockAttach", "customer_user_id": "36",
                    "instock_id": instock_id,"attach_id": "12650","del_attach_id": "","check_state": 2,"reason": "", "instock_money": instock_money, "user_token": ""}
        res6=self.check_interface(content6)
        res7=self.check_interface(content5)
        content8 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "CustomerInstock/checkInstockAttach", "customer_user_id": "36",
                    "instock_id": instock_id, "attach_id": "12650", "del_attach_id": "12649", "check_state": 1,
                    "reason": "", "instock_money": instock_money, "user_token": ""}
        res8=self.check_interface(content8)
        return res8


