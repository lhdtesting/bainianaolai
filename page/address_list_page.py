import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    new_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"
    default_receipt_text = By.ID, "com.yunmall.lc:id/receipt_name"
    default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    @allure.step(title='地址管理页面 点击新增地址')
    def page_click_new_address_btn(self):
        self.find_element_with_scroll(self.new_address_button).click()

    @allure.step(title='地址管理页面 获取收件人信息')
    def page_get_receipt_text(self):
        return self.base_get_text(self.default_receipt_text)

    def page_is_feature_exist(self):
        return self.is_feature_exist(self.default_feature)

    @allure.step(title='地址管理页面 点击默认地址')
    def page_click_default_address(self):
        self.base_click_element(self.default_feature)


