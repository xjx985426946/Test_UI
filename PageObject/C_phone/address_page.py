from PageLocators.C_phone import address_locator
from Common.basepage import BasePage
import time
from selenium import webdriver
class AddressPage(BasePage):
    name = '新增地址页面'

    #点击添加地址按钮
    def create_button(self):
        #点击添加地址按钮
        self.click_element(address_locator.create_address,model=self.name)


    #添加地址
    def input_address(self,name,mobile,deatiladdress):
        #点击设置按钮
        self.input_text(name,address_locator.input_name,model=self.name)
        self.input_text(mobile,address_locator.input_mobile,model=self.name)
        self.click_element(address_locator.select_address,model=self.name)
        time.sleep(2)
        self.click_element(address_locator.click_province,model=self.name)
        time.sleep(2)
        self.click_element(address_locator.click_city,model=self.name)
        time.sleep(2)
        self.click_element(address_locator.click_town,model=self.name)
        time.sleep(2)
        self.input_text(deatiladdress,address_locator.detailaddress,model=self.name)

        #点击确定按钮
        time.sleep(2)
        self.click_element(address_locator.button,model=self.name)

    #编辑地址
    def update_address(self):
        self.click_element(address_locator.edit_button,model="修改地址页面")
        time.sleep(2)
        self.click_element(address_locator.update_button)

    #删除地址
    def delete_address(self):
        self.click_element(address_locator.delete,model="修改地址页面")

    #获取toast提示
    def get_toast(self):
        return self.get_text(address_locator.toast_text,model=self.name)

    #获取页面添加地址文本
    def get_addresstext(self):
        return self.get_text(address_locator.address_text,model=self.name)


