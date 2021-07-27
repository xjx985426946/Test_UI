import time
import pytest
from Common import common,logger
from TestDatas.C_phone import pushorder_data
from PageObject.C_phone.productdetail_page import ProductdetailPage
from PageObject.C_phone.pushorder_page import PushorderPage
from PageObject.C_phone.pay_page import PayrPage
import logging
from other.api import Api

'''

送好友流程

1、成功送好友

2、

'''


@pytest.mark.usefixtures("login")
@pytest.mark.domes

class Testgivefriend:
    '''购买商品'''


    def setup_class(self):
        a = Api()
        cookies = a.f_login("13600000000", "e10adc3949ba59abbe56e057f20f883e").cookies
        # 登录v端
        access_token = a.v_login("13729542194", "e10adc3949ba59abbe56e057f20f883e").json()['result']['access_token']

        re = a.intbeecardacception(cookies, access_token)
        try:
            self.phone_url = re[1]
        except:
            logging.error("创建失败")

    @pytest.mark.smoke
    def test_successone(self,login):
        '''成功送好友'''
        time.sleep(4)

        #进入购买页面
        login.get(self.phone_url)

        #获取金额，提交订单页面验证金额是否正确
        amount = ProductdetailPage(login).get_amount()
        import re
        new_amount = re.sub("\D", "", amount.split(':')[0])
        time.sleep(2)
        #点击送好友按钮
        ProductdetailPage(login).click_friend()

        # time.sleep(5)
        #选择规格
        time.sleep(2)
        ProductdetailPage(login).click_standar()
        #确认购买
        ProductdetailPage(login).click_decide_botton()
        amout2 = PushorderPage(login).get_amount()
        new_amount2 = re.sub("\D", "", amount.split(':')[0])
        #判断金额是否正确
        try:
            assert new_amount2 == new_amount
            logging.info("金额正确")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="提交订单")
            raise
        #点击发票按钮
        PushorderPage(login).click_purchase()

        #输入发票信息
        PushorderPage(login).input_invoiceheader(pushorder_data.success_friend['invoice_hearder'])
        PushorderPage(login).input_invoice_phone(pushorder_data.success_friend['invoice_phone'])

        #输入留言信息
        PushorderPage(login).input_message(pushorder_data.success['message'])

        #填写提示口令
        PushorderPage(login).input_invitation(pushorder_data.success_friend['invitation'])
        #填写口令
        PushorderPage(login).input_command(pushorder_data.success_friend['comman'])

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




if __name__ == '__main__':
    pass
