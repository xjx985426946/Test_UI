from PageLocators.C_phone import shop_locator
from Common.basepage import BasePage


class ShopPage(BasePage):
    name = '专柜页面'

    # 获取专柜头部hearder
    def get_shop(self):
        return self.get_text(shop_locator.shop_description)


    #获取店铺描述
    def get_decription(self):
        return self.get_text(shop_locator.shop_description)


