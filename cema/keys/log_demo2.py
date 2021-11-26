import logging

# 创建日志器
logger = logging.getLogger()
# 设置级别 日志信息输出info以上的级别信息
logger.setLevel(logging.INFO)
# 自定义格式
fmt = '%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
# 创建一个格式器 设置格式
formater = logging.Formatter(fmt)
# 创建一个把日志输出到控制台的处理器Handler
sh = logging.StreamHandler()
# 把日志信息添加到控制台
logger.addHandler(sh)
# 控制台设置格式
sh.setFormatter(formater)
# 创建文件处理器
fh = logging.FileHandler('log1.log', encoding='utf-8')
# 添加日志信息到文件处理器中
logger.addHandler(fh)
# 给日志修改格式
fh.setFormatter(formater)

logger.debug('debug输出')
logger.info('info输出')
logger.warning('警告输出')
logger.error('错误输出')
logger.critical('critical输出')
