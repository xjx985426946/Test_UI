'''蜂卡页面'''
from PageLocators.F_web import intbeecard_locator
from Common.basepage import BasePage
from selenium import webdriver
class CardPage(BasePage):
    name = '全部蜂卡页面'

    #补充库存
    def create_stock(self):
        #点击第一条蜂卡补充库存按钮
        self.click_element(intbeecard_locator.stock,model=self.name)
        #点击确定按钮
        self.click_element(intbeecard_locator.button,model=self.name)
        #点击提交按钮
        self.click_element(intbeecard_locator.button_u,model=self.name)

    #终止蜂卡
    def supplement_card(self,supplement_reason):
        #点击终止蜂卡按钮
        self.click_element(intbeecard_locator.supplement_card,model=self.name)
        self.input_text(supplement_reason,intbeecard_locator.supplement_reason,model=self.name)
        self.click_element(intbeecard_locator.supplement_button,model=self.name)

    #查看详情、发布蜂卡
    def detail(self):
        #选择第一条点击蜂卡详情
        self.click_element(intbeecard_locator.card_detail,model=self.name)
        #点击查看规格按钮
        self.click_element(intbeecard_locator.standard,model=self.name)
        #点击确定按钮
        self.click_element(intbeecard_locator.standard_button,model=self.name)
        #点击定向发卡
        self.click_element(intbeecard_locator.card_dx,model=self.name)

    def search_spreader(self):
        pass