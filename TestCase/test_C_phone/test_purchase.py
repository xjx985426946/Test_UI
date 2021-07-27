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
@pytest.mark.domes

class Testpurchase:
    '''购买商品'''
    url = conf.url_c
    url = url + "customer/mobile/personal/orders?status=pending"
    def setup_class(self):
        a = Api()
        # token_c = a.v_login("13729542194", "e10adc3949ba59abbe56e057f20f883e")
        re = a.product(type='phone')

        try:
            self.phone_url = re
        except:
            logging.error("创建失败")


    @pytest.mark.smoke
    def test_successone(self,login):
        '''成功购买单件商品'''
        time.sleep(4)

        #进入购买页面
        login.get(self.phone_url)

        #获取金额，提交订单页面验证金额是否正确
        amount = ProductdetailPage(login).get_amount()
        new_amount = amount[1:]

        #点击购买按钮
        ProductdetailPage(login).click_purchase()
        # time.sleep(5)
        #选择规格
        # time.sleep(2)
        # ProductdetailPage(login).click_standar()
        #确认购买
        time.sleep(2)
        ProductdetailPage(login).click_decide_botton()
        amout2 = PushorderPage(login).get_amount()
        new_amount2 = amout2[1:]
        #判断金额是否正确
        try:
            assert new_amount2 == new_amount
            logging.info("金额正确")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="提交订单")
            raise

        #取消使用优惠券
        time.sleep(2)
        PushorderPage(login).click_couponse()

        time.sleep(2)
        #点击发票按钮
        PushorderPage(login).click_purchase()

        #输入发票信息
        PushorderPage(login).input_invoiceheader(pushorder_data.success['invoice_hearder'])
        PushorderPage(login).input_invoice_phone(pushorder_data.success['invoice_phone'],pushorder_data.success['email'])


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
        time.sleep(2)
        # 点击购买按钮
        ProductdetailPage(login).click_purchase()

        time.sleep(2)
        #增加购买商品
        ProductdetailPage(login).click_add()
        # 确认购买
        ProductdetailPage(login).click_decide_botton()

        time.sleep(2)
        PushorderPage(login).click_couponse()

        time.sleep(2)
        # 点击发票按钮
        PushorderPage(login).click_purchase()

        # 输入发票信息
        PushorderPage(login).input_invoiceheader(pushorder_data.success['invoice_hearder'])
        PushorderPage(login).input_invoice_phone(pushorder_data.success['invoice_phone'],
                                                 pushorder_data.success['email'])

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






if __name__ == '__main__':
    pass
