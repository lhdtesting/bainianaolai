

from appium import webdriver

# server 启动参数
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
# 比如版本是5.2.3，可以写成 “5.2.3”，“5.2”，“5”
desired_caps['platformVersion'] = '5.1'
# android随便写，但是不能不写，也不能为空字符串
# iOS不能随便写，写成“iPhone 8”
desired_caps['deviceName'] = '192.168.56.101:5555'
# 可以输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def scroll_to_feature(feature, direction="up"):
    """
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
            driver.find_element(*feature).click()
            break
        except Exception:

            width = driver.get_window_size()["width"]
            height = driver.get_window_size()["height"]
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
                driver.swipe(bottom_x, bottom_y, top_x, top_y, duration=3000)
            elif direction == "down":
                driver.swipe(top_x, top_y, bottom_x, bottom_y, duration=3000)
            elif direction == "left":
                driver.swipe(right_x, right_y, left_x, left_y, duration=3000)
            elif direction == "right":
                driver.swipe(left_x, left_y, right_x, right_y, duration=3000)
            else:
                raise Exception("请检查参数是否正确？ up/down/left/right")
            if driver.page_source == page_source:
                print("到底了")
                break
            page_source = driver.page_source


scroll_to_feature((By.XPATH, "//*[@text='关于手机']"), "up")













