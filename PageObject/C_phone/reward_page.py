'''赏金页面'''

from PageLocators.C_phone import reward_locator
from Common.basepage import BasePage

class RewardPage(BasePage):
    name = '用户赏金页面'

    #获取头部文本
    def get_rewardtext(self):
        return self.get_text(reward_locator.reward_text,model=self.name)

