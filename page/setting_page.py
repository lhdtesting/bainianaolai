from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    about_btn = By.XPATH, "//*[@text='关于百年奥莱']"
    clear_cache_btn = By.XPATH, "//*[@text='清理缓存']"
    address_list_button = By.XPATH, "//*[@text='地址管理']"

    def page_click_about_btn(self):
        self.find_element_with_scroll(self.about_btn).click()

    def page_click_clear_cache_btn(self):
        self.find_element_with_scroll(self.clear_cache_btn).click()

    def page_click_address_list_button(self):
        self.find_element_with_scroll(self.address_list_button).click()
