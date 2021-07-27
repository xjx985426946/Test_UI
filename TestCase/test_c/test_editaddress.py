from selenium import webdriver
import pytest
import time
import logging
from TestCase.test_c.addresspage2 import addressPage


@pytest.mark.usefixtures("Login")
class Test():

    def testtwo(self, Login):
        '''不填收货地址'''

        time.sleep(2)
        logging.info("进入地址管理页面！")

        try:
            Login.get('https://test-item.intbee.com/customer/personal/address#')
        except:
            logging.exception("进入地址管理页面失败")

        time.sleep(2)

        # 点击添加地址按钮操作
        addressPage(Login).click_addresss()
        # 输入姓名
        time.sleep(2)
        addressPage(Login).input_name("陈海镇")

        # 输入手机号
        addressPage(Login).input_mobile()
        # 输入详细地址
        addressPage(Login).input_deatil()

        # 点击保存按钮

        time.sleep(1)
        text = addressPage(Login).get_toast()
        assert text == '请选择所在地址'

    def test3(self, Login):

        time.sleep(2)
        logging.info("进入地址管理页面！")

        try:
            Login.get('https://test-item.intbee.com/customer/personal/address#')
        except:
            logging.exception("进入地址管理页面失败")

        time.sleep(2)

        addressPage(Login).address()


        assert text == '请选择所在地址'


    def test4(self,Login):
        '''手机号码格式不正确'''
        addressPage(Login).input_mobile("44555")
if __name__ == '__main__':
    pytest.main(['-m', 'smoke', '-v', 'test_address5.py'
                 ])














#1、封装我们的方法
#2\封装 操作流程
#testcase  测试代码
#执行测试集