from time import sleep

import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestSearch:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("search_data.yaml", "test_search"))
    def test_search(self, args):
        keyword = args["keyword"]
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_home_page_instance.page_click_home_button()
        self.page.get_home_page_instance.page_click_search_button()
        self.page.get_search_page_instance.page_input_search_keyword(keyword)
        self.page.get_search_page_instance.page_click_search_button()
        time.sleep(2)
        self.page.get_search_page_instance.page_click_back_button()
        assert self.page.get_search_page_instance.page_is_search_keyword_exist(keyword)

    def test_delete_history(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_home_page_instance.page_click_home_button()
        self.page.get_home_page_instance.page_click_search_button()
        self.page.get_search_page_instance.page_input_search_keyword("面膜")
        self.page.get_search_page_instance.page_click_search_button()
        time.sleep(2)
        self.page.get_search_page_instance.page_click_back_button()
        self.page.get_search_page_instance.page_click_delete_history_button()
        assert self.page.get_search_page_instance.page_is_feature_exist()




