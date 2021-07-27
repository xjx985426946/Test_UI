# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'V_app.py':
    shop_success = [{'username': '13640993513', 'password': '123456', 'check': '跳转成功'}]
else:
    shop_success = [{'username': '13640993513', 'password': '123456', 'check': '跳转成功'}]

# 售价排序
shop_price = [{'username': '13640993513', 'password': '123456', 'check': 'True'}]

create_inventory = [{'username': '13640993513', 'password': '123456', 'title': 'create inventory', 'remark': 'success inventory'}]

create_inventory_err = [{'username': '13640993513', 'password': '123456', 'check': '标题不能为空'}]

shop_null_create_inventory = [{'username': '19900000000', 'password': '123456', 'check': '哎呀，您的专柜空空如也！'}]

shop_set_name = [{'username': '13640993513', 'password': '123456', 'name': '测试昵称123'}]

shop_set_intro = [{'username': '13640993513', 'password': '123456', 'intro': '测试昵称测试昵称测试昵称'}]