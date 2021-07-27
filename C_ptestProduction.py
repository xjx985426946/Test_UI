import pytest,time,os

cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path = cur_path + '/web/autotest/ui/'


now = time.strftime("%Y-%m-%d")
xml_file =  path + 'phone_production_result.xml'
report_file =  path + now +'_phone_production_result.html'


pytest.main(['-m','production',
             '-v',
             "--reruns","5",  #将错误的用例重跑两次
             "--reruns-delay","2", #每个
             'TestCase/test_C_phone',
             "--html=%s" % (report_file),
             "--junitxml=%s"%(xml_file)])






