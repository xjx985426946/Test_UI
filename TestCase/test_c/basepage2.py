
import time
from selenium.webdriver.common.by import By
from Common import logger, dir_config
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, by=By.XPATH, model='model'):
        # 查找元素
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素失败。")
            self._save_screenShot(model)
            raise

        # 元素的点击操作。

    def click_element(self, locator, by=By.XPATH, model='model'):
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
        ele = self.find_element(locator, by, model)
        try:
            ele.click()
        except:
            logging.exception("{0}下的元素执行点击操作失败。".format(model))
            self._save_screenShot(model)
            raise


    def input_text(self, value, locator, by=By.XPATH, model='model'):
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
        ele = self.find_element(locator, by, model)
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logging.exception("{0}下的元素执行输入操作失败。".format(model))
            self._save_screenShot(model)
            raise

    def get_text(self, locator, by=By.XPATH, model='model'):
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
        ele = self.find_element(locator, by, model)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败。")
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

