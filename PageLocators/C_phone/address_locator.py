#管理地址页面

#添加地址按钮
create_address = '//div[@class="btn-bottom"]'

#收件人姓名文本框
input_name = '//input[@placeholder="请输入收件人姓名"]'

#收货人手机
input_mobile = '//input[@placeholder="请输入收件人手机号码"]'

#所在地区
select_address = '//div[text()=" 请输入地区 "]'
click_province = '//span[text()="上海市"]'

click_city = '//span[text()="市辖区"]'

click_town = '//span[text()="黄浦区"]'


# 详情地址
detailaddress = '//textarea[@placeholder="请输入详细地址"]'

#点击按钮
button = '//div[@class="btn-bottom" and text()="确定"]'

#地址文本
address_text = '//div[@class="btn-bottom"]'

#手机号码不正确提示
toast_text = '//div[text()="请输入正确的手机号码"]'

#点击编辑按钮
edit_button = '//span[text()="收货人：66"]/parent::div/following-sibling::div//span[text()="编辑"]'

#编辑保存按钮
update_button = '//div[text()="确定"]'

#删除按钮
delete = '//span[text()="收货人：66"]/parent::div/following-sibling::div//span[text()="删除"]'