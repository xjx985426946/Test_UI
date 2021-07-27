import datetime
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
# from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from Common import logger, dir_config
import logging
import re


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 等待元素可见 - 等待的时间 起始时间/结束时间
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("等待元素可见：{0},起始时间：{1},等待时长：{2}".format(locator, start, wait_times))
        except:
            # 日志
            logging.exception("等待元素可见异常")
            # 截图 - 图放哪儿去？图的名字？
            self._save_screenShot(model)
            raise

    # 等待元素存在
    def wait_elePrences(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 等待元素存在- 等待的时间 起始时间/结束时间
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("等待元素存在：{0},起始时间：{1},等待时长：{2}".format(locator, start, wait_times))
        except:
            # 日志
            logging.exception("等待元素存在异常")
            # 截图 - 图放哪儿去？图的名字？
            self._save_screenShot(model)
            raise

    # 等待元素存在
    def implicitly_wait(self, wait, model='model'):
        # 等待元素存在- 等待的时间 起始时间/结束时间
        try:
            return self.driver.implicitly_wait(wait)
        except:
            # 日志
            logging.exception("等待元素存在异常")
            # 截图 - 图放哪儿去？图的名字？
            self._save_screenShot(model)
            raise

    def find_element(self, locator, by=By.XPATH, model='model'):
        # 查找元素
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

    def find_element_by_id(self, locator, by=By.ID, model='model'):
        # 查找元素
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

    def find_element_wait_and_focus(self, locator, wait_ele, by=By.XPATH, model='model', wait=30,
                                    requence=0.5, index=None):
        # 查找元素
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        # 等待元素
        if wait_ele == 'visibility':
            self.wait_eleVisible(locator, by, model, wait,requence)
        else:
            self.wait_elePrences(locator, by, model, wait,requence)

        # 滚到元素到可视区域
        self.focus(locator, by, model,index)

        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

    def find_element_wait_and_focus_id(self, locator, wait_ele, by=By.ID, model='model', wait=30, requence=0.5, index=None):
        # 查找元素
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        # 等待元素
        if wait_ele == 'visibility':
            self.wait_eleVisible(locator, by, model, wait, requence)
        else:
            self.wait_elePrences(locator, by, model, wait, requence)

        # 滚到元素到可视区域
        self.focus_id(locator, by, model,index)

        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise


    # 查的多个元素
    def find_elements(self, locator, by=By.XPATH, model='model'):
        # 查找元素
        logging.info("开始查找符合表达式的所有元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_elements(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

    # 元素的点击操作。
    def click_element(self, locator, wait_ele='visibility', by=By.XPATH, model='model', wait=30, requence=0.5,
                       index=None):
        '''
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
           index=None表示查找一个元素。
           index=-1 表示查找多个元素，并在多个元素中随机选一个；
           index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        '''
        logging.info("执行点击操作！")
        ele = self.find_element_wait_and_focus(locator, wait_ele, by, model, wait,
                                               requence, index)
        try:
            ele.click()
        except:
            logging.exception("{0}下的元素执行点击操作失败。".format(model))
            self._save_screenShot(model)
            raise

        # 元素的输入操作

    def input_text(self, value, locator, by=By.XPATH, model='model',wait=30,requence=0.5,
                   wait_ele='visibility',index=None):
        """
        :param value: 要输入的文本值
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        """
        # ele = self._get_element(locator, by, model, index)
        ele = self.find_element_wait_and_focus(locator, wait_ele, by, model, wait,
                                               requence, index)
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logging.exception("{0}下的元素执行输入操作失败。".format(model))
            self._save_screenShot(model)
            raise

    # id元素的输入操作
    def id_input_text(self, value, locator, by=By.ID, model='model', wait=30, requence=0.5,
                    wait_ele='visibility', index=None):
        """
        :param value: 要输入的文本值
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
                index=None表示查找一个元素。
                index=-1 表示查找多个元素，并在多个元素中随机选一个；
                index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        """
        # ele = self._get_element(locator, by, model, index)
        ele = self.find_element_by_id(locator, by)
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logging.exception("{0}下的元素执行输入操作失败。".format(model))
            self._save_screenShot(model)
            raise

    # xpath元素的输入操作
    def xpath_input_text(self, value, locator, by=By.XPATH, model='model', wait=30, requence=0.5,
                    wait_ele='visibility', index=None):
        """
        :param value: 要输入的文本值
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
                index=None表示查找一个元素。
                index=-1 表示查找多个元素，并在多个元素中随机选一个；
                index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        """
        # ele = self._get_element(locator, by, model, index)
        ele = self.find_element(locator, by)
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logging.exception("{0}下的元素执行输入操作失败。".format(model))
            self._save_screenShot(model)
            raise

    def id_click_element(self, locator, wait_ele='visibility', by=By.ID, model='model', wait=30, requence=0.5,
                        index=None):
        '''
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
            index=None表示查找一个元素。
            index=-1 表示查找多个元素，并在多个元素中随机选一个；
            index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        '''
        logging.info("执行点击操作！")
        ele = self.find_element_by_id(locator, by)
        try:
            ele.click()
        except:
            logging.exception("{0}下的元素执行点击操作失败。".format(model))
            self._save_screenShot(model)
            raise

        # 获取元素的属性值。

    def get_element_attribube(self, attr_name, locator, by=By.XPATH,model='model',wait=30,requence=0.5,
                   wait_ele='visibility',index=None):
        """
        :param attr_name: 元素的属性名称
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的属性值。
        """
        logging.info("{0}：获取元素{1}={2} 的属性值：{3}。".format(model, by, locator, attr_name))
        ele = self.find_element_wait_and_focus(locator, wait_ele, by, model, wait,
                                               requence, index)
        try:
            return ele.get_attribute(attr_name)
        except:
            logging.exception("获取元素的属性：{0} 失败。".format(attr_name))
            self._save_screenShot(model)
            raise

        # 获取元素的文本内容

    def get_text(self, locator, by=By.XPATH, model='model',wait=30,requence=0.5,
                   wait_ele='visibility',index=None):
        """
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
          index=None表示查找一个元素。
          index=-1 表示查找多个元素，并在多个元素中随机选一个；
          index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的文本内容。
        """
        logging.info("{0}：获取元素{1}={2} 的文本内容。".format(model, by, locator))
        ele = self.find_element_wait_and_focus(locator, wait_ele, by, model, wait,
                                               requence, index)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败。")
            self._save_screenShot(model)
            raise

    def id_get_text(self, locator, by=By.ID, model='model',wait=30,requence=0.5,
                   wait_ele='visibility',index=None):
        """
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
          index=None表示查找一个元素。
          index=-1 表示查找多个元素，并在多个元素中随机选一个；
          index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的文本内容。
        """
        logging.info("{0}：获取元素{1}={2} 的文本内容。".format(model, by, locator))
        ele = self.find_element_wait_and_focus_id(locator, wait_ele, by, model, wait, requence, index)

        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败。")
            self._save_screenShot(model)
            raise

    def xpath_get_text(self, locator, by=By.XPATH):
        logging.info("{0}：获取元素{1}={2} 的文本内容。".format(model, by, locator))
        ele = self.find_element(by, locator)
        try:
            return ele.text()
        except:
            logging.exception("获取元素文本失败。")
            self._save_screenShot(model)
            raise

     # 元素滚动操作
    def focus(self, locator, by=By.XPATH, model='model', index=None):
        """
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return: 无
        """
        logging.info("{0}：滚动元素{1}={2} 到可见区域".format(model, by, locator))
        ele = self._get_element(locator, by, model, index)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except:
            logging.exception("滚动失败")
            self._save_screenShot(model)
            raise

     # 元素滚动操作
    def focus_id(self, locator, by=By.ID, model='model', index=None):
        """
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return: 无
        """
        logging.info("{0}：滚动元素{1}={2} 到可见区域".format(model, by, locator))
        ele = self._get_element(locator, by, model, index)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except:
            logging.exception("滚动失败")
            self._save_screenShot(model)
            raise

    # 截图函数
    def _save_screenShot(self, model_name="model"):
        # 根据功能和时间点生成截图
        # 文件格式 ：功能名称_年月日-时分秒.png
        try:
            file_path = dir_config.screenshot_dir + "/{0}_{1}.png".format(model_name,
                                                                          time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                        time.localtime()))
            # 截图文件存放在 Screenshot目录下
            # driver方法：self.driver.save_screenshot()
            self.driver.save_screenshot(file_path)
            logging.info("截图成功,路径为：{0}".format(file_path))
        except:
            logging.exception('截图失败')
            raise

     # 确定要操作的元素 - 查找多个和查找单个。确定元素操作对象。
    def _get_element(self, locator, by, model="model", index=None):
        # index为None表示查找单个元素。不为None表示查找多个元素，并在多个元素中选一个。
        if index is not None:
            # 在查找到多个元素的基础之上，选择其中的一个。
            return self._select_ele_from_elements(locator, by, model, index)
        else:
            return self.find_element(locator, by, model)

    # 在查找到的多个元素中，选择一个元素。
    def _select_ele_from_elements(self, locator, by, model="model", index=-1):
        """
        :param index: -1 表示随机选；0及0以上的值表示按下标选值。
        :return:返回选中的元素
        """
        import random
        eles = self.find_elements(locator, by, model)
        if index == -1 or index < 0:
            pos = random.randint(0, len(eles) - 1)
            return eles[pos]
        else:
            return eles[index]

    # 元素的点击操作。
    def click_element2(self, locator,wait_ele='visibility', by=By.XPATH, model='model', wait=30, requence=0.5,index=None):
        '''
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
           index=None表示查找一个元素。
           index=-1 表示查找多个元素，并在多个元素中随机选一个；
           index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        '''
        logging.info("执行点击操作！")
        ele = self.find_element_wait_and_focus(locator, wait_ele, by, model, wait,
                                               requence, index)
        try:
            ele.click()
        except:
            logging.exception("{0}下的元素执行点击操作失败。".format(model))
            self._save_screenShot(model)
            raise

    # 纯文本定位/toast，返回toast文本内容
    def get_toast_text(self, locator, by=By.XPATH, wait=5, requence=0.01, model='model'):
        """
        ########################################
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        ########################################
        """
        logging.info("查找toast")

        message = (by, locator)
        toast_element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(message))

        try:
            logging.exception("找到toast信息")
            return toast_element.text

        except:
            logging.exception("未查找到toast信息")
            self._save_screenShot(model)
            raise

    def find_toast(self, message):
        u'''获取toast信息文本并验证'''
        message1 = "//*[@text=\'{}\']".format(message)
        element = WebDriverWait(self.driver, 5, 0.01).until(
            EC.presence_of_element_located((By.XPATH, message1)))
        return element.text

    # 纯文本定位/toast
    def text_element(self, locator, by=By.XPATH, wait=5, requence=0.01, model='model'):
        """
        ########################################
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        ########################################
        """
        logging.info("查找toast")

        message = (by, locator)
        toast_element = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(message))

        try:
            return toast_element

        except:
            logging.exception("未查找到toast信息")
            self._save_screenShot(model)
            raise

    def swipeLeft(self, n):
        """
        向左滑动
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        time.sleep(2)

        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5

        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    def swipeRight(self, n):
        """
        向右滑动
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5

        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    def swipeUp(self, n):
        """
        向上滑动
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        x1 = width * 0.5
        y1 = width * 0.9
        y2 = height * 0.25

        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    def swipeDown(self, n):
        """
        向下滑动
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        x1 = width * 0.5
        y1 = width * 0.25
        y2 = height * 0.9

        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    # 具体文本不确定的时候，查找toast
    def find_toast(self, value, model='model'):
        # 查找toast
        logging.info("开始查找元素：{0}={1}")
        toast_msg = value
        message = '//*[@text=\'{}\']'.format(toast_msg)
        self.wait_eleVisible(message)
        toast_text = self.find_element(message)
        try:
            return toast_text.text
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

    # 手机-长按
    def long_press(self, locator):
        action = TouchAction(self.driver)
        el = self.find_elements(locator)[0]
        action.long_press(el=el, duration=2000).wait(2000).perform()

    # 坐标点击（用于处理蒙层）
    def touch_tap(self, x, y):  # 点击坐标  ,x1,x2,y1,y2
        '''method
        explain: 点击坐标
        parameter
        explain：【x, y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
        device.touch_coordinate(277, 431)  # 277.431为点击某个元素的x与y值
        '''

        TouchAction(self.driver).press(x=x, y=y).release().perform()

    # 判断元素是否存在于当前页面，备注：只能识别by_id
    def find_item(self, el):
        logging.info("开始查找元素：{0}={1}")
        source = self.driver.page_source
        if el in source:
            return True
        else:
            return False

    def back(self):
        self.driver.press_keycode(4)

    # 判断元素是否可见
    def find_element_page(self, locator, by=By.XPATH, wait=30, requence=0.05, model='model'):
        """
        ########################################
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        ########################################
        """
        logging.info("查找元素")

        message = (by, locator)

        try:
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(message))
            return True

        except:
            logging.exception("未查找到元素")
            self._save_screenShot(model)
            return False

    # 判断元素是否可见
    def find_element_pages(self, locator, by=By.XPATH, wait=30, requence=0.05, model='model'):
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
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_locateds(message))
            return True

        except:
            logging.exception("未查找到元素")
            self._save_screenShot(model)
            return False
