from PageLocators.C_phone import nick_locator
from Common.basepage import BasePage

class NickPage(BasePage):

    name = '昵称设置页面'

    #点击昵称设置按钮
    def input_nick(self,nick_name):

        # 输入昵称
        self.input_text(nick_name,nick_locator.nick_input,model=self.name)

    #点击确定按钮
    def click_button(self):

        # 点击确定按钮
        self.click_element(nick_locator.button,model=self.name)

    #获取弹窗
    def get_toast(self):
        return  self.get_text(nick_locator.toast_text,model=self.name)



