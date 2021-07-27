import time
import pytest
from Common import common
from TestDatas.C_web import address_manage_data
import logging
from PageObject.C_web.address_page import AddressPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestAddressManage:

    # 成功登录-跳转地址管理页面
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.login_success)
    def test_login_success(self, data, web_page):
        '''成功登录'''
        time.sleep(2)
        #步骤
        AddressPage(web_page).login(data['username'], data['code'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert AddressPage(web_page).login_success() == data['check']
            assert 1==1
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.add_address_err)
    def test_add_address_err(self, data, web_page):
        '''判断地址收货人姓名为空/收货人手机号错误/详细地址为空'''
        # 步骤 登录
        AddressPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(3)

        # 新增地址
        AddressPage(web_page).add_address(data['receiver_name'], data['receiver_mobile'], data['detail_address'])

        try:
            assert AddressPage(web_page).add_address_check() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.add_address_success)
    def test_add_address_success(self, data, web_page):
        '''新增地址成功'''
        # 步骤
        AddressPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(3)

        # 新增地址
        AddressPage(web_page).add_address(data['receiver_name'], data['receiver_mobile'], data['detail_address'])

        time.sleep(5)
        try:
            assert AddressPage(web_page).default_address_check() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("新增地址失败")
            common.save_screenShot(web_page, model_name="地址管理页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.edit_address_success)
    def test_edit_address(self, data, web_page):
        '''编辑地址'''
        # 步骤
        AddressPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(3)

        # 编辑地址
        AddressPage(web_page).edit_address(data['receiver_name'])
        time.sleep(3)

        try:
            assert AddressPage(web_page).default_address_check() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("编辑地址失败")
            common.save_screenShot(web_page, model_name="地址管理页面")
            raise


    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.delete_address_success)
    def test_delete_address(self, data, web_page):
        '''删除地址成功'''
        # 步骤 登录并跳转地址管理页面
        AddressPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(3)

        # 删除地址
        AddressPage(web_page).delete_address()
        time.sleep(2)

        try:
            assert AddressPage(web_page).check_delete_address() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("删除地址失败")
            common.save_screenShot(web_page, model_name="地址管理页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", address_manage_data.set_default_address)
    def test_set_default_address(self, data, web_page):
        '''设为默认地址'''
        # 步骤 登录并跳转地址管理页面
        AddressPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(3)
        # 设为默认地址
        AddressPage(web_page).set_default_address()
        time.sleep(2)
        try:
            assert AddressPage(web_page).check_set_default_address() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("设为默认地址失败")
            common.save_screenShot(web_page, model_name="地址管理页面")
            raise

if __name__ == '__main__':
    pass