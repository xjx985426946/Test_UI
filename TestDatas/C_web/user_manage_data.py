# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_success = [{'username': '13640993513', 'code': '6666a', 'check': '基本信息'}]

# 更换用户昵称
user_name = [{'username': '13640993513', 'code': '6666a', 'user_info_name': '星星点灯123', 'check': '星星点灯123'}]

# 密码修改成功
pwd_success = [{'username': '136', 'code': '6666a', 'pwd': '123456', 'new_pwd': '123456', 'second_pwd': '123456', 'check': '新密码与旧密码相同'},
               {'username': '13640993513', 'code': '6666a', 'pwd': '888888', 'new_pwd': '444444', 'second_pwd': '444444', 'check': '密码错误'},
               {'username': '13640993513', 'code': '6666a', 'pwd': '123456', 'new_pwd': '456789', 'second_pwd': '456789', 'check': '密码修改成功'}]
# 错误提示
pwd_err = [{'username': '13640993513', 'code': '6666a', 'pwd': '123', 'new_pwd': '444444', 'second_pwd': '444444', 'check': '密码长度最少6位'}]
new_pwd_err = [{'username': '13640993513', 'code': '6666a', 'pwd': '123456', 'new_pwd': '444', 'second_pwd': '444444', 'check': '密码长度最少6位'}]
second_pwd_err = [{'username': '13640993513', 'code': '6666a', 'pwd': '123456', 'new_pwd': '444444', 'second_pwd': '444555', 'check': '两次输入密码不一致!'}]


