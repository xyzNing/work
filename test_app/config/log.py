import os
import logging
from logging.handlers import TimedRotatingFileHandler
class Logger():
    def __init__(self,logger_name='name'):
        self.logger=logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name='log.log'
        self.backup_count=5
        self.console_level='WARNING'
        self.file_level='DEBUG'
        self.formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    def get_logger(self):
        if not self.logger.handlers:
            console_handles=logging.StreamHandler()
            console_handles.setFormatter(self.formatter)
            console_handles.setLevel(self.console_level)
            self.logger.addHandler(console_handles)

            file_handle=TimedRotatingFileHandler(filename=os.path.join(os.path.dirname(os.getcwd()),r'log\log.log'),
                                                 when='D' ,
                                                 interval=1,
                                                 backupCount=self.backup_count,
                                                 delay=True,
                                                 encoding='utf-8')
            # file_handle.suffix='%Y-%m-%d.log'
            file_handle.setFormatter(self.formatter)
            file_handle.setLevel(self.file_level)
            self.logger.addHandler(file_handle)
        return self.logger
logger=Logger().get_logger()

if __name__ == '__main__':
    print(os.getcwd())
    print(os.path.dirname(os.getcwd()))
    print(os.path.join(os.path.dirname(os.getcwd()),r'log\log.log'))