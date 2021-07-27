import time
import pytest
from Common import common,logger
from TestDatas.C_phone import productdetail_data
from PageObject.C_phone.productdetail_page import ProductdetailPage
from PageObject.C_phone.shop_page import ShopPage
import logging
from other.api import Api

'''

C端用户访问购买商品地址购买地址

1、将商品添加为喜欢
2、将商品设置为不喜欢
3、点击专柜进入用户专柜


'''


@pytest.mark.usefixtures("login")
@pytest.mark.production

class Testpurchase:
    '''商品详情页面的操作'''
    phone_url = 'https://item.intbee.com/customer/item/18803?uuid=5bea2cdf7663830006f140c2'
    @pytest.mark.parametrize("data", productdetail_data.toast)
    def test_addlike(self,login,data):
        '''将商品添加为喜欢/取消'''
        time.sleep(5)

        #进入购买页面
        login.get(self.phone_url)

        #点击喜欢按钮
        ProductdetailPage(login).click_like()

        #断言跳转页面正确
        try:
            assert ProductdetailPage(login).get_addtoast() == data['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="商品详情页面")

    @pytest.mark.smoke
    def test_contain(self,login):
        '''进入用户专柜'''
        time.sleep(4)

        # 进入购买页面
        login.get(self.phone_url)

        #点击专柜

        ProductdetailPage(login).click_shop()
        # 断言跳转页面正确
        try:
            assert ShopPage(login).get_shop() == productdetail_data.shop_text['shop_textcheck']
            assert ShopPage(login).get_decription() == productdetail_data.shop_text['shop_descriptcheck']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="专柜页面")

    @pytest.mark.smoke
    def test_server(self,login):
        '''商品详情页面查看客服信息'''
        time.sleep(4)
        # 进入购买页面
        login.get(self.phone_url)

        #点击客服按钮
        ProductdetailPage(login).click_server()

        #开始验证
        try:
            assert ProductdetailPage(login).get_serverphone() == productdetail_data.server['server_phone']
            assert ProductdetailPage(login).get_serverqq() == productdetail_data.server['server_qq']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="商品详情页面")

        ProductdetailPage(login).click_complte()




if __name__ == '__main__':
    pass
