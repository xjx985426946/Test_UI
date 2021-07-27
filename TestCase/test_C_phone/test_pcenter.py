import time
import pytest
from Common import common,logger
from TestDatas.C_phone import pcenter_data
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.returned_page import ReturnedPage
from PageObject.C_phone.couspon_page import CousponPage
from PageObject.C_phone.reward_page import RewardPage
from PageObject.C_phone.mylike_page import MylikePage
from PageObject.C_phone.personal_page import PersonalPage
import logging


'''
个人中心页面

1、  点击退货退款按钮，正确进入退货退款页面

2、 点击优惠券，正确进入优惠券页面

'''


@pytest.mark.usefixtures("login")
@pytest.mark.domes
@pytest.mark.production
class Testpcenter:
    '''用户中心页面'''

    @pytest.mark.smoke
    def test_returned(self,login):
        '''进入设置密码页面'''

        time.sleep(4)
        #点击退货退款按钮
        PcenterPage(login).click_set()

        #验证页面跳转正确
        try:
            assert login.current_url == pcenter_data.set_url['url']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="退货退款页面")

    @pytest.mark.smoke
    def test_cuspons(self, login):
        '''成功进入优惠券页面，页面信息展示正确'''

        time.sleep(4)
        # 点击优惠券
        PcenterPage(login).click_cuspon()

        # 验证页面跳转正确
        try:
            assert login.current_url == pcenter_data.url['url']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="优惠券页面")


    @pytest.mark.smoke
    def test_mylike(self,login):
        '''成功进入我的关注页面，喜欢商品展示正确'''

        time.sleep(4)

        #点击我的喜欢按钮
        PcenterPage(login).click_mylike()
        #验证页面跳转正确
        try:
            assert login.current_url == pcenter_data.like_url['like_url']
        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="我的喜欢页面")

    @pytest.mark.smoke
    def test_my(self,login):
        ''' 点击头像，进入个人设置页面，页面信息展示正确'''

        time.sleep(4)
        #点击我的
        PcenterPage(login).click_my()
        #验证页面跳转正确
        try:
            assert login.current_url == pcenter_data.address_url['url']

        except:
            logging.error("断言失败")
            common.save_screenShot(login, model_name="个人设置页面")

if __name__ == '__main__':
    pass
