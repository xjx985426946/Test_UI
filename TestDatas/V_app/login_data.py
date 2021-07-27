# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '等待十二的二十一'}]
else:
    login_success = [{'username': '13640993513', 'password': '123456', 'check': '等待十二的二十一'}]

# 错误提示
login_user_err = [{'username': '13640993513', 'password': '555555', 'check': '密码错误，请重新输入！'},
                  {'username': '1364099', 'password': '555555', 'check': '输入的手机号有误，请重新输入！'}]
                  # {'username': '1364099', 'password': '1234568', 'check': '输入的手机号有误，请重新输入！'}]

login_user_err2 = [{'username': '13655555555', 'password': '123456', 'check': '参数有误:用户信息不存在'}]
