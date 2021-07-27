import re

from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class LoginUserIntPage(BasePage):
    def login_user(self, username, password):
        name = '登录页面_登录操作'
        self.implicitly_wait(5)
        # 滑动引导页
        self.swipeLeft(2)
        # 点击立即体验
        self.find_element_by_id(login_locator.goto_main, model=name).click()
        time.sleep(2)
        # 关闭升级弹窗
        if self.find_item(login_locator.close_update_alert):
            self.find_element_by_id(login_locator.close_update_alert, model=name).click()
            self.find_element(login_locator.my, model=name).click()
        else:
            self.find_element(login_locator.my, model=name).click()

        time.sleep(2)
        # 输入用户名
        self.id_input_text(username, login_locator.user_input, model=name)
        # 输入密码
        self.id_input_text(password, login_locator.password_input, model=name)
        # 点击登录按钮
        self.find_element_by_id(login_locator.login_btn, model=name).click()
        time.sleep(2)
        # 点击引导浮层
        if self.find_item(login_locator.guide_btn):
            self.id_click_element(login_locator.guide_btn, model=name)
            self.id_click_element(login_locator.guide_btn2, model=name)
            self.id_click_element(login_locator.guide_btn3, model=name)
        else:
            print('if判断结束')
            return False

        print('开始执行')
        time.sleep(2)
        # 关闭首页弹窗,并跳转我的页面
        if self.find_item(login_locator.close_alert):
            self.find_element_by_id(login_locator.close_alert, model=name).click()
            time.sleep(2)
            self.find_element(login_locator.my, model=name).click()
        else:
            self.find_element(login_locator.my, model=name).click()

    # 确认我的积分页面跳转是否成功
    def confirm_go_user_integral(self):
        # self.implicitly_wait(5)
        name = "确认我的积分页面跳转是否成功"
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.explain):
            return ok
        else:
            return ng

    # 跳转我的积分页面
    def go_user_integral(self):
        name = '跳转我的积分页面'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.integral, model=name)

    # 跳转我的积分页面-积分规则
    def go_explain(self):
        name = '跳转我的积分页面-积分规则'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.explain, model=name)

    # 校验我的积分页面-积分规则跳转
    def confirm_go_explain(self):
        name = '校验我的积分页面-积分规则跳转'
        # self.implicitly_wait(5)
        explain = self.find_element_by_id(login_locator.check_header).text
        return explain

    # 跳转我的积分页面-积分明细
    def go_explain_detail(self):
        name = '跳转我的积分页面-积分明细'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.month_day_save, model=name)
