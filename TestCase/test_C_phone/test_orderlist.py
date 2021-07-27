import time
import pytest
from Common import common,logger
from TestDatas.C_phone import order_data
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.orderlist_page import OrderlistPage
from PageObject.C_phone.pay_page import PayrPage
from PageObject.C_phone.orderdetail_page import OrderdetailPage
from PageObject.C_phone.applyrefund_page import ApplyrefundPage
from PageObject.C_phone.logistics_page import LogisticPage
import logging
from other.api import Api

'''
个人中心页面

1、进入订单页面，取消待付款订单，验证取消订单成功
2、进入订单页面，选择待付款订单，进行立即付款，验证成功进入付款页面
3、进入订单页面，选择第一条信息，进入详情页面，验证成功进入详情页面，支付金额展示正确
4、进入订单页面，进入待发货页面，选择第一条订单，申请退款
5、进入订单页面，进入待发货页面，提醒发货
6、待发货页面，送好友信息，暂定
7、进入订单页面，进入已收货页面，选择第一条订单，查看物流信息
8、进入订单页面，进入已收货页面，选择第一条订单，申请退货
进入订单页面，进入已收货页面，选择第一条订单，评价商品
9、已发货页面，暂定

'''


@pytest.mark.usefixtures("login")
@pytest.mark.domes

class Testorderlist:
    '''订单列表页面'''

    def setup_class(self):
        # 登录F端
        a = Api()
        a = Api()
        token_c = a.c_login("13729542194", "e10adc3949ba59abbe56e057f20f883e")
        print(a.commit_order(token_c))
    @pytest.mark.smoke
    def test_orderdetail(self,login):
        '''待付款页面查看订单详情'''
        time.sleep(4)
        # 点击待付款按钮，进入待付款页面
        PcenterPage(login).click_pending()
        #获取第一条商品支付总价钱
        allmoney = OrderlistPage(login).get_ordermoney()
        # import re
        # new_amount = re.sub("\D", "", allmoney.split(':')[0])
        new_amount = allmoney[1:]
        #点击商品进入商品详情
        OrderlistPage(login).click_orderdetail()

        #验证成功进入详情页面，金额正确
        try:

            assert OrderdetailPage(login).get_allmoney()[1:] == new_amount

        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单详情页面")

    @pytest.mark.smoke
    def test_payorder(self,login):
        '''待付款订单立即付款'''
        time.sleep(4)
        PcenterPage(login).click_pending()
        #点击付款按钮
        OrderlistPage(login).click_paybutton()
        #验证成功进入付款页面
        try:
            assert PayrPage(login).get_alipay() == order_data.pay_text['check_wei']
            assert PayrPage(login).get_wepay() == order_data.pay_text['check_ali']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单列表付款订单页面")

    @pytest.mark.smoke
    def test_cancelorder(self,login):
        '''订单列表成功取消订单'''

        time.sleep(4)
        #点击待付款按钮，进入待付款页面
        PcenterPage(login).click_pending()
        time.sleep(2)
        #取消订单
        OrderlistPage(login).click_ordercancel()
        #验证成功取消订单
        try:
            assert OrderlistPage(login).get_toast() == order_data.cancleorder['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单列表取消订单页面")

    @pytest.mark.smoke
    def test_applyrefund(self,login):
        '''申请退款'''
        time.sleep(4)
        # 点击待发货按钮，进入待发货页面
        PcenterPage(login).click_processing()
        #点击申请退款按钮
        OrderlistPage(login).click_apply_refund()
        #验证进入退款页面
        #点击退款原因、
        ApplyrefundPage(login).click_reson()
        time.sleep(2)
        #选择退款原因
        ApplyrefundPage(login).click_cancle()
        #点击提交按钮
        time.sleep(2)
        ApplyrefundPage(login).click_button()
        try:
            assert ApplyrefundPage(login).get_toast() == order_data.toast_text['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="申请退款页面")

    @pytest.mark.smoke
    def test_orderdetail(self,login):
        '''待付款页面查看订单详情'''
        time.sleep(4)
        # 点击待付款按钮，进入待付款页面
        PcenterPage(login).click_pending()
        #获取第一条商品支付总价钱
        allmoney = OrderlistPage(login).get_ordermoney()
        # import re
        # new_amount = re.sub("\D", "", allmoney.split(':')[0])
        new_amount = allmoney[1:]
        #点击商品进入商品详情
        OrderlistPage(login).click_orderdetail()

        #验证成功进入详情页面，金额正确
        try:

            assert OrderdetailPage(login).get_allmoney()[1:] == new_amount

        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单详情页面")

    @pytest.mark.smoke
    def test_payorder(self,login):
        '''待付款订单立即付款'''
        time.sleep(4)
        PcenterPage(login).click_pending()
        #点击付款按钮
        OrderlistPage(login).click_paybutton()
        #验证成功进入付款页面
        try:
            assert PayrPage(login).get_alipay() == order_data.pay_text['check_wei']
            assert PayrPage(login).get_wepay() == order_data.pay_text['check_ali']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单列表付款订单页面")

    @pytest.mark.smoke
    def test_cancelorder(self,login):
        '''订单列表成功取消订单'''

        time.sleep(4)
        #点击待付款按钮，进入待付款页面
        PcenterPage(login).click_pending()
        time.sleep(2)
        #取消订单
        OrderlistPage(login).click_ordercancel()
        #验证成功取消订单
        try:
            assert OrderlistPage(login).get_toast() == order_data.cancleorder['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单列表取消订单页面")

    @pytest.mark.smoke
    def test_applyrefund(self,login):
        '''申请退款'''
        time.sleep(4)
        # 点击待发货按钮，进入待发货页面
        PcenterPage(login).click_processing()
        #点击申请退款按钮
        OrderlistPage(login).click_apply_refund()
        #验证进入退款页面
        #点击退款原因、
        ApplyrefundPage(login).click_reson()
        time.sleep(2)
        #选择退款原因
        ApplyrefundPage(login).click_cancle()
        #点击提交按钮
        time.sleep(2)
        ApplyrefundPage(login).click_button()
        try:
            assert ApplyrefundPage(login).get_toast() == order_data.toast_text['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="申请退款页面")

    @pytest.mark.smoke
    def test_remindgoods(self,login):
        '''待发货信息，提醒发货'''
        time.sleep(4)
        # 点击待发货按钮，进入待发货页面
        PcenterPage(login).click_processing()
        #点击提醒发货按钮
        OrderlistPage(login).click_remind()
        #验证进入退款页面
        try:
            assert OrderlistPage(login).get_toast() == order_data.remind['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单列表页面")



    @pytest.mark.smoke
    def test_click_logistics(self,login):
        '''已收货订单,评价'''
        time.sleep(4)
        # 点击已发货按钮，进入已收货页面
        PcenterPage(login).click_completed()
        # 点击评价按钮
        OrderlistPage(login).click_evaluate()
        #评价
        OrderlistPage(login).do_evaluate(order_data.evalucate['detail'])
        try:
            assert OrderlistPage(login).get_toast() == order_data.evalucate['toast']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="评价页面")

    # def test_refundgood(self):
    #     '''已收货信息，进行退货'''
    #     pass

if __name__ == '__main__':
    pass
