# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class iOSConf:

    LOGIN_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "LOGIN")]]')
