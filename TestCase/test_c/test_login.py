from selenium import webdriver
import pytest
import time
class Test():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://test-item.intbee.com/customer/login#")

    @pytest.mark.smoke
    def testone(self):
        '''成功登录'''

        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys("13729542194")
        self.driver.find_element_by_xpath('//input[@placeholder="请输入手机验证码"]').send_keys("6666a")
        self.driver.find_element_by_xpath('//button[@class="btnCell"]').click()

        a = self.driver.find_element_by_xpath('//span[text()="我的订单"]').text
        assert '我的订单' == a

        time.sleep(2)

        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-m', 'smoke','-v','test_login.py'])