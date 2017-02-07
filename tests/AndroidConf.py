# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class AndroidConf:

    LOGIN_BUTTON_android = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOGIN")]]')
