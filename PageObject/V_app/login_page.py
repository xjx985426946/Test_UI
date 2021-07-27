from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time
class LoginPage(BasePage):

    def login(self, username, password):
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
        # 输入用户名
        self.id_input_text(username, login_locator.user_input, model=name)
        time.sleep(1)
        # 输入密码
        self.id_input_text(password, login_locator.password_input, model=name)
        time.sleep(1)
        # 点击登录按钮
        self.find_element_by_id(login_locator.login_btn, model=name).click()

    def guide_btn(self):
        name = '新手引导'
        # 点击引导浮层
        self.id_click_element(login_locator.guide_btn, model=name)
        self.id_click_element(login_locator.guide_btn2, model=name)
        self.id_click_element(login_locator.guide_btn3, model=name)

    # toast提示：参数有误:用户信息不存在
    def get_errMsg_login(self):
        name = "登录页面_toast"
        ele = login_locator.toast_msg
        return self.get_toast_text(ele, model=name)

    # 错误提示：密码错误，请重新输入/输入的手机号有误，请重新输入！
    def login_err(self):
        name = "登录页面-密码错误，请重新输入"
        ele = login_locator.error_msg
        return self.id_get_text(ele, model=name)




