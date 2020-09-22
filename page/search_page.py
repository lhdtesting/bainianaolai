import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    search_keyword_text = By.ID, "com.yunmall.lc:id/text_search_keyword"
    search_button = By.XPATH, "//*[@text='搜索']"
    back_button = By.ID, "com.yunmall.lc:id/btn_back"
    delete_history_button = By.ID, "com.yunmall.lc:id/search_del"

    @allure.step(title='搜索页面 点击删除搜索记录 ')
    def page_click_delete_history_button(self):
        self.base_click_element(self.delete_history_button)

    @allure.step(title='搜索页面 输入关键字 ')
    def page_input_search_keyword(self, keyword):
        self.base_input_element(self.search_keyword_text, keyword)

    @allure.step(title='搜索页面 点击 搜索按钮 ')
    def page_click_search_button(self):
        self.base_click_element(self.search_button)

    @allure.step(title='搜索页面 点击 返回按钮 ')
    def page_click_back_button(self):
        self.base_click_element(self.back_button)

    def page_is_search_keyword_exist(self, keyword):
        xpath = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        return self.is_feature_exist(xpath)

    def page_is_feature_exist(self):
        feature = By.XPATH, "//*[@text='暂无搜索历史']"
        return self.is_feature_exist(feature)

