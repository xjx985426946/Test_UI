
# 帐号输入框
user_input = '//input[@placeholder="请输入手机号码"]'

# 验证码输入框
code_input = '//input[@placeholder="请输入手机验证码"]'

# 登录按钮
button = '//button[@class="btnCell"]'

# 我的订单
my_order = '//h2[text()="我的订单"]'

# 校验我的订单页面
check_my_order = '//h2[text()="我的订单"]'

# 待付款订单列表
wait_pay_order = '//span[text()="待付款"]'

# 待发货订单列表
wait_ship_order = '//span[text()="待发货"]'

# 已发货订单列表
shipped_order = '//span[text()="已发货"]'

# 已收货订单列表
received_order = '//span[text()="已收货"]'

# 校验订单列表跳转
check_order_list = '//div[@class="container"]/div/div[2]/div/ul[2]/li[2]/div/span'

# 查看详情按钮
detail_order = '//div[@class="container"]/ul[2]/li[2]/div[2]/div[2]/button[1]/span'

# 校验立即付款按钮跳转
check_paying_now = '//h2[text()="选择付款方式"]'

# 订单详情跳转校验-待付款/待发货/已发货/已收货
check_detail_order = '//div[@class="container"]/div/div/div/h2'

# 订单详情-第二个按钮（立即付款/提醒发货/确认收货/评价）
detail_order_button2 = '//div[@class="container"]/div/div/div/button[2]'

# 订单详情-第一个按钮(取消订单/申请退款/未收货退货/已收货退货)
detail_order_button1 = '//div[@class="container"]/div/div/div/button[1]'

# 订单列表-第二个按钮跳转（立即付款/提醒发货/查看物流）
order_list_button2 = '//div[@class="container"]/ul[2]/li[2]/div[2]/div[2]/button[2]'

# 订单已取消/已提醒商家发货/申请成功/请填写退货单号/已确认收货/请选择退货物流公司
check_msg = '//p[@class="el-message__content"]'

# 订单详情页面-取消订单
cancel_order = '//span[text()="取消订单"]'
refund_order = '//span[text()="申请退款"]'
return_order = '//span[text()="退货"]'

# 订单列表页面-确认收货
confirm_receipt = '//span[text()="确认收货"]'

# 确认取消订单
confirm_button = '//div[@class="el-message-box"]/div[3]/button'

# 退款校验
check_application_refund = '//h2[text()="退款申请"]'

# 退款原因
refund_reason = '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/span[2]/div/div/input'

select_refund_reason2 = '//span[text()="发货太慢了"]'
select_refund_reason1 = '//span[text()="不想要了"]'

# 退款留言
refund_msg = '//textarea[@class="el-textarea__inner"]'

# 退款提交按钮
refund_commit_button = '//button[@class="el-button el-button--primary"]'

# 退货校验
check_application_return = '//h2[text()="退货申请"]'

# 未收到货退货/已收到货退货
return_type = '//div[@class="body"]/div[2]/div[1]/span[2]'
goods_received = '//span[text()="已收到货，退货"]'
unreceived_goods = '//span[text()="未收到货，退货"]'

# 退货原因
return_reason = '//div[@class="body"]/div[2]/div[2]/span[2]'

return_reason1 = '//span[text()="不想要了"]'
return_reason2 = '//span[text()="质量问题"]'
return_reason3 = '//span[text()="与描述不符"]'

# 退货留言
return_msg = '//div[@class="body"]/div[2]/div[3]/span[2]/div[1]/textarea'

# 退货快递
return_express = '//div[@class="body"]/div[2]/div[5]/span/div[1]/div[1]'
return_express_sf = '//span[text()="顺丰快递"]'

# 退货快递单号
return_sf_no = '//div[@class="body"]/div[2]/div[6]/span[2]/div[1]/input'

# 退货提交按钮
return_commit_button = '//button[@class="el-button el-button--default"]'

# 查看物流校验
check_order_logistics = '//h3[text()="物流信息"]'

# 确认收货
Confirmation_receipt = '//div[@class="container"]/ul[2]/li[2]/div[2]/div[2]/button[3]'

# 已收货订单-评价
evaluate = '//span[text()="评价"]'

# 校验评价页面跳转
check_evaluate = '//h2[text()="商品评价"]'

# 评价内容
evaluate_msg = '//textarea[@placeholder="评价这件商品吧~500字内"]'

# 评价内容报错：请输入评价内容
evaluate_err = '//div[@class="bodyToast"]'

# 发布评价
commit_evaluate = '//span[text()="发表评价"]'

#我的订单页面

#待付款按钮
Payment_button = '//ul[@class="filterContainer filter"]//li[2]/span'

#待发货按钮
shipp_button = '//ul[@class="filterContainer filter"]//li[3]/span'

#已发货按钮
shipped_button = '//ul[@class="filterContainer filter"]//li[4]/span'

#已收货
receiving_button = '//ul[@class="filterContainer filter"]//li[5]/span'

#全部
all_order = '//ul[@class="filterContainer filter"]//li[1]/span'

#待付款、待发货、已发货、页面查看详情按钮
detail_button = '//span[text()="查看详情"]'

#待付款页面，立即付款按钮
pay = '//span[text()="立即付款"]'

#待发货页面，提醒发货按钮
admind = '//span[text()="提醒发货"]'

#已发货、已收货    页面查看物流按钮
logistics = '//span[text()="查看物流"]'

#已收货页面，查看确认收货按钮
confirm = '//span[text()="确认收货"]'

#待付款详情页面取消订单按钮
canll_order = '//button[@class="el-button el-button--default"]/span[text()="取消订单"]'

#待付款详情页面立即付款按钮
paykuang = '//button[@class="el-button el-button--default"]/span[text()="立即付款"]'

#获取收货人姓名
name = '//span[text()="收货人"]/following-sibling::span'

#获取收货人电话号码
mobile = '//span[text()="电话号码"]/following-sibling::span'

#获取收货人地址
address = '//span[text()="收货地址"]/following-sibling::span'

#详情页面获取商品金额
price = '//span[text()=" 商品金额： "]/span'

#详情页面商品运费
postage = '//span[text()=" 运费： "]/span'

#详情页面订单合计金额
all__money = '//span[text()=" 合计： "]/span'

#申请退款详情页面申请退款按钮
returnprice = '//span[text()="申请退款"]'


#申请退款详情页面提醒按钮
remind_goods = '//span[text()="提醒发货"]'


#我的订单页面获取购买的商品数量
quantity = '//li[@class="order"][1]//div[@class="sku"]/div[2]'

#我的订单页面获取商品单价
product_price = '//li[@class="order"][1]//div[@class="sku"]/div[3]'

#付款页面获取应付金额
ying_pay = '//div[@class="orderInfo"]/p[2]'