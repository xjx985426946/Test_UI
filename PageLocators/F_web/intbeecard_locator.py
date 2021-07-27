'''全部蜂卡页面'''

#补充库存按钮（选择第一条数据）
stock = '//div[@class="beeCard-card-list"]/div[@class="beeCardItem-item"][1]/div[@class="beeCardItem-bottom"]//span[text()="补充库存"]'

#终止蜂卡
supplement_card = '//div[@class="beeCard-card-list"]/div[@class="beeCardItem-item"][1]/div[@class="beeCardItem-bottom"]//span[text()="终止蜂卡"]'

#查看详情
card_detail = '//div[@class="beeCard-card-list"]/div[@class="beeCardItem-item"][1]/div[@class="beeCardItem-bottom"]//span[text()="查看详情"]'

#补充蜂卡确认按钮
button = '//div[@class="ant-modal-footer"]//span[text()="确 定"]'

#补充库存提交按钮
button_u = '//div[@class="beeCard-operate"]//span[text()="确 定"]'

# 终止蜂卡原因
supplement_reason = '//div[@class="modalContent-wait-stop-content"]//textarea'

#终止蜂卡确定按钮
supplement_button = '//div[@class="ant-modal-footer"]//span[text()="确 定"]'

#查看规格
standard = '//div[@class="beeCard-pro-info"]//span[text()="查看规格"]'

#点击规格确定按钮
standard_button = '//button[@class="ant-btn ant-btn-primary"]//span[text()="确 定"]'

#定向发卡
card_dx = '//div[@class="beeCard-pro-info"]//span[text()="定向发卡"]'

#智蜂客昵称
