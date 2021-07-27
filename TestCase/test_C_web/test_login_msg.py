import time
import pytest
from Common import common
from TestDatas.C_web import login_msg_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_web.login_msg_login_page import MsgLoginPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestMsgLogin:

    # 成功登录
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_msg_data.login_msg_success)
    def test_Msg_login_success(self, data, web_page):
        '''成功登录'''
        time.sleep(2)
        #步骤
        MsgLoginPage(web_page).login(data['username'], data['code'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert MsgLoginPage(web_page).login_success() == data['check']
            # assert 1==1
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_msg_data.login_msg_err)
    def test_Msg_usernotin(self, data, web_page):
        '''验证码错误'''
        # 步骤
        MsgLoginPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert MsgLoginPage(web_page).get_errMsg_from_user() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_msg_data.login_msg_err2)
    def test_Msg_usernotin2(self, data, web_page):
        '''手机号码错误'''
        # 步骤
        MsgLoginPage(web_page).login(data['username'], data['code'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert MsgLoginPage(web_page).get_errMsg_from_user2() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    if __name__ == '__main__':
        pass
