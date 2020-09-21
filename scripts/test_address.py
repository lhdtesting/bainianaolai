from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))
    def test_add_address(self, args):
        receipt_name = args["receipt_name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_person_center_page_instance.page_click_setting_btn()
        self.page.get_setting_page_instance.page_click_address_list_button()
        self.page.get_address_list_instance.page_click_new_address_btn()
        self.page.get_edit_address_page_instance.page_input_receipt(receipt_name)
        self.page.get_edit_address_page_instance.page_input_phone(phone)
        self.page.get_edit_address_page_instance.page_input_detail_address(info)
        self.page.get_edit_address_page_instance.page_input_post_code(post_code)
        self.page.get_edit_address_page_instance.page_click_default_address_btn()
        self.page.get_edit_address_page_instance.page_choose_region()
        self.page.get_edit_address_page_instance.page_click_save_button()

        if toast is None:
            assert self.page.get_address_list_instance.page_get_receipt_text() == "%s  %s" % (receipt_name, phone)
        else:
            assert self.page.get_edit_address_page_instance.is_toast_exist(toast), "toast信息与实际信息不符"

    def test_edit_address(self):
        self.page.get_home_page_instance.login_if_not(self.page)
        self.page.get_person_center_page_instance.page_click_setting_btn()
        self.page.get_setting_page_instance.page_click_address_list_button()

        if not self.page.get_address_list_instance.page_is_feature_exist():
            self.page.get_address_list_instance.page_click_new_address_btn()
            self.page.get_edit_address_page_instance.page_input_receipt("落落")
            self.page.get_edit_address_page_instance.page_input_phone("15348796574")
            self.page.get_edit_address_page_instance.page_input_detail_address("四单元675")
            self.page.get_edit_address_page_instance.page_input_post_code("245698")
            self.page.get_edit_address_page_instance.page_click_default_address_btn()
            self.page.get_edit_address_page_instance.page_choose_region()
            self.page.get_edit_address_page_instance.page_click_save_button()

        self.page.get_address_list_instance.page_click_default_address()
        self.page.get_edit_address_page_instance.page_input_receipt("凯凯")
        self.page.get_edit_address_page_instance.page_input_phone("18975648975")
        self.page.get_edit_address_page_instance.page_input_post_code("123654")
        self.page.get_edit_address_page_instance.page_input_detail_address("滋镇三回合")
        self.page.get_edit_address_page_instance.page_click_save_button()
        assert self.page.get_address_list_instance.is_toast_exist("保存成功")


