import time
import pytest
from Common import common
from TestDatas.V_app import media_bind_data
import logging
from PageObject.V_app.media_bind_page import MediaBindPage

@pytest.mark.usefixtures("app_page")
@pytest.mark.domes
@pytest.mark.production
class TestMediaBind:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.login_success)
    def test_media_bind(self, data, app_page):
        ''' 自媒体账号绑定页面跳转 '''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        success = MediaBindPage(app_page).confirm_my_media()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert success == data['check']
            logging.info("自媒体账号绑定页面跳转成功")
        except:
            print("自媒体账号绑定页面跳转失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.confirm_wb_cancel)
    def test_wb_cancel(self, data, app_page):
        '''自媒体账号绑定页面-微博-取消绑定'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).login_wb_cancel_bind()

        toast = MediaBindPage(app_page).confirm_login_wb()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-微博-取消绑定成功")
        except:
            print("自媒体账号绑定页面-微博-取消绑定失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-微博-取消绑定")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.confirm_wb_bind)
    def test_wb_bind(self, data, app_page):
        '''自媒体账号绑定页面-微博-绑定'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).login_wb_bind()

        toast = MediaBindPage(app_page).confirm_blog_authorized()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-微博-绑定成功")
        except:
            print("自媒体账号绑定页面-微博-绑定失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-微博-绑定")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.wx_bind)
    def test_wx_bind(self, data, app_page):
        '''自媒体账号绑定页面-公众号-绑定'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).wx_bind()

        time.sleep(3)

        toast = MediaBindPage(app_page).confirm_wx_bind()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-公众号-绑定成功")
        except:
            print("自媒体账号绑定页面-公众号-绑定失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-公众号-绑定")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.tips_bind_error)
    def test_dy_bind_error(self, data, app_page):
        '''自媒体账号绑定页面-抖音-绑定-非抖音链接'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).tips_bind(data['url'])

        toast = MediaBindPage(app_page).tips_login_error()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-抖音-绑定-非抖音链接报错成功")
        except:
            print("自媒体账号绑定页面-抖音-绑定-非抖音链接失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-抖音-绑定-非抖音链接")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", media_bind_data.tips_bind)
    def test_dy_bind(self, data, app_page):
        '''自媒体账号绑定页面-抖音-绑定成功'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).tips_bind(data['url'])

        toast = MediaBindPage(app_page).confirm_tips_bind(data['tips'])

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-抖音-绑定成功")
        except:
            print("自媒体账号绑定页面-抖音-绑定失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-抖音-绑定")
            raise

    @pytest.mark.test
    @pytest.mark.parametrize("data", media_bind_data.red_book_error)
    def test_red_book_error(self, data, app_page):
        '''自媒体账号绑定页面-小红书-绑定-非小红书链接报错'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).red_book(data['url'])

        toast = MediaBindPage(app_page).red_book_error()

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-小红书-绑定-非小红书链接报错成功")
        except:
            print("自媒体账号绑定页面-小红书-绑定-非小红书链接报错失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-小红书-绑定-非小红书链接报错")
            raise

    @pytest.mark.test
    @pytest.mark.parametrize("data", media_bind_data.red_book)
    def test_red_book_bind(self, data, app_page):
        '''自媒体账号绑定页面-小红书-绑定'''
        # 步骤
        MediaBindPage(app_page).login_user(data['username'], data['password'])

        MediaBindPage(app_page).my_media()

        MediaBindPage(app_page).red_book(data['url'])

        toast = MediaBindPage(app_page).confirm_red_book_bind(data['name'])

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert toast == data['check']
            logging.info("自媒体账号绑定页面-小红书-绑定成功")
        except:
            print("自媒体账号绑定页面-小红书-绑定失败")
            common.save_screenShot(app_page, model_name="自媒体账号绑定页面-小红书-绑定")
            raise


if __name__ == '__main__':
    pass
