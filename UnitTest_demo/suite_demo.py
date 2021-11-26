import os
import unittest
import time
from unit_demo import UnitTest
from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

# 创建套件
suite = unittest.TestSuite()
# 1.添加单个用例
# suite.addTest(UnitTest('test_01'))
# suite.addTest(UnitTest('test_02'))
# 2.添加多个用例
cases = [UnitTest('test_01'), UnitTest('test_02')]
suite.addTests(cases)
# 3.添加多个用例到套件：通过添加一整个UnitTest类作为套件中的用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitTest))
# 4.添加多个用例到套件：通过Name来实现，执行unittest文件名.类名
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitTest'))
# 5.批量添加：通过文件名批量添加，在执行runner.run时将括号内容换为discover
# case_dir = './'  # 获取当前根路径
# discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='unit*.py')
# 创建默认的运行器
# runner = unittest.TextTestRunner(verbosity=2)

# 配置测试报告信息
# 测试执行者：在HTMLTestReport报告中专属参数
report_tester = '李丹杨'
# 测试报告的title
report_title = '李丹杨的测试报告'
# 描述
report_description = '这是测试报告的描述'
# 测试报告的路径
report_dir = './report/'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
# 时间戳
time_ = time.strftime('%Y-%m-%d-%H-%M-%S')
# 测试报告的名称
report_file = report_dir + time_ + 'report.html'
# 生成HTMLTestRunner测试报告相当于在文件中写入内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, tester=report_tester, title=report_title, description='测试内容', verbosity=2)
    # 运行器执行套件
    runner.run(suite)
