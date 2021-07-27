import time
import pytest
from Common import common,logger
from TestDatas.C_phone import order_data
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.orderlist_page import OrderlistPage
import logging

@pytest.mark.usefixtures("login")
@pytest.mark.domes
@pytest.mark.production

class Testsearchorder:
    '''查询我的订单'''
    @pytest.mark.smoke
    def test_allorder(self,login):
        '''成功查询全部订单'''
        time.sleep(6)
        PcenterPage(login).click_order()
        try:
            assert OrderlistPage(login).get_ordertext() == order_data.order_success['check']
            logging.info("成功进入订单页面")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单查询页面")
            raise

    @pytest.mark.smoke
    def test_pending(self,login):
        '''成功查询待付款订单'''
        time.sleep(6)
        PcenterPage(login).click_order()
        OrderlistPage(login).click_pending()
        try:
            assert login.current_url == order_data.order_url[0]['pending']
            logging.info("成功查询待付款订单")
        except:
            logging.error("断言失败")
            logging.error(login.current_url)
            common.save_screenShot(login, model_name="订单查询页面")
            raise

    @pytest.mark.smoke
    def test_processing(self,login):
        '''成功查询待发货订单'''
        time.sleep(6)
        PcenterPage(login).click_order()
        OrderlistPage(login).click_processing()
        try:
            assert login.current_url == order_data.order_url[1]['processing']
            logging.info("成功查询待发货订单")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单查询页面")
            raise

    @pytest.mark.smoke
    def test_delivering(self,login):
        '''成功查询已发货订单'''
        time.sleep(6)
        PcenterPage(login).click_order()
        OrderlistPage(login).click_delivering()
        try:
            assert login.current_url == order_data.order_url[2]['delivering']
            logging.info("成功查询已发货订单")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单查询页面")
            raise

    @pytest.mark.smoke
    def test_completed(self,login):
        '''成功查询已收货订单'''
        time.sleep(6)
        PcenterPage(login).click_order()
        OrderlistPage(login).click_complete()
        try:
            assert login.current_url == order_data.order_url[3]['completed']
            logging.info("成功查询已发货订单")
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="订单查询页面")
            raise

if __name__ == '__main__':
    pass