import time
import pytest
from Common import common
from TestDatas.C_phone import nick_data
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.nick_page import NickPage
from PageObject.C_phone.personal_page import PersonalPage
import logging,time

@pytest.mark.usefixtures("login")
@pytest.mark.domes
@pytest.mark.production
class Testsetnick:
    #设置昵称

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", nick_data.nick_name)
    def test_setnick_success(self,data,login):
        '''成功修改昵称'''
        # 步骤
        time.sleep(2)
        PcenterPage(login).click_set()
        time.sleep(2)
        PersonalPage(login).click_nick()
        time.sleep(2)
        NickPage(login).input_nick(data['nick_name'])
        time.sleep(2)
        NickPage(login).click_button()
        time.sleep(2)

        logging.info("开始断言")

        # 验证-检查点
        try:
            assert NickPage(login).get_toast() == data['check']
            logging.info("登录成功")
        except:
            print("登录失败")
            common.save_screenShot(login,model_name="修改昵称页面")
            raise



if __name__ == '__main__':
    pass