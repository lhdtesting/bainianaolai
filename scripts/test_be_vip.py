from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestBeVip:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_be_vip(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_person_center_page_instance.page_click_be_vip()
        sleep(4)
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.page.get_be_vip_instance.page_input_invitation_code("hahaaaa")
        self.page.get_be_vip_instance.page_click_be_vip_btn()
        self.driver.switch_to.context("NATIVE_APP")
