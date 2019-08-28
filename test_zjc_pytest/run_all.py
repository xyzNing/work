import os
def run_case():
    os.system(r'pytest -s -q --alluredir C:\gitStore\test_zjc_pytest\report')
    # os.system(r'allure generate C:\gitStore\test_zjc_pytest\report -o C:\gitStore\test_zjc_pytest\report\html')

if __name__ == '__main__':
    run_case()