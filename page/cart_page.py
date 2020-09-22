import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CartPage(BaseAction):
    select_all_btn = By.ID, "com.yunmall.lc:id/iv_select_all"
    add_button = By.ID, "com.yunmall.lc:id/iv_add"
    edit_button = By.XPATH, "//*[@text='编辑']"
    commit_button = By.XPATH, "//*[@text='完成']"
    price = By.ID, "com.yunmall.lc:id/tv_price"
    total_price = By.ID, "com.yunmall.lc:id/tv_count_money"
    delete_cart = By.ID, "com.yunmall.lc:id/tv_del_all"
    confirm_button = By.XPATH, "//*[@text='确认']"

    @allure.step(title='购物车页面 点击删除')
    def page_click_delete_btn(self):
        self.base_click_element(self.delete_cart)

    @allure.step(title='购物车页面 点击确认按钮去')
    def page_click_confirm_btn(self):
        self.base_click_element(self.confirm_button)

    @allure.step(title='购物车页面 点击全选')
    def page_click_select_all_btn(self):
        self.base_click_element(self.select_all_btn)

    @allure.step(title='购物车页面 点击+按钮')
    def page_click_add_btn(self):
        self.base_click_element(self.add_button)

    @allure.step(title='购物车页面 点击编辑按钮')
    def page_click_edit_btn(self):
        self.base_click_element(self.edit_button)

    @allure.step(title='购物车页面 点击完成按钮')
    def page_click_commit_btn(self):
        self.base_click_element(self.commit_button)

    @allure.step(title='购物车页面 处理价格')
    def page_deal_with_price(self, price):
        return float(price[2:])

    @allure.step(title='购物车页面 获取单价')
    def page_get_price(self):
        price_text = self.base_get_text(self.price)
        return self.page_deal_with_price(price_text)

    @allure.step(title='购物车页面 获取总价')
    def page_get_total_price(self):
        total_price_text = self.base_get_text(self.total_price)
        return self.page_deal_with_price(total_price_text)

    def page_is_empty_cart(self):
        xpath = By.XPATH, "//*[contains(@text, '购物车还是空的')]"
        return self.is_feature_exist(xpath)






