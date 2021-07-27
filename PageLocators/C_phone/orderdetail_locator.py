'''订单详情页面'''

#获订单详情头部文本
text = '/div[@class="header"]//span[text()="订单详情"]'

#获取合计金额
money = '//div[@class="flex" and text()=" 合计： "]//span'