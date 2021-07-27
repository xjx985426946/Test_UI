from PageLocators.C_web import address_locator
from Common.basepage import BasePage
import time
class AddressPage(BasePage):

    def login(self, username, code):
        name = '登录页面_登录操作_账户管理'

        # 输入用户名
        self.wait_eleVisible(address_locator.user_input, model=name)
        self.input_text(username, address_locator.user_input, model=name)
        # 输入验证码
        self.input_text(code, address_locator.code_input, model=name)
        # 点击登录按钮
        self.click_element(address_locator.button, model=name)

        time.sleep(8)
        # 点击地址管理
        self.wait_eleVisible(address_locator.address_manage, model=name)
        self.click_element(address_locator.address_manage, model=name)

    # 地址管理页面判断
    def address_manage(self):
        name = '地址管理页面'
        ele = address_locator.address_check
        return self.get_text(ele, model=name)

    # 新增地址
    def add_address(self, receiver_name, receiver_mobile, detail_address):
        name = "地址管理-新增地址"
        self.wait_eleVisible(address_locator.add_address, model=name)
        self.click_element(address_locator.add_address, model=name)
        time.sleep(2)
        # 输入收货人姓名、手机号
        self.wait_eleVisible(address_locator.receiver_name, model=name)
        self.input_text(receiver_name, address_locator.receiver_name, model=name)
        time.sleep(2)
        self.input_text(receiver_mobile, address_locator.receiver_mobile, model=name)
        time.sleep(2)
        # 选择省市区
        self.click_element(address_locator.location_name, model=name)
        self.click_element(address_locator.provincial, model=name)
        self.click_element(address_locator.urban, model=name)
        self.click_element(address_locator.areas, model=name)
        # 输入详细地址
        time.sleep(1)
        self.input_text(detail_address, address_locator.detail_address, model=name)
        time.sleep(1)
        # 选择默认地址
        self.click_element(address_locator.default_address, model=name)
        time.sleep(1)
        # 保存地址
        self.click_element(address_locator.save_button, model=name)

    # 判断地址收货人姓名为空/收货人手机号错误/详细地址为空
    def add_address_check(self):
        name = "地址管理-新增地址_toast"
        ele = address_locator.address_success
        return self.get_text(ele, model=name)

    # 地址新增/编辑是否成功
    def default_address_check(self):
        name = "地址管理-新增地址-check"
        # 校验默认地址是否成功
        self.wait_eleVisible(address_locator.check_default_address, model=name)
        default_address = address_locator.check_default_address
        return self.get_text(default_address, model=name)

    # 编辑地址
    def edit_address(self, receiver_name):
        name = "编辑地址"
        # 编辑地址
        self.wait_eleVisible(address_locator.edit_address, model=name)
        self.click_element(address_locator.edit_address, model=name)

        time.sleep(2)
        # 输入收货人姓名、手机号
        self.input_text(receiver_name, address_locator.receiver_name, model=name)
        time.sleep(1)
        # 保存地址
        self.click_element(address_locator.save_button, model=name)

    # 删除地址
    def delete_address(self):
        name = '删除地址'
        self.wait_eleVisible(address_locator.delete_address, model=name)
        self.click_element(address_locator.delete_address, model=name)
        time.sleep(3)
        self.wait_eleVisible(address_locator.delete_address_button)
        self.click_element(address_locator.delete_address_button)

    # 校验地址删除成功
    def check_delete_address(self):
        name = "校验地址删除成功"
        check_address = address_locator.address_success
        return self.get_text(check_address, model=name)

    # 设为默认地址
    def set_default_address(self):
        name = "设为默认地址"
        self.wait_eleVisible(address_locator.set_default_address, model=name)
        self.click_element(address_locator.set_default_address, model=name)

    # 校验设为默认地址
    def check_set_default_address(self):
        name = "校验设为默认地址"
        check_name = address_locator.check_set_default_address
        return self.get_text(check_name, model=name)

    # 地址管理
    def login_success(self):
        name = "登录页面_地址管理"
        ele = address_locator.address_check
        return self.get_text(ele, model=name)





