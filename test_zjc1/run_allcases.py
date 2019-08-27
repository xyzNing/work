#  coding=utf-8
import unittest
import os
import HTMLTestRunner
case_path=os.getcwd()+r"\testcase"
report_path=os.getcwd()+r"\report"
report_abspath=os.path.join(report_path,'result.html')
print(report_abspath)
print(case_path)
# print(report_path)
def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover
#
# def get_report():
#     report_abspath = os.path.join(report_path, 'result.html')
#     fp = open(report_abspath, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
#     discover=all_case()
#     runner.run(discover)
#     fp.close()
if __name__=="__main__":
    # runner=unittest.TextTestRunner()
    # runner.run(all_case())
    # report_abspath=os.path.join(report_path,'result.html')
    # print(report_abspath)
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
    discover = all_case()
    runner.run(discover)
    fp.close()