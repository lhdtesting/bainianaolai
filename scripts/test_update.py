from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_update(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_person_center_page_instance.page_click_setting_btn()
        self.page.get_setting_page_instance.page_click_about_btn()
        self.page.get_about_page_instance.page_click_update_btn()

        assert self.page.get_about_page_instance.is_toast_exist("当前已是最新版本")
