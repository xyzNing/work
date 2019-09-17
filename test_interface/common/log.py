import logging
import logging.handlers
import os
from _datetime import datetime
class Logger(object):
    def __init__(self,logger,):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        rp = datetime.strftime(datetime.now(), "%Y%m%d")
        file_path = os.path.join(os.getcwd(), "Log") + "\\" + str(rp) + '.logs'
        dd = logging.handlers.TimedRotatingFileHandler(file_path,when='d',interval=1,backupCount=3)
        fh=logging.FileHandler(file_path,encoding='utf-8')
        ch=logging.StreamHandler()

        format=logging.Formatter("%(asctime)s-%(name)s-%(lineno)d-%(filename)s-%(funcName)s-%(message)s")

        # fh.setFormatter(format)
        ch.setFormatter(format)
        dd.setFormatter(format)

        self.logger.addHandler(dd)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger


log=Logger("mylog").get_logger()


if __name__ == '__main__':
    print(os.getcwd())
    rp = datetime.strftime(datetime.now(), "%Y%m%d%H%M")
    print(os.path.dirname(os.getcwd()))
    print(rp)
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print("*"*20)
    print(os.path.abspath('.'))
    print(os.path.dirname(os.path.abspath('.')))
    file_path = os.path.join(os.path.dirname(os.getcwd()),"Log")+"\\"+str(rp)+'.logs'
    print(file_path)
    print('111')
    print(os.path.abspath(os.curdir))
    print(os.path.abspath('..'))