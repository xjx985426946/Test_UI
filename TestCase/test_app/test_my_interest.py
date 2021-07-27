import time
import pytest
from Common import common
from TestDatas.V_app import my_interest_data
import logging
from PageObject.V_app.my_interest_page import MyInterestPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestLoginUser:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", my_interest_data.login_success)
    def test_login_my_interest(self, data, app_page):
        ''' 确认我的兴趣页面跳转是否成功 '''
        # 步骤
        MyInterestPage(app_page).login_user(data['username'], data['password'])

        MyInterestPage(app_page).my_interest()

        success = MyInterestPage(app_page).confirm_my_interest()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的兴趣页面跳转成功")
        except:
            print("我的兴趣页面跳转失败")
            common.save_screenShot(app_page, model_name="我的兴趣页面")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", my_interest_data.add_interest)
    def test_my_interest_add(self, data, app_page):
        '''我的兴趣-添加兴趣'''
        # 步骤
        MyInterestPage(app_page).login_user(data['username'], data['password'])

        MyInterestPage(app_page).my_interest()

        time.sleep(3)

        num_before = MyInterestPage(app_page).get_interest_number()

        MyInterestPage(app_page).add_interest(data['add_interest'])

        time.sleep(3)

        add = MyInterestPage(app_page).confirm_add_interest(data['add_interest'])

        num_after = MyInterestPage(app_page).get_interest_number()

        logging.info("开始断言")

        # 验证-检查点
        try:
            if num_after - num_before == 1:
                assert add == data['add_interest']
            logging.info("我的兴趣-添加兴趣成功")
        except:
            print("我的兴趣-添加兴趣失败")
            common.save_screenShot(app_page, model_name="我的兴趣-添加兴趣")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", my_interest_data.add_interest)
    def test_my_interest_del(self, data, app_page):
        '''我的兴趣-删除兴趣'''
        # 步骤
        MyInterestPage(app_page).login_user(data['username'], data['password'])

        MyInterestPage(app_page).my_interest()

        time.sleep(3)

        num_before = MyInterestPage(app_page).get_interest_number()

        MyInterestPage(app_page).del_my_interest()

        num_after = MyInterestPage(app_page).get_interest_number()

        logging.info("开始断言")

        # 验证-检查点
        try:
            if num_before - num_after == 1:
                assert add == data['add_interest']
            logging.info("我的兴趣-添加兴趣成功")
        except:
            print("我的兴趣-添加兴趣失败")
            common.save_screenShot(app_page, model_name="我的兴趣-添加兴趣")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", my_interest_data.add_interest_err)
    def test_my_interest_add_err(self, data, app_page):
        '''我的兴趣-添加兴趣-标签名不能为空'''
        # 步骤
        MyInterestPage(app_page).login_user(data['username'], data['password'])

        MyInterestPage(app_page).my_interest()

        time.sleep(3)

        err = MyInterestPage(app_page).add_interest_err()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert err == data['check']
            logging.info("我的兴趣-添加兴趣-标签名不能为空成功")
        except:
            print("我的兴趣-添加兴趣-标签名不能为空失败")
            common.save_screenShot(app_page, model_name="我的兴趣-添加兴趣-标签名不能为空")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", my_interest_data.add_interest_err2)
    def test_my_interest_add_err2(self, data, app_page):
        '''我的兴趣-添加兴趣-标签名不能少于4个字'''
        # 步骤
        MyInterestPage(app_page).login_user(data['username'], data['password'])

        MyInterestPage(app_page).my_interest()

        time.sleep(3)

        err = MyInterestPage(app_page).add_interest_err2()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert err == data['check']
            logging.info("我的兴趣-添加兴趣-标签名不能少于4个字成功")
        except:
            print("我的兴趣-添加兴趣-标签名不能少于4个字失败")
            common.save_screenShot(app_page, model_name="我的兴趣-添加兴趣-标签名不能少于4个字")
            raise


if __name__ == '__main__':
    pass