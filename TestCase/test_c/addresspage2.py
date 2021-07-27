from TestCase.test_c.basepage2 import BasePage
import time
from TestCase.test_c import address_locator
class addressPage(BasePage):

    name = '添加地址页面'

    #点击添加地址
    def click_addresss(self):
        # 点击设置按钮
        self.click_element(address_locator.address_button,model=self.name)

    #输入姓名
    def input_name(self,name):
        self.input_text(name,address_locator.name,self.name)


    #输入手机号
    def input_mobile(self):
        # 点击设置按钮
        time.sleep(1)
        self.input_text("13729542194", '//input[@class="el-input__inner" and @placeholder="请输入收件人手机号码"]', self.name)

    #请输入详细地址

    def input_deatil(self):
        self.input_text('HC','//input[@placeholder = "请输入详细地址"]')
        time.sleep(1)
        self.click_element('//span[@class="el-switch__core"]', model=self.name)

    #点击保存按钮
    def click_button(self):
        self.click_element('//span[text() = "保存"]', model=self.name)

    #获取toast
    def get_toast(self):
        text= self.get_text('//p[@class="el-message__content" and text()="请选择所在地址"]')
        return text


    def address(self):
        '''正确添加地址'''
        self.click_element(address_locator.address_button, model=self.name)
        self.input_text(name, address_locator.name, self.name)
        self.input_text('HC', address_locator.name)
        time.sleep(1)
        self.click_element('//span[@class="el-switch__core"]', model=self.name)
        text = self.get_text('//p[@class="el-message__content" and text()="请选择所在地址"]')

    def address(self,mobile):
        '''手机号码不正确地址'''
        self.click_element(address_locator.address_button, model=self.name)
        self.input_text(name, address_locator.name, self.name)
        self.input_text('HC', address_locator.name)
        time.sleep(1)
        self.click_element('//span[@class="el-switch__core"]', model=mobile)
        text = self.get_text('//p[@class="el-message__content" and text()="请选择所在地址"]')