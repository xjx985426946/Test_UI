from PageLocators.C_phone import orderlist_locator
from Common.basepage import BasePage
from TestDatas.C_phone import order_data

class OrderlistPage(BasePage):

    name = '订单页面'

    #点击待付款按钮
    def click_pending(self):
        self.click_element(orderlist_locator.pending_order, wait_ele='presence', model=self.name)  #没有点击之前元素是不可见的  所以一直会点击不到，这里不能等待元素可见，要等待元素出现

    #点击待发货按钮
    def click_processing(self):

        self.click_element(orderlist_locator.processing_order, wait_ele='presence', model=self.name)

    #点击已发货按钮
    def click_delivering(self):
       self.click_element(orderlist_locator.delivering_order, wait_ele='presence', model=self.name)

    #点击已收货按钮
    def click_complete(self):
        self.click_element(orderlist_locator.complete_order, wait_ele='presence', model=self.name)

    #获取页面订单列表文本
    def get_ordertext(self):
        return self.get_text(orderlist_locator.order_text, wait_ele='presence', model=self.name)

    #关闭提示弹窗
    def close_float(self):
        pass

    #获取待付款第一条订单商品titile
    def get_ordertitle(self):
        return self.get_text(orderlist_locator.title,model=self.name)

    #获取第一条订单商品单价
    def get_orderamount(self):
        return self.get_text(orderlist_locator.amount,model=self.name)

    #获取第一条订单支付总价钱
    def get_ordermoney(self):
        return self.get_text(orderlist_locator.all_money,model=self.name)

    #点击待付款第一条订单的取消按钮
    def click_ordercancel(self):
        self.click_element(orderlist_locator.cancel_order,model=self.name)

    #点击带付款第一条待付款的立即付款按钮
    def click_paybutton(self):
        self.click_element(orderlist_locator.pay_button,model=self.name)

    #获取待付款页面第一条订单订单状态
    def get_status(self):
        return self.get_text(orderlist_locator.status,model=self.name)

    #点击第一条订单申请退款按钮
    def click_apply_refund(self):
        self.click_element(orderlist_locator.apply_refund,model=self.name)

    #点击第一条订单的提醒发货按钮
    def click_remind(self):
        self.click_element(orderlist_locator.reminder_shipment,model=self.name)

    #点击第一条订单查看物流按钮
    def click_logistics(self):
        self.click_element(orderlist_locator.logistics,model=self.name)

    #点击第一条订单退货按钮
    def click_returngoods(self):
        self.click_element(orderlist_locator.return_goods,model=self.name)

    #点击评价按钮
    def click_evaluate(self):
        self.click_element(orderlist_locator.evaluate,model=self.name)

    #获取toast文本
    def get_toast(self):
        return self.get_text(orderlist_locator.toast_text,model=self.name)

    #点击第一条信息详情
    def click_orderdetail(self):
        self.click_element(orderlist_locator.detail,model=self.name)

    #评价商品
    def do_evaluate(self,detail):
        self.input_text(detail,orderlist_locator.evaluate_detail)
        self.click_element(orderlist_locator.evaluate_button)




