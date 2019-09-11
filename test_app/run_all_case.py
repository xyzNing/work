import unittest
import os
import HTMLTestRunner
case_path=os.path.join(os.getcwd(),'testcase')
report_path=os.path.join(os.getcwd(),r'report\report.html')
def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
    return discover

if __name__ == '__main__':
    print(case_path)
    print(all_case())
    print(report_path)
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'这是测试报告',
                                         description=u'用例执行情况')
    runner.run(all_case())
    fp.close()
    # runner=unittest.TextTestRunner()
    # runner.run(all_case())