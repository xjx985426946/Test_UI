from PageLocators.V_app import login_locator
from Common.basepage import BasePage
from other import api as A
import time

class ForGetPwdPage(BasePage):

    def forget(self, username):
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
        # 点击忘记密码
        self.find_element_by_id(login_locator.forget_password, model=name).click()
        time.sleep(2)
        # 输入手机号
        self.id_input_text(username, login_locator.user_input, model=name)
        time.sleep(2)
        next_forget = self.find_element(login_locator.forget_next, model=name)
        next_forget.click()

    def guide_btn(self):
        name = '新手引导'
        # 点击引导浮层
        self.id_click_element(login_locator.guide_btn, model=name)
        self.id_click_element(login_locator.guide_btn2, model=name)
        self.id_click_element(login_locator.guide_btn3, model=name)

    def forget_success(self, username, new_pwd, new_pwd_second):
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
        time.sleep(2)
        pwd1 = self.find_element(login_locator.forget_new_pwd2, model=name)
        pwd1.send_keys(new_pwd)
        time.sleep(1)
        pwd2 = self.find_element(login_locator.forget_new_pwd_second2, model=name)
        pwd2.send_keys(new_pwd_second)
        time.sleep(1)
        self.find_element(login_locator.forget_confirm, model=name).click()

    def forget_error(self, code):
        name = '忘记密码-验证码错误'
        conf = self.find_element_by_id(login_locator.forget_code, model=name)
        conf.send_keys(code)
        time.sleep(1)
        self.find_element(login_locator.forget_code_next, model=name).click()

    # toast提示：验证码不正确
    def get_errmsg_forget(self):
        name = "忘记密码页面_toast"
        ele = login_locator.forget_pwd_toast
        return self.get_toast_text(ele, model=name)

    # toast提示：超出短信发送次数
    def get_errmsg_forge2(self):
        name = "忘记密码页面_toast"
        ele = login_locator.forget_pwd_toast2
        return self.get_toast_text(ele, model=name)

    # toast提示：两次密码输入不一致，请重新输入
    def get_errmsg_forge3(self):
        name = "登录页面"
        ele = login_locator.forget_pwd_toast
        return self.id_get_text(ele, model=name)




