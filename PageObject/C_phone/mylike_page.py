from PageLocators.C_phone import mylike_locator
from Common.basepage import BasePage

class MylikePage(BasePage):
    name = '我的喜欢页面'

    #获取头部文本
    def get_myliketext(self):
        #点击添加地址按钮
        return self.get_text(mylike_locator.mylike_text,model=self.name)


