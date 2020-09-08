from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):
    update_btn = By.XPATH, "//*[@text='版本更新']"

    def page_click_update_btn(self):
        self.base_click_element(self.update_btn)
