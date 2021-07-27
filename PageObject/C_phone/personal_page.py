from PageLocators.C_phone import personal_locator
from Common.basepage import BasePage

class PersonalPage(BasePage):
    name = '个人设置页面'
    #点击昵称设置按钮
    def click_nick(self):

        # 输入用户名
        self.click_element(personal_locator.nick,model=self.name)

    #获取个人设置文本
    def get_settext(self):
        return self.get_text(personal_locator.set_text,model=self.name)



