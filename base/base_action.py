from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=10, poll=1.0):
        feature_by, feature_value = feature
        return (WebDriverWait(self.driver, timeout, poll).
                until(lambda x: x.find_element(feature_by, feature_value)))

    def base_click_element(self, feature):
        self.base_find_element(feature).click()

    def base_input_element(self, feature, value):
        ele = self.base_find_element(feature)
        ele.clear()
        ele.send_keys(value)

    # 点击返回键
    def base_back_press(self):
        self.driver.press_keycode(4)

    def is_toast_exist(self, message):

        message_xpath = By.XPATH, "//*[contains(@text, '"+message+"')]"  # 使用包含的方式定位
        try:
            self.base_find_element(message_xpath, timeout=5, poll=0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text, '"+message+"')]"  # 使用包含的方式定位
            return self.base_find_element(message_xpath,  timeout=5, poll=0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确")





