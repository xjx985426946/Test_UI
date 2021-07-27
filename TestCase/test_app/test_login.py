import time
import pytest
from Common import common
from TestDatas.V_app import login_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.V_app.login_page import LoginPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_data.login_success)
    def test_login_success(self, data, app_page):
        '''成功登录'''
        # 步骤
        LoginPage(app_page).login(data['username'], data['password'])

        time.sleep(3)

        LoginPage(app_page).guide_btn()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert 1 == 1
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(app_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_data.login_user_err2)
    def test_login_toast(self, data, app_page):
        '''参数有误:用户信息不存在'''
        #步骤
        LoginPage(app_page).login(data['username'], data['password'])

        logging.info("开始断言")

        try:
            assert LoginPage(app_page).get_errMsg_login() == data['check']
            logging.info("成功：参数有误:用户信息不存在")

        except:
            print("断言失败")
            print("账户不存在")
            common.save_screenShot(app_page, model_name="账户不存在")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_data.login_user_err)
    def test_login_err(self, data, app_page):
        '''密码错误，请重新输入'''
        #步骤
        LoginPage(app_page).login(data['username'], data['password'])

        logging.info("开始断言")

        try:
            assert LoginPage(app_page).login_err() == data['check']
            logging.info("成功：密码错误，请重新输入")

        except:
            print("断言失败")
            print("密码错误校验失败")
            common.save_screenShot(app_page, model_name="密码错误校验失败")
            raise

if __name__ == '__main__':
    pass