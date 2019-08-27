import os
from selenium import webdriver
from selenium.webdriver.common.by import By
path=os.path.dirname(os.getcwd())
path1=os.path.dirname(os.getcwd())+r"\Date\date.xls"
print(path)
print(path1)
ele="//table[@class='list-table list-table-cover']/tbody/tr[i]/td/div[@class='textleft pl15']"
for i in range(1,11):
    loc_invoice_num=(By.XPATH,"//table[@class='list-table list-table-cover']/tbody/tr[%s]/td/div[@class='textleft pl15']"%i)
    print(loc_invoice_num)
driver=webdriver.Firefox()
driver.find_elements_by_xpath()