from Common import dir_config
import time
import logging
from PIL import Image
from pytesseract import image_to_string


def save_screenShot(driver, model_name="model"):
    # 根据功能和时间点生成截图
    # 文件格式 ：功能名称_年月日-时分秒.png
    try:
        file_path = dir_config.screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                                time.localtime()))
        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        driver.save_screenshot(file_path)
        logging.info("截图成功,路径为：{0}".format(file_path))
    except:
        logging.exception('截图失败')
        raise


def ocr():
    im = Image.open('test.png')
    imgry = im.convert("L")
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()

    aa = image_to_string(out)
    print(aa)

