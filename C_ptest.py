import pytest,time,os

# cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(cur_path)
path = cur_path + '/web/autotest/ui/'


now = time.strftime("%Y-%m-%d")
xml_file = path + 'uiphone_result.xml'
report_file = path + now +'_uiphone_result.html'


pytest.main(['-m','domes',
             '-v',
             # "--reruns","5",  #将错误的用例重跑两次
             # "--reruns-delay","2", #每个
             # 'TestCase/test_C_phone/test_orderdetail.py',
             'TestCase/test_C_web/test_login.py',
             "--html=%s" % (report_file),
             "--junitxml=%s"%(xml_file)])


