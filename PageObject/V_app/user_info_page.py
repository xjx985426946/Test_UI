import re

from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class LoginUserPage(BasePage):
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
            return False

        time.sleep(2)
        # 关闭首页弹窗,并跳转我的页面
        if self.find_item(login_locator.close_alert):
            self.find_element_by_id(login_locator.close_alert, model=name).click()
            time.sleep(2)
            self.find_element(login_locator.my, model=name).click()
        else:
            self.find_element(login_locator.my, model=name).click()

    # 确认我的页面跳转是否成功
    def confirm_my(self):
        # self.implicitly_wait(5)
        name = "确认我的页面跳转是否成功"
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.user_icon):
            print(ok)
            return ok
        else:
            return ng

    # 跳转个人信息页面
    def edit_user(self):
        name = '跳转个人信息页面'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.user_icon, model=name)

    # 获取用户昵称
    def get_nick_name(self):
        name = '获取用户昵称'
        # self.implicitly_wait(5)
        user_name = self.find_element_by_id(login_locator.nick_name, model=name).text
        print(user_name)
        return user_name

    # 校验个人信息页面跳转
    def confirm_user_info(self):
        name = '校验个人信息页面跳转'
        # self.implicitly_wait(5)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.change_user_icon):
            print(ok)
            return ok
        else:
            return ng

    # 更换头像
    def change_user_icon(self):
        name = '更换头像'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.change_user_icon, model=name)
        time.sleep(3)
        self.find_element(login_locator.select_image, model=name).click()
        self.id_click_element(login_locator.select_image_ok, model=name)
        self.id_click_element(login_locator.crop_image, model=name)
        time.sleep(3)

    # 更换昵称
    def change_user_name(self, user_name):
        name = '更换昵称'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.nick_name, model=name)
        self.id_input_text(user_name, login_locator.input_user_name, model=name)
        self.id_click_element(login_locator.month_day_save, model=name)

