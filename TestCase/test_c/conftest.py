import pytest
from selenium import webdriver
import time
@pytest.fixture()
def Login():
    driver = webdriver.Chrome()
    driver.get("https://test-item.intbee.com/customer/login#")
    time.sleep(2)
    driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys("13729542194")
    driver.find_element_by_xpath('//input[@placeholder="请输入手机验证码"]').send_keys("6666a")
    driver.find_element_by_xpath('//button[@class="btnCell"]').click()
    yield driver
    driver.quit()