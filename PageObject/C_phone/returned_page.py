'''退货退款页面'''

from PageLocators.C_phone import returned_locator
from Common.basepage import BasePage

class ReturnedPage(BasePage):

    name = '退货退款页面'

    #获取退货退款文本
    def get_turnedtext(self):
        return self.get_text(returned_locator.returned,model=self.name)

