import os
import time

# 项目路径
project_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(project_dir)

# 测试报告路径
report_dir = os.path.join(project_dir,'report')
# now = time.strftime('%Y-%m-%d_%H_%M_%S')
# # print(now)
# report = os.path.join(report_dir,'report_'+now+'.html')

# 测试用例
case_dir = os.path.join(project_dir,'TestCase')
# print(case_dir)

# 日志
# logs_dir = os.path.join(project_dir,'logs')

# 截图
screenshot_dir = os.path.join(project_dir, 'ScreenShot')

