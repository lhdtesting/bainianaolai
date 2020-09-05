from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.get_home_page_instance.page_click_me_button()
        self.page.get_register_page_instance.page_click_login_btn()
        self.page.get_login_page_instance.page_input_username(username)
        self.page.get_login_page_instance.page_input_password(password)
        self.page.get_login_page_instance.page_click_login_btn()

        if toast is None:
            assert username == self.page.get_person_center_page_instance.page_get_nickname()
        else:
            assert self.page.get_login_page_instance.is_toast_exist(toast)

