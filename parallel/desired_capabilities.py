import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class DesiredCapabilities(object):

    desired_capabilities_for_android_4 = {
        "platformName": "ANDROID",
        "platformVersion": "4.4.2",
        "deviceName": "QUANTUM_2_400",
        "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        "appPackage": "com.noggin.oca",
        "appActivity": "com.noggin.oca.OCApp",
        "udid": "0123456789ABCDEF",
        "newCommandTimeout": "600"
    }

    desired_capabilities_for_android_5 = {
        "platformName": "ANDROID",
        "platformVersion": "5.1.1",
        "deviceName": "Alcatel POP3",
        "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        "appPackage": "com.noggin.oca",
        "appActivity": "com.noggin.oca.OCApp",
        "udid": "7d7d9a62",
        "newCommandTimeout": "600"
    }

    desired_capabilities_for_android_6 = {
        "platformName": "ANDROID",
        "platformVersion": "6.0.1",
        "deviceName": "Samsung Galaxy S7",
        "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        "appPackage": "com.noggin.oca",
        "appActivity": "com.noggin.oca.OCApp",
        "udid": "ad0816033848eb0443",
        "newCommandTimeout": "600"
    }
