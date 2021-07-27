import time
import pytest
from Common import common
from TestDatas.V_app import shopper_data
import logging
from PageObject.V_app.shopper_page import LoginShopperPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestLoginShopper:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_success)
    def test_shop(self, data, app_page):
        '''小店页面跳转'''

        # 步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        logging.info("开始断言")

        # 验证-检查点
        time.sleep(2)
        try:
            assert LoginShopperPage(app_page).confirm_shopper() == data['check']
            logging.info("专柜页面跳转成功")
        except:
            print("小店页面跳转失败")
            common.save_screenShot(app_page, model_name="小店页面跳转失败")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_price)
    def test_shop_price_sort(self, data, app_page):
        '''销量排行'''

        # 步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).sort_sell()

        price1 = LoginShopperPage(app_page).confirm_price_1()

        price2 = LoginShopperPage(app_page).confirm_price_2()

        logging.info("开始断言")

        # 验证-检查点
        time.sleep(2)
        try:
            assert price1 > price2
            logging.info("销量排行成功")
        except:
            print("销量排行失败")
            common.save_screenShot(app_page, model_name="销量排行失败")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_price)
    def test_shop_reward_sort(self, data, app_page):
        '''可赚金额排序'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).sort_money()

        money1 = LoginShopperPage(app_page).product_detail_1()
        time.sleep(2)
        money2 = LoginShopperPage(app_page).product_detail_2()

        logging.info("开始断言")

        try:
            assert money1 > money2
            logging.info("可赚金额排序成功")

        except:
            print("断言失败")
            print("可赚金额排序失败")
            common.save_screenShot(app_page, model_name="可赚金额排序失败")
            raise


    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.create_inventory)
    def test_create_inventory(self, data, app_page):
        '''创建清单'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).create_inventory(data['title'], data['remark'])

        logging.info("开始断言")

        time.sleep(2)

        try:
            assert LoginShopperPage(app_page).check_create_inventory() == data['title']
            logging.info("创建清单成功")

        except:
            print("断言失败")
            print("创建清单失败")
            common.save_screenShot(app_page, model_name="创建清单失败")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.create_inventory_err)
    def test_create_inventory_title_err(self, data, app_page):
        '''创建清单-标题为空'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).create_inventory_title_err()

        logging.info("开始断言")

        try:
            assert LoginShopperPage(app_page).check_inventory_title_err() == data['check']
            logging.info("判断成功：创建清单-标题为空")

        except:
            print("断言失败")
            print("判断失败：创建清单-标题为空")
            common.save_screenShot(app_page, model_name="判断失败：创建清单-标题为空")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_null_create_inventory)
    def test_shop_null_create_inventory(self, data, app_page):
        '''小店为空-创建清单'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        logging.info("开始断言")

        try:
            assert LoginShopperPage(app_page).check_shop_null_create_inventory() == data['check']
            logging.info("判断成功：小店为空-创建清单")

        except:
            print("断言失败")
            print("判断失败：小店为空-创建清单")
            common.save_screenShot(app_page, model_name="判断失败：小店为空-创建清单")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.create_inventory)
    def test_del_inventory(self, data, app_page):
        '''删除清单'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).del_inventory()

        logging.info("开始断言")

        try:
            assert LoginShopperPage(app_page).check_create_inventory() != data['title']
            logging.info("判断成功：删除清单")

        except:
            print("断言失败")
            print("判断失败：删除清单")
            common.save_screenShot(app_page, model_name="判断失败：删除清单")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_set_name)
    def test_shop_set_name(self, data, app_page):
        '''更换小店昵称'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).shop_set_name(data['name'])

        logging.info("开始断言")

        try:
            assert LoginShopperPage(app_page).check_shop_name_change(data['name']) == data['name']
            logging.info("判断成功：更换小店昵称")

        except:
            print("断言失败")
            print("判断失败：更换小店昵称")
            common.save_screenShot(app_page, model_name="判断失败：更换小店昵称")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", shopper_data.shop_set_intro)
    def test_shop_set_intro(self, data, app_page):
        '''更换小店公告'''
        #步骤
        LoginShopperPage(app_page).login_shopper(data['username'], data['password'])

        LoginShopperPage(app_page).shop_set_intro(data['intro'])

        logging.info("开始断言")

        try:
            assert LoginShopperPage(app_page).check_shop_set_intro(data['intro']) == data['intro']
            logging.info("判断成功：更换小店公告")

        except:
            print("断言失败")
            print("判断失败：更换小店公告")
            common.save_screenShot(app_page, model_name="判断失败：更换小店公告")
            raise

if __name__ == '__main__':
    pass