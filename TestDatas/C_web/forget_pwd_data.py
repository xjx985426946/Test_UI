# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    retrieve_pwd_success = [{'username': '13640993513', 'code': '6666a', 'password': '123456', 'second_password': '123456', 'check': '我的订单'}]

# 错误提示
phone_err = [{'username': '1364099', 'code': '6666a', 'password': '123456', 'second_password': '123456', 'check': '手机号码有误'}]
code_err = [{'username': '13640993513', 'code': '123', 'password': '123456', 'second_password': '123456', 'check': '验证码有误'}]
pwd_err = [{'username': '13640993513', 'code': '6666a', 'password': '123', 'second_password': '123456', 'check': '密码为6-20个字符'}]
second_pwd_err = [{'username': '13640993513', 'code': '6666a', 'password': '123456', 'second_password': '456789', 'check': '两次密码不一致'}]

