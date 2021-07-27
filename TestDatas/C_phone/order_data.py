#订单URL检查
order_success = {'check':'全部'}

import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_ptest.py':
    order_url = [{'pending': 'https://test-item.intbee.com/customer/mobile/personal/orders?status=11#'},
                 {'processing': 'https://test-item.intbee.com/customer/mobile/personal/orders?status=21,22,25#'},
                 {'delivering': 'https://test-item.intbee.com/customer/mobile/personal/orders?status=26#'},
                 {'completed': 'https://test-item.intbee.com/customer/mobile/personal/orders?status=27,28#'}]
if path == 'C_ptestProduction.py':
    order_url = [{'pending': 'https://item.intbee.com/customer/mobile/personal/orders?status=pending'},
                 {'processing': 'https://item.intbee.com/customer/mobile/personal/orders?status=processing'},
                 {'delivering': 'https://item.intbee.com/customer/mobile/personal/orders?status=delivering'},
                 {'completed': 'https://item.intbee.com/customer/mobile/personal/orders?status=completed'}]


#去掉订单toast检查
cancleorder = {'check','订单已取消'}

#支付页面验证
pay_text = {'check_wei':'微信','check_ali':'支付宝'}

#订单详情
orderdetail = {'check':'订单详情'}

#验证进入退款页面
refund = {'check':'退款'}

#toast验证
toast_text = {'check':'申请成功'}

#提醒发货验证
remind = {'check':'你已提醒卖家发货，我们会通知卖家尽快发货，请您耐心等待！'}

#物流页面验证
logistic = {'check':'物流'}
evalucate  = {'detail':'评价','toast':'评价成功'}
