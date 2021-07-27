from PageLocators.C_phone import pcenter_locator
from Common.basepage import BasePage

class PcenterPage(BasePage):
    name = '个人中心页面'
    #获取个人中心页面，个人中心文本
    def get_ptext(self):
        # 输入用户名
        self.wait_eleVisible(pcenter_locator.personal_text,model=self.name)
        return self.get_text(pcenter_locator.personal_text,model=self.name)

    #点击设置按钮
    def click_set(self):
        #点击设置按钮
        self.click_element(pcenter_locator.set_button,model=self.name)

    #点击地址管理按钮
    def click_addresss(self):
        # 点击设置按钮
        self.click_element(pcenter_locator.address_button,model=self.name)

    #点击我的订单按钮
    def click_order(self):
        self.click_element(pcenter_locator.order_button,model=self.name)

    #点击退回退款按钮
    def click_retuned(self):
        self.click_element(pcenter_locator.returned,model=self.name)

    #点击优惠券按钮
    def click_cuspon(self):
        self.click_element(pcenter_locator.cuspon,model=self.name)

    #点击我的赏金按钮
    def click_reward(self):
        self.click_element(pcenter_locator.reward,model=self.name)

    #点击我的喜欢
    def click_mylike(self):
        self.click_element(pcenter_locator.my_like,model=self.name)

    #点击待付款按钮
    def click_pending(self):
        self.click_element(pcenter_locator.pending,model=self.name)

    #点击待发货按钮
    def click_processing(self):
        self.click_element(pcenter_locator.processing,model=self.name)

    #点击已发货按钮
    def click_delivering(self):
        self.click_element(pcenter_locator.delivering,model=self.name)

    #点击已收货按钮
    def click_completed(self):
        self.click_element(pcenter_locator.completed,model=self.name)

    #点击我的按钮
    def click_my(self):
        self.click_element(pcenter_locator.my,model=self.name)


