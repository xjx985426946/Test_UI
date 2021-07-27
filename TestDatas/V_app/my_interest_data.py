# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '我的兴趣'}]
else:
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '我的兴趣'}]

add_interest = [{'username': '13640993513', 'password': '123456', 'add_interest': '测试添加', 'check': '跳转成功'}]

add_interest_err = [{'username': '13640993513', 'password': '123456', 'check': '标签名不能为空'}]

add_interest_err2 = [{'username': '13640993513', 'password': '123456', 'check': '标签名不能少于4个字'}]
