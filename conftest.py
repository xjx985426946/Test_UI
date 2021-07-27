import pytest, os
from selenium import webdriver
# from appium import webdriver
import logging
from PageObject.C_phone.login_page import LoginPage as lp
from PageObject.C_web.login_page import LoginPage
from TestDatas import CommonData
from py._xmlgen import html
from Common import conf
# from selenium.webdriver.chrome.options import Options
C_phone = conf.m_lg_url
C_web = conf.w_lg_url
cur_path = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture()
def page():
    logging.info('----------------测试开始-----------------')
    mobile_emulation = {"deviceName": "iPhone 6 Plus"}
    option = webdriver.ChromeOptions()
    option.add_experimental_option('mobileEmulation', mobile_emulation)
    driver = webdriver.Chrome(options=option)
    driver.get(C_phone)
    yield driver
    logging.info('----------------测试结束-----------------')
    driver.quit()


@pytest.fixture()
def web_page():
    logging.info('----------------测试开始-----------------')
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.get(C_web)
    driver.maximize_window()
    yield driver
    logging.info('----------------测试结束-----------------')
    driver.quit()

@pytest.fixture()
def app_page():
    logging.info('----------------测试开始-----------------')
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = 'c6e989d7'
    desired_caps['appPackage'] = 'xyz.nesting.intbee'
    desired_caps['appActivity'] = '.ui.activity.WelcomeActivity'
    desired_caps['app'] = cur_path + '\\TestCase\\test_app\\intbee_v4.3.1.apk'
    # desired_caps['noReset'] = True
    desired_caps['autoGrantPermissions'] = True
    desired_caps['automationName'] = 'uiautomator2'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    yield driver
    logging.info('----------------测试结束-----------------')
    driver.quit()

@pytest.fixture()
def login():
    logging.info('----------------测试开始-----------------')
    mobile_emulation = {"deviceName": "iPhone 6 Plus"}
    option = webdriver.ChromeOptions()
    option.add_experimental_option('mobileEmulation', mobile_emulation)
    # option.add_argument('window-size=667x375')
    driver = webdriver.Chrome(options=option)
    driver.get(C_phone)
    login_page = lp(driver)
    # 登录
    login_page.login(CommonData.username, CommonData.password)
    yield driver
    logging.info('----------------测试结束-----------------')
    driver.quit()

@pytest.fixture()
def web_login():
    logging.info('----------------测试开始-----------------')

    driver = webdriver.Chrome()
    driver.get(C_phone)
    login_page = LoginPage(driver)
    # 登录
    login_page.login(CommonData.username, CommonData.password)
    yield driver
    logging.info('----------------测试结束-----------------')
    driver.quit()


@pytest.fixture(scope="class")
def class_use():
    print("我是class级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="class")
def class_use():
    print("我是class级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="module")
def module_use():
    print("我是模块级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="class")
def uilogin():
    print("登录操作")


#通过conftest来实现报告的描述
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except:
        pass

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
