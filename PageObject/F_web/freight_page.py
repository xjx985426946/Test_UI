from PageLocators.F_web import freight_locator
from Common.basepage import BasePage
from selenium import webdriver
class FreightPage(BasePage):
    name = '运费模板页面'

    #添加运费模板
    def create_freight(self,freight_name,input_freight):
        #点击添加运费按钮
        self.click_element(freight_locator.create_freight,model=self.name)
        # 输入运费模板名称
        self.input_text(freight_name,freight_locator.freight_name,model=self.name)
        #输入运费
        self.input_text(input_freight,freight_locator.input_freight,model=self.name)
        #点击保存按钮
        self.click_element(freight_locator.button,model=self.name)


    #编辑运费模板
    def edit_freight(self):
        #点击编辑按钮
        self.click_element(freight_locator.freight_edit,model=self.name)
        self.click_element(freight_locator.edit_button,model=self.name)

    #删除按钮
    def delete_freight(self):
        #选择第一条点击删除按钮
        self.click_element(freight_locator.freight_delete,model=self.name)
        self.click_element(freight_locator.delete_button,model=self.name)


