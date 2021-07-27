from PageLocators.C_web import regist_locator
from Common.basepage import BasePage
import time
class RegistPage(BasePage):

    def regist(self, username, code, password):
        name = '登录页面_登录操作'

        #密码登录
        self.find_element(regist_locator.pwd_login, model=name).click()
        #去注册
        self.find_element(regist_locator.regist, model=name).click()
        # 输入手机号
        self.wait_eleVisible(regist_locator.user_input, model=name)
        self.input_text(username, regist_locator.user_input, model=name)
        # 输入验证码
        self.input_text(code, regist_locator.code_input, model=name)
        # 输入密码
        self.input_text(password, regist_locator.pwd_input, model=name)
        # 点击登录按钮
        self.click_element(regist_locator.button, model=name)

    # 手机号码错误
    def get_phone_errMsg(self):
        name = "登录页面_手机号码错误_toast"
        ele = regist_locator.toast_phone_err
        return self.get_text(ele, model=name)

    #验证码错误
    def get_code_errMsg(self):
        name = "登录页面_验证码错误_toast"
        ele = regist_locator.toast_code_err
        return self.get_text(ele, model=name)

    #密码错误
    def get_pwd_errMsg(self):
        name = "登录页面_密码错误_toast"
        ele = regist_locator.toast_pwd_err
        return self.get_text(ele, model=name)

    # 注册信息已存在
    def get_regist_errMsg(self):
        name = "登录页面_密码错误_toast"
        ele = regist_locator.regist_err
        return self.get_text(ele, model=name)

    #我的订单
    def login_success(self):
        name = "登录页面_我的订单"
        ele = regist_locator.my_order
        return self.get_text(ele, model=name)




