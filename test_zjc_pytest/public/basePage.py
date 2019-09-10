#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from public.log import Logger
from time import sleep
import os.path
import time
import xlwt
import xlrd
from xlutils.copy import copy
# import sys

mylog=Logger(logger="BasePage").getlog()
#初始化浏览器
# def browser(browser='Firefox'):
#     try:
#         if browser=='Firefox':
#             profile_dir=r"C:\Users\ning\AppData\Roaming\Mozilla\Firefox\Profiles\vug7kmnt.default-1558406072358"
#             profile=webdriver.FirefoxProfile(profile_dir)
#             driver=webdriver.Firefox(profile)
#             mylog.info("打开火狐浏览器")
#             return driver
#         elif browser=='Chrome':
#             driver=webdriver.Chrome()
#             mylog.info("打开谷歌浏览器")
#             return driver
#         elif browser=='Ie':
#             driver=webdriver.Ie()
#             mylog.info("打开ie浏览器")
#             return driver
#         else:
#             print(u"请重新选择浏览器")
#     except Exception as msg:
#         print('%s' %msg)
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def open(self,url):
        '''
        打开网页，并最大化处理
        :param url:
        :return:
        '''
        self.driver.get(url)
        mylog.info(u"打开网址 %s"%url)
        self.driver.maximize_window()

    def refresh(self):
        '''
        刷新浏览器
        :return:
        '''
        self.driver.reresh()
        mylog.info(u"刷新浏览器")

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def find_element(self,selector,time=10):
        '''
        定位元素，超过10s未定位到直接定位失败
        :param selector:
        :param time:
        :return:
        '''
        # mylog.info("调用模块的名字是：%s"%sys._getframe().f_code.co_name)
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

    def find_element_all(self,selector,time=10):
        '''
        定位一组元素
        :param selector: 元祖参数，格式为（By.ID,'xxx'）
        :param time:
        :return:
        '''
        try:
            elements=WebDriverWait(self.driver,time,1).until(EC.presence_of_all_elements_located(selector))
            sleep(1)
            mylog.info(u"找到元素——%s" % selector[1])
            return elements
        except Exception as msg:
            mylog.info(u"定位元素失败——%s" %selector[1])
            self.get_screen()

    def scroll(self,high='10000'):
        '''
        处理滚动条，滑动到底部，
        :param high: 滑到顶部high=0
        :return:
        '''
        js = "var q=document.documentElement.scrollTop=%s"%high
        self.driver.execute_script(js)

    def click(self,selector):
        try:
            element=self.find_element(selector)
            element.click()
            mylog.info(u"点击元素成功——%s" % selector[1])
        except Exception as msg:
            mylog.error(u"点击元素失败——%s" %selector[1])
            self.get_screen()
            raise

    def send_keys(self,selector,text):
        '''
        文本框中输入信息
        :param selector:
        :param text:
        :return:
        '''
        element=self.find_element(selector)
        element.clear()
        element.send_keys(text)

    # def send_keys_all(self,selector,text):
    #     elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(selector))
    #     for element in elements:
    #         self.driver.execute_script("arguments[0].style.border='1px solid red'", element)
    #         element.clear()
    #         element.send_keys(text)
    #     print('111')

    def upload_pictures(self,selector):
        '''
        统一处理上传图片的插件
        :param selector: 插件按钮的元素地址
        :return:
        '''
        self.click(selector)
        mylog.info("开始上传图片")
        os.system(r"C:\Users\ning\Desktop\SendPhoto.exe")
        mylog.info("上传图片成功")
        time.sleep(1)

    #类似选择发票。选择合同的处理
    def choose(self,selector1,selector2,text,selector3,selector4,selector5):
        self.click(selector1)
        self.send_keys(selector2,text)
        self.click(selector3)
        sleep(1)
        self.click(selector4)
        self.click(selector5)

    def switch_default_handel(self):
        '''
        当前打开多个窗口时，切换到默认的窗口
        :return:
        '''
        handle=self.driver.current_window_handle()
        self.driver.switch_to.window(handle)

    def switch_handel(self):
        '''
         切换到新打开页面
        :return:
        '''
        all_handles=self.driver.window_handles
        print(all_handles)
        self.driver.switch_to.window(all_handles[1])


    def switch_to_frame(self,selector):
        '''
        切换到浏览器frame
        :param selector:
        :return:
        '''
        if selector[0]=='BY.ID' or selector[0]=='BY.NAME':
            self.driver.switch_to.frame(selector[1])
        else:
            iframe=self.find_element(selector)
            self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        '''
        切换到进入fram前页面
        :return:
        '''
        self.driver.switch_to_default_content()

    def select_by_value(self,selector,value):
        '''
         通过value值选择下拉框内容
        :param selector:
        :param value:
        :return:
        '''
        s=self.find_element(selector)
        Select(s).select_by_value(value)

    def select_by_index(self,selector,index):
        '''
         #通过索引选择下拉框
        :param selector:
        :param index:
        :return:
        '''
        s=self.find_element(selector)
        Select(s).select_by_index(index)

    def select_by_text(self,selector,text):
        '''
        通过下拉框的内容
        :param selector:
        :param text:
        :return:
        '''
        s=self.find_element(selector)
        Select(s).select_by_visible_text(text)

    def move_to_element(self,selector):
        '''
        移动到元素上
        :param selector:
        :return:
        '''
        try:
            s=self.find_element(selector)
            ActionChains(self.driver).move_to_element(s).perform()
            mylog.info(u"移动到元素成功——%s" % selector[1])
        except:
            mylog.info(u"移动到元素失败——%s" % selector[1])

    def context_click(self,selector):
        '''
        模拟鼠标右击
        :param selector:
        :return:
        '''
        s=self.find_element(selector)
        ActionChains(self.driver).context_click(s)

    def double_click(self,selector):
        '''
        模拟鼠标双击
        :param selector:
        :return:
        '''
        s = self.find_element(selector)
        ActionChains(self.driver).double_click(s)

    def send_date(self,selector,date):
        '''
        处理日期控件,输入日期格式的内容
        :param selector:
        :param date:
        :return:
        '''
        element = self.find_element(selector)
        js='document.getElementById("%s").removeAttribute("readonly")'%selector[1]
        self.driver.execute_script(js)
        element.clear()
        element.send_keys(date)

    # def alert(self,selector):
    #     element=self.find_element(selector)
    #     t=self.switch_to_alert()
    #     print(t.text)
    #     t.accept()

    def get_screen(self):
        '''
        截图并保存
        :return:
        '''
        file_path=os.path.dirname(os.getcwd())+r'\screens\''
        now_time=time.strftime('%Y-%m-%d-%H-%M-%S')
        screen_name=file_path+now_time+'.png'
        self.driver.get_screenshot_as_file(screen_name)

    def element_text(self,selector):
        '''
        获取元素的文本内容
        :param selector:
        :param time:
        :return:
        '''
        element=self.find_element(selector)
        return element.text

    def element_texts(self,selector,time=10):
        '''
        获取一组元素文本属性
        :param selector:
        :param time:
        :return: 返回元素文本的列表
        '''
        try:
            elements = WebDriverWait(self.driver, time, 1).until(EC.presence_of_all_elements_located(selector))
            print('1111')
            sleep(1)
            L=[]
            for ele in elements:
                text1 = ele.text
                print(text1)
                L.append(text1)
            return L
        except Exception as msg:
            mylog.error(msg)


    def accept(self):
        '''
        #处理浏览器自带alert框,点击确定
        :return:
        '''
        alert=self.driver.switch_to.alert
        alert.accept()
        mylog.info('aletr点击确定成功')

    def dismiss(self):
        '''
        点击取消
        :return:
        '''
        alert = self.driver.switch_to.alert
        alert.dismiss()
        mylog.info('aletr点击取消成功')

    def text(self):
        '''
        获取浏览器自带alert中的文本
        :return:
        '''
        alert = self.driver.switch_to.alert
        return alert.text

    def text_in_element(self,selector,text):
        '''
        判断text是否在元素属性的文本中
        :param selector:
        :param text:
        :return:
        '''
        result=EC.text_to_be_present_in_element(selector,text)(self.driver)
        return result

    def text_in_elementValue(self,selector,text):
        '''
        判断text是否在元素的值中
        :param selector:
        :param text:
        :return:
        '''
        result=EC.text_to_be_present_in_element_value(selector,text)(self.driver)
        return result

    def element_is_select(self,selector):
        '''
        判断元素是否被选中
        :param selector:
        :return:
        '''
        return EC.element_located_to_be_selected(selector)(self.driver)


    def write_excel(self,List,type1):
        '''
        写excel
        :param List: 列表，需要写入excel的值
        :param type1: excel中sheet的名字
        :return:
        '''
        # file = os.path.dirname(os.getcwd()) + r"\Date\date.xls"
        file=r'C:\gitStore\test_zjc_pytest\Data\date.xls'
        if os.path.exists(file):
            book = xlrd.open_workbook(file)
            row = book.sheet_by_name(type1).nrows
            sheets = book.sheet_names()
            print(sheets)
            print(row)
            new_book = copy(book)
            sheet=new_book.get_sheet(type1)
            mylog.info('开始写入%s编号'%type1)
            for i in range(len(List)):
                print(len(List))
                print(List[i])
                sheet.write(row + 1, i, List[i])
                mylog.info("正在写入%s编号"%type1+List[i])
            mylog.info("%s写入完成"%type1)
            new_book.save(file)
        else:
            book = xlwt.Workbook(encoding="utf-8")
            sheet = book.add_sheet("instock")
            sheet2 = book.add_sheet("invoice")
            for i in range(len(List)):
                sheet.write(1, i, List[i])
            book.save(file)

    def read_excel(self,type):
        '''
        读取excel中的内容
        :param type: 需要读取的excel的表格sheet名称
        :return:
        '''
        file = r'C:\gitStore\test_zjc_pytest\Data\date.xls'
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_name(type)
        row = book.sheet_by_name(type).nrows
        mylog.info("开始读"+type+"信息")
        data = sheet.row_values(row - 1)
        mylog.info("读取%s的值为%s"%(type,data))
        return data

    def arr_sort(self,arr):
        '''
        冒泡排序,先从小到大排序,最后按照从大到小返回
        :param arr: 数组
        :param m: 默认取最大的一个
        :return: 数组，按照从大到小，方便取值
        '''
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
        return arr[::-1]
























