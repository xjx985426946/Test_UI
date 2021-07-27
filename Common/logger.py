import logging
from logging.handlers import RotatingFileHandler
import os,sys
import time
from Common import dir_config


cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
log_path = os.path.join(os.path.dirname('/Users/xujianxin/'), 'logs/autotest/ui')
# print(cur_path)
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.makedirs(log_path)

path = str(sys.argv[0]).split('/')[-1]

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d", time.localtime())


if path == 'C_ptest.py':
    handler_2 = RotatingFileHandler(log_path+"/C_phone_{0}.log".format(curTime),backupCount=20,encoding='utf-8')
if path == 'C_ptestProduction.py':
    handler_2 = RotatingFileHandler(log_path + "/C_phoneProduction_{0}.log".format(curTime), backupCount=20,
                                    encoding='utf-8')
if path == 'C_web.py':
    handler_2 = RotatingFileHandler(log_path + "/C_web_{0}.log".format(curTime), backupCount=20,
                                    encoding='utf-8')
if path == 'C_webProduction.py':
    handler_2 = RotatingFileHandler(log_path + "/C_webProduction_{0}.log".format(curTime), backupCount=20,
                            encoding='utf-8')
else:
    handler_2 = RotatingFileHandler(log_path + "/C_phone_{0}.log".format(curTime), backupCount=20, encoding='utf-8')
# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])




