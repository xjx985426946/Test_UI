from selenium import webdriver
import pytest
import time
import logging
@pytest.mark.usefixtures("Login")
class Test():

    def testtwo(self,Login):
        '''不填收货地址'''

        time.sleep(2)
        logging.info("进入地址管理页面！")

        try:
            Login.get('https://test-item.intbee.com/customer/personal/address#')
        except:
            logging.exception("进入地址管理页面失败")

        time.sleep(2)

        self.click_element()


        time.sleep(2)

        Login.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人姓名"]').send_keys(
            "HC")

        Login.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人手机号码"]').send_keys(
            "132729542194")


        Login.find_element_by_xpath('// input[@placeholder = "请输入详细地址"]').send_keys("HC")
        time.sleep(1)

        Login.find_element_by_xpath('//span[@class="el-switch__core"]').click()
        Login.find_element_by_xpath('//span[text() = "保存"]').click()
        time.sleep(1)
        text = Login.find_element_by_xpath('//p[@class="el-message__content" and text()="请选择所在地址"]').text
        assert text == '请选择所在地址'




if __name__ == '__main__':
    pytest.main(['-m', 'smoke','-v','test_address3.py'
                 ])