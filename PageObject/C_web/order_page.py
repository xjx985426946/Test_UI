
from PageLocators.C_web import order_locator
from Common.basepage import BasePage
# 这里是我的订单页面

class OrderPage(BasePage):
    name = "我的订单页面"

    # 点击待付款按钮
    def click_payment(self):
        name = "我的订单页面"
        self.click_element(order_locator.Payment_button, model=name)

    # 点击待发货按钮
    def click_shipp(self):
        name = "我的订单页面"
        self.click_element(order_locator.shipp_button, model=name)

    # 点击已发货按钮
    def click_shipped(self):
        name = "我的订单页面"
        self.click_element(order_locator.shipped_button,model=name)

    #点击已收货按钮
    def click_receiving(self):
        name = "我的订单页面"
        self.click_element(order_locator.receiving_button,model=name)

    #点击查看详情按钮
    def click_detail(self):
        name = "我的订单页面"
        self.click_element(order_locator.detail_button,model=name)

    #我的订单页面点击立即付款按钮
    def click_pay(self):
        name = "我的订单页面"
        self.click_element(order_locator.pay,model=self.name)

    #我的订单页面获取商品单价和购买数量
    def get_quantity(self):
        quantity = self.find_element(order_locator.quantity)
        product_price = self.find_element(order_locator.product_price)
        return quantity,product_price

