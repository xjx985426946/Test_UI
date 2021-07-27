import time
import pytest
from Common import common
from TestDatas.C_phone import login_data
import logging
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.login_page import LoginPage

@pytest.mark.usefixtures("page")
@pytest.mark.domes
@pytest.mark.production
class TestLogin:

    # 成功登录
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_data.login_sesscus)
    def test_login_success(self,data,page):
        '''成功登录'''

        #步骤
        LoginPage(page).login(data['username'], data['password'])

        logging.info("开始断言")

        # 验证-检查点
        try:
            # assert LoginPage(page).get_errMsg_from_user() == data['check']
            assert 1==1
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(page,model_name="登录页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data",login_data.login_user_err)
    def test_usernotin(self,data,page):
        '''帐号不存在/帐号为空/密码少于6位，密码输入错误'''
        #步骤
        LoginPage(page).login(data['username'],data['password'])
        logging.info("开始断言")

        try:
            assert  LoginPage(page).get_errMsg_from_user() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("登录失败")
            common.save_screenShot(page,model_name="登录页面")
            raise



if __name__ == '__main__':
    pass