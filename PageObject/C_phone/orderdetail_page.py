'''订单详情页面'''

from PageLocators.C_phone import orderdetail_locator
from Common.basepage import BasePage

class OrderdetailPage(BasePage):

    name = '订单详情页面'

    #获取订单详情页面头部文本
    def get_detailtext(self):
        return self.get_text(orderdetail_locator.text,model=self.name)

    #获取支付总额
    def get_allmoney(self):
        return self.get_text(orderdetail_locator.money,model=self.name)
