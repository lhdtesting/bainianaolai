from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PersonCenterPage(BaseAction):
    nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    def page_get_nickname(self):
        return self.base_find_element(self.nickname).text
