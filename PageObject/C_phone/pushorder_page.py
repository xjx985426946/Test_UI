from PageLocators.C_phone import pushorder_locator
from Common.basepage import BasePage
import time


'''

提交订单页面

'''

class PushorderPage(BasePage):
    name = 'C端提交订单页面'

    # 点击发票按钮
    def click_purchase(self):
        self.click_element(pushorder_locator.invoice,model=self.name)


    #输入发票抬头
    def input_invoiceheader(self,invoice):
        self.input_text(invoice,pushorder_locator.invoice_header,model=self.name)



    #输入纳税人识别号和邮箱
    def input_invoice_phone(self,invoice_phone,email):
        self.input_text(invoice_phone,pushorder_locator.invoice_phone,model=self.name)
        self.input_text(email,pushorder_locator.invoice_email,model=self.name)

    #输入买家留言
    def input_message(self,message):
        self.input_text(message,pushorder_locator.message,model=self.name)

    #获取商品金额
    def get_amount(self):
        return self.get_text(pushorder_locator.amount,model=self.name)

    # 点击收货地址
    def click_address(self):
        self.click_element(pushorder_locator.address,model=self.name)

    # 点击提交订单按钮
    def click_button(self):
        self.click_element(pushorder_locator.button,model=self.name)

    #送好友页面输入口令提示信息
    def input_invitation(self,invitation):
        self.input_text(invitation,pushorder_locator.intvitation,model=self.name)
    #送好友页面输入口令
    def input_command(self,command):
        self.input_text(command,pushorder_locator.command,model=self.name)

    #去掉使用优惠券
    def click_couponse(self):
        self.click_element(pushorder_locator.counpons, model=self.name)
        time.sleep(2)
        self.click_element(pushorder_locator.quxiao,model=self.name)





