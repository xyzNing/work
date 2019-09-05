import pymysql
class Db():
    def __init__(self,host='120.78.189.5',port=3306,user='ninggq@zhujc.com',password='lILVNHmErNr4VoGy',db='zjcbytest',charset='utf8'):
        self.db=pymysql.connect(host=host,port=port,user=user,passwd=password,db=db,charset=charset)
        self.cursor=self.db.cursor()

    def modify_db(self,number):
        '''
        修改标书状态，由正在招标变为开标议标
        :param number: 标书编号
        :return:
        '''
        sql="update zjc_bid set state='4' where number=%s"
        try:
            self.cursor.execute(sql,[number])
            self.db.commit()
            print('xiugai success')
        except:
            self.db.rollback()
        self.db.close()

    def select_db(self,phone):
        '''
         传入手机号，获取短信验证码
        :param phone: 需要查询的手机号
        :return: 返回截取的验证码的值
        '''
        sql="select content from zjc_sms where phone=%s order by sendtime desc "%phone
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchone()
            return result[0][11:15:]
        except:
            raise ("查询失败")
if __name__ == '__main__':
    db=Db()
    # s=db.select_db('13937949015')
    # print(s)
    # print(s[0][11:15:])
    db.modify_db('ZB190902030')
