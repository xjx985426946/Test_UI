import time
import pytest
from Common import common
from TestDatas.C_web import user_manage_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_web.user_info_page import UserInfoPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestUserManage:

    # 成功登录-跳转账户管理页面
    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.login_success)
    def test_login_success(self, data, web_page):
        '''成功登录-跳转账户管理页面'''
        time.sleep(2)
        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert UserInfoPage(web_page).user_manage() == data['check']
            logging.info("账号管理页面跳转成功")
        except:
            print("账号管理页面跳转失败")
            common.save_screenShot(web_page, model_name="账号管理页面")
            raise


    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.user_name)
    def test_user_name_info(self, data, web_page):
        '''账号管理页面'''
        time.sleep(2)
        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        time.sleep(2)
        # 步骤2 更换昵称
        UserInfoPage(web_page).get_user_info_name(data['user_info_name'])

        logging.info("开始断言")

        time.sleep(3)

        # 验证-检查点
        try:
            assert UserInfoPage(web_page).user_info_name_check() == ''
            logging.info("昵称修改成功")
        except:
            print("昵称修改失败")
            common.save_screenShot(web_page, model_name="账号管理页面")
            raise

    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.pwd_err)
    def test_user_pwd_err(self, data, web_page):
        '''旧密码密码长度最少6位'''

        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        time.sleep(5)
        # 步骤2 修改密码
        UserInfoPage(web_page).user_edit_pwd_page()
        time.sleep(3)
        UserInfoPage(web_page).user_edit_pwd(data['pwd'], data['new_pwd'], data['second_pwd'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert UserInfoPage(web_page).user_edit_pwd_err() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("密码修改失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.new_pwd_err)
    def test_user_pwd_err2(self, data, web_page):
        '''新密码密码长度最少6位'''

        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        time.sleep(5)
        # 步骤2 修改密码
        UserInfoPage(web_page).user_edit_pwd_page()
        time.sleep(3)
        UserInfoPage(web_page).user_edit_pwd(data['pwd'], data['new_pwd'], data['second_pwd'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert UserInfoPage(web_page).user_edit_new_pwd_err() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("密码修改失败")
            common.save_screenShot(web_page, model_name="登录页面")
            raise

    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.second_pwd_err)
    def test_user_pwd_err3(self, data, web_page):
        '''两次输入密码不一致'''

        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        time.sleep(5)
        # 步骤2 修改密码
        UserInfoPage(web_page).user_edit_pwd_page()
        time.sleep(3)
        UserInfoPage(web_page).user_edit_pwd(data['pwd'], data['new_pwd'], data['second_pwd'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert UserInfoPage(web_page).user_edit_second_pwd_err() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("密码修改失败")
            common.save_screenShot(web_page, model_name="修改密码页面")
            raise

    @pytest.mark.demos
    @pytest.mark.parametrize("data", user_manage_data.pwd_success)
    def test_user_content_err(self, data, web_page):
        '''密码修改成功/新旧密码相同/密码错误'''

        # 步骤1 登录
        UserInfoPage(web_page).login(data['username'], data['code'])

        time.sleep(5)
        # 步骤2 修改密码
        UserInfoPage(web_page).user_edit_pwd_page()
        time.sleep(3)
        UserInfoPage(web_page).user_edit_pwd(data['pwd'], data['new_pwd'], data['second_pwd'])
        logging.info("开始断言")
        time.sleep(1)

        try:
            assert UserInfoPage(web_page).user_edit_pwd_success() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("密码修改失败")
            common.save_screenShot(web_page, model_name="修改密码页面")
            raise

if __name__ == '__main__':
    pass