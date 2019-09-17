#conding=utf-8
import os
import time


def run_case():
    os.system(r"pytest --reruns 1 -v --alluredir C:\gitStore\test_zjc_pytest\report")
    time.sleep(2)
    os.system(r'allure generate C:\gitStore\test_zjc_pytest\report -o C:\gitStore\test_zjc_pytest\report\html --clean')

if __name__ == '__main__':
    run_case()