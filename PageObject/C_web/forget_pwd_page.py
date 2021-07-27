from PageLocators.C_web import forget_pwd_locator
from Common.basepage import BasePage
import time
class ForgetPwdPage(BasePage):

    def forget_pwd(self, username, code, password, second_password):
        name = '登录页面_登录操作'

        #密码登录
        self.find_element(forget_pwd_locator.pwd_login, model=name).click()
        #忘记密码
        self.find_element(forget_pwd_locator.forget_pwd, model=name).click()
        # 输入手机号
        self.wait_eleVisible(forget_pwd_locator.user_input, model=name)
        self.input_text(username, forget_pwd_locator.user_input, model=name)
        # 输入验证码
        self.input_text(code, forget_pwd_locator.code_input, model=name)
        # 输入密码
        self.input_text(password, forget_pwd_locator.pwd_input, model=name)
        # 再次输入密码
        self.input_text(second_password, forget_pwd_locator.second_pwd_input, model=name)
        # 点击登录按钮
        self.click_element(forget_pwd_locator.button, model=name)

    # 手机号码错误
    def get_phone_errMsg(self):
        name = "登录页面_手机号码错误_toast"
        ele = forget_pwd_locator.toast_phone_err
        return self.get_text(ele, model=name)

    #验证码错误
    def get_code_errMsg(self):
        name = "登录页面_验证码错误_toast"
        ele = forget_pwd_locator.toast_code_err
        return self.get_text(ele, model=name)

    #密码错误
    def get_pwd_errMsg(self):
        name = "登录页面_密码错误_toast"
        ele = forget_pwd_locator.toast_pwd_err
        return self.get_text(ele, model=name)

    #二次密码错误
    def get_second_pwd_errMsg(self):
        name = "登录页面_二次密码错误_toast"
        ele = forget_pwd_locator.toast_second_pwd_err
        return self.get_text(ele, model=name)

    #我的订单
    def login_success(self):
        name = "登录页面_我的订单"
        ele = forget_pwd_locator.myorder
        return self.get_text(ele, model=name)




