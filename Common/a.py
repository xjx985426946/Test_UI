# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys #引入Keys类包
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('https://www.baidu.com')
#
# input = driver.find_element_by_id('kw') #定位搜索框
# sleep(2)
# input.send_keys('this is a test')
# sleep(2)
# for n in range(4):
#     input.send_keys(Keys.LEFT) #光标左移四次
#     #可以用input.send_keys('\ue012')代替
# sleep(2)
# for n in range(4):
#     input.send_keys(Keys.DELETE) #向后删除四个字母，即'test'
# sleep(2)
# input.send_keys(Keys.BACK_SPACE) #向前删除一个字符，即空格
# sleep(2)
# input.send_keys(Keys.SPACE) #继续添加一个空格
# sleep(2)
# input.send_keys('a test two')
# sleep(2)
# input.send_keys(Keys.ENTER) #点击回车，开始搜索
# sleep(5)
# driver.quit()


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# builder = ActionChains(driver)
# builder.key_down(Keys.F12).perform()
#
# sleep(5)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# mobile_emulation = {"deviceName":"iPhone X"}
# option = webdriver.ChromeOptions()
# option.add_experimental_option('mobileEmulation',mobile_emulation)
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('https://test-item.intbee.com/customer/mobile/login')
# print('打开浏览器')
# print(driver.title)
# time.sleep(2)
# locator = '//input[@placeholder="请输入您的手机号"]'
# WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH,locator)))
# driver.find_element_by_xpath('//input[@placeholder="请输入您的手机号"]').send_keys('13729542194')
# time.sleep(2)
# driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('123456')
# time.sleep(2)
# driver.find_element_by_xpath('//button[@class="mint-button mint-button--primary mint-button--large"]').click()
# time.sleep(4)
# driver.get("https://test-item.intbee.com/customer/mobile/item/19031/?uuid=5bc59a1e9a1d090007a0464a&platform_id=0")
# time.sleep(10)
# # el = driver.find_element_by_id("index-bn")
# # TouchActions(driver).tap(el).perform()
# # print('关闭')
# driver.quit()
# print('测试完成')



# from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# mobile_emulation = {"deviceName":"iPhone X"}
# option = webdriver.ChromeOptions()
# option.add_experimental_option('mobileEmulation',mobile_emulation)
# driver = webdriver.Chrome(chrome_options=option)
#
# # driver.get('https://test-item.intbee.com/customer/mobile/login')
# # time.sleep(2)
#
# driver.get('https://test-item.intbee.com/customer/mobile/item/19031/?uuid=5bc59a1e9a1d090007a0464a&platform_id=0')
# time.sleep(2)
# driver.find_element_by_xpath('//div[@class="bottom"]//span[text()=" 立即购买 "]').click()
#
#
# locator = '//input[@placeholder="请输入您的手机号"]'
# WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH,locator)))
# driver.find_element_by_xpath('//input[@placeholder="请输入您的手机号"]').send_keys('13729542194')
# time.sleep(2)
# driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('123456')
# time.sleep(2)
# driver.find_element_by_xpath('//button[@class="mint-button mint-button--primary mint-button--large"]').click()
# time.sleep(4)
#
#
# driver.find_element_by_xpath('//div[@class="bottom"]//span[text()=" 立即购买 "]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//ul[@class="standardValues"]/li[text()="红色"]').click()
# driver.quit()
# print('测试完成')


# import re
# amount = '$ 100:00'
# new_amount = re.sub("\D", "",amount.split(':')[0])
# print(new_amount)





# from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# mobile_emulation = {"deviceName":"iPhone X"}
# option = webdriver.ChromeOptions()
# option.add_experimental_option('mobileEmulation',mobile_emulation)
# driver = webdriver.Chrome(chrome_options=option)
#
# # driver.get('https://test-item.intbee.com/customer/mobile/login')
# # time.sleep(2)
#
# driver.get('https://test-item.intbee.com/customer/mobile/item/19031/?uuid=5bc59a1e9a1d090007a0464a&platform_id=0')
# time.sleep(2)
# driver.find_element_by_xpath('//div[@class="bottom"]//span[text()=" 立即购买 "]').click()



#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# mobile_emulation = {"deviceName": "Galaxy S5"}
# chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
# # chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
# chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#
#
# driver=webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://test-item.intbee.com/customer/mobile/login')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/div[1]/input').send_keys("13729542194")
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/div[2]/input').send_keys("123456")
# import time
# time.sleep(4)
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/button').click()
# import time
# time.sleep(8)
# print(driver.current_url)
# # print('hao123' in driver.page_source)
#
#
# driver.close() #切记关闭浏览器，回收资源





# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# mobile_emulation = {"deviceName": "Galaxy S5"}
# chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
# chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
# chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#
#
# driver=webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://www.baidu.com')
# driver.find_element_by_xpath('//*[@id="index-kw"]').send_keys('梅西')
# driver.find_element_by_xpath('//*[@id="index-bn"]').click()
# import time
# time.sleep(4)
# print(driver.current_url)
# # print('hao123' in driver.page_source)
#
#
# driver.close() #切记关闭浏览器，回收资源




# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.get("http://hotel.qunar.com/")
# data = driver.title
# print(data)


#
# from selenium import webdriver
#
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# browser.get('https://www.baidu.com')
# browser.find_element_by_xpath('//input[@id="kw"]').send_keys('selenium')
# browser.find_element_by_xpath('//input[@id="su"]').click()
# print(browser.current_url)
# print("成功")
# browser.quit()

#
# from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://authzui.alipay.com/login/index.htm")
# login_windows = driver.current_window_handle
# try:
#     element = WebDriverWait(driver, 10, 1).until(
#         EC.presence_of_element_located((By.ID, "J-input-user"))
#     )
#     pe = WebDriverWait(driver, 10, 1).until(
#         EC.presence_of_element_located((By.ID, "password_rsainput"))
#     )
#
#     login_btn = WebDriverWait(driver, 10, 1).until(
#         EC.presence_of_element_located((By.ID, "J-login-btn"))
#     )
#     if element and pe and login_btn:
#         element.send_keys("*******")  # 参数为您的支付宝帐号
#         pe.click()
#         pe.send_keys("xxxxxxx")  # 在此输入您的支付宝密码
#         time.sleep(10)
#         # login_btn.send_keys(Keys.ENTER)
#         login_btn.click()
#         time.sleep(5)
#         driver.implicitly_wait(10)
#         print (driver.current_window_handle)
#         driver.switch_to.window(driver.current_window_handle)
#         login_el = driver.find_element_by_link_text("转 账")
#         login_el.click()
# except:
#     print("找不到")
#

# from TestDatas.C_phone import login_data
# b = login_data.login_sesscus

# import re
# amount = '123vv'
# new_amount = re.sub("\D", "", amount.split(':')[0])
# print(new_amount)