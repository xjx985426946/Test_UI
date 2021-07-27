from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test():

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://test-item.intbee.com/customer/login#")

    @pytest.mark.smoke
    def testone(self):
        '''添加地址'''

        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys("13729542194")
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机验证码"]').send_keys("6666a")
        self.driver.find_element_by_xpath('//button[@class="btnCell"]').click()

        # self.driver.find_element_by_xpath('//ul[@class="list"]/li[5]/a').click()
        time.sleep(2)
        self.driver.get('https://test-item.intbee.com/customer/personal/address#')
        time.sleep(2)
        # WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="添加地址"]')))
        self.driver.find_element_by_xpath('//span[text()="添加地址"]').click()

        self.driver.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人姓名"]').send_keys("HC")
        self.driver.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人手机号码"]').send_keys("132729542194")
        self.driver.find_element_by_xpath('//div[@class="region el-popover__reference"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[text()="浙江省"]').click()
        self.driver.find_element_by_xpath('//span[text()="温州市"]').click()
        self.driver.find_element_by_xpath('//span[text()="瓯海区"]').click()
        self.driver.find_element_by_xpath('// input[@placeholder = "请输入详细地址"]').send_keys("HC")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[@class="el-switch__core"]').click()
        self.driver.find_element_by_xpath('//span[text() = "保存"]').click()
        time.sleep(1)
        a = self.driver.find_element_by_xpath('//li[@class="isDefault"]//div').text
        time.sleep(2)
        assert a == '收货人：HC'

        self.driver.quit()

    def testtwo(self):
        '''不填收货地址'''

        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys("13729542194")
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机验证码"]').send_keys("6666a")
        self.driver.find_element_by_xpath('//button[@class="btnCell"]').click()

        time.sleep(2)
        self.driver.get('https://test-item.intbee.com/customer/personal/address#')
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[text()="添加地址"]').click()

        self.driver.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人姓名"]').send_keys(
            "HC")
        self.driver.find_element_by_xpath('//input[@class="el-input__inner" and @placeholder="请输入收件人手机号码"]').send_keys(
            "132729542194")

        self.driver.find_element_by_xpath('// input[@placeholder = "请输入详细地址"]').send_keys("HC")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[@class="el-switch__core"]').click()
        self.driver.find_element_by_xpath('//span[text() = "保存"]').click()
        time.sleep(1)
        text = self.driver.find_element_by_xpath('//p[@class="el-message__content" and text()="请选择所在地址"]').text
        assert text == '请选择所在地址'
        self.driver.quit()

    #
    # def test_3(self):
    #     '''手机号码不合法'''
    #     pass
    #
    # def test_4(self):
    #     '''不填写默认地址'''
    #     pass
    #
    # def test_4(self):
    #     '''删除地址'''
    #     pass
    #
    # def test_5(self):
    #     '''修改地址'''

if __name__ == '__main__':
    pytest.main(['-m', 'smoke','-v','test_address.py'
                 ])