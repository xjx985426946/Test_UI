from PageLocators.C_web import center_locator
from Common.basepage import BasePage
import time
class Test(BasePage):

    name = '个人中心页面'
    #点击账号管理
    def click_account(self):

        #点击账号管理按钮
        self.find_element(center_locator.account_button, model=self.name).click()


    # 点击我的订单
    def click_order(self):

        # 点击我的订单
        self.find_element(center_locator.order_button, model=self.name).click()

    #我的优惠券
    def click_coupons(self):
        # 点击我的优惠券
        self.find_element(center_locator.coupons_button, model=self.name).click()

   #我的喜欢
    def click_like(self):
        #点击我的喜欢
        self.find_element(center_locator.like_button, model=self.name).click()


    def click_address(self):
        #点击我的地址管理
        self.find_element(center_locator.address__button, model=self.name).click()
