'''商品管理页面'''

#添加商品按钮
createproduct = '//button//span[text()="添加商品"]'

#实体商品按钮
normal_product = '//a[@class="productCenter-normal"]'
#新建蜂卡
createcard = '//button//span[text()="新建蜂卡"]'

#实体商品
product = '//a[@class="productCenter-normal"]'

#商品名称
productname = '//input[@id="name"]'

#商品描述
product_description = '//textarea[@id="des"]'

#商品编码
product_code = '//input[@id="code"]'

category = '//input[@placeholder="选择品类"]'

category1 = '//li[@title="家居生活"]'

category2 = '//li[@title="家具"]'

category3 = '//li[@title="置物架"]'

#商品标签
createtags = '//div[@class="productInfo-tags"]//span[text()="添 加"]'

#地址
addresslimit = '//input[@placeholder="请输入你的发货国家/省市"]'

#规格名称
sdandarname1= '//div[@class="productInfo-item"][1]/p[@class="productInfo-name"]//input[@class="ant-checkbox-input"]'

#规格选项
sdandarname1_1 = '//div[@class="productInfo-item"][1]/div[@class="productInfo-element"][1]//p[1]//label[@class="ant-checkbox-wrapper"]//input'

#规格名称
sdandarname2 = '//div[@class="productInfo-item"][2]/p[@class="productInfo-name"]//input[@class="ant-checkbox-input"]'

#规格选项
sdandarname2_1 = '//div[@class="productInfo-item"][2]/div[@class="productInfo-element"][1]//p[1]//label[@class="ant-checkbox-wrapper"]//input'

#价格
price = '//input[@placeholder="批量输入价格"]'

#库存
stock = '//input[@placeholder="批量输入库存"]'

#价格库存确定按钮
stockbutton = '//div[@class="productInfo-input"]//button[@class="ant-btn ant-btn-primary"]'

#下一步按钮
next_button = '//div[@class="productInfo-operate"]//button[@class="ant-btn ant-btn-primary"]'

#商品默认文案
wenan = '//textarea[@placeholder="请输入商品默认分享文案"]'

#保存按钮
save_button = '//button//span[text()="保 存"]'

#定向蜂卡
card = '/div[@class="creatCard-orient"]'

#普通蜂卡
commin_card = '//div[@class="creatCard-normal"]'

#搜索智蜂客
search_spreader = '//input[@placeholder="输入你想输入的智蜂客昵称"]'

search_button = '//button[@class="ant-btn ant-input-search-button ant-btn-primary"]'

#选择智蜂客
select_preader = '//div[@class="ant-list ant-list-split"]//div[@class="ant-list-item"][1]//input'

#选择智蜂客下一步
next_submit = '//button//span[text()="下一步"]'

#商品选择
select_product = '//tr[@class="ant-table-row ant-table-row-level-0"][1]//input'

#选择商品后下一步
button = '//button//span[text()="下一步"]'

#普通智蜂客服务费
commom_service = '//p[text()="普通智蜂客服务费/件：￥"]//input'

#vip智蜂客服务费
vip_servicer = '//p[text()="优质（VIP）客服务费/件：￥"]//input'

#蜂卡信息下一步
but = '//button//span[text()="下一步"]'

#协议
Agreement = '//input[@class="ant-checkbox-input"]'

#发布蜂卡按钮
publish_card = '//button//span[text()="发布蜂卡"]'

#编辑商品按钮
edit_product = '//tbody[@class="ant-table-tbody"]//tr[@class="ant-table-row ant-table-row-level-0"][1]//span[text()="删除"]'
