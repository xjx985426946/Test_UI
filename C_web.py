import pytest, time, os
cur_path = os.path.dirname(os.path.realpath(__file__))
now = time.strftime("%Y-%m-%d")
report_file = 'report/'+now+'_test_result.html'
pytest.main(['-m', 'domes',
             '-v',
             # "--reruns", "1",  #将错误的用例重跑两次
             # "--reruns-delay","1", #每个
             cur_path + '/TestCase/test_C_web',
             "--html=%s" % (report_file),
             "--junitxml=" + cur_path +"/report/result.xml"])
#
# from other.api import Api
# a = Api()
# cookies = a.f_login("13600000000", "e10adc3949ba59abbe56e057f20f883e").cookies
# # 登录v端
# access_token = a.v_login("13729542194", "e10adc3949ba59abbe56e057f20f883e").json()['result']['access_token']
# # 登录c端
# Au = a.c_login("13729542194", "e10adc3949ba59abbe56e057f20f883e")
# c_access_token = Au.json()['result']['token']
# ccookies = Au.cookies
#
# a.repay()


#网络慢执行会报错，其实不是bug

#5个是报错

#但是不清楚是网络问题 还是 bug  这是UI自动化测试的痛点

#80%
#

