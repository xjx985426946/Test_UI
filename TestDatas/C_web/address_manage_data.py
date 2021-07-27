# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_success = [{'username': '13640993513', 'code': '6666a', 'check': '地址管理'}]

# 新增地址
add_address_success = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '收货人：深圳测试'}]

# 新增地址错误提示
add_address_err = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '收货人不能为空'},
                   {'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '', 'detail_address': '讯美科技广场3号楼', 'check': '请输入正确的手机号码'},
                   {'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '13640993513', 'detail_address': '', 'check': '详细地址不能为空'}]
# 编辑地址
edit_address_success = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试2', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '收货人：深圳测试2'}]

# 删除地址
delete_address_success = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试2', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '地址已经删除'}]

set_default_address = [{'username': '13640993513', 'code': '6666a', 'check': '已设为默认地址'}]

