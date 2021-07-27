from PageLocators.C_phone import logistics_locator
from Common.basepage import BasePage

class LogisticPage(BasePage):
    name = '物流页面'
    #获取头部信息
    def get_header(self):
        return self.click_element(logistics_locator.header,model=self.name)


