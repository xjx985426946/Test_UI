# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_msg_success = [{'username': '13640993513', 'code': '6666a', 'password':'', '':'' , 'check': '我的订单'}]

# 错误提示
login_msg_err = [{'username': '13640993513', 'code': '123456', 'check': '验证码不正确'}]

login_msg_err2 = [{'username': '', 'code': '123456', 'check': '手机号码有误'},{'username': '1364000', 'code': '123456', 'check': '手机号码有误'}]
