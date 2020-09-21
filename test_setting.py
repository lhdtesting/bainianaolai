

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


















