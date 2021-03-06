import allure

from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class LoginPage(BaseAction):
    username = By.ID, "com.yunmall.lc:id/logon_account_textview"
    password = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_btn = By.XPATH, "//*[@text='登录']"

    @allure.step(title='登录页面 输入用户名')
    def page_input_username(self, username):
        self.base_input_element(self.username, username)

    @allure.step(title='登录页面 输入密码')
    def page_input_password(self, password):
        self.base_input_element(self.password, password)

    @allure.step(title='登录页面 点击登录')
    def page_click_login_btn(self):
        self.base_click_element(self.login_btn)
