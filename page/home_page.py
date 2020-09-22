import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    me_button = By.ID, "com.yunmall.lc:id/tab_me"
    category_button = By.ID, "com.yunmall.lc:id/tab_category"
    cart_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    @allure.step(title='主页 点击 搜索 放大镜')
    def page_click_search_button(self):
        self.base_click_element(self.search_button)

    @allure.step(title='主页 点击 购物车')
    def page_click_cart_button(self):
        self.base_click_element(self.cart_button)

    @allure.step(title='主页 点击 首页按钮')
    def page_click_home_button(self):
        self.base_click_element(self.home_button)

    @allure.step(title='主页 点击 我')
    def page_click_me_button(self):
        self.base_click_element(self.me_button)

    @allure.step(title='如果没有登录就先登录')
    def login_if_not(self, page):
        self.page_click_me_button()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            # 说明已经登录
            return
        # 没有登录，进入登录
        page.get_register_page_instance.page_click_login_btn()
        page.get_login_page_instance.page_input_username("itheimatest")
        page.get_login_page_instance.page_input_password("1314@gensuizhu")
        page.get_login_page_instance.page_click_login_btn()

    @allure.step(title='主页 点击 分类')
    def page_click_category_button(self):
        self.base_click_element(self.category_button)
