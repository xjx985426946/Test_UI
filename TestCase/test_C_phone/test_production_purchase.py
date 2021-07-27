import time
import pytest
from Common import common,logger
from TestDatas.C_phone import pushorder_data
from PageObject.C_phone.productdetail_page import ProductdetailPage
from PageObject.C_phone.pushorder_page import PushorderPage
from PageObject.C_phone.pay_page import PayrPage
from PageObject.C_phone.orderlist_page import OrderlistPage
import logging
from other.api import Api
from Common import conf

'''

C端用户访问购买商品地址购买地址

1、成功购买商品  ，验证商品金额正确


2、购买多个商品

3、购买商品、下单不购买，订单页面查看此订单，数据展示正确

'''


@pytest.mark.usefixtures("login")


class Testpurchase:
    '''购买商品'''
    url = conf.url_c
    url = url + "customer/mobile/personal/orders?status=pending"
    phone_url = 'https://item.intbee.com/customer/item/18803/?uuid=5bea2cdf7663830006f140c2&platform_id=4'

    @pytest.mark.smoke
    @pytest.mark.production
    def test_successone(self,login):
        '''成功购买单件商品'''
        time.sleep(4)

        #进入购买页面
        login.get(self.phone_url)

        #获取金额，提交订单页面验证金额是否正确
        amount = ProductdetailPage(login).get_amount()
        import re
        new_amount = re.sub("\D", "", amount.split(':')[0])

        #点击购买按钮
        ProductdetailPage(login).click_purchase()
        # time.sleep(5)
        #选择规格
        time.sleep(2)
        ProductdetailPage(login).click_standar()
        #确认购买
        ProductdetailPage(login).click_decide_botton()
        amount2 = PushorderPage(login).get_amount()
        new_amount2 = re.sub("\D", "", amount2.split(':')[0])
        #判断金额是否正确
        try:
            assert new_amount2 == new_amount
            logging.info("金额正确")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="提交订单")
            raise
        #点击发票按钮
        time.sleep(4)
        PushorderPage(login).click_purchase()

        #输入发票信息
        PushorderPage(login).input_invoiceheader(pushorder_data.success['invoice_hearder'])
        PushorderPage(login).input_invoice_phone(pushorder_data.success['invoice_phone'])

        #输入留言信息
        PushorderPage(login).input_message(pushorder_data.success['message'])
        time.sleep(3)
        #点击提交订单按钮
        PushorderPage(login).click_button()

        #断言跳转页面正确
        try:
            assert PayrPage(login).get_alipay() == pushorder_data.success['check1']
            assert PayrPage(login).get_wepay() == pushorder_data.success['check2']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="支付页面")



    def test_successtwo(self, login):
        '''成功购买两件商品'''
        time.sleep(4)

        # 进入购买页面
        login.get(self.phone_url)

        # 点击购买按钮
        ProductdetailPage(login).click_purchase()
        # time.sleep(5)
        # 选择规格
        time.sleep(2)
        ProductdetailPage(login).click_standar()
        #增加购买商品
        ProductdetailPage(login).click_add()
        # 确认购买
        ProductdetailPage(login).click_decide_botton()
        time.sleep(4)
        # 点击发票按钮
        PushorderPage(login).click_purchase()

        # 输入发票信息
        PushorderPage(login).input_invoiceheader(pushorder_data.success['invoice_hearder'])
        PushorderPage(login).input_invoice_phone(pushorder_data.success['invoice_phone'])

        # 输入留言信息
        PushorderPage(login).input_message(pushorder_data.success['message'])
        time.sleep(3)
        # 点击提交订单按钮
        PushorderPage(login).click_button()

        # 断言跳转页面正确
        try:
            assert PayrPage(login).get_alipay() == pushorder_data.success['check1']
            assert PayrPage(login).get_wepay() == pushorder_data.success['check2']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="支付页面")

    @pytest.mark.smoke
    @pytest.mark.production
    def test_checkorderlist(self,login):
        '''用户下单后，订单列表正确显示为付款订单'''
        #进入订单页面
        time.sleep(4)
        login.get(self.url)
        import re
        new_amount = re.sub("\D", "", OrderlistPage(login).get_orderamount().split(':')[0])
        #验证第一条信息正确
        try:

            assert OrderlistPage(login).get_ordertitle() == pushorder_data.success_order['title']
            assert  new_amount == pushorder_data.success_order['amount']
        except:
            logging.error("购买进入订单失败")
            common.save_screenShot(login, model_name="订单页面")




if __name__ == '__main__':
    pass
