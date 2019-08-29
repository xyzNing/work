#conding=utf-8
import os
def run_case():
    os.system(r"pytest  --alluredir=C:\Work\test_zjc_pytest\report")
    os.system(r'allure generate C:/Work/test_zjc_pytest/report -o C:/Work/test_zjc_pytest/report/html --clean')

if __name__ == '__main__':
    run_case()