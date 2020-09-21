import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsListPage(BaseAction):
    goods_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    def page_click_goods_btn(self):
        goods_list = self.base_find_elements(self.goods_button)
        list_count = len(goods_list)
        list_index = random.randint(0, list_count-1)
        goods_list[list_index].click()
