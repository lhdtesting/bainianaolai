from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestCart:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_cart(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_home_page_instance.page_click_category_button()
        self.page.get_category_page_instance.page_click_goods_list()
        self.page.get_goods_list_page_instance.page_click_goods_btn()
        good_title = self.page.get_good_detail_page_instance.page_get_good_title()
        self.page.get_good_detail_page_instance.page_click_add_cart_btn()
        self.page.get_good_detail_page_instance.click_spec()
        self.page.get_good_detail_page_instance.page_click_shop_cart()
        assert self.page.get_good_detail_page_instance.page_is_good_title_exist(good_title)

