from config.basePage import BasePage
from selenium.webdriver.common.by import By
import time
class PubProject(BasePage):
    project_name=(By.XPATH,"//*[@text='填写项目名称']")

    manage_unit=(By.XPATH,"//*[@text='填写管理单位']")
    manage_unit_detail=(By.ID,'com.zhujc.purchasedev:id/im_item_recy_dialog')
    manage_unit_ensure=(By.ID,'com.zhujc.purchasedev:id/tv_dialog_select_list_ok')

    project_type = (By.XPATH, "//*[@text='填写项目类型']")
    project_manage=(By.XPATH,"//*[@text='填写项目经理']")
    contact=(By.XPATH,"//*[@text='填写联系方式']")
    total_project_cost=(By.XPATH,"//*[@text='填写项目总造价']")
    floor_area=(By.XPATH,"//*[@text='填写占地面积']")
    building_area=(By.XPATH,"//*[@text='填写建筑面积']")
    project_cycle=(By.XPATH,"//*[@text='填写项目周期']")
    add_project_is=(By.XPATH,"//*[@text='是']")
    add_project_no=(By.XPATH,"//*[@text='否']")

    project_state=(By.XPATH,"//*[@text='选择项目状态']")
    project_state_detail=(By.ID,'com.zhujc.purchasedev:id/im_item_recy_dialog')
    project_state_ensure=(By.ID,'com.zhujc.purchasedev:id/tv_dialog_select_list_ok')

    project_address1=(By.XPATH,"//*[@text='选择省市区域']")
    project_address1_provice=(By.ID,'com.zhujc.purchasedev:id/wv_dialog_address_province')
    project_address1_city=(By.ID,'com.zhujc.purchasedev:id/wv_dialog_address_city')
    project_address1_area=(By.ID,'com.zhujc.purchasedev:id/wv_dialog_address_area')
    project_address1_ensure=(By.ID,'com.zhujc.purchasedev:id/tv_dialog_address_commit')
    # 159,1695 ,1830
    project_address2 = (By.XPATH, "//*[@text='填写具体街道']")
    project_desc=(By.XPATH,"//*[@text='填写具体描述']")

    add_pictures=(By.XPATH,"//*[@text='添加图片']")
    add_pictures_1=(By.ID,'com.zhujc.purchasedev:id/bt_dialog_img_album')
    # 305,407
    # 778, 476
    project_save=(By.ID,'com.zhujc.purchasedev:id/tv_add_project_save')

    def pub_project(self,text,text2,text3,text4,text5,area1,area2,cycle,address,desc):
        self.send_text(self.project_name,text)
        self.select(self.manage_unit,self.manage_unit_detail,self.manage_unit_ensure)
        self.send_text(self.project_type,text2)
        self.send_text(self.project_manage,text3)
        self.send_text(self.contact,text4)
        self.send_text(self.total_project_cost,text5)
        self.send_text(self.floor_area,area1)
        self.send_text(self.building_area,area2)
        self.send_text(self.project_cycle,cycle)
        self.select(self.project_state,self.project_state_detail,self.project_state_ensure)
        self.swipe_up()
        time.sleep(1)
        self.click(self.project_address1)
        self.swipe(200,1730,200,1660)
        time.sleep(1)
        self.swipe(575,1730,575,1660)
        time.sleep(1)
        self.swipe(900,1730,900,1660)
        time.sleep(1)
        self.click(self.project_address1_ensure)
        self.send_text(self.project_address2,address)
        self.send_text(self.project_desc,desc)
        self.uoload_photo(self.add_pictures,self.add_pictures_1,self.project_save)
        # self.click(self.add_pictures)
        # self.click(self.add_pictures_1)
        # self.tap(305,407)
        # time.sleep(1)
        # self.tap(778,476)
        # self.click(self.project_save)










