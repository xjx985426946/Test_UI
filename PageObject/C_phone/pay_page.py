from PageLocators.C_phone import pay_locator
from Common.basepage import BasePage


'''

支付选择页面

'''

class PayrPage(BasePage):
    name = 'C端支付选择页面'

    # 获取 支付宝
    def get_alipay(self):
        return self.get_text(pay_locator.alipay,model=self.name)

    def get_wepay(self):
        return self.get_text(pay_locator.wepay,model=self.name)


    #获取微信文本
    def input_invoiceheader(self):
        return self.get_text(pay_locator.wepay,model=self.name)






