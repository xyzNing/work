from common.base import Base
class InvoiceInfoPage(Base):
    def check_invoiceInfo(self,content):
        title=self.get_value(content,'title')
        company_id=self.get_value(content,'company_id')
        res=self.check_interface(content)
        content1={"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"InvoiceInfo/invoiceInfoList","company_id":company_id,"state":"","search":title,"list_type":"1","page_number":1,"anumber":"10","all_state":"1","user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        res1=self.check_interface(content1)
        invoice_info_id=self.get_value(res1[1],'invoice_info_id')
        content2= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInvoiceInfo/checkInvoiceInfo","customer_user_id":"36","invoice_info_id":invoice_info_id,"reason":"butonggguo","check_state":2,"user_token":""}
        res2=self.check_interface(content2)
        content3= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"InvoiceInfo/updateInvoiceInfo","company_id":company_id,"invoice_info_id":invoice_info_id,"title":title,"taxno":"111","address":"北京市 县 密云县 aa","financetel":"022-33336666","linkman":"aa","bank":"建设","account":"565656","short_name":"简称a","user_token":"d7570826997e4e612d9752cf83c6ea091561257682"}
        re3=self.check_interface(content3)
        content4= {"pname":"web","sn":"d41d8cd98f00b204e9800998ecf8427e","interface_name":"CustomerInvoiceInfo/checkInvoiceInfo","customer_user_id":"36","invoice_info_id":invoice_info_id,"reason":"","check_state":1,"user_token":""}
        res4=self.check_interface(content4)
        return res4

    def del_invoiceInfo(self,content):
        title = self.get_value(content, 'title')
        company_id = self.get_value(content, 'company_id')
        res = self.check_interface(content)
        content1 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "InvoiceInfo/invoiceInfoList", "company_id": company_id, "state": "", "search": title,
                    "list_type": "1", "page_number": 1, "anumber": "10", "all_state": "1",
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res1 = self.check_interface(content1)
        invoice_info_id = self.get_value(res1[1], 'invoice_info_id')
        content2={"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "InvoiceInfo/delInvoiceInfo", "company_id": company_id, "invoice_info_id": invoice_info_id,
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res2=self.check_interface(content2)
        return res2

    def set_invoiceInfo(self,content):
        title = self.get_value(content, 'title')
        company_id = self.get_value(content, 'company_id')
        res = self.check_interface(content)
        content1 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "InvoiceInfo/invoiceInfoList", "company_id": company_id, "state": "",
                    "search": title,
                    "list_type": "1", "page_number": 1, "anumber": "10", "all_state": "1",
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res1 = self.check_interface(content1)
        invoice_info_id = self.get_value(res1[1], 'invoice_info_id')
        content2 = {"pname": "web", "sn": "d41d8cd98f00b204e9800998ecf8427e",
                    "interface_name": "InvoiceInfo/setInvoiceInfo", "company_id": company_id,
                    "invoice_info_id": invoice_info_id,
                    "user_token": "d7570826997e4e612d9752cf83c6ea091561257682"}
        res2 = self.check_interface(content2)
        return res2







