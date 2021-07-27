'''退款页面'''

#获取退款页面头部信息
header_text = '//div[@class="header"]//span[text()="退款"]'

#点击退款原因
refund_reason = '//span[@class="cellTitle"]'

#点击弹窗不想要了
cancle ='//li[@class="mint-actionsheet-listitem"][1]'

#点击提交按钮
button = '//div[@class="btn-bottom"]'

#获取toast
toast_text = '//div[@class="bodyToast"]'