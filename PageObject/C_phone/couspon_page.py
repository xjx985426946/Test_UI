'''
优惠券页面

'''

from PageLocators.C_phone import couspon_locator
from Common.basepage import BasePage
import time

class CousponPage(BasePage):
    name = '优惠券页面'

    #获取优惠券文本
    def get_couspon(self):
        #点击添加地址按钮
        return self.get_text(couspon_locator.couson_text,model=self.name)




