from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=10, poll=0.5):
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



