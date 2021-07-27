import time
import pytest
from Common import common
from TestDatas.V_app import user_integral_data
import logging
from PageObject.V_app.user_integral_page import LoginUserIntPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestLoginUser:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_integral_data.login_success)
    def test_login_success_my(self, data, app_page):
        ''' 我的积分页面跳转 '''
        # 步骤
        LoginUserIntPage(app_page).login_user(data['username'], data['password'])

        LoginUserIntPage(app_page).go_user_integral()

        success = LoginUserIntPage(app_page).confirm_go_user_integral()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的积分页面跳转成功")
        except:
            print("我的积分页面跳转失败")
            common.save_screenShot(app_page, model_name="我的积分页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_integral_data.confirm_go_explain)
    def test_edit_user_info(self, data, app_page):
        '''我的页面-我的积分-积分规则页面跳转'''
        # 步骤
        LoginUserIntPage(app_page).login_user(data['username'], data['password'])

        time.sleep(3)

        LoginUserIntPage(app_page).go_user_integral()

        time.sleep(3)

        LoginUserIntPage(app_page).go_explain()

        time.sleep(3)

        explain = LoginUserIntPage(app_page).confirm_go_explain()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert explain == data['check']
            logging.info("我的页面-我的积分-积分规则页面跳转成功")
        except:
            print("我的页面-我的积分-积分规则页面跳转失败")
            common.save_screenShot(app_page, model_name="我的页面-我的积分-积分规则页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", user_integral_data.explain_detail)
    def test_change_user_name(self, data, app_page):
        '''我的页面-我的积分-积分明细'''
        # 步骤
        LoginUserIntPage(app_page).login_user(data['username'], data['password'])

        time.sleep(3)

        LoginUserIntPage(app_page).go_user_integral()

        time.sleep(3)

        LoginUserIntPage(app_page).go_explain_detail()

        time.sleep(3)

        explain_detail = LoginUserIntPage(app_page).confirm_go_explain()

        time.sleep(3)

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert explain_detail == data['check']
            logging.info("我的页面-我的积分-积分明细成功")
        except:
            print("我的页面-我的积分-积分明细失败")
            common.save_screenShot(app_page, model_name="我的页面-我的积分-积分明细")
            raise


if __name__ == '__main__':
    pass