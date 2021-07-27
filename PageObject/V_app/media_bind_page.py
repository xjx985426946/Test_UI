import re

from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class MediaBindPage(BasePage):
    def login_user(self, username, password):
        name = '登录页面_登录操作'
        self.implicitly_wait(5)
        # 用户协议
        if self.find_item(login_locator.user_bg):
            self.find_element_by_id(login_locator.user_confirm, model=name).click()
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

    # 自媒体绑定页面跳转是否成功
    def confirm_my_media(self):
        self.implicitly_wait(5)
        name = "自媒体绑定页面跳转是否成功"
        center = self.find_element_by_id(login_locator.check_header, model=name).text
        return center

    # 跳转自媒体绑定页面
    def my_media(self):
        name = '跳转自媒体绑定页面'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.my_media, model=name)

    # 绑定微博-跳转微博登录页面
    def not_login_wb(self):
        name = '绑定微博-跳转微博登录页面'
        # self.implicitly_wait(5)
        time.sleep(2)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[0].click()

    # 已登录微博-绑定微博-跳转微博登录页面-确认授权
    def login_wb_bind(self):
        name = '绑定微博-跳转微博登录页面'
        # self.implicitly_wait(5)
        time.sleep(2)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[0].click()
        self.find_element(login_locator.blog_authorized_Yes, model=name).click()

    # 已登录微博-绑定微博-跳转微博登录页面-取消授权
    def login_wb_cancel_bind(self):
        name = '未登录微博-绑定微博-跳转微博登录页面'
        # self.implicitly_wait(5)
        time.sleep(2)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[0].click()
        time.sleep(3)
        self.find_element_by_id(login_locator.cancel, model=name).click()

    # 校验绑定微博-跳转微博登录页面-取消授权
    def confirm_login_wb(self):
        name = '校验绑定微博-跳转微博登录页面-取消授权'
        cancel = self.get_toast_text(login_locator.cancel_toast, model=name)
        return cancel

    # 校验已登录微博-绑定微博-跳转微博登录页面-授权
    def confirm_blog_authorized(self):
        name = '校验已登录微博-绑定微博-跳转微博登录页面-授权'
        bind = self.get_toast_text(login_locator.authorized_toast, model=name)
        # blog2 = blog[0].text
        return bind

    # 绑定公众号页面
    def wx_bind(self):
        name = '绑定公众号页面'
        self.implicitly_wait(5)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[1].click()
        self.find_element(login_locator.wx_save).click()

    # 校验跳转绑定公众号页面
    def confirm_wx_bind(self):
        name = '校验跳转绑定公众号页面'
        self.implicitly_wait(5)
        toast = self.get_toast_text(login_locator.wx_success, model=name)
        return toast

    # 绑定抖音页面-跳转抖音
    def dy_bind(self):
        name = '绑定抖音页面'
        self.implicitly_wait(5)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[2].click()

    # 绑定抖音页面-未登录(已安装抖音)
    def confirm_dy_bind(self):
        name = '绑定抖音页面-未登录'
        self.implicitly_wait(5)
        user_name = self.find_element(login_locator.not_login_tips, model=name).text
        return user_name

    # 绑定抖音页面-登录(已安装抖音)——授权并登录
    def confirm_dy_bind_login(self):
        name = '绑定抖音页面-未登录'
        self.implicitly_wait(5)
        user_name = self.find_element_by_id(login_locator.tips_login, model=name).text
        return user_name

    # 绑定抖音页面-授权登录
    def tips_bind(self, url):
        name = '绑定抖音页面'
        self.implicitly_wait(5)
        # time.sleep(2)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[2].click()
        # time.sleep(3)
        if self.find_item(login_locator.tips_login):
            self.find_element_by_id(login_locator.tips_login, model=name).click()
        time.sleep(3)
        self.id_input_text(url, login_locator.page_Et, model=name)
        self.find_element_by_id(login_locator.commit, model=name).click()

    # 校验抖音授权是否成功
    def confirm_tips_bind(self, point):
        name = '校验抖音授权是否成功'
        ok = '成功'
        ng = '失败'
        success = '//*[@text=\'' + point + '\']'
        if self.find_element_page(success, model=name):
            return ok
        else:
            return ng

    # 绑定抖音页面-抖音-非抖音链接报错
    def tips_login_error(self):
        name = '绑定抖音页面-抖音-非抖音链接报错'
        # self.implicitly_wait(5)
        error = self.get_toast_text(login_locator.tips_login_error, model=name)
        print(error)
        return error

    # 绑定小红书页面-小红书授权
    def red_book(self, url):
        name = '绑定小红书页面-小红书授权'
        self.implicitly_wait(5)
        user_name = self.find_elements(login_locator.bind_name, model=name)
        user_name[3].click()
        time.sleep(2)
        self.find_element_by_id(login_locator.name_Et).send_keys('小红书测试')
        self.find_element_by_id(login_locator.page_Et).send_keys(url)
        self.find_element_by_id(login_locator.commit, model=name).click()
        # time.sleep(3)

    # 绑定小红书页面-小红书授权报错
    def red_book_error(self):
        name = '绑定小红书页面-小红书授权报错'
        # self.implicitly_wait(5)
        error = self.get_toast_text(login_locator.red_book_error, model=name)
        return error

    # 校验小红书授权是否成功
    def confirm_red_book_bind(self, point):
        name = '校验小红书授权是否成功'
        ok = '成功'
        ng = '失败'
        success = '//*[@text=\'' + point + '\']'
        if self.find_element_page(success, model=name):
            return ok
        else:
            return ng

    # # 未登录微博-绑定微博-跳转微博登录页面-取消授权
    # def not_login(self):
    #     name = '未登录微博-绑定微博-跳转微博登录页面'
    #     # self.implicitly_wait(5)
    #     time.sleep(2)
    #     user_name = self.find_elements(login_locator.bind_name, model=name)
    #     user_name[0].click()
    #     self.find_element_by_id(login_locator.cancel_not, model=name)
    #
    # # 校验未登录微博-绑定微博-跳转微博登录页面
    # def confirm_not_login_wb(self):
    #     name = '校验未登录微博-绑定微博-跳转微博登录页面'
    #     # self.implicitly_wait(5)
    #     time.sleep(2)
    #     ok = '跳转成功'
    #     ng = '跳转失败'
    #     if self.find_item(login_locator.confirm_not_authorized):
    #         return ok
    #     else:
    #         return ng


