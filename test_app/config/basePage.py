from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from config.log import logger
import time
import os
import random


def get_driver(plat_name, device_name, plat_version, app_package, app_activity):
    desired_caps = {
            'platformName': plat_name,
            'deviceName': device_name,
            'platformVersion': plat_version,
            'appPackage': app_package,
            'appActivity': app_activity,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            "noReset": True
        }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logger.info(u'获取driver成功')
    return driver


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, loc_time=10):
        """
        查找元素
        :param locator: 元素的元祖参数
        :param loc_time: 查找时间，默认超时时间10s
        :return:
        """
        try:
            element = WebDriverWait(self.driver, loc_time).until(ec.presence_of_element_located(locator))
            return element
        except WebDriverException:
            logger.error('未找到元素' + '%s' % list(locator))
        else:
            logger.info(u'找到元素%s' % (list(locator)))


    def find_elements(self, locator, loc_time=10):
        try:
            elements = WebDriverWait(self.driver, loc_time).until(ec.presence_of_all_elements_located(locator))
            logger.info(u'找到元素' + '%s' % (list(locator)))
            return elements
        except Exception as msg:
            logger.error('未找到元素' + '%s' % list(locator))
            logger.error("报错信息是：%s" % msg)

    def swipe(self, x, y, x1, y1, loc_time=500):
        self.driver.swipe(x, y, x1, y1, loc_time)
        logger.info(u'滑动成功')

    def tap(self, x, y, loc_time=500):
        self.driver.tap([(x, y)], loc_time)
        logger.info('tap success')

    def scroll(self, ori_loc, des_loc):
        ele1 = self.find_element(ori_loc)
        ele2 = self.find_element(des_loc)
        self.driver.scroll(ele1, ele2)
        logger.info(u'从%s滑动到%s' % (list(ori_loc), list(des_loc)))

    def upload_photo(self, locator1, locator2, locator3):
        self.find_element(locator1)
        self.find_element(locator2)
        self.tap(305, 407)
        time.sleep(1)
        self.tap(778, 476)
        self.click(locator3)

    def select(self, locator1, locator2, locator3):
        """
        :param locator1: 第一个点击的元素，点击进入弹框页面
        :param locator2: 定位弹框里的一组元素，任意选择其中的一个点击
        :param locator3: 弹框中的确定按钮
        :return:
        """
        try:
            self.find_element(locator1).click()
            elements = self.find_elements(locator2)
            num = random.randint(0, len(elements)-1)
            elements[num].click()
            self.find_element(locator3).click()
            logger.info(u'选择%s成功' % list(locator2))
        except Exception as msg:
            logger.info(u'选择%s失败' % list(locator2))
            logger.error("报错信息是：%s" % msg)

    def add_material(self, loc1, loc2, text2, loc3, tex3, loc4, text4, loc5, text5, loc6,
                     text6, loc7, text7, loc8, text8):
        self.click(loc1)
        self.send_text(loc2, text2)
        self.send_text(loc3, tex3)
        self.send_text(loc4, text4)
        self.send_text(loc5, text5)
        self.send_text(loc6, text6)
        self.send_text(loc7, text7)
        self.send_text(loc8, text8)

    def get_contexts(self):
        logger.info(u'获取contexts成功')
        return self.driver.contexts

    def switch_to_context(self, con_type):
        try:
            if con_type == '1':
                self.driver.switch_to.context('NATIVE_APP')
                logger.info(u'切换到NATIVE_APP成功')
            else:
                contexts = self.get_contexts()
                self.driver.switch_tocontent(contexts[1])
                logger.info(u'切换到%s成功' % contexts[1])
        except Exception as msg:
            logger.error(u'切换content失败')
            logger.error("报错信息是：%s" % msg)

    def get_element_size(self):
        # element=self.find_element(locator)
        x = self.driver.element.location.get('x')
        y = self.driver.element.location.get('y')
        return x, y

    def get_screen(self):
        file = r'c:\gitStore\test_app\screens\''
        file_path = file + time.strftime('%Y%m%d%H%M') + '.png'
        self.driver.get_screenshot_as_file(file_path)

    def click(self, locator):
        try:
            self.find_element(locator).click()
            logger.info(u'点击%s成功' % (list(locator)))
        except Exception as msg:
            logger.error(u'点击%s失败' % (list(locator)))
            logger.error("报错信息是：%s" % msg)

    def send_to_text(self, locator1, locator2, text, locator3):
        """
        定位到元素后，点击在新的页面填写内容，保存后再回到之前页面
       :param locator1: 定位的元素
       :param locator2: 输入内容框的元素
       :param locator3: 保存按钮
       :param text: 输入的内筒
       :return:
        """
        try:
            self.find_element(locator1).click()
            self.send_text(locator2, text)
            self.find_element(locator3).click()
            logger.info(u'输入%s成功' % text)
        except Exception as msg:
            logger.error(u'输入%s失败' % text)
            logger.error("报错信息是：%s" % msg)

    def send_text(self, locator, text):
        """
        :param locator: 定位元素
        :param text: 输入的文本信息
        :return:
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as msg:
            logger.error(u'输入%s失败，原因是%s' % (text, msg))

        else:
            logger.info(u'输入%s成功' % text)

    def send_time(self, loc1, loc_year, loc_month, loc_day, loc2):
        """
        点击元素，选择年月日
        :param loc1:
        :param loc_year: 年
        :param loc_month: 月
        :param loc_day: 日
        :param loc2: 确定
        :return:
        """
        self.click(loc1)
        ele_year = self.find_elements(loc_year)
        ele_year[random.randint(0, len(ele_year)-1)].click()
        ele_month = self.find_elements(loc_month)
        ele_year[random.randint(0, len(ele_month) - 1)].click()
        ele_day = self.find_elements(loc_day)
        ele_year[random.randint(0, len(ele_day) - 1)].click()
        self.click(loc2)

    def get_ele_attribute(self, locator, ele_type):
        try:
            element = self.find_element(locator)
            if ele_type=='text':
                return element.text
            else:
                return element.get_attribute(ele_type)
        except Exception as msg:
            logger.error(u"获取%s失败" % list(locator))
            logger.effor("报错信息是：%s" % msg)
        else:
            logger.info(u"获取%s成功，值为：%s" % (list(locator), element.text))

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, t=1000):
        size = self.get_size()
        x = int(size[0]*0.5)
        y1 = int(size[1]*0.9)
        y2 = int(size[1]*0.1)
        self.driver.swipe(x, y1, x, y2, t)
        logger.info(u'向上滑动成功')

    def swipe_down(self, t=1000):
        size = self.get_size()
        x = int(size[0]*0.5)
        y1 = int(size[1]*0.1)
        y2 = int(size[1]*0.9)
        self.driver.swipe(x, y1, x, y2, t)
        logger.info(u'向下滑动成功')

    def swipe_left(self, t=1000):
        size = self.get_size()
        y = int(size[1]*0.5)
        x1 = int(size[0]*0.9)
        x2 = int(size[0]*0.1)
        self.driver.swipe(x1, y, x2, y, t)
        logger.info(u'向左滑动成功')

    def swipe_right(self, t=1000):
        size = self.get_size()
        y = int(size[1]*0.5)
        x1 = int(size[0]*0.25)
        x2 = int(size[0]*0.75)
        self.driver.swipe(x1, y, x2, y, t)
        logger.info(u'向下滑动成功')


if __name__ == '__main__':
    print('%s' % ([1, 2]))
    print(time.strftime('%Y%m%d%H%M'))
    #  file = r'c:\gitStore\test_app\screens'
    file1 = os.path.join(os.path.dirname(os.getcwd()), r'screens')
    file_path1 = file1 + time.strftime('%Y%m%d%H%M') + '.png'
    print(file_path1)
