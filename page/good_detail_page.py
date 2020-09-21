import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodDetailPage(BaseAction):
    add_shop_cart_button = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
    confirm_button = By.ID, "com.yunmall.lc:id/select_detail_sure_btn"
    good_title = By.ID, "com.yunmall.lc:id/tv_product_title"
    shop_cart = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

    # 获取商品标题
    def page_get_good_title(self):
        return self.base_get_text(self.good_title)

    # 根据标题判断商品是否存在页面上
    def page_is_good_title_exist(self, title):
        title_xpath = By.XPATH, "//*[@text='%s']" % title
        return self.is_feature_exist(title_xpath)

    def page_click_shop_cart(self):
        self.base_click_element(self.shop_cart)

    def page_click_add_cart_btn(self):
        self.base_click_element(self.add_shop_cart_button)

    def page_click_confirm_btn(self):
        self.base_click_element(self.confirm_button)

    def choose_spec(self, text):
        return text.split(" ")[1]

    def click_spec(self):
        while True:
            self.page_click_confirm_btn()
            if self.is_toast_exist("请选择"):
                spec_name = self.choose_spec(self.get_toast_text("请选择"))
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.base_click_element(spec_feature)
            else:
                break
