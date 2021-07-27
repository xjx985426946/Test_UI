import re

from PageLocators.V_app import login_locator
from Common.basepage import BasePage
import time

class UserValuesPage(BasePage):
    def login_user(self, username, password):
        name = '登录页面_登录操作'
        self.implicitly_wait(5)
        # 滑动引导页
        self.swipeLeft(2)
        # 点击立即体验
        self.find_element_by_id(login_locator.goto_main, model=name).click()
        time.sleep(2)
        # 关闭升级弹窗
        if self.find_item(login_locator.close_update_alert):
            self.find_element_by_id(login_locator.close_update_alert, model=name).click()
            self.find_element(login_locator.my, model=name).click()
        else:
            self.find_element(login_locator.my, model=name).click()

        time.sleep(2)
        # 输入用户名
        self.id_input_text(username, login_locator.user_input, model=name)
        # 输入密码
        self.id_input_text(password, login_locator.password_input, model=name)
        # 点击登录按钮
        self.find_element_by_id(login_locator.login_btn, model=name).click()
        time.sleep(2)
        if self.find_item(login_locator.next_btn):
            self.find_element(login_locator.book_review).click()
            self.find_element_by_id(login_locator.next_btn).click()

        # 点击引导浮层
        if self.find_item(login_locator.guide_btn):
            self.id_click_element(login_locator.guide_btn, model=name)
            self.id_click_element(login_locator.guide_btn2, model=name)
            self.id_click_element(login_locator.guide_btn3, model=name)

        time.sleep(2)
        # 点击引导浮层
        if self.find_item(login_locator.guide_btn):
            self.id_click_element(login_locator.guide_btn, model=name)
            self.id_click_element(login_locator.guide_btn2, model=name)
            self.id_click_element(login_locator.guide_btn3, model=name)
        else:
            return False

        time.sleep(2)
        # 关闭首页弹窗,并跳转我的页面
        if self.find_item(login_locator.close_alert):
            self.find_element_by_id(login_locator.close_alert, model=name).click()
            time.sleep(2)
            self.find_element(login_locator.task, model=name).click()
        else:
            self.find_element(login_locator.task, model=name).click()

    # 确认我的成长值跳转是否成功
    def confirm_task_values(self):
        # self.implicitly_wait(5)
        name = "确认我的成长值跳转是否成功"
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.task_value):
            return ok
        else:
            return ng

    # 我的成长值页面跳转
    def task(self):
        name = '我的成长值页面跳转'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.task, model=name)

    # 我的成长值说明页面跳转
    def task_value_des(self):
        name = '我的成长值说明页面跳转'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.task_value_des, model=name)

    # 我的成长值-更多等级福利跳转
    def task_value_des_more(self):
        name = '我的成长值-更多等级福利跳转'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.moreTv, model=name)

    # 校验更多等级福利跳转
    def confirm_task_values_des_more(self):
        name = '校验更多等级福利跳转'
        # self.implicitly_wait(5)
        time.sleep(3)
        center = self.find_element_by_id(login_locator.check_header, model=name).text
        return center

    # 确认成长值说明跳转是否成功
    def confirm_task_value_des(self):
        # self.implicitly_wait(5)
        name = "确认成长值说明跳转是否成功"
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_item(login_locator.task_value_des_card):
            return ok
        else:
            return ng

    # 获取用户成长值
    def get_task_value(self):
        name = '获取用户成长值'
        # self.implicitly_wait(5)
        str_value = self.find_element_by_id(login_locator.task_value, model=name).text
        value = ''.join([x for x in str_value if x.isdigit()])
        return int(value)

    # 领取奖励后获取用户成长值
    def award_get_task_value(self):
        name = '获取用户成长值'
        # self.implicitly_wait(5)
        self.swipeDown(3)
        str_value = self.find_element_by_id(login_locator.task_value, model=name).text
        value = ''.join([x for x in str_value if x.isdigit()])
        return int(value)

    # 我的成长值页面-签到
    def sign_in(self):
        name = '我的成长值页面-签到'
        self.implicitly_wait(5)
        self.id_click_element(login_locator.task_sign, model=name)

    # 校验签到成功，按钮文本是否变化
    def confirm_sign_info(self):
        name = '校验签到成功，按钮文本是否变化'
        # self.implicitly_wait(5)
        time.sleep(3)
        success = self.find_element_by_id(login_locator.task_sign, model=name).text
        return success

    # 校验签到成功，toast弹窗
    def confirm_sign_toast(self):
        name = '校验签到成功，toast弹窗'
        # self.implicitly_wait(5)
        success = self.get_toast_text(login_locator.task_sign_success, model=name)
        return success

    # 日常任务-每日分享任务
    def share_everyday(self):
        name = '日常任务-每日分享任务'
        self.implicitly_wait(5)
        go = self.find_elements(login_locator.task_go, model=name)
        go[0].click()

        main = self.find_elements(login_locator.main_product_iv, model=name)
        main[0].click()

        time.sleep(2)

        self.find_element_by_id(login_locator.main_product_share, model=name).click()

        time.sleep(2)

        logo = self.find_elements(login_locator.main_product_share_channel, model=name)
        logo[1].click()
        print(logo)

        self.id_click_element(login_locator.wx_back, model=name)
        time.sleep(3)

    # 日常任务-每日分享任务
    def share_everyday_2(self):
        name = '2日常任务-每日分享任务2'
        self.implicitly_wait(5)

        self.back()

        time.sleep(2)

        self.touch_tap(277, 500)

        time.sleep(2)

        self.find_element_by_id(login_locator.back).click()

        time.sleep(3)

        self.find_element(login_locator.my, model=name).click()

        self.id_click_element(login_locator.task, model=name)

    # 校验每日分享任务完成
    def confirm_share_everyday(self):
        name = '校验每日分享任务完成'
        time.sleep(2)
        suc = self.get_toast_text(login_locator.task_share_success_toast, model=name)
        suc2 = self.get_toast_text(login_locator.task_share_success_toast2, model=name)
        suc3 = self.get_toast_text(login_locator.task_share_success_toast3, model=name)
        return suc + suc2 + suc3

    # 日常任务-随便逛逛
    def go_around(self):
        name = '日常任务-随便逛逛'
        time.sleep(2)
        go2 = self.find_elements(login_locator.go_around_product, model=name)
        str_value = go2[1].text
        re_obj = re.compile(r'[（](.*?)[）]', re.S)
        res_list = re.findall(re_obj, str_value)
        val = ''.join(res_list)
        value = ''.join([x for x in val if x.isdigit()])

        tim = 5 - int(value)
        print(tim)

        if tim == 0:
            self.confirm_go_around_finish()
        else:
            go = self.find_elements(login_locator.task_go)
            go[0].click()

            if tim == 0:
                self.find_item(login_locator.task_finish2)
            elif tim == 0:
                main = self.find_elements(login_locator.main_product_iv, model=name)
                main[0].click()
            else:
                self.swipeUp(3)
                for i in range(tim):
                    main = self.find_elements(login_locator.main_product_iv, model=name)
                    main[i].click()
                    if i != tim - 1:
                        self.find_element_by_id(login_locator.back).click()

    # 校验随便逛逛任务弹窗文案
    def confirm_go_around(self):
        name = '校验随便逛逛任务弹窗文案'
        time.sleep(2)
        title = self.find_element_by_id(login_locator.task_alert, model=name).text
        text = self.find_element_by_id(login_locator.task_alert_text, model=name).text
        return title + text

    # 随便逛逛任务弹窗-去任务中心看看
    def confirm_go_around_action(self):
        self.implicitly_wait(5)
        action = self.find_element_by_id(login_locator.task_alert_action)
        action.click()

    # 随便逛逛任务-已完成图标校验
    def confirm_go_around_finish(self):
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_element_pages(login_locator.task_finish2):
            return ok
        else:
            return ng

    # 每日分享任务-已完成图标校验
    def confirm_share_finish(self):
        time.sleep(2)
        ok = '跳转成功'
        ng = '跳转失败'
        if self.find_element_page(login_locator.task_finish):
            return ok
        else:
            return ng

    # 新手任务-修改名称
    def new_user_change_name(self, user_name):
        name = '新手任务-修改名称'
        self.implicitly_wait(5)
        self.swipeUp(3)
        go_task = self.find_elements(login_locator.task_new_go, model=name)
        go_task[0].click()
        time.sleep(3)
        self.id_click_element(login_locator.nick_name, model=name)
        self.id_input_text(user_name, login_locator.input_user_name, model=name)
        self.id_click_element(login_locator.month_day_save, model=name)
        time.sleep(3)
        self.id_click_element(login_locator.leftItem, model=name)

    # 校验新手任务-修改名称-按钮：领取奖励
    def confirm_new_user_change_name(self):
        name = '校验新手任务-修改名称'
        # self.implicitly_wait(5)
        time.sleep(2)
        success = self.find_elements(login_locator.task_new_go, model=name)
        return success[0].text

    # 点击领取奖励
    def receive_awards(self):
        name = '点击领取奖励'
        # self.implicitly_wait(5)
        time.sleep(2)
        go_award = self.find_elements(login_locator.task_new_go, model=name)
        go_award[0].click()

    # 校验领取奖励-toast提示：领取成功
    def confirm_receive_awards(self):
        name = '校验修改名称领取奖励'
        # self.implicitly_wait(5)
        time.sleep(2)
        rec = self.get_toast_text(login_locator.task_new_go, model=name)
        return rec

    # 新手任务-修改头像
    def new_user_change_icon(self):
        name = '新手任务-修改头像'
        self.implicitly_wait(5)
        self.swipeUp(4)
        go_task = self.find_elements(login_locator.task_new_go, model=name)
        go_task[0].click()
        time.sleep(3)
        self.id_click_element(login_locator.change_user_icon, model=name)
        self.find_element(login_locator.select_image, model=name).click()
        self.id_click_element(login_locator.select_image_ok, model=name)
        self.id_click_element(login_locator.crop_image, model=name)
        time.sleep(3)
        self.id_click_element(login_locator.leftItem, model=name)

    # 校验新手任务-修改头像
    def confirm_new_user_change_icon(self):
        name = '校验新手任务-修改头像'
        self.implicitly_wait(5)
        success = self.find_elements(login_locator.task_new_go, model=name)
        return success[0].text




