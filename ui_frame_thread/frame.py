'''
    关键字驱动框架主入口
data：
	存放测试用例文件
excel_driver：
	1、excel_conf，excel表格的样式配置封装成方法
	2、excel_read，数据驱动类，负责从读取frame.py处理好的数据
my_conf：
	1、log.ini，log的配置文件
	2、log_conf.py，封装log的方法，生成日志器的配置
	3、chrome_options.py，chrome浏览器的配置
ui_keys：
	Web_Keys，关键字驱动类，将定位元素、输入元素、断言等逻辑进行封装
frame.py：
	1、程序执行的主入口
	2、批量处理excel，将处理好的excel通过列表形式传给excel_read
mylog.log：
	通过log.ini生成的日志，记录程序执行的日志

'''
from ui_frame.excel_driver import excel_read
from ui_frame.my_conf import log_conf
import os

if __name__ == '__main__':
    # 通过主入口调用excel驱动读写(excel_read)，实现自动化测试
    # 1.生成日志器
    log = log_conf.get_log('./my_conf/log.ini')
    # 2.excel驱动实现
    # excel_read.excel_runner(log)
    # 3.读取指定路径，获取所有的测试用例
    # cases的list：用于接收所有的测试用例文件
    cases = []
    # 读取指定路径下的所有文件
    for path, dir, files in os.walk('./data/'):
        for file in files:
            # 获取文件的后缀名0是文件名，1是后缀名
            file_type = os.path.splitext(file)[1]
            # 判断后缀是否为。xlsx，如果是就将路径和文件进行拼接
            if file_type == '.xlsx':
                excel_path = path + file
                # 将拼接好的文件添加到cases中
                cases.append(excel_path)
                # print(excel_path)
            else:
                log.info('文件类型错误：{}'.format(file))
        # 3.调用excel_read进行关键字驱动自动化测试
        for case in cases:
            log.info('执行{}测试用例'.format(case))
            # 调用excel_read方法运行，将用例、log传给excel_read方法
            excel_read.excel_runner(case, log)
