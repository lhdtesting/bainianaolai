import time
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

    def base_find_elements(self, feature, timeout=10, poll=1.0):
        feature_by, feature_value = feature
        return (WebDriverWait(self.driver, timeout, poll).
                until(lambda x: x.find_elements(feature_by, feature_value)))

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

        message_xpath = By.XPATH, "//*[contains(@text, '%s')]" % message # 使用包含的方式定位
        try:
            self.base_find_element(message_xpath, timeout=5, poll=0.1)
            return True
        except TimeoutException:
            return False

    def is_feature_exist(self, feature):
        try:
            self.base_find_element(feature, timeout=5, poll=0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text, '%s')]" % message  # 使用包含的方式定位
            return self.base_find_element(message_xpath,  timeout=5, poll=0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确")

    def scroll_page_one_time(self, direction="up"):
        """滑动一次屏幕
        :param direction:
           "up":从下往上滑
           "down":从上往下滑
           "left":从右往左滑
           "right":从左往右滑
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, duration=3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, duration=3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, duration=3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, duration=3000)
        else:
            raise Exception("请检查参数是否正确？ up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """边滑边找元素
        :param feature:
        :param direction:
           "up":从下往上滑
           "down":从上往下滑
           "left":从右往左滑
           "right":从左往右滑
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.base_find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)

                if self.driver.page_source == page_source:  # 说明已经滑到底了
                    break
                page_source = self.driver.page_source

    def is_keyword_in_page_source(self, keyword, timeout=10, poll=0.1):
        """
        判断某字符串关键字是否出现在页面源码中
        :param keyword: 字符串关键字
        :param timeout:
        :param poll:
        :return: 如果字符串关键字在页面源码中，返回True,否则返回False
        """
        end_time = time.time() + timeout
        while True:
            if end_time < time.time():
                return False
            if keyword in self.driver.page_source:
                return True
            time.sleep(poll)

    def base_get_text(self, feature):
        return self.base_find_element(feature).text









