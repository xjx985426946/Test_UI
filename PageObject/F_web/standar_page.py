from PageLocators.F_web import standar_locator
from Common.basepage import BasePage
from selenium import webdriver
class StandardPage(BasePage):
    name = '规格管理页面'

    #添加规格
    def create_standard(self,standard_name,input_attributes1,input_attributes2):
        #点击添加规格按钮
        self.click_element(standar_locator.create_sdandard,model=self.name)
        # 输入规格名称
        self.input_text(standard_name,standar_locator.standard_name,model=self.name)
        #点击添加规格属性
        self.click_element(standar_locator.standard_attributes,model=self.name)
        #输入规格属性
        self.input_text(input_attributes1,standar_locator.input_attributes1,model=self.name)
        self.input_text(input_attributes2,standar_locator.input_attributes2,model=self.name)
        #点击保存按钮
        self.click_element(standar_locator.button,model=self.name)



    #编辑规格
    def edit_standard(self):
        #点击编辑按钮
        self.click_element(standar_locator.edit_standard,model=self.name)
        self.click_element(standar_locator.edit_button,model=self.name)

    #删除按钮
    def delete_standard(self):
        #选择第一条点击删除按钮
        self.click_element(standar_locator.delete_standard,model=self.name)
        self.click_element(standar_locator.delete_button,model=self.name)

