from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    def page_click_me_button(self):
        self.base_click_element(self.me_button)

    def login_if_not(self, page):
        self.page_click_me_button()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            # 说明已经登录
            return
        # 没有登录，进入登录
        page.get_register_page_instance.page_click_login_btn()
        page.get_login_page_instance.page_input_username("itheimatest")
        page.get_login_page_instance.page_input_password("1314@gensuizhu")
        page.get_login_page_instance.page_click_login_btn()
