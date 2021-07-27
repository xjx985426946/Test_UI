# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_ptest.py':
    login_sesscus = [{'username':'18126094462','password':'123456','check':'登录成功'}]
if path == 'C_ptestProduction.py':
    login_sesscus = [{'username': '13729542194', 'password': 'zckj123456', 'check': [{'personal_text': '个人中心'}]}]

# 错误提示
login_user_err = [{'username':'186847205531','password':'123456','check':'帐号未注册'},
             {'username':'','password':'123456','check':'请输入正确的手机号码'},
                  {'username':'18126094462','password':'1234','check':'请输入6位密码'},
                  {'username':'13729542194','password':'1234568','check':'密码错误'}]


