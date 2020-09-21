import random

import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    receipt_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    phone_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    detail_address_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"
    region_button = By.ID, "com.yunmall.lc:id/address_province"
    province_button = By.ID, "com.yunmall.lc:id/area_title"
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    @allure.step(title='编辑地址页面 输入收件人')
    def page_input_receipt(self, receipt_name):
        self.base_input_element(self.receipt_text, receipt_name)

    @allure.step(title='编辑地址页面 输入电话')
    def page_input_phone(self, phone):
        self.base_input_element(self.phone_text, phone)

    @allure.step(title='编辑地址页面 输入详细地址')
    def page_input_detail_address(self, detail_address):
        self.base_input_element(self.detail_address_text, detail_address)

    @allure.step(title='编辑地址页面 输入邮编')
    def page_input_post_code(self, post_code):
        self.base_input_element(self.post_code_edit_text, post_code)

    @allure.step(title='编辑地址页面 点击设置默认地址')
    def page_click_default_address_btn(self):
        self.base_click_element(self.default_address_button)

    @allure.step(title='编辑地址页面 点击区域')
    def page_click_region_button(self):
        self.base_click_element(self.region_button)

    @allure.step(title='编辑地址页面 选择地区')
    def page_choose_region(self):
        self.page_click_region_button()
        time.sleep(2)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            provinces = self.base_find_elements(self.province_button)
            areas_count = len(provinces)
            areas_index = random.randint(0, areas_count - 1)
            provinces[areas_index].click()
            time.sleep(2)

    def page_click_save_button(self):
        self.base_click_element(self.save_button)



