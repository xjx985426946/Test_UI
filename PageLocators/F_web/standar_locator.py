'''规格管理页面'''

#添加规格按钮
create_sdandard = '//button//span[text()="添加规格"]'

#添加规格名称
standard_name = '//div[@class="standard-name"]//input'

#添加规格属性
standard_attributes = '//button//span[text()="添加规格属性"]'

#属性输入框
input_attributes1 = '//div[@class="standard-item"]//span[text()="1"]/following-sibling::div/input'
input_attributes2 = '//div[@class="standard-item"]//span[text()="2"]/following-sibling::div/input'

#保存按钮
button = '//button[@class="ant-btn ant-btn-primary"]//span[text()="保 存"]'

#规格编辑按钮
edit_standard = '//tbody[@class="ant-table-tbody"]/tr[1]//span[text()="编辑"]'

#编辑点击保存按钮
edit_button = '//button/span[text()="保 存"]'

#规格删除按钮
delete_standard = '//tbody[@class="ant-table-tbody"]/tr[1]//span[text()="删除"]'

#删除确认按钮
delete_button = '//button[@class="ant-btn ant-btn-primary ant-btn-sm"]//span[text()="确 定"]'