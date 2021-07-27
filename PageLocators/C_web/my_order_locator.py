
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

# 订单已取消/已提醒商家发货/申请成功/请填写退货单号/已确认收货/请选择退货物流公司/该商品已成功添加到我的喜欢列表！/你已经取消收藏该商品！/领取成功/请先选择规格/收货人不能为空/请输入正确的手机号码/详细地址不能为空/请选择所在地址
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

# toast报错：请输入评价内容/请填写收货口令/请填写口令提示/请选择举报类型/举报详细内容不少于20字
evaluate_err = '/html/body/div[2]'

# 发布评价
commit_evaluate = '//span[text()="发表评价"]'

# 订单列表跳转商品详情
order_list_product_detail = '//div[@class="container"]/div/div[2]/div/ul[2]/li[2]/div[2]/div/div/div/img'

# 校验订单列表跳转商品详情
check_product_detail = '//div[text()="商品详情"]'

# 订单列表-商品名称
order_list_product_name = '//div[@class="container"]/div/div[2]/div/ul[2]/li[2]/div[2]/div/div/div/div/div[1]'

# 商品详情-商品名称
product_detail_name = '//div[@class="container"]/div[1]/div[1]/div[2]/div/div/div[1]'

# 商品详情-喜欢
product_detail_like = '//div[@class="container"]/div[1]/div[1]/div[2]/div/div[2]/span/img'

# 商品详情-领取优惠券
get_coupons = '//span[text()="立即领取"]'

# 商品详情-选择规格
standards = '//ul[@class="standardList cell"]/ul/li[1]'

# 商品详情-举报
report = '//span[text()="举报"]'

# 举报页面
check_report = '//h2[text()="举报"]'

# 举报类型
report_type = '//div[@class="container"]/div/ul/li[3]'

# 举报内容
report_msg = '//div[@class="section"][2]/div/textarea'

# 提交按钮
commit = '//span[text()="提交"]'

# 举报帮助
report_help = '//span[@class="link"]'

# 校验举报帮助跳转
check_report_help = '//h2'

# 立即购买
buying = '//div[@class="buyActions"]/span[1]'

# 送好友
send_friends = '//div[@class="buyActions"]/span[2]'

# 去结算
settle = '//span[text()="去结算"]'

# 新增收货地址
address = '//a[text()="新增收货地址"]'

# 输入收货人姓名
receiver_name = '//input[@placeholder="请输入收件人姓名"]'

# 收货人手机号
receiver_mobile = '//input[@placeholder="请输入收件人手机号码"]'

# 请输入地区
location_name = '//div[text()="请输入地区"]'

# 选择省/市/区
provincial = '//span[text()="广东省"]'

urban = '//span[text()="深圳市"]'

areas = '//span[text()="南山区"]'

# 请输入详细地址
detail_address = '//input[@placeholder="请输入详细地址"]'

# 设为默认地址
set_default_address = '//span[@class="el-switch__core"]'

# 保存按钮
save_button = '//span[text()="保存"]'

# 新增收货地址成功
address_success = '//div[@class="addressList"]/ul/li/span[1]'

# 开发票
invoice = '//span[text()="我要开发票"]'

# 纸质发票-发票抬头
invoice_name = '//input[@placeholder="请输入发票抬头"]'

# 纸质发票-发票编号
invoice_no = '//input[@placeholder="请输入纳税人识别号，个人发票不填写，单位发票需要填写"]'

# 电子发票-收件人邮箱
invoice_email = '//input[@placeholder="请输入收票人邮件"]'

# 校验纸质发票
check_paper_invoice = '//div[@class="invoice"]/div[2]'

# 选择电子发票
electronic_invoice = '//div[@aria-label="发票信息"]/div[2]/div/div/span[2]/div/span[2]'

# 选择纸质发票
paper_invoice = '//div[@aria-label="发票信息"]/div[2]/div/div/span[2]/div/span[1]'

# 校验电子发票
check_electronic_invoice = '//div[@class="invoice"]/div[3]'

# 备注
remarks = '//textarea'

# 确定提交
invoice_commit = '//span[text()="确定"]'

# 取消使用优惠券
not_coupon = '//div[@class="couponRight"]'

# 提交订单
order_commit = '//span[text()="提交订单"]'
