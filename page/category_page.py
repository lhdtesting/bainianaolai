import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    @allure.step(title='分类页面 商品列表中随机点击一个商品')
    def page_click_goods_list(self):
        goods_list = self.base_find_elements(self.goods_list_button)
        list_count = len(goods_list)
        list_index = random.randint(0, list_count-1)
        goods_list[list_index].click()
