import time
import pytest
from Common import common
from TestDatas.V_app import task_values_data
import logging
from PageObject.V_app.task_value_page import UserValuesPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestUserValues:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.login_success)
    def test_login_success_task(self, data, app_page):
        ''' 我的成长值页面跳转 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        success = UserValuesPage(app_page).confirm_task_values()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的成长值页面跳转成功")
        except:
            print("我的成长值页面跳转失败")
            common.save_screenShot(app_page, model_name="我的成长值页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.login_success)
    def test_task_values_des(self, data, app_page):
        ''' 我的成长值说明页面跳转 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        UserValuesPage(app_page).task_value_des()

        success = UserValuesPage(app_page).confirm_task_value_des()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的成长值说明页面跳转成功")
        except:
            print("我的成长值说明页面跳转失败")
            common.save_screenShot(app_page, model_name="我的成长值说明页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.values_des_more)
    def test_task_values_des_more(self, data, app_page):
        ''' 我的成长值说明页面-更多福利说明跳转 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        UserValuesPage(app_page).task_value_des()

        UserValuesPage(app_page).task_value_des_more()

        success = UserValuesPage(app_page).confirm_task_values_des_more()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("我的成长值说明页面-更多福利说明跳转成功")
        except:
            print("我的成长值说明页面跳转-更多福利说明失败")
            common.save_screenShot(app_page, model_name="我的成长值说明页面-更多福利说明跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.sign_success)
    def test_task_sign(self, data, app_page):
        ''' 我的成长值页面-签到 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        values = UserValuesPage(app_page).get_task_value()

        UserValuesPage(app_page).sign_in()

        toast = UserValuesPage(app_page).confirm_sign_toast()

        success = UserValuesPage(app_page).get_task_value()

        button = UserValuesPage(app_page).confirm_sign_info()

        check = success - values

        logging.info("开始断言")

        # 验证-检查点
        try:
            if toast == data['check_toast'] and button == data['check_button']:
                assert check == 10
                logging.info("我的成长值说明页面-更多福利说明跳转成功")
        except:
            print("我的成长值说明页面跳转-更多福利说明失败")
            common.save_screenShot(app_page, model_name="我的成长值说明页面-更多福利说明跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.share_success)
    def test_task_share_everyday(self, data, app_page):
        ''' 我的成长值页面-每日分享任务 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        values = UserValuesPage(app_page).get_task_value()

        UserValuesPage(app_page).share_everyday()

        success = UserValuesPage(app_page).confirm_share_everyday()

        UserValuesPage(app_page).share_everyday_2()

        values_share = UserValuesPage(app_page).get_task_value()

        check = values_share - values

        ok = UserValuesPage(app_page).confirm_share_finish()

        logging.info("开始断言")

        # 验证-检查点
        try:
            if success == data['check_toast'] and ok == data['check_ok']:
                assert check == 30
                logging.info("我的成长值页面-每日分享任务成功")
        except:
            print("我的成长值页面-每日分享任务失败")
            common.save_screenShot(app_page, model_name="我的成长值页面-每日分享任务")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.go_around_success)
    def test_task_go_around(self, data, app_page):
        ''' 我的成长值页面-随便逛逛任务 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        values = UserValuesPage(app_page).get_task_value()

        UserValuesPage(app_page).go_around()

        time.sleep(3)

        success = UserValuesPage(app_page).confirm_go_around()

        UserValuesPage(app_page).confirm_go_around_action()

        values_share = UserValuesPage(app_page).get_task_value()

        check = values_share - values

        ok = UserValuesPage(app_page).confirm_go_around_finish()

        logging.info("开始断言")

        # 验证-检查点
        try:
            if success == data['check_alert'] and ok == data['check_ok']:
                assert check == 30
                logging.info("我的成长值页面-随便逛逛任务成功")
        except:
            print("我的成长值页面-随便逛逛任务失败")
            common.save_screenShot(app_page, model_name="我的成长值页面-随便逛逛任务")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.change_name)
    def test_task_change_name(self, data, app_page):
        ''' 我的成长值页面-新手任务-修改昵称 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        values = UserValuesPage(app_page).get_task_value()

        UserValuesPage(app_page).new_user_change_name(data['user_name'])

        time.sleep(3)

        success = UserValuesPage(app_page).confirm_new_user_change_name()

        UserValuesPage(app_page).receive_awards()

        toast = UserValuesPage(app_page).confirm_receive_awards()

        ok = UserValuesPage(app_page).confirm_share_finish()

        values_award = UserValuesPage(app_page).award_get_task_value()

        check = values_award - values

        logging.info("开始断言")

        # 验证-检查点
        try:
            if success == data['check_btn'] and ok == data['check_ok'] and toast == data['check_toast']:
                assert check == 50
                logging.info("我的成长值页面-新手任务-修改昵称成功")
        except:
            print("我的成长值页面-新手任务-修改昵称失败")
            common.save_screenShot(app_page, model_name="我的成长值页面-新手任务-修改昵称")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", task_values_data.change_icon)
    def test_task_change_icon(self, data, app_page):
        ''' 我的成长值页面-新手任务-修改头像 '''
        # 步骤
        UserValuesPage(app_page).login_user(data['username'], data['password'])

        UserValuesPage(app_page).task()

        values = UserValuesPage(app_page).get_task_value()

        UserValuesPage(app_page).new_user_change_icon()

        time.sleep(3)

        success = UserValuesPage(app_page).confirm_new_user_change_name()

        UserValuesPage(app_page).receive_awards()

        toast = UserValuesPage(app_page).confirm_receive_awards()

        ok = UserValuesPage(app_page).confirm_share_finish()

        values_award = UserValuesPage(app_page).award_get_task_value()

        check = values_award - values

        logging.info("开始断言")

        # 验证-检查点
        try:
            if success == data['check_btn'] and ok == data['check_ok'] and toast == data['check_toast']:
                assert check == 50
                logging.info("我的成长值页面-新手任务-修改头像成功")
        except:
            print("我的成长值页面-新手任务-修改头像失败")
            common.save_screenShot(app_page, model_name="我的成长值页面-新手任务-修改头像")
            raise


if __name__ == '__main__':
    pass
