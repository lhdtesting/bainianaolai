import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    def page_click_goods_list(self):
        goods_list = self.base_find_elements(self.goods_list_button)
        list_count = len(goods_list)
        print(list_count)
        list_index = random.randint(0, list_count-1)
        goods_list[list_index].click()
