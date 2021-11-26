'''
    生成日志器的配置
'''
import logging.config


#  路径一定要在调用的地方填写，否则会报错，所以这里用变量来传入
def get_log(path):
    logging.config.fileConfig(path)
    return logging.getLogger()
