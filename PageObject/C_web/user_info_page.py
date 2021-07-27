from PageLocators.C_web import user_info_locator
from Common.basepage import BasePage
import time
class UserInfoPage(BasePage):

    def login(self, username, code):
        name = '登录页面_登录操作_账户管理'

        # 输入用户名
        self.wait_eleVisible(user_info_locator.user_input, model=name)
        self.input_text(username, user_info_locator.user_input, model=name)
        # 输入验证码
        self.input_text(code, user_info_locator.code_input, model=name)
        # 点击登录按钮
        self.click_element(user_info_locator.button, model=name)

        time.sleep(8)
        # 点击账户管理
        self.wait_eleVisible(user_info_locator.user_manage, model=name)
        self.click_element(user_info_locator.user_manage, model=name)

    # 账号管理页面判断
    def user_manage(self):

        name = '账号管理页面'
        ele = user_info_locator.info
        return self.get_text(ele, model=name)

    # 更换昵称
    def get_user_info_name(self, user_info_name):
        name = "账户管理-修改昵称_toast"
        self.wait_eleVisible(user_info_locator.name_input, model=name)
        self.input_text(user_info_name, user_info_locator.name_input, model=name)
        time.sleep(2)
        self.click_element(user_info_locator.name_save, model=name)

    # 判断昵称更换是否成功
    def user_info_name_check(self):
        name = "账户管理-修改昵称_toast"
        ele = user_info_locator.name_input
        return self.get_text(ele, model=name)

    # 修改密码页面跳转
    def user_edit_pwd_page(self):
        name = "修改密码页面_toast"
        # 点击修改密码
        self.wait_eleVisible(user_info_locator.edit_pwd, model=name)
        edit = self.find_element(user_info_locator.edit_pwd, model=name)
        edit.click()

    def user_edit_pwd(self, pwd, new_pwd, second_pwd):
        name = "修改密码页面_toast"

        # 修改密码页面
        # 输入旧密码
        self.wait_eleVisible(user_info_locator.input_pwd, model=name)
        self.input_text(pwd, user_info_locator.input_pwd, model=name)

        # 输入新密码
        self.input_text(new_pwd, user_info_locator.input_new_pwd, model=name)

        # 二次输入新密码
        self.input_text(second_pwd, user_info_locator.intput_second_pwd, model=name)
        # 点击提交
        self.click_element(user_info_locator.button_pwd, model=name)

    # 旧密码错误
    def user_edit_pwd_err(self):
        name = '"旧密码错误_toast"'
        err = user_info_locator.pwd_err
        return self.get_text(err, model=name)

    # 新密码错误
    def user_edit_new_pwd_err(self):
        name = '"新密码错误_toast"'
        err = user_info_locator.new_pwd_err
        return self.get_text(err, model=name)

    # 二次新密码错误
    def user_edit_second_pwd_err(self):
        name = '"二次新密码错误_toast"'
        err = user_info_locator.pwd_second_err
        return self.get_text(err, model=name)

    #新旧密码相同/新密码错误/密码修改成功
    def user_edit_pwd_success(self):
        name = '"修改密码页面_toast"'
        err = user_info_locator.pwd_success
        return self.get_text(err, model=name)






