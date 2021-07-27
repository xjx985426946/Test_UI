# 正常登录
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_web.py':
    login_success = [{'username': '13640993513', 'code': '6666a', 'check': '我的订单'}]

# 订单列表-待付款订单列表页跳转
wait_pay = [{'username': '13640993513', 'code': '6666a', 'check': '待付款'}]
check_now_pay = [{'username': '13640993513', 'code': '6666a', 'check': '选择付款方式'}]
# 订单列表-待发货订单列表页跳转
wait_ship_order = [{'username': '13640993513', 'code': '6666a', 'check': '待发货'}]
remind_ship = [{'username': '13640993513', 'code': '6666a', 'check': '已提醒商家发货'}]
application_refund = [{'username': '13640993513', 'code': '6666a', 'check': '退款申请'}]
application_refund_success = [{'username': '13640993513', 'code': '6666a', 'refund_msg': '申请退款自动化UI', 'check': '申请成功'}]
cancel_order = [{'username': '13640993513', 'code': '6666a', 'check': '订单已取消'}]
# 订单列表-已发货订单列表页跳转
shipped_order = [{'username': '13640993513', 'code': '6666a', 'check': '已发货'}]
order_logistics = [{'username': '13640993513', 'code': '6666a', 'check': '物流信息'}]
confirm_receipt = [{'username': '13640993513', 'code': '6666a', 'check': '已确认收货'}]
return_order = [{'username': '13640993513', 'code': '6666a', 'check': '退货申请'}]
return_err = [{'username': '13640993513', 'code': '6666a', 'return_msg': '申请退款自动化UI', 'return_no': '123', 'check': '请选择退货快递公司'}]
return_err2 = [{'username': '13640993513', 'code': '6666a', 'return_msg': '申请退款自动化UI', 'return_no': '', 'check': '请填写退货单号'}]
return_success = [{'username': '13640993513', 'code': '6666a', 'return_msg': '申请退款自动化UI', 'return_no': '456', 'check': '申请成功'}]
return_unreceived_success = [{'username': '13640993513', 'code': '6666a', 'return_msg': '申请退款自动化UI', 'check': '申请成功'}]
# 订单列表-已收货订单列表页跳转
received_order = [{'username': '13640993513', 'code': '6666a', 'check': '已收货'}]
detail_evaluate = [{'username': '13640993513', 'code': '6666a', 'check': '商品评价'}]
evaluate_err = [{'username': '13640993513', 'code': '6666a', 'evaluate_msg': '', 'check': '请输入评价内容'}]
evaluate_success = [{'username': '13640993513', 'code': '6666a', 'evaluate_msg': '申请退款自动化UI', 'check': '申请成功'}]


