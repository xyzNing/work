from config.basePage import BasePage
from selenium.webdriver.common.by import By
import random
import time
class PubBid(BasePage):
    # 招标项目
    bid_type_select = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_type')
    bid_type1 = (By.ID, 'com.zhujc.purchasedev:id/cb_dialog_publish_item_select')
    bid_type_confirm = (By.ID, 'com.zhujc.purchasedev:id/bt_dialog_enter')

    bill_info_select = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_invoice')
    bill_info1 = (By.ID, 'com.zhujc.purchasedev:id/cb_dialog_publish_item_select')
    bill_info_confirm = (By.ID, 'com.zhujc.purchasedev:id/bt_dialog_right')

    bid_name = (By.ID, 'com.zhujc.purchasedev:id/et_bid_publish_name')

    bid_project_select = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_project')
    bid_project1 = (By.ID, 'com.zhujc.purchasedev:id/cb_dialog_publish_item_select')
    bid_project_confirm = (By.ID, 'com.zhujc.purchasedev:id/bt_dialog_enter')

    bid_content = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_write_content')
    bid_content_send = (By.ID, 'com.zhujc.purchasedev:id/et_write_content')
    bid_content_save = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_ok')

    # 招标物资,
    material_type_select = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_product_type')

    # 非专业分包
    material_type = (By.ID, 'com.zhujc.purchasedev:id/tv_invite_type_group_title')  # 一组元素
    material_type_detail = (By.ID, 'com.zhujc.purchasedev:id/tv_invite_type_child_title')  # 一组元素
    material_type_confirm = (By.ID, 'com.zhujc.purchasedev:id/bt_dialog_enter')

    # 专业分包
    material_title = (By.ID, 'com.zhujc.purchasedev:id/tv_dialog_title')
    material_profession = (By.ID, 'com.zhujc.purchasedev:id/cb_dialog_publish_item_select')

    material_list = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_product')
    material_name = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_name')
    material_model = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_model')
    material_brand = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_brand')
    material_place = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_place')
    material_price = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_expect')
    material_unit = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_unit')
    material_count = (By.ID, 'com.zhujc.purchasedev:id/et_bid_product_count')
    material_confirm = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_product_save')

    # 供应商设置
    bid_way1 = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_way_public')
    bid_way2 = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_way_no')
    bid_way3 = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_way_invitation')

    # 商务条款
    cash_need = (By.ID, 'com.zhujc.purchasedev:id/rb_cash_need')
    cash_no = (By.ID, 'com.zhujc.purchasedev:id/rb_cash_no')
    invoice_type1 = (By.ID, 'com.zhujc.purchasedev:id/rb_cash_special')
    invoice_type2 = (By.ID, 'com.zhujc.purchasedev:id/rb_cash_common')
    invoice_type3 = (By.ID, 'com.zhujc.purchasedev:id/rb_cash_all')
    price_type1 = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_quote_fixed')
    price_type2 = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_quote_float')
    pay_content = (By.ID, 'com.zhujc.purchasedev:id/et_bid_publish_payway')
    supply_finance_no = (By.ID, 'com.zhujc.purchasedev:id/rb_no')
    supply_finance_need = (By.ID, 'com.zhujc.purchasedev:id/rb_need')
    finance_product1 = (By.ID, 'com.zhujc.purchasedev:id/cb_haier_factoring')
    sample_need = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_sample_need')
    sample_no = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_sample_no')
    delive_need = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_delivery_need')
    delive_no = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_publish_delivery_no')
    delive_address = (By.ID, 'com.zhujc.purchasedev:id/et_bid_publish_address')

    # 投标定标时间
    end_time = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_endtime')
    end_time_year = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_year')
    end_time_month = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_month')
    end_time_day = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_day')
    end_time_hour = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_hour')
    end_time_mins = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_mins')
    end_time_confirm = (By.ID, 'com.zhujc.purchasedev:id/tv_dialog_time_commit')

    confirm_time = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_confirmtime')
    confirm_time_year = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_year')
    confirm_time_month = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_month')
    confirm_time_day = (By.ID, 'com.zhujc.purchasedev:id/wv_dialog_time_day')
    confirm_time_confirm = (By.ID, 'com.zhujc.purchasedev:id/tv_dialog_time_commit')
    # 联系方式
    link_name = (By.ID, 'com.zhujc.purchasedev:id/et_bid_publish_contact')
    phone = (By.ID, 'com.zhujc.purchasedev:id/et_bid_publish_mobile')
    phone_hide_need = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_mobile_need')
    phone_hide_no = (By.ID, 'com.zhujc.purchasedev:id/rb_bid_mobile_no')
    submit = (By.ID, 'com.zhujc.purchasedev:id/bt_bid_publish_release')

    def pub_bid(self, bname, content, name, model, brand, place, price, unit, count, paycontent, linkname,
                      phonenum):
        self.click(self.bid_type_select)
        elements3 = self.find_elements(self.bid_type1)
        print(elements3)
        # num=random.choice([0,2])
        # print(num)
        elements3[0].click()
        self.click(self.bid_type_confirm)
        self.select(self.bill_info_select, self.bill_info1, self.bill_info_confirm)
        self.send_text(self.bid_name, bname)
        self.select(self.bid_project_select, self.bid_project1, self.bid_project_confirm)
        self.send_to_text(self.bid_content, self.bid_content_send, content, self.bid_content_save)
        self.click(self.material_type_select)
        text = self.get_text(self.material_title)
        print("**********")
        print(text)
        if text == u'物资类别':
            elements1 = self.find_elements(self.material_type)
            num = random.randint(0, len(elements1) - 1)
            elements1[num].click()
            elements2 = self.find_elements(self.material_type_detail)
            num = random.randint(0, len(elements2) - 1)
            elements2[num].click()
        else:
            elements = self.find_elements(self.material_profession)
            print('*' * 20)
            print(elements)
            num = random.randint(0, len(elements) - 1)
            elements[num].click()
        self.click(self.material_type_confirm)
        self.click(self.material_list)
        self.send_text(self.material_name, name)
        self.send_text(self.material_model, model)
        self.send_text(self.material_brand, brand)
        self.send_text(self.material_place, place)
        self.send_text(self.material_price, price)
        self.send_text(self.material_unit, unit)
        self.send_text(self.material_count, count)
        self.click(self.material_confirm)
        self.swipe_up()
        time.sleep(5)
        self.send_text(self.pay_content, paycontent)
        self.click(self.supply_finance_no)
        self.swipe_up()
        self.click(self.end_time)
        # contents=self.get_contexts()
        # print(contents)
        # ele_year = self.find_elements(self.end_time_year)
        self.swipe(70, 1695, 137, 1630)
        # a=self.get_element_size(self.end_time_year)
        # ele_year[random.randint(3, len(ele_year) - 1)].click()
        # ele_month = self.find_elements(self.end_time_month)
        # ele_year[random.randint(4, len(ele_month) - 1)].click()
        # ele_day = self.find_elements(self.end_time_day)
        # ele_year[random.randint(0, len(ele_day) - 1)].click()
        # ele_hour=self.find_elements(self.end_time_hour)
        # ele_hour[random.randint(0,len(ele_hour)-1)].click()
        # ele_min=self.find_elements(self.end_time_mins)
        # ele_min[random.randint(0,len(ele_min)-1)].click()
        self.click(self.end_time_confirm)
        self.click(self.confirm_time)
        self.swipe(70, 1695, 137, 1630)
        self.click(self.confirm_time_confirm)
        self.send_text(self.link_name, linkname)
        self.send_text(self.phone, phonenum)
        self.click(self.submit)