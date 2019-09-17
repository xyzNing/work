from common.log import log
import unittest
def test(self):
    # num = self.get_excel()
    # print(num[0], num[1])
    value = self.get_excel_value('case')
    num=len(value)
    print(value)
    for i in range(num):
        log.info("用例id：%s--用户类型；%s--接口名称：%s--请求方式：%s" % (value[i][0], value[i][1], value[i][2], value[i][3]))
        res = self.check_interface(value[i][4])
        if isinstance(res, tuple):
            self.write_excel('case', i, 7, res[0])
            self.write_excel('case', i, 8, res[1]['code'])
            self.write_excel('case', i, 9, str(res[1]))
        else:
            self.write_excel(i, 7, res)
        # new_value=self.get_excel_value(i)
        # if new_value[5]==new_value[7] and new_value[6]==new_value[8]:
        #    self.write_excel(i,10,'Pass')
        #    self.case_pass+=1
        # else:
        #    self.write_excel(i,10,'fail')
        #    self.case_fail+=1

    print(self.case_pass)
    print(self.case_fail)


if __name__ == '__main__':
    unittest.main()