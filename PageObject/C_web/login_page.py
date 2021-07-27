from PageLocators.C_web import login_locator
from Common.basepage import BasePage
import time
class LoginPage(BasePage):

    def login(self, username, password):
        name = '登录页面_登录操作'

        # 密码登录
        self.find_element(login_locator.pwd_login, model=name).click()
        # 输入用户名
        self.wait_eleVisible(login_locator.user_input, model=name)
        self.input_text(username, login_locator.user_input, model=name)
        # 输入密码
        self.input_text(password, login_locator.pwd_input, model=name)
        # 点击登录按钮
        self.click_element(login_locator.button, model=name)

    # 帐号不存在
    def get_errMsg_from_user2(self):
        name = "登录页面_toast"
        ele = login_locator.toast_text1
        return self.get_text(ele, model=name)

    #密码错误/账户未注册
    def get_errMsg_from_user(self):
        name = "登录页面_toast"
        ele = login_locator.toast_text
        return self.get_text(ele, model=name)

    #我的订单
    def login_success(self):
        name = "登录页面_我的订单"
        ele = login_locator.myorder
        return self.get_text(ele, model=name)




