import logging
import logging.handlers
import os
import time


class Logger():
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        rp=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=r'C:\gitStore\test_zjc_pytest\logs\\'
        log_name=log_path+rp+".log"
        dd=logging.handlers.TimedRotatingFileHandler(log_name,when='D',interval=1, backupCount=3,encoding='utf-8')
        # fh=logging.FileHandler(log_name,encoding='utf-8')
        # fh.setLevel(logging.INFO)
        dd.setLevel(logging.INFO)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fh.setFormatter(formatter)
        dd.setFormatter(formatter)
        ch.setFormatter(formatter)

        # self.logger.addHandler(fh)
        self.logger.addHandler(dd)
        self.logger.addHandler(ch)
        # self.logger.removeHandler(dd)
        # self.logger.removeHandler(ch)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    print( os.path.dirname(os.getcwd())+'/logs'+"/")