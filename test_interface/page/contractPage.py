from common.base import *
from common.log import log


class ContractPage(Base):
    def del_contract(self,content):
        '''
        新增合同存草稿后删除合同的流程
        :return:
        '''
        print(content)
        print(type(content))
        # content_3=self.json_to_dict(content)
        company_id = self.get_value(content, 'company_id')
        contract_number = self.get_value(content, 'contract_number')
        res1=self.check_interface(content)
        log.info('新增合同存草稿')
        content_1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","company_id":company_id,"page_number":1,"anumber":10,"update_time_start":"","update_time_end":"","search":contract_number,"state":"6","sort":1,"type":0,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res2=self.check_interface(content_1)
        log.info('查看合同列表')
        # print(type(res2[1]))
        # print(res2[1])
        # content_dict=self.json_to_dict(res2[1])
        contract_id=self.get_value(res2[1],'contract_id')
        print(contract_id)
        content_2={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","company_id":company_id,"contract_id":contract_id,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res=self.check_interface(content_2)
        log.info('删除合同')
        return res

    def edict_contract(self,content):
        '''
        新增合同客服审核不通股再次编辑审核通过
        :param content:
        :return:
        '''
        # company_id = self.get_value(content, 'company_id')
        company_id=  self.get_value(content, 'company_id')
        contract_number=self.get_value(content,'contract_number')
        log.info('新增合同')
        res1=self.check_interface(content)
        content_1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","company_id":company_id,"page_number":1,"anumber":10,"update_time_start":"","update_time_end":"","search":contract_number,"state":"","sort":2,"type":0,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res2=self.check_interface(content_1)
        log.info('合同列表')
        contract_id=self.get_value(res2[1],'contract_id')
        content_2={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","customer_user_id":"36","contract_id":contract_id,"reason":"6666","check_state":2,"user_token":""}
        res3=self.check_interface(content_2)
        log.info('审核合同不通过')
        content_3={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","company_id":"674","pur_company_id":"674","sur_company_id":"671","contract_id":contract_id,"contract_number":"08021645","type":"1","pur_name":"集团001","pur_address":"aa","sup_name":"筑链智融供应商1","sup_address":"ss","pur_invoice_name":"集团001","pur_invoice_header":"2a","pur_project_address":"天津市 市辖县 宁河县 111","pur_taxno":"2222","pur_financetel":"022-6663334","pur_linkman":"aa","pur_bank":"建设银行","pur_account":"56523232","sup_invoice_name":"筑链智融供应商1","sup_invoice_header":"发票抬头1","sup_project_address":"天津市 市辖区 和平区 天津市","sup_taxno":"123123123123","sup_financetel":"021-4756222","sup_linkman":"小方","sup_bank":"华夏","sup_account":"45555552222222222","project_name":"0802","engineering_address":"北京市 市辖区 东城区 aaa","linkman":"ss","linkphone":"123","quote_way":"1","quantity_select":"1","cooperation_type":"1","material_json":'[{"productName":"a","name":"a","model":"s","para":"","brand":"","place":"","unit":"d","number":"10","amount":"1000","sum":"10000.00","remark":""}]',"remark":"ceshihetong","content":"1、本合同经双方协商一致后可以变更或解除；未尽事宜双方可协商制订出补充协议，上传至平台。补充协议与本合同具有具等法律效力；\n2、执行本合同发生争议时，由当事人协商解决，若协商不成，可向有管辖权的人民法院提起诉讼；\n3、本合同一式两份，甲、乙双方各执壹份，自甲、乙双方代表签字及盖章之日生效，双方结清货款后自动失效\n                    ","payway":"","last_pay_date":"","sign_date":"2019-08-02","attach_id":"12471","source":1,"is_draft":2,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res4=self.check_interface(content_3)
        log.info('编辑合同')
        content_4={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","customer_user_id":"36","contract_id":contract_id,"reason":"","check_state":1,"user_token":""}
        res5=self.check_interface(content_4)
        log.info('审核合同通过')
        return res5

    def edict_attach(self,content):
        '''
        新增合同审核通过编辑附件审核不通过后再次修改附件，客服审核通过
        :param content:
        :return:
        '''
        contract_number=self.get_value(content,"contract_number")
        company_id=self.get_value(content,"company_id")
        res=self.check_interface(content)
        log.info('新增合同')
        # print(type(res))
        # res1=self.check_interface(content1)
        contract_id=self.get_value(res[1],"contract_id")
        print(contract_id)
        content2={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","customer_user_id":"36","contract_id":contract_id,"reason":"","check_state":1,"user_token":""}
        res2=self.check_interface(content2)
        log.info('审核合同通过')
        content3= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","company_id":company_id,"contract_id":contract_id,"attach_id":"12650,12651","user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res3=self.check_interface(content3)
        log.info('编辑合同附件')
        content4={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","customer_user_id":"36","check_state":"2","contract_id":contract_id,"attach_id":"12650,12651","reason":"不通过","user_token":""}
        res4=self.check_interface(content4)
        log.info('审核附件不通过')
        res5=self.check_interface(content3)
        log.info('编辑合同附件')
        content6={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"","customer_user_id":"36","check_state":"2","contract_id":contract_id,"attach_id":"12650,12651","reason":"通过","user_token":""}
        res5=self.check_interface(content6)
        log.info('审核附件通过')
        return res5















