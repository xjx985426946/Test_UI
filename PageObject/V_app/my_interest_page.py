
from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class MyInterestPage(BasePage):
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

    # 确认我的兴趣页面跳转是否成功
    def confirm_my_interest(self):
        # self.implicitly_wait(5)
        name = "确认我的兴趣页面跳转是否成功"
        interest = self.id_get_text(login_locator.check_header, model=name)
        return interest

    # 跳转我的兴趣页面
    def my_interest(self):
        name = '跳转我的兴趣页面页面'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.my_interest, model=name)

    # 获取我的兴趣总个数（包括推荐兴趣、已添加兴趣）
    def get_interest_number(self):
        name = '获取我的兴趣总个数'
        # self.implicitly_wait(5)
        time.sleep(2)
        user_name = self.find_elements(login_locator.interest_name_tv, model=name)
        count = len(user_name)
        return count

    # 我的兴趣-删除已添加兴趣
    def del_my_interest(self):
        name = '我的兴趣-删除已添加兴趣'
        # self.implicitly_wait(5)
        time.sleep(2)
        self.id_click_element(login_locator.interest_edit, model=name)
        delete = self.find_elements(login_locator.interest_edit_del, model=name)
        delete[0].click()
        self.id_click_element(login_locator.interest_edit, model=name)

    # 我的兴趣-添加兴趣
    def add_interest(self, interest_name):
        name = '我的兴趣-添加兴趣'
        self.implicitly_wait(5)
        self.click_element(login_locator.interest_edit_add, model=name)
        self.id_input_text(interest_name, login_locator.interest_edit_add_input, model=name)
        self.id_click_element(login_locator.create_right_add, model=name)

    # 我的兴趣-添加兴趣-标签名不能为空
    def add_interest_err(self):
        name = '我的兴趣-添加兴趣'
        self.implicitly_wait(5)
        self.click_element(login_locator.interest_edit_add, model=name)
        self.id_click_element(login_locator.create_right_add, model=name)
        toast = self.get_toast_text(login_locator.interest_edit_add_input_err)
        return toast

    # 我的兴趣-添加兴趣-标签名不能少于4个字
    def add_interest_err2(self):
        name = '我的兴趣-添加兴趣'
        self.implicitly_wait(5)
        interest_name = '12'
        self.click_element(login_locator.interest_edit_add, model=name)
        self.id_input_text(interest_name, login_locator.interest_edit_add_input, model=name)
        self.id_click_element(login_locator.create_right_add, model=name)
        toast = self.get_toast_text(login_locator.interest_edit_add_input_err2)
        return toast

    # 校验添加兴趣是否成功
    def confirm_add_interest(self, interest_name):
        name = '校验添加兴趣是否成功'
        time.sleep(2)
        confirm = '//*[@text=\'' + interest_name + '\']'
        success = self.find_element(confirm, model=name).text
        return success