from PageLocators.C_web import my_order_locator
from Common.basepage import BasePage
import time
class OrderPage(BasePage):

    def login(self, username, code):
        name = '登录页面_登录-我的订单'
        # 输入用户名
        self.wait_eleVisible(my_order_locator.user_input, model=name)
        self.input_text(username, my_order_locator.user_input, model=name)
        # 输入密码
        self.input_text(code, my_order_locator.code_input, model=name)
        # 点击登录按钮
        self.click_element(my_order_locator.button, model=name)

    def login_success(self):
        name = "登录页面_我的订单"
        ele = my_order_locator.my_order
        return self.get_text(ele, model=name)

    # 订单列表-待付款订单列表页跳转
    def wait_pay(self):
        name = '待付款订单列表页'
        # 点击待付款
        self.wait_eleVisible(my_order_locator.wait_pay_order, model=name)
        self.click_element(my_order_locator.wait_pay_order, model=name)

    # 订单列表-待发货订单列表页跳转
    def wait_ship(self):
        name = '待发货订单列表页跳转'
        # 点击待发货
        self.wait_eleVisible(my_order_locator.wait_ship_order, model=name)
        self.click_element(my_order_locator.wait_ship_order, model=name)

    # 订单列表-已发货订单列表页跳转
    def shipped_order(self):
        name = '已发货订单列表页'
        # 点击已发货
        self.wait_eleVisible(my_order_locator.shipped_order, model=name)
        self.click_element(my_order_locator.shipped_order, model=name)

    # 订单列表-已收货订单列表页跳转
    def received_order(self):
        name = '已收货订单列表页'
        # 点击已收货
        self.wait_eleVisible(my_order_locator.received_order, model=name)
        self.click_element(my_order_locator.received_order, model=name)

    # 校验订单列表跳转
    def check_order_jump(self):
        name = '校验订单列表跳转'
        ele = my_order_locator.check_order_list
        return self.get_text(ele, model=name)

    # 订单详情跳转
    def detail_order(self):
        name = '订单详情跳转'
        # 点击查看详情
        self.wait_eleVisible(my_order_locator.detail_order, model=name)
        self.click_element(my_order_locator.detail_order, model=name)

    # 校验订单详情跳转
    def check_detail_order(self):
        name = '校验订单详情跳转'
        ele = my_order_locator.check_detail_order
        return self.get_text(ele, model=name)

    # 订单详情-申请退款/未收货退货/已收货退货
    def return_refund_order(self):
        name = '申请退款/未收货退货/已收货退货'
        self.wait_eleVisible(my_order_locator.detail_order_button1, model=name)
        self.click_element(my_order_locator.detail_order_button1, model=name)

    # 取消订单
    def cancel_order(self):
        name = '取消订单'
        self.wait_eleVisible(my_order_locator.detail_order_button1, model=name)
        self.click_element(my_order_locator.detail_order_button1, model=name)
        time.sleep(3)
        self.click_element(my_order_locator.confirm_button, model=name)

    # 校验订单已取消/已提醒商家发货/申请成功/请填写退货单号/已确认收货/请选择退货物流公司
    def check_order_msg(self):
        name = '校验订单已取消/已提醒商家发货/申请成功/请填写退货单号/已确认收货/请选择退货物流公司'
        self.wait_eleVisible(my_order_locator.check_msg)
        ele = my_order_locator.check_msg
        return self.get_text(ele, model=name)

    # 订单列表页-立即付款页面跳转/提醒发货/查看物流
    def order_list_button2(self):
        name = '订单列表页-立即付款页面跳转/提醒发货/查看物流跳转'
        self.wait_eleVisible(my_order_locator.order_list_button2)
        self.click_element(my_order_locator.order_list_button2, model=name)

    # 校验查看物流跳转
    def check_order_logistics(self):
        name = '校验查看物流跳转'
        ele = my_order_locator.check_order_logistics
        return self.get_text(ele, model=name)

    # 订单列表页-确认收货
    def order_list_confirm_receipt(self):
        name = '订单列表页-确认收货'
        self.wait_eleVisible(my_order_locator.confirm_receipt, model=name)
        self.click_element(my_order_locator.confirm_receipt, model=name)
        time.sleep(3)
        self.click_element(my_order_locator.confirm_button, model=name)

    # 订单详情页-立即付款/提醒发货/确认收货/评价页面跳转
    def detail_order_button2(self):
        name = '订单详情页-立即付款页面跳转'
        self.wait_eleVisible(my_order_locator.detail_order_button2, model=name)
        self.click_element(my_order_locator.detail_order_button2, model=name)

    # 校验评价页面跳转
    def check_evaluate(self):
        name = '订单详情页-评价页面跳转'
        ele = my_order_locator.check_evaluate
        return self.get_text(ele, model=name)

    def detail_order_button2_confirm(self):
        name = '订单详情页-立即付款/提醒发货/确认收货/评价页面跳转'
        self.wait_eleVisible(my_order_locator.detail_order_button2, model=name)
        self.click_element(my_order_locator.detail_order_button2, model=name)

    # 校验立即付款页面跳转
    def check_paying_now(self):
        name = '校验立即付款页面跳转'
        ele = my_order_locator.check_paying_now
        return self.get_text(ele, model=name)

    # 校验订单详情-申请退款页面跳转
    def check_order_refund(self):
        name = '校验订单详情-申请退款页面跳转'
        ele = my_order_locator.check_application_refund
        return self.get_text(ele, model=name)

    # 申请退款-不想要了
    def refund_order(self, refund_msg):
        name = '申请退款-不想要了'
        self.wait_eleVisible(my_order_locator.refund_reason, model=name)
        self.click_element(my_order_locator.refund_reason, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.select_refund_reason1, model=name)
        time.sleep(2)
        self.input_text(refund_msg, my_order_locator.refund_msg, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.refund_commit_button, model=name)

    # 申请退款-发货太慢了
    def refund_order2(self, refund_msg):
        name = '申请退款-发货太慢了'
        self.wait_eleVisible(my_order_locator.refund_reason, model=name)
        self.click_element(my_order_locator.refund_reason, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.select_refund_reason2, model=name)
        time.sleep(2)
        self.input_text(refund_msg, my_order_locator.refund_msg, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.refund_commit_button, model=name)

    # 校验已发货-退货申请页面跳转
    def check_return_order(self):
        name = '校验已发货-退货申请'
        ele = my_order_locator.check_application_return
        return self.get_text(ele, model=name)

    # 退货申请-未收到货退货
    def return_order_unreceived_goods(self, return_msg):
        name = '退货申请'

        self.wait_eleVisible(my_order_locator.return_type, model=name)
        self.click_element(my_order_locator.return_type, model=name)
        # 选择未收到货退货
        time.sleep(1)
        self.click_element(my_order_locator.unreceived_goods, model=name)
        # 选择退货原因
        time.sleep(1)
        self.click_element(my_order_locator.return_reason, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.return_reason2, model=name)
        # 输入退货留言
        time.sleep(1)
        self.input_text(return_msg, my_order_locator.return_msg, model=name)
        # 点击提交按钮
        time.sleep(1)
        self.click_element(my_order_locator.return_commit_button)

    # 退货申请-已收到货，退货-未选择退货物流
    def return_order_express_err(self, return_msg, return_no):
        name = '退货申请'

        self.wait_eleVisible(my_order_locator.return_type, model=name)
        self.click_element(my_order_locator.return_type, model=name)
        # 选择已收到货，退货
        time.sleep(1)
        self.click_element(my_order_locator.goods_received, model=name)
        # 选择退货原因
        time.sleep(1)
        self.click_element(my_order_locator.return_reason, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.return_reason2, model=name)
        # 输入退货留言
        time.sleep(1)
        self.input_text(return_msg, my_order_locator.return_msg, model=name)
        # 输入退货快递单号
        time.sleep(1)
        self.input_text(return_no, my_order_locator.return_sf_no, model=name)
        # 点击提交按钮
        time.sleep(1)
        self.click_element(my_order_locator.return_commit_button)

    # 退货申请-已收到货，退货-退货物流单号为空
    def return_order_express_success(self, return_msg, return_no):
        name = '退货申请'
        self.wait_eleVisible(my_order_locator.return_type, model=name)
        self.click_element(my_order_locator.return_type, model=name)
        # 选择已收到货，退货
        time.sleep(1)
        self.click_element(my_order_locator.goods_received, model=name)
        # 选择退货原因
        time.sleep(1)
        self.click_element(my_order_locator.return_reason, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.return_reason2, model=name)
        # 输入退货留言
        time.sleep(1)
        self.input_text(return_msg, my_order_locator.return_msg, model=name)
        # 选择顺丰快递
        time.sleep(1)
        self.click_element(my_order_locator.return_express, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.return_express_sf, model=name)
        # 输入退货快递单号
        time.sleep(1)
        self.input_text(return_no, my_order_locator.return_sf_no, model=name)
        # 点击提交按钮
        time.sleep(1)
        self.click_element(my_order_locator.return_commit_button)

    # 订单详情-已收货-评价页面跳转
    def return_order_evaluate(self):
        name = '评价'
        self.wait_eleVisible(my_order_locator.evaluate, model=name)
        self.click_element(my_order_locator.evaluate, model=name)

    # 评价-评价内容为空
    def evaluate_err(self, evaluate_msg):
        name = '评价内容为空'
        self.wait_eleVisible(my_order_locator.evaluate_msg, model=name)
        self.input_text(evaluate_msg, my_order_locator.evaluate_msg, model=name)
        time.sleep(1)
        evaluate = self.find_element(my_order_locator.commit_evaluate, model=name)
        evaluate.click()

    # 校验评价-评价内容为空
    def check_evaluate_err(self):
        name = '评价内容为空'
        ele = my_order_locator.evaluate_err
        return self.get_text(ele, model=name)
