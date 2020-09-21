from time import sleep

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PersonCenterPage(BaseAction):
    nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    be_vip = By.XPATH, "//*[@text='加入超级VIP']"

    @allure.step(title='我的页面获取昵称')
    def page_get_nickname(self):
        return self.base_find_element(self.nickname).text

    @allure.step(title='我的页面点击设置')
    def page_click_setting_btn(self):
        self.find_element_with_scroll(self.setting_btn).click()

    @allure.step(title='我的页面点击加入VIP')
    def page_click_be_vip(self):
        self.find_element_with_scroll(self.be_vip).click()

