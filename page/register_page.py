from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class RegisterPage(BaseAction):
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    def page_click_login_btn(self):
        self.base_click_element(self.login_button)