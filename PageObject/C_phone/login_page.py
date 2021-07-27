from PageLocators.C_phone import login_locator
from Common.basepage import BasePage
import time
class LoginPage(BasePage):

    def login(self,username,password):
        name = '登录页面_登录操作'
        # 输入用户名
        self.wait_eleVisible(login_locator.user_input,model=name)
        self.input_text(username,login_locator.user_input,model=name)
        # 输入密码
        self.input_text(password,login_locator.pwd_input,model=name)
        # 点击登录按钮
        self.click_element(login_locator.button,model=name)

    # 帐号不存在
    def get_errMsg_from_user(self):
        name = "登录页面_toast"
        ele = login_locator.toast_text
        return self.get_text(ele,model=name)



