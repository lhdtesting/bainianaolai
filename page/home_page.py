from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    def page_click_me_button(self):
        self.base_click_element(self.me_button)