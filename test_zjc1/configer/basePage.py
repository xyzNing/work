#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from configer.log import Logger
from time import sleep
import os.path
import time
import xlwt
import xlrd
from xlutils.copy import copy


mylog=Logger(logger="BasePage").getlog()
#初始化浏览器
def browser(browser='Firefox'):
    try:
        if browser=='Firefox':
            profile_dir=r"C:\Users\ning\AppData\Roaming\Mozilla\Firefox\Profiles\vug7kmnt.default-1558406072358"
            profile=webdriver.FirefoxProfile(profile_dir)
            driver=webdriver.Firefox(profile)
            mylog.info("打开火狐浏览器")
            return driver
        elif browser=='Chrome':
            driver=webdriver.Chrome()
            mylog.info("打开谷歌浏览器")
            return driver
        elif browser=='Ie':
            driver=webdriver.Ie()
            mylog.info("打开ie浏览器")
            return driver
        else:
            print(u"请重新选择浏览器")
    except Exception as msg:
        print('%s' %msg)

#创建一个基础的页面对象，重写selenium的一些方法
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def open(self,url):   #打开浏览器
        self.driver.get(url)
        mylog.info(u"打开网址 %s"%url)
        self.driver.maximize_window()

    def refresh(self):    #刷新浏览器
        self.driver.reresh()
        mylog.info(u"刷新浏览器")

    def back(self):    #返回前一页面
        self.driver.back()

    def forward(self):   #进入下一页面
        self.driver.forward()

    def find_element(self,selector,time=10):   #查找元素
        try:
            element=WebDriverWait(self.driver,time).until(EC.presence_of_element_located(selector))
            self.driver.execute_script("arguments[0].style.border='2px solid red'", element)
            sleep(1)
            mylog.info(u"定位元素成功——%s" % selector[1])
            return element
        except Exception :
            mylog.error(u"定位元素失败——%s" %selector[1])
            self.get_screen()
            raise Exception('元素未找到')

    def find_element_all(self,selector,time=10):    #定位一组元素
        try:
            elements=WebDriverWait(self.driver,time,1).until(EC.presence_of_all_elements_located(selector))
            sleep(1)
            mylog.info(u"找到元素——%s" % selector[1])
            return elements
        except Exception as msg:
            mylog.info(u"定位元素失败——%s" %selector[1])
            self.get_screen()

    # def find_elements(self,selector,time=10):   #查找元素
    #     try:
    #         elements=WebDriverWait(self.driver,time).until(EC.presence_of_element_located(selector))
    #         self.driver.execute_script("arguments[0].style.border='1px solid red'", elements)
    #         sleep(1)
    #         mylog.info(u"定位元素成功——%s" % selector[1])
    #         return elements
    #     except Exception as msg:
    #         mylog.error(u"定位元素失败——%s" %selector[1])
    #         self.get_screen()

    def click(self,selector):    #点击元素
        try:
            element=self.find_element(selector)
            element.click()
            mylog.info(u"点击元素成功——%s" % selector[1])
        except Exception as msg:
            mylog.error(u"点击元素失败——%s" %selector[1])
            self.get_screen()
            raise

    def send_keys(self,selector,text):     #文本框中输入信息
        element=self.find_element(selector)
        element.clear()
        element.send_keys(text)

    def send_keys_all(self,selector,text):
        elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(selector))
        for element in elements:
            self.driver.execute_script("arguments[0].style.border='1px solid red'", element)
            element.clear()
            element.send_keys(text)
        print('111')

    #类似选择发票。选择合同的处理
    def choose(self,selector1,selector2,text,selector3,selector4,selector5):
        self.click(selector1)
        self.send_keys(selector2,text)
        self.click(selector3)
        sleep(1)
        self.click(selector4)
        self.click(selector5)


    def send_pictures(self):
        mylog.info("开始上传图片")
        os.system(r"C:\Users\ning\Desktop\SendPhoto.exe")
        mylog.info("上传图片成功")
        time.sleep(1)

    def switch_default_handel(self):      #切换到默认页面
        handle=self.driver.current_window_handle()
        self.driver.switch_to.window(handle)

    def switch_handel(self):     #切换到新打开页面
        all_handles=self.driver.window_handles
        print(all_handles)
        self.driver.switch_to.window(all_handles[1])


    def switch_to_frame(self,selector):     #切换到浏览器frame
        if selector[0]=='BY.ID' or selector[0]=='BY.NAME':
            self.driver.switch_to.frame(selector[1])
        else:
            iframe=self.find_element(selector)
            self.driver.switch_to.frame(iframe)

    def switch_to_default(self):      #切换到进入fram前页面
        self.driver.switch_to_default_content()
#处理下拉框
    def select_by_value(self,selector,value):   #通过value值选择下拉框内容
        s=self.find_element(selector)
        Select(s).select_by_value(value)

    def select_by_index(self,selector,index):    #通过索引选择下拉框
        s=self.find_element(selector)
        Select(s).select_by_index(index)
