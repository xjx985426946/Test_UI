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
@pytest.mark.domes

class Testpurchase:
    '''商品详情页面的操作'''

    def setup_class(self):
        a = Api()
        # token_c = a.v_login("13729542194", "e10adc3949ba59abbe56e057f20f883e")
        re = a.product(type='phone')

        try:
            self.phone_url = re
        except:
            logging.error("创建失败")

    @pytest.mark.smoke
    def test_addlike(self,login):
        '''将商品添加为喜欢'''
        time.sleep(5)

        #进入购买页面

        login.get(self.phone_url)
        time.sleep(2)
        #点击喜欢按钮
        ProductdetailPage(login).click_like()

        #断言跳转页面正确
        try:
            assert ProductdetailPage(login).get_addtoast() == productdetail_data.toast[0]['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="商品详情页面")

    @pytest.mark.smoke
    def test_notlike(self, login):
        '''将商品添加为取消喜欢'''
        time.sleep(5)

        # 进入购买页面
        login.get(self.phone_url)
        time.sleep(2)
        # 点击喜欢按钮
        ProductdetailPage(login).click_notlike()

        # 断言跳转页面正确
        try:
            assert ProductdetailPage(login).get_addtoast() == productdetail_data.toast[1]['check']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="商品详情页面")

    @pytest.mark.smoke
    def test_contain(self,login):
        '''进入用户专柜'''
        time.sleep(4)

        # 进入购买页面
        login.get(self.phone_url)

        time.sleep(2)
        #点击专柜

        ProductdetailPage(login).click_shop()
        # 断言跳转页面正确
        try:
            assert ShopPage(login).get_decription() == productdetail_data.shop_text['shop_descriptcheck']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="专柜页面")




if __name__ == '__main__':
    pass
