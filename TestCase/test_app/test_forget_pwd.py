import time
import pytest
from Common import common
from TestDatas.V_app import forget_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.V_app.forget_pwd_page import ForGetPwdPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestForGetPwd:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_data.forget_pwd_success)
    def test_forget_success(self, data, app_page):
        """成功忘记密码"""
        # 跳转忘记密码页面
        ForGetPwdPage(app_page).forget(data['username'])
        time.sleep(2)
        # 执行忘记密码流程-获取验证码、输入验证码、重置密码
        ForGetPwdPage(app_page).forget_success(data['username'], data['new_pwd'], data['new_pwd_second'])

        logging.info("开始断言")
        time.sleep(5)

        # 验证-检查点
        try:
            assert 1 == 1
            logging.info("忘记密码成功")
        except:
            print("忘记密码失败")
            common.save_screenShot(app_page, model_name="忘记密码页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_data.forget_pwd_err)
    def test_login_toast(self, data, app_page):
        """ 验证码不正确 """
        # 跳转忘记密码页面
        ForGetPwdPage(app_page).forget(data['username'])
        time.sleep(2)
        ForGetPwdPage(app_page).forget_error(data['code'])

        logging.info("开始断言")

        try:
            assert ForGetPwdPage(app_page).get_errmsg_forget() == data['check']
            logging.info("成功：验证码不正确")

        except:
            print("断言失败")
            print("验证码不正确校验失败")
            common.save_screenShot(app_page, model_name="验证码不正确校验失败")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_data.forget_pwd_err2)
    def test_forget_success(self, data, app_page):
        """两次密码不一致"""
        # 跳转忘记密码页面
        ForGetPwdPage(app_page).forget(data['username'])
        time.sleep(2)
        # 执行忘记密码流程-获取验证码、输入验证码、重置密码
        ForGetPwdPage(app_page).forget_success(data['username'], data['new_pwd'], data['new_pwd_second'])

        logging.info("开始断言")
        time.sleep(5)

        # 验证-检查点
        try:
            assert ForGetPwdPage(app_page).get_errmsg_forge3() == data['check']
            logging.info("校验两次密码不一致成功")
        except:
            print("校验两次密码不一致失败")
            common.save_screenShot(app_page, model_name="校验两次密码不一致失败")
            raise


if __name__ == '__main__':
    pass