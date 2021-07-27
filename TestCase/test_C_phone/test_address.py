import time
import pytest
from Common import common
from TestDatas.C_phone import createaddress_data
from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_phone.address_page import AddressPage

import logging,time

@pytest.mark.usefixtures("login")
@pytest.mark.domes
class Testaddress:
    #管理地址

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", createaddress_data.createsuccess)
    def test_addresssuccess(self,data,login):
        '''成功新增管理地址'''
        # 步骤
        time.sleep(2)
        #点击地址管理按钮
        PcenterPage(login).click_addresss()
        time.sleep(2)
        AddressPage(login).create_button()
        time.sleep(2)
        #输入信息
        AddressPage(login).input_address(data['input_name'],data['input_mobile'],data['detailaddress'])
        time.sleep(2)
        logging.info("开始断言")

        # 验证-检查点
        try:
            assert AddressPage(login).get_addresstext() == data['check']
            logging.info("添加成功")
        except:
            logging.info('添加失败')
            common.save_screenShot(login,model_name="管理地址页面")
            raise


    @pytest.mark.smoke
    def test_updateaddress(self,login):
        '''编辑地址'''
        time.sleep(2)
        #点击管理地址按钮
         #点击地址管理按钮
        PcenterPage(login).click_addresss()
        time.sleep(2)
        AddressPage(login).update_address()

        try:
            assert AddressPage(login).get_addresstext() == createaddress_data.update_success['check']
        except:
            print("更新失败")
            common.save_screenShot(login,model_name="修改地址")

    @pytest.mark.smoke
    def test_deleteaddress(self,login):
        '''删除地址'''
        time.sleep(2)
        PcenterPage(login).click_addresss()
        time.sleep(2)
        AddressPage(login).delete_address()
        try:
            assert AddressPage(login).get_addresstext() == createaddress_data.update_success['check']
        except:
            logging.info("删除失败")
            common.save_screenShot(login,model_name="删除地址页面")

if __name__ == '__main__':
    pass