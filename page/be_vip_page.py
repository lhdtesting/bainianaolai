from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class BeVipPage(BaseAction):
    invitation_code_text = By.XPATH, "//input[@type='tel']"
    be_vip_btn = By.XPATH, "//input[@value='立即成为会员']"

    def page_input_invitation_code(self, code):
        self.base_input_element(self.invitation_code_text, code)

    def page_click_be_vip_btn(self):
        self.base_click_element(self.be_vip_btn)

