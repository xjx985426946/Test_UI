import time
import pytest
from Common import common
from TestDatas.V_app import sms_login_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.V_app.sms_login_page import SmsLoginPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestSmsLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", sms_login_data.sms_login_success)
    def test_sms_login_success(self, data, app_page):
        """短信登录成功"""
        # 跳转短信登录页面
        SmsLoginPage(app_page).sms_login(data['username'])
        time.sleep(2)
        # 输入短信
        SmsLoginPage(app_page).sms_login_success(data['username'])

        logging.info("开始断言")
        time.sleep(5)

        # 验证-检查点
        try:
            assert 1 == 1
            logging.info("短信登录成功")
        except:
            print("短信登录失败")
            common.save_screenShot(app_page, model_name="短信登录成功")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", sms_login_data.sms_login_err)
    def test_login_toast(self, data, app_page):
        """ 验证码不正确 """
        # 跳转短信登录页面
        SmsLoginPage(app_page).sms_login(data['username'])
        time.sleep(2)
        SmsLoginPage(app_page).sms_login_code_err(data['code'])

        logging.info("开始断言")

        try:
            assert SmsLoginPage(app_page).sms_login_toast() == data['check']
            logging.info("成功：验证码不正确")

        except:
            print("断言失败")
            print("验证码不正确校验失败")
            common.save_screenShot(app_page, model_name="验证码不正确校验失败")
            raise


if __name__ == '__main__':
    pass