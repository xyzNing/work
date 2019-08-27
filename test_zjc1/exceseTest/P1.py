from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
try:
    ele=driver.find_element_by_xpath("//aA90909")
    print(ele)
except Exception:
    raise Exception('未找到该元素')

print(type(ele))
print(len(ele))


result=EC.text_to_be_present_in_element((By.ID,'su'),'百度一下')(driver)
print(result)

# for s in ele:
#     print(s)


# e=driver.find_element_by_id("su")
# print(type(e))
# print(e)
# print(len(e))

