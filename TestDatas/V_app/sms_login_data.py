# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    sms_login_success = [{'username': '19900000012', 'code': '5555', 'check': 'True'}]
else:
    sms_login_success = [{'username': '19900000012', 'code': '5555', 'check': 'True'}]

# 错误提示
sms_login_err = [{'username': '19900000012', 'code': '5555', 'check': '验证码不正确'}]

