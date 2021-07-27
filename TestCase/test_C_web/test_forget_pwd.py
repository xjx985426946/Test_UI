import time
import pytest
import logging
from Common import common
from TestDatas.C_web import forget_pwd_data
from PageObject.C_web.forget_pwd_page import ForgetPwdPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestForGetPassword:

    # 成功登录
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_pwd_data.retrieve_pwd_success)
    def test_retrieve_pwd_success(self, data, web_page):
        '''成功登录'''
        time.sleep(2)
        #步骤
        ForgetPwdPage(web_page).forget_pwd(data['username'], data['code'], data['password'], data['second_password'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert ForgetPwdPage(web_page).login_success() == data['check']
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_pwd_data.phone_err)
    def test_user_phone_err(self, data, web_page):
        '''手机号码错误'''
        #步骤
        ForgetPwdPage(web_page).forget_pwd(data['username'], data['code'], data['password'], data['second_password'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert ForgetPwdPage(web_page).get_phone_errMsg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_pwd_data.code_err)
    def test_user_code_err(self, data, web_page):
        '''验证码错误'''
        # 步骤
        ForgetPwdPage(web_page).forget_pwd(data['username'], data['code'], data['password'], data['second_password'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert ForgetPwdPage(web_page).get_code_errMsg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_pwd_data.pwd_err)
    def test_user_pwd_err(self, data, web_page):
        '''密码错误'''
        # 步骤
        ForgetPwdPage(web_page).forget_pwd(data['username'], data['code'], data['password'], data['second_password'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert ForgetPwdPage(web_page).get_pwd_errMsg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", forget_pwd_data.second_pwd_err)
    def test_user_second_pwd_err(self, data, web_page):
        '''二次密码错误'''
        # 步骤
        ForgetPwdPage(web_page).forget_pwd(data['username'], data['code'], data['password'], data['second_password'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert ForgetPwdPage(web_page).get_second_pwd_errMsg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

if __name__ == '__main__':
    pass