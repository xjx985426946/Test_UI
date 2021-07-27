from PageLocators.C_phone import applyrefund_locator
from Common.basepage import BasePage

class ApplyrefundPage(BasePage):

    name = '申请退款页面'

    #点击退款原因
    def click_reson(self):
        self.click_element(applyrefund_locator.refund_reason,model=self.name)

    #选择退款原因
    def click_cancle(self):
        self.click_element(applyrefund_locator.cancle,wait_ele='presence', model=self.name)

    #点击提交按钮
    def click_button(self):
        self.click_element(applyrefund_locator.button,model=self.name)

    #获取头部文本、
    def get_headertext(self):
        return self.get_text(applyrefund_locator.header_text,model=self.name)

    #获取toast
    def get_toast(self):
        return self.get_text(applyrefund_locator.toast_text,model=self.name)
