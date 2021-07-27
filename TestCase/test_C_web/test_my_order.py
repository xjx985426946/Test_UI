import time
import pytest
from Common import common
from TestDatas.C_web import order_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_web.order_page import OrderPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestMyOrder:

    # 登录成功-我的订单页面
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.login_success)
    def test_login_success(self, data, web_page):
        '''登录成功-我的订单页面'''
        time.sleep(2)
        #步骤
        OrderPage(web_page).login(data['username'], data['code'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert OrderPage(web_page).login_success() == data['check']
            logging.info("登录成功-我的订单页面")
        except:
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录成功-我的订单页面")
            raise

    # 待付款订单列表页跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.wait_pay)
    def test_wait_pay(self, data, web_page):
        '''订单列表-待付款订单列表页跳转'''
        # 步骤-登录
        OrderPage(web_page).login(data['username'], data['code'])
        # 步骤-待付款订单列表页跳转
        time.sleep(5)
        OrderPage(web_page).wait_pay()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_jump() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待付款订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="待付款订单列表页跳转")
            raise

    # 待发货订单列表页跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.wait_ship_order)
    def test_wait_ship_order(self, data, web_page):
        '''订单列表-待发货订单列表页跳转 '''
        # 步骤-登录
        OrderPage(web_page).login(data['username'], data['code'])
        # 步骤-待发货订单列表页跳转
        time.sleep(5)
        OrderPage(web_page).wait_ship()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_jump() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="待发货订单列表页跳转")
            raise

    # 已发货订单列表页跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.shipped_order)
    def test_shipped_order(self, data, web_page):
        '''订单列表-已发货订单列表页跳转 '''
        # 步骤-已发货订单列表页跳转
        OrderPage(web_page).login(data['username'], data['code'])
        # 步骤-已发货订单列表页跳转
        time.sleep(5)
        OrderPage(web_page).shipped_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_jump() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单列表页跳转")
            raise

    # 已收货订单列表页跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.received_order)
    def test_received_order(self, data, web_page):
        '''订单列表-已收货订单列表页跳转 '''
        # 步骤-登录
        OrderPage(web_page).login(data['username'], data['code'])
        # 步骤-已收货订单列表页跳转
        time.sleep(5)
        OrderPage(web_page).received_order()
        time.sleep(5)
        logging.info("开始断言")


        try:
            assert OrderPage(web_page).check_order_jump() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="已收货订单列表页跳转")
            raise

    # 查看订单详情-待付款订单
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.wait_pay)
    def test_wait_pay_detail(self, data, web_page):
        '''订单列表-待付款订单列表页跳转'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待付款订单列表页跳转
        OrderPage(web_page).wait_pay()
        time.sleep(3)
        # 步骤3-点击查看详情
        OrderPage(web_page).detail_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_detail_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待付款订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="待付款订单列表页跳转")
            raise

    # 查看订单详情-待发货订单
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.wait_ship_order)
    def test_wait_ship_order_detail(self, data, web_page):
        '''订单列表-待发货订单列表页跳转'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-点击查看详情
        OrderPage(web_page).detail_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_detail_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="待发货订单列表页跳转")
            raise

    # 查看订单详情-已发货订单
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.shipped_order)
    def test_shipped_order_detail(self, data, web_page):
        '''订单列表-已发货订单列表页跳转'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-点击查看详情
        OrderPage(web_page).detail_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_detail_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单列表页跳转")
            raise

    # 查看订单详情-已收货订单
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.received_order)
    def test_received_order_detail(self, data, web_page):
        '''订单列表-已收货订单列表页跳转'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-点击查看详情
        OrderPage(web_page).detail_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_detail_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单列表页跳转失败")
            common.save_screenShot(web_page, model_name="已收货订单列表页跳转")
            raise

    # 订单列表-待付款订单-立即付款跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.check_now_pay)
    def test_now_pay(self, data, web_page):
        '''订单列表-待付款订单-立即付款跳转'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待付款订单列表页跳转
        OrderPage(web_page).wait_pay()
        time.sleep(3)
        # 步骤3-点击立即付款
        OrderPage(web_page).order_list_button2()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_paying_now() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("订单列表-待付款订单-立即付款跳转失败")
            common.save_screenShot(web_page, model_name="订单列表-待付款订单-立即付款")
            raise

    # 订单列表-待发货订单-提醒发货
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.remind_ship)
    def test_order_list_remind_ship(self, data, web_page):
        '''订单列表-待发货订单-提醒发货'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-点击提醒发货
        OrderPage(web_page).order_list_button2()
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("订单列表-待发货订单-提醒发货失败")
            common.save_screenShot(web_page, model_name="订单列表-待发货订单-提醒发货")
            raise

    # 订单列表-已发货订单-查看物流
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.order_logistics)
    def test_order_list_logistics(self, data, web_page):
        '''订单列表-已发货订单-查看物流'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-点击查看物流
        OrderPage(web_page).order_list_button2()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_logistics() == data['check']
            logging.info("断言成功")

        except:
            logging.error("断言失败")
            logging.info("订单列表-已发货订单-查看物流失败")
            common.save_screenShot(web_page, model_name="订单列表-已发货订单-查看物流")
            raise

    # 订单列表-已发货订单-确认收货
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.confirm_receipt)
    def test_order_list_confirm_receipt(self, data, web_page):
        '''订单列表-已发货订单-确认收货'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-点击确认收货
        OrderPage(web_page).order_list_confirm_receipt()
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("订单列表-已发货订单-确认收货失败")
            common.save_screenShot(web_page, model_name="订单列表-已发货订单-确认收货")
            raise

