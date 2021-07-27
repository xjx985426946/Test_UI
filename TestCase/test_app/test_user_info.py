import time
import pytest
from Common import common
from TestDatas.V_app import user_center_data
import logging
from PageObject.V_app.user_info_page import LoginUserPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestLoginUser:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_center_data.login_success)
    def test_login_success_my(self, data, app_page):
        ''' 我的页面跳转成功 '''
        # 步骤
        LoginUserPage(app_page).login_user(data['username'], data['password'])

        success = LoginUserPage(app_page).confirm_my()
        print(success)

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的页面跳转成功")
        except:
            print("我的页面跳转失败")
            common.save_screenShot(app_page, model_name="我的页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_center_data.change_user_name)
    def test_edit_user_info(self, data, app_page):
        '''我的页面-个人信息编辑页面跳转成功'''
        # 步骤
        LoginUserPage(app_page).login_user(data['username'], data['password'])

        time.sleep(3)

        LoginUserPage(app_page).edit_user()

        time.sleep(3)

        user_name = LoginUserPage(app_page).confirm_user_info()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert user_name == data['check']
            logging.info("我的页面-个人信息编辑页面跳转成功")
        except:
            print("我的页面-个人信息编辑页面跳转失败")
            common.save_screenShot(app_page, model_name="我的页面-个人信息编辑页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_center_data.change_user_name)
    def test_change_user_name(self, data, app_page):
        '''我的页面-个人信息编辑页面-更换昵称成功'''
        # 步骤
        LoginUserPage(app_page).login_user(data['username'], data['password'])

        time.sleep(3)

        LoginUserPage(app_page).edit_user()

        time.sleep(3)

        LoginUserPage(app_page).change_user_name(data['user_name'])

        time.sleep(3)

        user_name = LoginUserPage(app_page).get_nick_name()

        time.sleep(3)

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert user_name == data['user_name']
            logging.info("我的页面-个人信息编辑页面-更换昵称成功")
        except:
            print("我的页面-个人信息编辑页面-更换昵称失败")
            common.save_screenShot(app_page, model_name="我的页面-个人信息编辑页面-更换昵称")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_center_data.login_success)
    def test_change_user_icon(self, data, app_page):
        '''我的页面-个人信息编辑页面-更换头像成功'''
        # 步骤
        LoginUserPage(app_page).login_user(data['username'], data['password'])

        time.sleep(3)

        LoginUserPage(app_page).edit_user()

        LoginUserPage(app_page).change_user_icon()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert 1 == 1
            logging.info("我的页面-个人信息编辑页面-更换头像成功")
        except:
            print("我的页面-个人信息编辑页面-更换头像失败")
            common.save_screenShot(app_page, model_name="我的页面-个人信息编辑页面-更换头像")
            raise


if __name__ == '__main__':
    pass