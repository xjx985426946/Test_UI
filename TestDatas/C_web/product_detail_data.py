# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_success = [{'username': '13640993513', 'code': '6666a', 'check': '商品详情'}]

product_like_success = [{'username': '13640993513', 'code': '6666a', 'check': '该商品已成功添加到我的喜欢列表！'}]

product_unlike_success = [{'username': '13640993513', 'code': '6666a', 'check': '你已经取消收藏该商品！'}]

product_coupon_success = [{'username': '13640993513', 'code': '6666a', 'check': '领取成功'}]

product_buying_err = [{'username': '13640993513', 'code': '6666a', 'check': '请先选择规格'}]

product_settle = [{'username': '13640993513', 'code': '6666a', 'check': '新增收货地址'}]

product_address_err = [{'username': '13640993513', 'code': '6666a', 'check': '新增收货地址'}]

add_address_err = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '收货人不能为空'},
                   {'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '', 'detail_address': '讯美科技广场3号楼', 'check': '请输入正确的手机号码'},
                   {'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '13640993513', 'detail_address': '', 'check': '详细地址不能为空'}]

add_address_err2 = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '13640993513', 'check': '请选择所在地址'}]

add_address_success = [{'username': '13640993513', 'code': '6666a', 'receiver_name': '深圳测试', 'receiver_mobile': '13640993513', 'detail_address': '讯美科技广场3号楼', 'check': '深圳测试'}]

paper_invoice = [{'username': '13640993513', 'code': '6666a',  'invoice_name': '测试发票',  'invoice_no': '123456', 'check': '纳税人识别号: 123456'}]

electronic_invoice = [{'username': '13640993513', 'code': '6666a',  'invoice_name': '测试发票',  'invoice_no': '123456', 'invoice_email': '13556', 'check': '收票邮件: 13556'}]

remarks = [{'username': '13640993513', 'code': '6666a', 'remarks': '测试留言', 'check': '选择付款方式'}]

report = [{'username': '13640993513', 'code': '6666a', 'check': '举报'}]

report_help = [{'username': '13640993513', 'code': '6666a', 'check': '知识产权侵权投诉处理程序'}]

report_err = [{'username': '13640993513', 'code': '6666a', 'report_msg': '测试举报', 'check': '请选择举报类型'}]

report_msg = [{'username': '13640993513', 'code': '6666a', 'report_msg': '', 'check': '举报详细内容不少于20字'},
              {'username': '13640993513', 'code': '6666a', 'report_msg': '测试举报测试举报测试举报测试举报测试举报11', 'check': '提交成功，我们将尽快处理！感谢您的监督'}]
