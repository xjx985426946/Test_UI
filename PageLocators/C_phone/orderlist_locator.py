'''我的订单页面'''

#订单头部文本
order_text = '//ul[@class="filterContainer filters type1"]//span[text()="全部"]'

#待付款
# pending_order = '//li[@class="active"]//span[text()="待付款"]'    #被坑了半个钟 没有点击之前active是没有的  所以不能加这个

pending_order = '//ul[@class="filterContainer filters type1"]//span[text()="待付款"]'

processing_order = '//ul[@class="filterContainer filters type1"]//span[text()="待发货"]'

delivering_order = '//ul[@class="filterContainer filters type1"]//span[text()="待收货"]'

complete_order = '//ul[@class="filterContainer filters type1"]//span[text()="已收货"]'

float_text = '//div[@class="float"]//span[text()="X"]'

aa = '//*[@id="app"]/div/div[2]/div/div[1]/div/ul[2]/li[1]/div[2]/div[1]'


#订单页面第一条订单
order_one = '//li[@class="order"][1]/div[@class="orderInfo"]//div[@class="sku"]'

#第一条订单商品title
title = '//li[@class="order"][1]/div[@class="orderInfo"]//div[@class="sku"]/div/div[1]'

#获取第一条订单的商品价钱
amount = '//li[@class="order"][1]/div[@class="orderInfo"]//div[@class="sku"]/div/div[2]'

#获取第一条订单的总价钱
all_money = '//li[@class="order"][1]/div[@class="orderInfo"]//div[@class="orderData"]//span[@class="price"]'

#获取第一条订单的取消订单按钮（待付款）
cancel_order = '//li[@class="order"][1]/div[@class="orderInfo"]//span[text()="取消订单"]'

#获取第一条订单的立即付款按钮（待付款）
pay_button = '//li[@class="order"][1]/div[@class="orderInfo"]//span[text()="立即付款"]'

#获取第一条订单，订单状态
status = '//li[@class="order"][1]//span[@class="status"]//span'

#获取第一条订单申请退款按钮（待发货）
apply_refund = '//li[@class="order"][1]/div[@class="orderInfo"]//span[text()="申请退款"]'

#获取第一条订单提醒发货按钮（待发货）
reminder_shipment = '//li[@class="order"][1]/div[@class="orderInfo"]//span[text()="提醒发货"]'

#获取第一条信息查看物流按钮
logistics = '//li[@class="order"][1]/div[@class="orderInfo"]//label[text()="查看物流"]//parent::button'

#获取第一条信息退货按钮
return_goods = '//li[@class="order"][1]/div[@class="orderInfo"]//label[text()="退货"]//parent::button'

#获取第一条商品的评价按钮
evaluate = '//li[@class="order"][1]/div[@class="orderInfo"]//span[text()="评价"]'

#获取toast文本
toast_text = '//div[@class="bodyToast"]'  #你已提醒卖家发货，我们会通知卖家尽快发货，请您耐心等待！

#点击商品，进入详情页面
detail = '//li[@class="order"][1]/div[@class="orderInfo"]//div[@class="sku"]'

#评论页面评价商品
evaluate_detail = '//textarea[@placeholder="评价这件商品吧~~"]'
evaluate_button = '//span[text()="发表评价"]'