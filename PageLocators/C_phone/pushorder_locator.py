#发票按钮
invoice = '//label[@class="mint-switch switch"]'

#发票抬头
invoice_header = '//input[@placeholder="请填写发票抬头"]'

#纳税人识别号
invoice_phone = '//input[@placeholder="个人发票不填写，单位发票需要填写"]'

invoice_email = '//div[@class="cellContainer borderBottom"]/input[@placeholder="请填写收票人邮件"]'

#买家留言
message = '//div[@class="cellContainer"]/input[@placeholder="选填"]'

#商品金额
amount = '//span[text()="商品金额"]/following-sibling::span'

#收货地址
address = '//div[@class="addressView"]'

#提交订单按钮
button = '//div[@class="btn-bottom"]/span[text()="提交订单"]'

intvitation = '//input[@ placeholder ="可以留言提示一下口令是啥"]'

#送好友收获口令
command = '//span[text()="收货口令"]/parent::span/following-sibling::input'

counpons = '//span[text()="优惠券"]'
#取消优惠券按钮
quxiao = '//img[@class="selected"]'