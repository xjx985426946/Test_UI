import re

from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class LoginShopperPage(BasePage):
    def login_shopper(self, username, password):
        name = '登录页面_登录操作'
        self.implicitly_wait(5)
        # 滑动引导页
        self.swipeLeft(2)
        # 点击立即体验
        self.find_element_by_id(login_locator.goto_main, model=name).click()
        time.sleep(2)
        # 关闭升级弹窗
        # self.find_element_by_id(login_locator.close_update_alert, model=name).click()
        if self.find_item(login_locator.close_update_alert):
            self.find_element_by_id(login_locator.close_update_alert, model=name).click()
            self.find_element(login_locator.shop, model=name).click()
        else:
            self.find_element(login_locator.shop, model=name).click()
        # 点击专柜

        # 输入用户名
        self.id_input_text(username, login_locator.user_input, model=name)
        # 输入密码
        self.id_input_text(password, login_locator.password_input, model=name)
        # 点击登录按钮
        self.find_element_by_id(login_locator.login_btn, model=name).click()
        time.sleep(2)
        # 点击引导浮层
        if self.find_item(login_locator.guide_btn):
            self.id_click_element(login_locator.guide_btn, model=name)
            self.id_click_element(login_locator.guide_btn2, model=name)
            self.id_click_element(login_locator.guide_btn3, model=name)
        else:
            return False

        time.sleep(2)
        # 关闭首页弹窗,并跳转专柜页面
        if self.find_item(login_locator.close_alert):
            self.find_element_by_id(login_locator.close_alert, model=name).click()
            self.find_element(login_locator.shop, model=name).click()
        else:
            self.find_element(login_locator.shop, model=name).click()

        self.shop_alert()

    def guide_btn(self):
        name = '新手引导'
        # 点击引导浮层
        self.id_click_element(login_locator.guide_btn, model=name)
        self.id_click_element(login_locator.guide_btn2, model=name)
        self.id_click_element(login_locator.guide_btn3, model=name)

    def shop_alert(self):
        name = '小店-引导弹窗'
        # 判断是否存在小店页面弹窗，有则关闭
        if self.find_item(login_locator.close_alert):
            self.id_click_element(login_locator.close_alert)
        else:
            return False

    # 确认专柜页面跳转是否成功
    def confirm_shopper(self):
        name = "确认专柜页面跳转是否成功"
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.shopper_icon):
            return ok
        else:
            return ng

    def shopper_icon(self):
        name = "编辑专柜头像"
        # 点击专柜头像
        self.id_click_element(login_locator.shopper_icon, model=name)
        time.sleep(2)
        self.id_click_element(login_locator.shop_name, model=name)

    def price_sort(self):
        name = '售价排序'
        # 点击售价
        self.id_click_element(login_locator.shopper_sort_price, model=name)

    # 点击销量
    def sort_sell(self):
        name = "销量排序"
        self.id_click_element(login_locator.shopper_sort_price, model=name)

    # 点击可赚金额
    def sort_money(self):
        name = "可赚金额"
        self.id_click_element(login_locator.shopper_sort_money, model=name)

    # 获取商品的售价
    def confirm_price_1(self):
        name = "专柜-售价排序"
        self.implicitly_wait(5)
        # 获取第二个商品的售价
        product_price = self.find_elements(login_locator.shop_price, model=name)
        return product_price[0].text

    # 获取商品的售价
    def confirm_price_2(self):
        name = "专柜-售价排序"
        self.implicitly_wait(5)
        # 获取第二个商品的售价
        product_price = self.find_elements(login_locator.shop_price, model=name)
        return product_price[1].text

    # 根据商品是否是纯CPS来获取不同的报酬任务的佣金
    def get_reward(self):
        time.sleep(2)
        if self.find_item(login_locator.product_detail_price):
            cpp = self.find_element_by_id(login_locator.product_detail_price)
            confirm_price = cpp.text
            return confirm_price
        else:
            cps = self.find_element_by_id(login_locator.product_detail_price_cps_vip)
            cps_price = cps.text
            re_obj = re.compile(r"\d+\.?\d*")
            res_list = re_obj.findall(cps_price)
            # 获取字符串中的数字
            x = list(map(float, res_list))
            str1 = " "
            # 转换类型为字符串
            confirm = str1.join([str(i) for i in x])
            print(confirm)
            return confirm

    # 获取第一个商品的佣金
    def product_detail_1(self):
        self.implicitly_wait(5)
        product_image = self.find_elements(login_locator.shop_product_image)
        product_image[0].click()
        money_1 = self.get_reward()
        self.find_element(login_locator.product_back).click()
        return money_1

    # 获取第二个商品的佣金
    def product_detail_2(self):
        self.implicitly_wait(5)
        product_image = self.find_elements(login_locator.shop_product_image)
        product_image[1].click()
        money_2 = self.get_reward()
        return money_2

    # 创建清单
    def create_inventory(self, title, remark):
        self.implicitly_wait(5)
        self.find_element(login_locator.shopper_inventory).click()
        self.id_click_element(login_locator.create_inventory)
        self.id_input_text(title, login_locator.create_inventory_title)
        self.id_input_text(remark, login_locator.create_inventory_remark)
        self.id_click_element(login_locator.create_inventory_add_pro)
        self.find_elements(login_locator.shop_product_image)[0].click()
        self.id_click_element(login_locator.create_right_add)
        self.id_click_element(login_locator.create_right_add)

    # 校验创建清单
    def check_create_inventory(self):
        self.implicitly_wait(5)
        title = self.find_elements(login_locator.inventory_title)[0]
        return title.text

    def create_inventory_title_err(self):
        self.implicitly_wait(5)
        self.find_element(login_locator.shopper_inventory).click()
        self.id_click_element(login_locator.create_inventory)
        self.id_click_element(login_locator.create_right_add)

    # 校验创建清单，标题为空提示
    def check_inventory_title_err(self):
        name = '校验创建清单标题为空'
        err = login_locator.create_inventory_title_toast_msg
        return self.get_toast_text(err, model=name)

    # 校验小店为空时，创建清单-添加商品中的商品是否为空
    def check_shop_null_create_inventory(self):
        self.implicitly_wait(5)
        self.find_element(login_locator.shopper_inventory).click()
        self.id_click_element(login_locator.create_inventory)
        self.id_click_element(login_locator.create_inventory_add_pro)
        main = self.find_element(login_locator.shop_null_create_inventory_add_pro)
        return main.text

    # 删除清单
    def del_inventory(self):
        self.implicitly_wait(5)
        self.find_element(login_locator.shopper_inventory).click()
        time.sleep(2)
        self.long_press(login_locator.inventory_pro)
        time.sleep(2)
        self.text_element(login_locator.del_inventory).click()

    # 更换昵称
    def shop_set_name(self, name):
        self.implicitly_wait(5)
        self.id_click_element(login_locator.shopper_icon)
        self.text_element(login_locator.shop_setting).click()
        self.id_click_element(login_locator.shop_name)
        self.id_input_text(name, login_locator.shop_name_input)
        self.find_element(login_locator.shop_set_save).click()

    # 校验更换昵称是否成功
    def check_shop_name_change(self, name):
        time.sleep(2)
        self.implicitly_wait(5)
        check_name = self.find_toast(name)
        return check_name

    # 更换公告
    def shop_set_intro(self, remake):
        self.implicitly_wait(5)
        self.id_click_element(login_locator.shopper_icon)
        self.text_element(login_locator.shop_setting).click()
        time.sleep(2)
        self.id_click_element(login_locator.shop_set_intro)
        time.sleep(2)
        if self.find_item(login_locator.shop_intro):
            intro = self.find_element(login_locator.shop_intro_input)
            intro.clear()
            intro.send_keys(remake)
        else:
            self.find_element(login_locator.shop_set_save).click()

    # 校验更换公告
    def check_shop_set_intro(self, remark):
        time.sleep(2)
        self.implicitly_wait(5)
        intro = self.find_toast(remark)
        return intro
