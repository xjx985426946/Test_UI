from PageLocators.V_app import login_locator
from Common.basepage import BasePage
from other import api as A
import time

class SmsLoginPage(BasePage):

    def sms_login(self, username):
        name = '登录页面_登录操作'
        # 滑动引导页
        self.swipeLeft(2)
        # 点击立即体验
        time.sleep(2)
        self.find_element_by_id(login_locator.goto_main, model=name).click()
        # 关闭升级弹窗
        time.sleep(2)
        self.find_element_by_id(login_locator.close_update_alert, model=name).click()
        time.sleep(2)
        # 点击我的
        self.find_element(login_locator.my, model=name).click()
        time.sleep(2)
        # 点击短信登录
        self.find_element_by_id(login_locator.sms_login, model=name).click()
        time.sleep(2)
        # 输入手机号
        self.id_input_text(username, login_locator.user_input, model=name)
        time.sleep(2)
        next_forget = self.find_element(login_locator.forget_next, model=name)
        next_forget.click()

    def sms_login_success(self, username):
        name = '忘记密码成功'
        # 输入验证码
        time.sleep(2)
        fun = A.Api()
        cookie = "JSESSIONID=ee54bb7c-99f9-49a8-bec2-cd67bf6d4ad3; UM_distinctid=16e6cd884021bb-0285a4927cca88-3d375b01-1fa400-16e6cd88403750; Hm_lvt_00afeb4ef16c81073eb44365f9cd61bc=1576207868,1576461890,1577070624,1577079420; Hm_lpvt_00afeb4ef16c81073eb44365f9cd61bc=1577086578"
        code = fun.get_code(cookie, username)
        print(code)
        time.sleep(2)
        conf = self.find_element_by_id(login_locator.forget_code, model=name)
        conf.send_keys(code)
        time.sleep(1)
        self.find_element(login_locator.forget_code_next, model=name).click()

    def sms_login_code_err(self, code):
        name = '短信登录-验证码不正确'
        conf = self.find_element_by_id(login_locator.forget_code, model=name)
        conf.send_keys(code)
        time.sleep(1)
        self.find_element(login_locator.forget_code_next, model=name).click()

    # toast提示：验证码不正确
    def sms_login_toast(self):
        name = "忘记密码页面_toast"
        ele = login_locator.forget_pwd_toast
        return self.get_toast_text(ele, model=name)

    # toast提示：超出短信发送次数
    def sms_login_toast2(self):
        name = "忘记密码页面_toast"
        ele = login_locator.forget_pwd_toast2
        return self.get_toast_text(ele, model=name)

    # 校验短信登录是否成功
    def check_sms_login(self):
        name = "校验短信登录是否成功"
        try:
            self.find_element_by_id(login_locator.guide_btn, model=name)
            return True
        except:
            return False




