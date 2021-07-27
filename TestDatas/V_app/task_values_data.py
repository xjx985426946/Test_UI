# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    login_success = [{'username': '13600000004', 'password': '123456', 'check': '跳转成功'}]
else:
    login_success = [{'username': '13600000006', 'password': '123456', 'check': '跳转成功'}]

sign_success = [{'username': '13600000006', 'password': '123456', 'check': '10', 'check_button': '已连续签到1天',
                 'check_toast': '签到成功，获取成长值10，连续签到可获得更多奖励哦', 'check_ok': '跳转成功'}]

values_des_more = [{'username': '13600000006', 'password': '123456', 'check': '等级福利说明'}]

share_success = [{'username': '13600000006', 'password': '123456', 'check_toast': '获得每日首次分享奖励价值点+30', 'check_ok': '跳转成功'}]

go_around_success = [{'username': '13600000006', 'password': '123456', 'check_alert': '奖励30成长值随便逛逛：每日浏览商品5/5',
                      'check_ok': '跳转成功'}]

change_name = [{'username': '13600000006', 'password': '123456', 'user_name': '测试测试', 'check_btn': '领取奖励',
                'check_ok': '跳转成功', 'check_toast': '领取成功'}]

change_icon = [{'username': '13600000006', 'password': '123456', 'check_btn': '领取奖励',
                'check_ok': '跳转成功', 'check_toast': '领取成功'}]
