#coding=utf-8
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from other import api
import unittest
import pytest
import os
from time import sleep
from PageLocators.V_app import login_locator
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from appium import webdriver
from Common.basepage import BasePage

cur_path = os.path.dirname(os.path.realpath(__file__))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'c6e989d7'
desired_caps['appPackage'] = 'xyz.nesting.intbee'
desired_caps['appActivity'] = '.ui.activity.WelcomeActivity'
desired_caps['app'] = cur_path + '\\TestCase\\test_app\\intbee_v4.3.1.apk'
desired_caps['automationName'] = 'uiautomator2'
# desired_caps['noReset'] = True
desired_caps['autoGrantPermissions'] = True

# 启动 APP
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 向左滑动屏幕
def swipeleft(n):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    sleep(1)
    x1 = width * 0.8
    x2 = width * 0.2
    y1 = height * 0.5
    sleep(1)
    for i in range(n):
        sleep(1)
        driver.swipe(x1, y1, x2, y1)

def swipeUp(n):
    """
    向上滑动
    """
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    x1 = width * 0.5
    y1 = width * 0.9
    y2 = height * 0.25

    for i in range(n):
        driver.swipe(x1, y1, x1, y2)


def find_item(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False

# 登录
def login():
    driver.implicitly_wait(5)
    # 用户协议
    if find_item(login_locator.user_bg):
        driver.find_element_by_id(login_locator.user_confirm).click()
    # 滑动引导页
    swipeleft(2)
    # 点击立即体验
    driver.find_element_by_id(login_locator.goto_main).click()
    sleep(2)
    # 关闭升级弹窗
    if find_item(login_locator.close_update_alert):
        driver.find_element_by_id(login_locator.close_update_alert).click()
        driver.find_element_by_xpath(login_locator.my).click()
    else:
        driver.find_element_by_xpath(login_locator.my).click()

    sleep(2)
    # 输入用户名
    driver.find_element_by_id(login_locator.user_input).send_keys('19900008884')
    # 输入密码
    driver.find_element_by_id(login_locator.password_input).send_keys('123456')
    # 点击登录按钮
    driver.find_element_by_id(login_locator.login_btn).click()
    sleep(2)
    # 点击引导浮层
    if find_item(login_locator.guide_btn):
        driver.find_element_by_id(login_locator.guide_btn).click()
        driver.find_element_by_id(login_locator.guide_btn2).click()
        driver.find_element_by_id(login_locator.guide_btn3).click()

    sleep(2)
    # 点击引导浮层
    if find_item(login_locator.guide_btn):
        driver.find_element_by_id(login_locator.guide_btn).click()
        driver.find_element_by_id(login_locator.guide_btn2).click()
        driver.find_element_by_id(login_locator.guide_btn3).click()
    else:
        return False

    sleep(2)
    # 关闭首页弹窗,并跳转我的页面
    if find_item(login_locator.close_alert):
        driver.find_element_by_id(login_locator.close_alert).click()
        sleep(2)
        driver.find_element_by_id(login_locator.my).click()
    else:
        driver.find_element_by_id(login_locator.my).click()

def test(x):
    try:
        driver.find_element_by_id(x)
        return x
    except:
        return False

# 获取toast弹窗内容
def get_toast(message):

    try:
        print(1)
        # toast消息内容，方便定位
        toast_info = (By.XPATH, '//*[@text=\'{}\']'.format(message))

        # 获取toast提示框内容
        toast_element = WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located(toast_info))
        print(toast_element)

        ele = toast_element.text
        print(ele)
        return ele
    except:
        print(2)
        return print("toast弹窗内容获取失败")


def update_image():
    print('更新头像')
    file_path = 'D:\\intbee\\intbee-test-script\\Test-UI\\PageObject\\V_app\\user_icon.jpg'

    user_icon = driver.find_element_by_id('xyz.nesting.intbee:id/user_icon')
    user_icon.send_keys(file_path)

def find_element(test):
    a = 'selenium.common.exceptions.NoSuchElementException'
    b = 'selenium.common.exceptions.TimeoutException'
    try:
        WebDriverWait(driver, 3).until(driver.find_element_by_id(test))
        return True
    except a:
        return False
    except b:
        return False

def get_code():

    if find_item(login_locator.product_detail_price):
        cpp = driver.find_element_by_id(login_locator.product_detail_price)
        confirm_price = cpp.text
        return confirm_price
    else:
        cps = driver.find_element_by_id(login_locator.product_detail_price_cps_vip)
        cps_price = cps.text
        re_obj = re.compile(r"\d+")
        res_list = re_obj.findall(cps_price)
        x = list(map(int, res_list))  # 获取字符串中的数字
        str1 = " "
        # 转换类型为整型
        confirm = str1.join([str(i) for i in x])
        return confirm

def long_press():
    action = TouchAction(driver)
    el = driver.find_elements_by_xpath(login_locator.inventory_pro)[0]
    action.long_press(el=el, duration=2000).wait(2000).perform()

