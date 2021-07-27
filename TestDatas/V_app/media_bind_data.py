# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    login_success = [{'username': '13600000000', 'password': '123456', 'check': '自媒体账号绑定'}]
else:
    login_success = [{'username': '13600000000', 'password': '123456', 'check': '自媒体账号绑定'}]

confirm_wb_cancel = [{'username': '13600000000', 'password': '123456', 'check': '授权取消！'}]

confirm_wb_bind = [{'username': '13600000000', 'password': '123456', 'check': '21338:sso package or sign error'}]

tips_bind_error = [{'username': '13600000000', 'password': '123456', 'url': '测试测试', 'check': '请求参数有误:请输入正确的抖音个人主页'}]

tips_bind = [{'username': '13600000000', 'password': '123456', 'url': 'https://v.douyin.com/GW5tuA/',
              'tips': '徐健鑫1', 'check': '成功'}]

wx_bind = [{'username': '13600000000', 'password': '123456', 'check': '二维码已经保存到相册'}]

red_book_error = [{'username': '13600000000', 'password': '123456', 'name': '测试测试', 'url': '小红书测试',
                   'check': '请求参数有误:请输入正确的小红书个人主页'}]

red_book = [{'username': '13600000000', 'password': '123456',
             'url': 'https://www.xiaohongshu.com/user/profile/5b6a516648b4b400014c1ec4?'
                    'xhsshare=CopyLink&appuid=5b6a516648b4b400014c1ec4&apptime=1582709076',
             'name': '小红书测试', 'check': '成功'}]