# 订单列表-已收货订单-查看物流
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.order_logistics)
    def test_order_list_logistics(self, data, web_page):
        '''订单列表-已收货订单-查看物流'''
        # 步骤2-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-点击查看物流
        OrderPage(web_page).order_list_button2()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_logistics() == data['check']
            logging.info("断言成功")

        except:
            logging.error("断言失败")
            logging.info("订单列表-已收货订单-查看物流失败")
            common.save_screenShot(web_page, model_name="订单列表-已收货订单-查看物流")
            raise

    # 订单详情-待付款订单-取消订单
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.cancel_order)
    def test_order_detail_cancel(self, data, web_page):
        '''订单详情-待付款订单-取消订单'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待付款订单列表页跳转
        OrderPage(web_page).wait_pay()
        time.sleep(3)
        # 步骤3-待付款订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待付款订单详情页-取消订单
        OrderPage(web_page).cancel_order()
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-申请退款失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-申请退款")
            raise

    # 订单详情-待付款订单-立即付款
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.check_now_pay)
    def test_order_detail_paying(self, data, web_page):
        '''订单详情-待付款订单-立即付款'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待付款订单列表页跳转
        OrderPage(web_page).wait_pay()
        time.sleep(3)
        # 步骤3-待付款订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待付款订单详情页-立即付款跳转
        OrderPage(web_page).detail_order_button2()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_paying_now() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-申请退款失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-申请退款")
            raise

    # 订单详情-待发货订单-申请退款跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.application_refund)
    def test_order_detail_application_refund1(self, data, web_page):
        '''待发货订单-订单详情-申请退款'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-待发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待发货订单详情页-申请退款跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_refund() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-申请退款跳转失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-申请退款跳转")
            raise

    # 订单详情-待发货订单-申请退款-不想要了
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.application_refund_success)
    def test_order_detail_application_refund2(self, data, web_page):
        '''待发货订单-订单详情-申请退款-不想要了'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-待发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待发货订单详情页-申请退款跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-申请退款-不想要了
        OrderPage(web_page).refund_order(data['refund_msg'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-申请退款-不想要了失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-申请退款-不想要了")
            raise

    # 订单详情-待发货订单-申请退款-不想要了
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.application_refund_success)
    def test_order_detail_application_refund3(self, data, web_page):
        '''待发货订单-订单详情-申请退款-不想要了'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-待发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待发货订单详情页-申请退款跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-申请退款-不想要了
        OrderPage(web_page).refund_order2(data['refund_msg'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-申请退款-不想要了失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-申请退款-不想要了")
            raise

    # 订单详情-待发货订单-提醒发货
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.remind_ship)
    def test_order_detail_remind_ship(self, data, web_page):
        '''待发货订单-订单详情-提醒发货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-待发货订单列表页跳转
        OrderPage(web_page).wait_ship()
        time.sleep(3)
        # 步骤3-待发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-待发货订单详情页-提醒发货
        OrderPage(web_page).detail_order_button2()
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("待发货订单-订单详情-提醒发货失败")
            common.save_screenShot(web_page, model_name="待发货订单-订单详情-提醒发货")
            raise

    # 订单详情-已发货订单-退货页面跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_order)
    def test_detail_shipped_order_return(self, data, web_page):
        '''订单详情-已发货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_return_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已发货订单-已收到货退货-快递为空
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_err)
    def test_detail_shipped_order_return_err1(self, data, web_page):
        '''订单详情-已发货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-退货页面-不选择退货快递
        OrderPage(web_page).return_order_express_err(data['return_msg'], data['return_no'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已发货订单-已收到货退货-快递为空
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_err2)
    def test_detail_shipped_order_return_err2(self, data, web_page):
        '''订单详情-已发货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-退货页面-退货单号为空
        OrderPage(web_page).return_order_express_success(data['return_msg'], data['return_no'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已发货订单-已收到货退货-申请成功
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_success)
    def test_detail_shipped_order_return_success(self, data, web_page):
        '''订单详情-已发货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-退货页面-退货单号为空
        OrderPage(web_page).return_order_express_success(data['return_msg'], data['return_no'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已发货订单-未收到货退货-申请成功
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_unreceived_success)
    def test_detail_shipped_order_return_success(self, data, web_page):
        '''订单详情-已发货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(3)
        # 步骤5-退货页面-退货单号为空
        OrderPage(web_page).return_order_unreceived_goods(data['return_msg'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已发货订单-确认收货
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.confirm_receipt)
    def test_order_detail_confirm_receipt(self, data, web_page):
        '''待发货订单-订单详情-确认收货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已发货订单列表页跳转
        OrderPage(web_page).shipped_order()
        time.sleep(3)
        # 步骤3-已发货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已发货订单详情页-确认收货
        OrderPage(web_page).order_list_confirm_receipt()
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已发货订单-订单详情-确认收货失败")
            common.save_screenShot(web_page, model_name="已发货订单-订单详情-确认收货")
            raise

    # 订单详情-已收货订单-退货页面跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.return_order)
    def test_order_detail_received_order_return(self, data, web_page):
        '''订单详情-已收货订单-退货'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-已收货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已收货订单详情页-退货页面跳转
        OrderPage(web_page).return_refund_order()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_return_order() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单-订单详情-退货页面跳转失败")
            common.save_screenShot(web_page, model_name="已收货订单-订单详情-退货页面跳转")
            raise

    # 订单详情-已收货订单-评价页面跳转
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.detail_evaluate)
    def test_order_detail_evaluate(self, data, web_page):
        '''订单详情-已发货订单-评价页面跳转'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-已收货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已收货订单详情页-评价
        OrderPage(web_page).detail_order_button2()
        time.sleep(5)
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_evaluate() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单-订单详情-评价页面跳转失败")
            common.save_screenShot(web_page, model_name="已收货订单-订单详情-评价页面跳转")
            raise

    # 订单详情-已收货订单-评价页面
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.evaluate_err)
    def test_order_detail_evaluate_err(self, data, web_page):
        '''订单详情-已发货订单-评价页面'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-已收货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已收货订单详情页-评价
        OrderPage(web_page).detail_order_button2()
        time.sleep(3)
        # 步骤5-评价页面-评价内容为空/评价成功
        OrderPage(web_page).evaluate_err(data['evaluate_msg'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_evaluate_err() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单-订单详情-评价页面-评价失败")
            common.save_screenShot(web_page, model_name="已收货订单-订单详情-评价页面")
            raise

    # 订单详情-已收货订单-评价页面
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", order_data.evaluate_success)
    def test_order_detail_evaluate_success(self, data, web_page):
        '''订单详情-已发货订单-评价页面'''
        # 步骤1-登录
        OrderPage(web_page).login(data['username'], data['code'])
        time.sleep(5)
        # 步骤2-已收货订单列表页跳转
        OrderPage(web_page).received_order()
        time.sleep(3)
        # 步骤3-已收货订单详情页跳转
        OrderPage(web_page).detail_order()
        time.sleep(3)
        # 步骤4-已收货订单详情页-评价
        OrderPage(web_page).detail_order_button2()
        time.sleep(3)
        # 步骤5-评价页面-评价内容为空/评价成功
        OrderPage(web_page).evaluate_err(data['evaluate_msg'])
        logging.info("开始断言")

        try:
            assert OrderPage(web_page).check_order_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("已收货订单-订单详情-评价页面-评价失败")
            common.save_screenShot(web_page, model_name="已收货订单-订单详情-评价页面")
            raise

if __name__ == '__main__':
    pass