def text_element(locator, by=By.XPATH, wait=5, requence=0.01):

    message = (by, locator)
    toast_element = WebDriverWait(driver, wait, requence).until(EC.presence_of_element_located(message))

    return toast_element

def text_element1(locator, by=By.XPATH, wait=5, requence=0.01):

    message = (by, locator)
    toast_element = WebDriverWait(driver, wait, requence).until(EC.presence_of_element_located(message))

    try:
        return toast_element

    except:
        raise

def shop_set_intro(remake):
    driver.implicitly_wait(5)
    driver.find_element_by_id(login_locator.shopper_icon).click()
    text_element1(login_locator.shop_setting).click()
    sleep(2)
    driver.find_element_by_id(login_locator.shop_set_intro).click()
    sleep(2)
    if find_item(login_locator.shop_intro_input):
        print('开始查找元素')
        intro = '欢迎来到北京师范大学'
        intro_after = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText')
        intro_after.send_keys(remake)
        print('输入成功')
    else:
        print('元素查找失败')
    driver.find_element_by_xpath(login_locator.shop_set_save).click()


def confirm_my():
    name = "确认我的页面跳转是否成功"
    sleep(2)
    ok = '跳转成功'
    ng = '跳转失败'
    if find_item(login_locator.user_icon):
        print(ok)
        return ok
    else:
        return ng

def confirm_my2(self):
    name = "确认我的页面跳转是否成功"
    sleep(2)
    ok = '跳转成功'
    ng = '跳转失败'
    if find_item(login_locator.user_icon):
        print(ok)
        return ok
    else:
        return ng

    # 判断元素是否可见
def find_element_page(locator, by=By.XPATH, wait=30, requence=0.05, model='model'):
    """
    ########################################
    描述：获取Toast的文本信息
    参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
    返回值：返回与之匹配到的toast信息
    异常描述：none
    ########################################
    """

    message = (by, locator)

    try:
        WebDriverWait(driver, wait, requence).until(EC.presence_of_element_locateds(message))
        return True

    except:
        return False

def find():
    if find_element_page(login_locator.task_finish2):
        print('成功')
    else:
        print('失败')

def touch_tap(x, y, locator, by=By.XPATH, wait=5, requence=0.01, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
    '''method
    explain: 点击坐标
    parameter
    explain：【x, y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
    device.touch_coordinate(277, 431)  # 277.431为点击某个元素的x与y值
    '''

    screen_width = driver.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = driver.get_window_size()['height']  # 获取当前屏幕的高
    a = (float(x) / screen_width) * screen_width
    x1 = int(a)
    b = (float(y) / screen_height) * screen_height
    y1 = int(b)
    message = (by, locator)
    WebDriverWait(driver, wait, requence).until(EC.presence_of_element_located(message))
    sleep(3)
    driver.tap([(x1, y1), (x1, y1)], duration)

def confirm_share_finish():
    sleep(2)
    ok = '跳转成功'
    ng = '跳转失败'
    if find_element_page(login_locator.task_finish):
        return ok
    else:
        return ng

def get_toast_text(locator, by=By.XPATH, wait=10, requence=0.01, model='model'):
    """
    ########################################
    描述：获取Toast的文本信息
    参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
    返回值：返回与之匹配到的toast信息
    异常描述：none
    ########################################
    """

    message = (by, locator)
    toast_element = WebDriverWait(driver, wait, requence).until(EC.presence_of_element_located(message))

    try:
        print("找到toast信息")
        return toast_element.text

    except:
        print("未查找到toast信息")
        raise


if __name__ == '__main__':
    driver.implicitly_wait(5)
    login()
    sleep(2)
    driver.find_element_by_id(login_locator.my_media).click()

    sleep(2)
    go = driver.find_elements(By.XPATH, login_locator.bind_name)
    go[3].click()

    sleep(2)
    driver.find_element_by_id(login_locator.name_Et).send_keys('测试33')

    driver.find_element_by_id(login_locator.page_Et).send_keys('测试')
    driver.find_element_by_id(login_locator.commit).click()

    # touch_tap(277, 500, login_locator.main_product_share_channel)
    # driver.find_element_by_id(login_locator.back).click()
    # driver.tap([(25,906),(695,1058)], 100)
    # TouchAction(driver).press(x=277, y=500).release().perform()
    # sleep(2)
    toast = get_toast_text(login_locator.red_book_error)
    print(toast)

    if toast == '请求参数有误:请输入正确的小红书个人主页':
        print('执行成功')
    else:
        print('执行失败')

    sleep(3)
    driver.quit()


# sleep(2)
# # 点击我的
# el1 = driver.find_element_by_xpath("//android.widget.TextView[@text='我的']")
# el1.click()
# sleep(2)
# driver.find_element_by_id("xyz.nesting.intbee:id/icon").click()z
#
#
# import re
#
# string = '每日浏览任务5次（已浏览商品1次）'
# p1 = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
# p2 = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
# print(re.findall(p1, string))
# print(re.findall(p2, string))
# print(re.findall(r'[（](.*?)[）]', string))

