import os
import unittest
import HTMLTestRunner
case_dir=os.path.join(os.getcwd(),'testcase')
report_file=os.path.join(os.getcwd(),'report')+r'\result.html'


def all_case():
    cases=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    print(cases)
    return cases


def get_report(case):
   fp=open(report_file,'wb')
   runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
   runner.run(case)
   fp.close()


print(os.getcwd())


if __name__ == '__main__':
    print(case_dir)
    print(report_file)
    all=all_case()
    get_report(all)
    # fp = open(report_file, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
    # discover = all_case()
    # runner.run(discover)
    # fp.close()