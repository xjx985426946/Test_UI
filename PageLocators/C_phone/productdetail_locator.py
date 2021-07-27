'''

手机端商品详情页面

'''

# 商品链接
# production_url = "https://test-item.intbee.com/customer/item/19031/?uuid=5bc59a1e9a1d090007a0464a&platform_id=0"

#立即购买按钮
purcharse_button = '//div[@class="strong"]'

#客服按钮
server_button = '//div[@class="bottom"]//span[text()=" 客服 "]'
#客服电话
server_phone = '//span[text()="客服电话"]'
server_qq = '//span[text()="客服QQ"]'
#进入客服弹窗，点击完成按钮
complete = '//div[text()="完成" and @class="complete"]'


#送好友按钮
friend_button = '//div[@class="bottom"]//span[text()=" 送好友 "]'

# #送好友购买页面留言提醒
# intvitation = '//input[@ placeholder ="可以留言提示一下口令是啥"]'
#
# #送好友收获口令
# command = '//span[text()="收货口令"]/parent::span/following-sibling::input'

#商品详情
column_productdetail = '//div[@class="productDetail"]//span[text()="商品详情"]'

#商品参数
production_param = '//div[@class="productDetail"]//span[text()="商品参数"]'

#领券
cuspons = '//span[text()="领券"]'

#专柜
shop = '//img[@class="icon"]/following-sibling::span'

#商品评价
product_evaluate = '//span[text()="商品评价"]'

#试用报告
try_report = '//span[text()="试用报告"]'

#添加喜欢

like = '//div[@class="like"]//img'

not_like = '//div[@class="like active"]//img'

#点击规格

color = '//ul[@class="standardValues"]/li[text()="红色"]'

big = '//ul[@class="standardValues"]/li[text()="39"]'


coupon = '//span[text()="优惠券"]'

# 确定购买按钮
decide_botton = '//span[text()="确定购买"]'


#获取商品金额
amount = '//span[@class="price"]'

#数量增加按钮
add = '//span[text()="＋"]'

#数量减少按钮
reduce = '//span[@class="buyNum"]/span[text()="-"]'

#添加成功的toast
add_toast = '//div[@class="bodyToast"]'