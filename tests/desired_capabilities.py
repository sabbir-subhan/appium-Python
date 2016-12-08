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
        "newCommandTimeout": "600",
        "udid": "0123456789ABCDEF"
    }

    desired_capabilities_for_android_5 = {
        "platformName": "ANDROID",
        "platformVersion": "5.1.1",
        "deviceName": "Alcatel POP3",
        "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        "appPackage": "com.noggin.oca",
        "appActivity": "com.noggin.oca.OCApp",
        "newCommandTimeout": "600",
        "udid": "7d7d9a62"
    }

    desired_capabilities_for_android_6 = {
        "platformName": "ANDROID",
        "platformVersion": "6.0.1",
        "deviceName": "Samsung Galaxy S7",
        #"app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        "app": PATH("/Users/lukasl/repos/appium-poc/com.noggin.oca.apk"),
        "appPackage": "com.noggin.oca",
        "appActivity": "com.noggin.oca.OCApp",
        "newCommandTimeout": "600",
        "udid": "ad0816033848eb0443"
    }

    desired_capabilities_for_iOS_iPad = {
        # iPad mini with iOS 9.3.5
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPad mini",
        "app": PATH("/Users/lukasl/Library/Developer/Xcode/DerivedData"
                    "/OCA-bdxtjnqokrqssihekwhfopxonvwa/Build/Products/Debug-iphoneos/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "600",
        "udid": "db55c238e873230ee454c54a63724397a2981acd"
    }

    desired_capabilities_for_iOS_iPhone4 = {
        # iPhone 4s simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 4s",
        "app": PATH("/Users/lukasl/Library/Developer/Xcode/DerivedData/"
                    "OCA-bdxtjnqokrqssihekwhfopxonvwa/Build/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "600"
    }

    desired_capabilities_for_iOS_iPhone5 = {
        # iPhone 5 simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 5",
        "app": PATH("/Users/lukasl/Library/Developer/Xcode/DerivedData/"
                    "OCA-bdxtjnqokrqssihekwhfopxonvwa/Build/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "600"
    }

    desired_capabilities_for_iOS_iPhone6 = {
        # iPhone 6s simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 6",
        "app": PATH("/Users/lukasl/Library/Developer/Xcode/DerivedData"
                    "/OCA-bdxtjnqokrqssihekwhfopxonvwa/Build/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "600"
    }
