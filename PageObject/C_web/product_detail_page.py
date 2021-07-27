from PageLocators.C_web import my_order_locator
from Common.basepage import BasePage
import time
class ProductDetailPage(BasePage):

    def login_product_detail(self, username, code):
        name = '登录页面_登录操作_订单列表跳转商品详情'
        # 输入用户名
        self.wait_eleVisible(my_order_locator.user_input, model=name)
        self.input_text(username, my_order_locator.user_input, model=name)
        # 输入密码
        self.input_text(code, my_order_locator.code_input, model=name)
        # 点击登录按钮
        self.click_element(my_order_locator.button, model=name)
        # 跳转商品详情页面
        time.sleep(5)
        self.wait_eleVisible(my_order_locator.order_list_product_detail, model=name)
        self.click_element(my_order_locator.order_list_product_detail, model=name)

    # 校验订单列表页跳转商品详情页
    def check_product_detail(self):
        name = "校验订单列表页跳转商品详情页"
        ele = my_order_locator.check_product_detail
        return self.get_text(ele, model=name)

    # 校验订单列表页跳转商品详情页-商品详情页页商品名称
    def product_detail_product_name(self):
        name = "校验订单列表页跳转商品详情页"
        self.wait_eleVisible(my_order_locator.product_detail_name)
        ele = my_order_locator.product_detail_name
        return self.get_text(ele, model=name)

    # 商品详情-点击我的喜欢
    def my_like(self):
        name = "商品详情-点击我的喜欢"
        self.wait_eleVisible(my_order_locator.product_detail_like, model=name)
        self.click_element(my_order_locator.product_detail_like, model=name)

    # 商品详情-领取优惠券
    def get_coupon(self):
        name = "商品详情-领取优惠券"
        self.wait_eleVisible(my_order_locator.get_coupons, model=name)
        self.click_element(my_order_locator.get_coupons, model=name)

    # 商品详情-举报
    def report(self):
        name = "商品详情-举报"
        self.wait_eleVisible(my_order_locator.report, model=name)
        self.click_element(my_order_locator.report, model=name)

    # 校验商品详情-举报跳转
    def check_report(self):
        name = "校验商品详情-举报跳转"
        report = my_order_locator.check_report
        return self.get_text(report, model=name)

    # 举报页面-点击举报类型
    def report_type(self):
        name = '举报页面-举报类型'
        self.wait_eleVisible(my_order_locator.report_type, model=name)
        self.click_element(my_order_locator.report_type, model=name)

    # 举报页面-提交举报
    def report_success(self, report_msg):
        name = '举报页面-举报'
        self.wait_eleVisible(my_order_locator.report_msg, model=name)
        self.input_text(report_msg, my_order_locator.report_msg, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.commit, model=name)

    # 举报页面-点击获取帮助
    def report_help(self):
        name = '举报页面-获取帮助'
        self.wait_eleVisible(my_order_locator.report_help, model=name)
        self.click_element(my_order_locator.report_help, model=name)

    # 校验举报页面-获取帮助页面跳转:知识产权侵权投诉处理程序
    def check_report_help(self):
        name = '校验举报页面-获取帮助页面跳转'
        report_help = my_order_locator.check_report_help
        return self.get_text(report_help, model=name)

    # 商品详情-选择规格
    def standards(self):
        name = "商品详情-选择规格"
        self.wait_eleVisible(my_order_locator.standards, model=name)
        self.click_element(my_order_locator.standards, model=name)

    # 商品详情-点击立即购买
    def buying(self):
        name = "商品详情-立即购买"
        self.wait_eleVisible(my_order_locator.buying, model=name)
        self.click_element(my_order_locator.buying, model=name)

    # 商品详情-点击去结算
    def settle(self):
        name = "商品详情-立即购买"
        self.wait_eleVisible(my_order_locator.settle, model=name)
        self.click_element(my_order_locator.settle, model=name)

    # 校验商品详情-点击去结算跳转
    def check_settle(self):
        name = "校验商品详情-点击去结算跳转"
        address = my_order_locator.address
        return self.get_text(address, model=name)

    # 提交订单-新增收货地址-无所在地区
    def order_commit_address_err(self, receiver_name, receiver_mobile):
        name = "商品详情-提交订单"
        self.wait_eleVisible(my_order_locator.address, model=name)
        self.click_element(my_order_locator.address, model=name)
        time.sleep(1)
        self.input_text(receiver_name, my_order_locator.receiver_name, model=name)
        time.sleep(1)
        self.input_text(receiver_mobile, my_order_locator.receiver_mobile, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.save_button, model=name)

    # 提交订单-新增收货地址
    def order_commit_address_success(self, receiver_name, receiver_mobile, detail_address):
        name = "商品详情-提交订单"
        self.wait_eleVisible(my_order_locator.address, model=name)
        self.click_element(my_order_locator.address, model=name)
        time.sleep(1)
        self.input_text(receiver_name, my_order_locator.receiver_name, model=name)
        time.sleep(1)
        self.input_text(receiver_mobile, my_order_locator.receiver_mobile, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.location_name, model=name)
        self.click_element(my_order_locator.provincial, model=name)
        self.click_element(my_order_locator.urban, model=name)
        self.click_element(my_order_locator.areas, model=name)
        time.sleep(1)
        self.input_text(detail_address, my_order_locator.detail_address, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.set_default_address, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.save_button, model=name)

    # 商品详情-提交订单-无优惠券-纸质发票
    def order_commit_paper_invoice(self, invoice_name, invoice_no):
        name = "商品详情-提交订单-无优惠券-纸质发票"
        self.wait_eleVisible(my_order_locator.not_coupon, model=name)
        self.click_element(my_order_locator.not_coupon, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.invoice, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.paper_invoice, model=name)
        time.sleep(1)
        self.input_text(invoice_name, my_order_locator.invoice_name, model=name)
        time.sleep(1)
        self.input_text(invoice_no, my_order_locator.invoice_no, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.invoice_commit, model=name)

    # 商品详情-提交订单-无优惠券-电子发票
    def order_commit_electronic_invoice(self, invoice_name, invoice_no, invoice_emali):
        name = "商品详情-提交订单-无优惠券-电子发票"
        self.wait_eleVisible(my_order_locator.not_coupon, model=name)
        self.click_element(my_order_locator.not_coupon, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.invoice, model=name)
        time.sleep(2)
        self.click_element(my_order_locator.electronic_invoice, model=name)
        time.sleep(1)
        self.input_text(invoice_name, my_order_locator.invoice_name, model=name)
        time.sleep(1)
        self.input_text(invoice_no, my_order_locator.invoice_no, model=name)
        time.sleep(1)
        self.input_text(invoice_emali, my_order_locator.invoice_email, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.invoice_commit, model=name)

    # 商品详情-提交订单-无优惠券-留言
    def order_commit_remarks(self, remarks):
        name = "商品详情-提交订单-无优惠券-无发票"
        self.wait_eleVisible(my_order_locator.not_coupon, model=name)
        self.click_element(my_order_locator.not_coupon, model=name)
        time.sleep(1)
        self.input_text(remarks, my_order_locator.remarks, model=name)
        time.sleep(1)
        self.click_element(my_order_locator.order_commit, model=name)

    # 校验纸质发票
    def check_paper_invoice(self):
        name = "校验纸质发票"
        self.wait_eleVisible(my_order_locator.check_paper_invoice, model=name)
        address_success = my_order_locator.check_paper_invoice
        return self.get_text(address_success, model=name)

    # 校验电子发票
    def check_electronic_invoice(self):
        name = "校验电子发票"
        self.wait_eleVisible(my_order_locator.check_electronic_invoice, model=name)
        address_success = my_order_locator.check_electronic_invoice
        return self.get_text(address_success, model=name)

    # 校验商品详情-提交订单跳转
    def check_order_commit(self):
        name = "校验商品详情-提交订单跳转"
        self.wait_eleVisible(my_order_locator.check_paying_now, model=name)
        check_paying_now = my_order_locator.check_paying_now
        return self.get_text(check_paying_now, model=name)

    # 校验商品详情-新增收货地址成功
    def check_address_success(self):
        name = "校验商品详情-新增收货地址成功"
        self.wait_eleVisible(my_order_locator.address_success, model=name)
        address_success = my_order_locator.address_success
        return self.get_text(address_success, model=name)

    # 校验/该商品已成功添加到我的喜欢列表！/你已经取消收藏该商品！/领取成功/请先选择规格/收货人不能为空/请输入正确的手机号码/详细地址不能为空/请选择所在地址
    def check_msg(self):
        name = "校验错误弹窗"
        self.wait_eleVisible(my_order_locator.check_msg, model=name)
        msg = my_order_locator.check_msg
        return self.get_text(msg, model=name)

    # 校验/请填写收货口令/请填写口令提示/请选择举报类型/举报详细内容不少于20字/提交成功，我们将尽快处理！感谢您的监督
    def check_toast(self):
        name = "校验错误弹窗"
        self.wait_eleVisible(my_order_locator.evaluate_err, model=name)
        toast = my_order_locator.evaluate_err
        return self.get_text(toast, model=name)




