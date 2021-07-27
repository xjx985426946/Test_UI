# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    forget_pwd_success = [{'username': '19900000012', 'new_pwd': '123456', 'new_pwd_second': '123456', 'check': '欢迎登录智蜂'}]
else:
    forget_pwd_success = [{'username': '19900000012', 'new_pwd': '123456', 'new_pwd_second': '123456', 'check': '欢迎登录智蜂'}]

# 错误提示
forget_pwd_err = [{'username': '19900000012', 'code': '5555', 'check': '验证码不正确'}]

forget_pwd_err2 = [{'username': '19900000012', 'new_pwd': '123456', 'new_pwd_second': '456789', 'check': '两次密码输入不一致，请重新输入'}]
