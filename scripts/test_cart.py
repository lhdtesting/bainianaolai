from time import sleep

import time

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

    def test_cart_price(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_home_page_instance.page_click_cart_button()
        self.page.get_cart_page_instance.page_click_select_all_btn()
        total_price = self.page.get_cart_page_instance.page_get_total_price()
        self.page.get_cart_page_instance.page_click_edit_btn()
        self.page.get_cart_page_instance.page_click_add_btn()
        self.page.get_cart_page_instance.page_click_commit_btn()
        assert self.page.get_cart_page_instance.page_get_total_price() == total_price + self.page.get_cart_page_instance.page_get_price()

    def test_delete_cart(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_home_page_instance.page_click_cart_button()
        if self.page.get_cart_page_instance.page_is_empty_cart():
            self.page.get_home_page_instance.page_click_category_button()
            self.page.get_category_page_instance.page_click_goods_list()
            self.page.get_goods_list_page_instance.page_click_goods_btn()
            self.page.get_good_detail_page_instance.page_click_add_cart_btn()
            self.page.get_good_detail_page_instance.click_spec()
            self.page.get_good_detail_page_instance.base_back_press()
            time.sleep(4)
            self.page.get_good_detail_page_instance.base_back_press()
        self.page.get_home_page_instance.page_click_cart_button()
        self.page.get_cart_page_instance.page_click_select_all_btn()
        self.page.get_cart_page_instance.page_click_edit_btn()
        self.page.get_cart_page_instance.page_click_delete_btn()
        self.page.get_cart_page_instance.page_click_confirm_btn()
        assert self.page.get_cart_page_instance.is_toast_exist("删除成功")
        assert self.page.get_cart_page_instance.page_is_empty_cart()



