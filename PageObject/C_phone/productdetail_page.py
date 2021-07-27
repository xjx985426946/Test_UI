from PageLocators.C_phone import productdetail_locator
from Common.basepage import BasePage


class ProductdetailPage(BasePage):
    name = 'C端购买页面'

    # 点击购买按钮
    def click_purchase(self):
        self.click_element(productdetail_locator.purcharse_button,model=self.name)


    #点击客服按钮
    def click_server(self):
        self.click_element(productdetail_locator.server_button,model=self.name)
    #获取客服电话
    def get_serverphone(self):
        return self.get_text(productdetail_locator.server_phone,model=self.name)
    #获取客服qq
    def get_serverqq(self):
        return self.get_text(productdetail_locator.server_qq,model=self.name)
    def click_complte(self):
        self.click_element(productdetail_locator.complete,model=self.name)


    #点击送好友按钮
    def click_friend(self):
        self.click_element(productdetail_locator.friend_button,model=self.name)

    #点击商品详情按钮
    def click_productdetail(self):
        self.click_element(productdetail_locator.column_productdetail,model=self.name)

    #点击商品参数按钮
    def click_productparam(self):
        self.click_element(productdetail_locator.production_param,model=self.name)

    # 点击领券按钮
    def click_coupons(self):
        self.click_element(productdetail_locator.cuspons,model=self.name)

    # 点击商品评价
    def click_productevaluate(self):
        self.click_element(productdetail_locator.product_evaluate,model=self.name)

    # 点击试用报告
    def click_tryreport(self):
        self.click_element(productdetail_locator.try_report,model=self.name)

    # 点击喜欢
    def click_like(self):
        self.click_element(productdetail_locator.like,model=self.name)
    #/取消喜欢
    def click_notlike(self):
        self.click_element(productdetail_locator.not_like, model=self.name)
    #获取添加喜欢的toast/取消喜欢
    def get_addtoast(self):
        return self.get_text(productdetail_locator.add_toast,model=self.name)

    # 选择规格
    def click_standar(self):
        self.click_element(productdetail_locator.color,model=self.name)

        self.click_element(productdetail_locator.big,model=self.name)
    #增加购买数量
    def click_add(self):
        self.click_element(productdetail_locator.add,model=self.name)

    #减少购买数量
    def click_resuce(self):
        self.click_element(productdetail_locator.reduce,model=self.name)

    # 点击确认购买按钮
    def click_decide_botton(self):
        self.click_element(productdetail_locator.decide_botton,model=self.name)

    #获取商品金额
    def get_amount(self):
        return self.get_text(productdetail_locator.amount,model=self.name)

    #点击专柜
    def click_shop(self):
        self.click_element(productdetail_locator.shop,model=self.name)






