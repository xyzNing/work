from common.base import Base
from _datetime import datetime
class InovicePage(Base):
    def check_invoice(self,content):
        res=self.check_interface(content)
        company_id=self.get_value(res[1],'pur_company_id')
        sup_company_id=self.get_value(res[1],'sup_company_id')
        contract_id=self.get_value(res[1],'contract_id')
        contract_number=self.get_value(res[1],'contractno')
        pur_name=self.get_value(res[1],'pur_name')
        sup_name=self.get_value(res[1],'sup_name')
        invoice_data=datetime.strftime(datetime.now(),'%Y-%m-%d')
        product_json='{"total":"","content":[{"name":"a","model":"","unit":"","quantity":"","no_tax_pric":"","no_tax_total":"5000","tax":"10","tax_paid":"500","brand":"","para":"","place":"","id":"","invoiceId":"","amount":"","price":""}]}'
        tax=self.get_value(eval(product_json),'tax')
        no_tax_total=self.get_value(eval(product_json),'no_tax_total')
        amount=str(int(no_tax_total)+int(no_tax_total)*int(tax)/100)
        code=datetime.strftime(datetime.now(),'%Y%m%d%H%M')+'a'
        word=datetime.strftime(datetime.now(),'%Y%m%d%H%M')+'b'
        content1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Invoice/updateInvoice","company_id":company_id,"invoice_id":"","contract_id":contract_id, "contract_number":contract_number,"code":code,"pur_name":pur_name,
                  "sup_name":sup_name,"tax":tax,"amount":amount,"word":word,"type_dic_key":19003,"invoice_date":invoice_data,"product_json":product_json,"attach_id":"12672","sup_company_id":sup_company_id,"source":1,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res1=self.check_interface(content1)
        content2= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"Invoice/invoiceList","company_id":company_id,"page_number":1,"anumber":10,"source":"","update_time_start":"","update_time_end":"","search":"","state":"","sort":1,"sort_type":1,"user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res2=self.check_interface(content2)
        invoice_id=self.get_value(res2[1],'invoice_id')
        content3= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInvoice/checkInvoice","customer_user_id":"36","invoice_id":invoice_id,"reason":"6666","check_state":2,"user_token":""}
        res3=self.check_interface(content3)
        content4= {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e", "interface_name": "Invoice/updateInvoice",
                    "company_id": company_id, "invoice_id": invoice_id, "contract_id": contract_id,
                    "contract_number": contract_number, "code": code, "pur_name": pur_name,
                    "sup_name": sup_name, "tax": tax, "amount": amount, "word": word, "type_dic_key": 19003,
                    "invoice_date": invoice_data, "product_json": product_json, "attach_id": "12672",
                    "sup_company_id": sup_company_id, "source": 1, "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res4=self.check_interface(content4)
        content5= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInvoice/checkInvoice","customer_user_id":"36","invoice_id":invoice_id,"reason":"","check_state":1,"user_token":""}
        res5=self.check_interface(content5)
        return res5