#模拟鼠标操作
    def move_to_element(self,selector):     #移动到元素中
        try:
            s=self.find_element(selector)
            ActionChains(self.driver).move_to_element(s).perform()
            mylog.info(u"移动到元素成功——%s" % selector[1])
        except:
            mylog.info(u"移动到元素失败——%s" % selector[1])

    def context_click(self,selector):       #模拟鼠标右击
        s=self.find_element(selector)
        ActionChains(self.driver).context_click(s)

    def double_click(self,selector):     #模拟鼠标双击
        s = self.find_element(selector)
        ActionChains(self.driver).double_click(s)

    def send_date(self,selector,date):    #处理日期控件
        element = self.find_element(selector)
        js='document.getElementById("%s").removeAttribute("readonly")'%selector[1]
        # print(js)
        # print()
        self.driver.execute_script(js)
        # js_value="getElementById(selector[1]).value='value'"
        element.clear()
        element.send_keys(date)

    # def alert(self,selector):
    #     element=self.find_element(selector)
    #     t=self.switch_to_alert()
    #     print(t.text)
    #     t.accept()

    def get_screen(self):    #截图并保存
        file_path=os.path.dirname(os.getcwd())+r'\screens\''
        now_time=time.strftime('%Y-%m-%d-%H-%M-%S')
        screen_name=file_path+now_time+'.png'
        self.driver.get_screenshot_as_file(screen_name)

    def element_text(self,selector,time=10):
            element=self.find_element(selector)
            return element.text

    def element_texts_all(self,time=10):
        L=[]
        for i in range(1,11):
            selector= "//table[@class='list-table list-table-cover']/tbody/tr[%s]/td/div[@class='textleft pl15']"%i
            element=self.driver.find_element_by_xpath(selector)

            print(selector)
            print(element.text)
            L.append(element.text)
            sleep(1)
        return L

    def element_texts(self,selector,time=10):     #获取元素文本属性
        try:
            elements = WebDriverWait(self.driver, time, 1).until(EC.presence_of_all_elements_located(selector))
            print('1111')
            # self.driver.execute_script("arguments[0].style.border='1px solid red'",elements)
            # print('2222')
            sleep(1)
            L=[]
            for ele in elements:
                text1 = ele.text
                print(text1)
                L.append(text1)
            return L
        except Exception as msg:
            mylog.error(msg)

#处理alert框
    def accept(self,selector):    #确定
        element=self.find_element(selector)
        alert=self.driver.switch_to.alert(element)
        alert.accept()

    def dismiss(self,selector):    #取消
        element = self.find_element(selector)
        alert = self.driver.switch_to.alert(element)
        alert.dismiss()

    def text(self,selector):    #获取alert中的文本
        element = self.find_element(selector)
        alert = self.driver.switch_to.alert(element)
        return alert.text

    def text_in_element(self,selector,text):
        result=EC.text_to_be_present_in_element(selector,text)(self.driver)
        return result

    def text_in_elementValue(self,selector,text):
        result=EC.text_to_be_present_in_element_value(selector,text)(self.driver)
        return result

    def element_is_select(self,selector):
        return EC.element_located_to_be_selected(selector)(self.driver)


    def write_excel(self,List,type1):
        file = os.path.dirname(os.getcwd()) + r"\Date\date.xls"
        # file=os.path.join(file_path,"date.xls")
        if os.path.exists(file):
            book = xlrd.open_workbook(file)
            row1 = book.sheet_by_name("instock").nrows
            row2 = book.sheet_by_name("invoice").nrows
            sheets = book.sheet_names()
            print(sheets)
            print(row1, row2)
            new_book = copy(book)
            sheet1 = new_book.get_sheet(0)
            sheet2 = new_book.get_sheet(1)
            if type1 == "instock":
                mylog.info("开始写入入库单编号")
                for i in range(len(List)):
                    print(len(List))
                    print(List[i])
                    sheet1.write(row1 + 1, i, List[i])
                    mylog.info("正在写入"+List[i])
                mylog.info("入库单写入完成")
            elif type1 == "invoice":
                mylog.info("开始写入发票编号")
                for i in range(len(List)):
                    sheet2.write(row2 + 1, i, List[i])
                mylog.info("写入发票编号完成")
            new_book.save(file)
        else:
            book = xlwt.Workbook(encoding="utf-8")
            sheet = book.add_sheet("instock")
            sheet2 = book.add_sheet("invoice")
            for i in range(len(List)):
                sheet.write(1, i, List[i])
            book.save(file)

    def read_excel(self,type):
        file = os.path.dirname(os.getcwd()) + r"\Date\date.xls"
        print(file)
        book = xlrd.open_workbook(file)
        sheet1 = book.sheet_by_name(type)
        # sheet2 = book.sheet_by_name("invoice")
        row1 = book.sheet_by_name(type).nrows
        # row2 = book.sheet_by_name("invoice").nrows
        mylog.info("开始读"+type+"信息")
        data1 = sheet1.row_values(row1 - 1)
        mylog.info("读取"+type+"完成")
        return data1

    def read_data(self, type):
        file = os.path.dirname(os.getcwd()) + r"\Date\casedate.xls"
        print(file)
        book = xlrd.open_workbook(file)
        sheet1 = book.sheet_by_name(type)
        # sheet2 = book.sheet_by_name("invoice")
        row1 = book.sheet_by_name(type).nrows
        col1=book.sheet_by_name(type).ncols
        print(row1,col1)
        # row2 = book.sheet_by_name("invoice").nrows
        # mylog.info("开始读" + type + "信息")
        # data1 = sheet1.row_values(row1 )
        # mylog.info("读取" + type + "完成")
        # return data1
























