from time import sleep

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PersonCenterPage(BaseAction):
    nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    be_vip = By.XPATH, "//*[@text='加入超级VIP']"

    def page_get_nickname(self):
        return self.base_find_element(self.nickname).text

    def page_click_setting_btn(self):
        self.find_element_with_scroll(self.setting_btn).click()

    def page_click_be_vip(self):
        self.find_element_with_scroll(self.be_vip).click()

