from PageLocators.C_web import msg_login_locator
from Common.basepage import BasePage
import time
class MsgLoginPage(BasePage):

    def login(self, username, password):
        name = '登录页面_登录操作'

        # 输入用户名
        self.wait_eleVisible(msg_login_locator.user_input, model=name)
        self.input_text(username, msg_login_locator.user_input, model=name)
        # 输入密码
        self.input_text(password, msg_login_locator.code_input, model=name)
        # 点击登录按钮
        self.click_element(msg_login_locator.button, model=name)

    # 手机号码有误
    def get_errMsg_from_user2(self):
        name = "登录页面_toast"
        ele = msg_login_locator.toast_text1
        return self.get_text(ele, model=name)

    #验证码错误
    def get_errMsg_from_user(self):
        name = "登录页面_toast"
        ele = msg_login_locator.toast_text
        return self.get_text(ele, model=name)

    #我的订单
    def login_success(self):
        name = "登录页面_我的订单"
        ele = msg_login_locator.myorder
        return self.get_text(ele, model=name)




