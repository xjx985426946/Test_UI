# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '我的订单'}]
else:
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '我的订单'}]

# 错误提示
login_user_err = [{'username': '13611111112', 'password': '123456', 'check': '帐号未注册'},
                   {'username': '13640993513', 'password': '1234', 'check': '密码为6-20个字符'},
                   {'username': '13640993513', 'password': '1234568', 'check': '密码错误'}]

login_user_err2 = [{'username': '', 'password': '123456', 'check': '手机号码有误'}]
