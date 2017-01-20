import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class DesiredCapabilities(object):

    desired_capabilities_for_android_4 = {
        "platformName": "ANDROID",
        "platformVersion": "4.4.2",
        "deviceName": "QUANTUM_2_400",
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "80",
        "androidDeviceReadyTimeout": "60",
        "udid": "0123456789ABCDEF"
    }

    desired_capabilities_for_android_simulator_4 = {
        "platformName": "ANDROID",
        "platformVersion": "4.4.4",
        "deviceName": "Samsung Galaxy Note 3",
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "80",
        "androidDeviceReadyTimeout": "60"
    }

    desired_capabilities_for_android_5 = {
        "platformName": "ANDROID",
        "platformVersion": "5.1.1",
        "deviceName": "POP 3",
        # "app": PATH("/Users/lukasl/repos/appium-poc/com.noggin.oca.apk"),
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "45",
        "udid": "7d7d9a62"
    }

    desired_capabilities_for_android_6 = {
        "platformName": "ANDROID",
        "platformVersion": "6.0.1",
        # "automationName": "Appium",                       # probably necessary to enable this and disable platformVersion when switching to webview context, but currently there is only NATIVE_APP context
        "deviceName": "SM-G930F",
        # "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
        # "app": PATH("/Users/lukasl/repos/appium-poc/com.noggin.oca.apk"),
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        # "apppackage": "com.noggin.ocalukasl",
        # "appactivity": "com.noggin.ocalukasl.MainActivity",
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "60",
        # "unicodekeyboard": "true",
        # "resetkeyboard": "true",
        "udid": "ad0816033848eb0443"
    }

    desired_capabilities_for_android_simulator_6 = {
        "platformName": "ANDROID",
        "platformVersion": "6.0.0",
        "deviceName": "android6",
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "60",
        "androidDeviceReadyTimeout": "60",
        "udid": "emulator-5554"
    }

    desired_capabilities_for_android_simulator_7 = {
        "platformName": "ANDROID",
        "platformVersion": "7.0.0",
        "deviceName": "Google Nexus 5X",
        "app": PATH("/Users/lukasl/repos/appium-poc/oca-v9.2.2.apk"),
        "apppackage": "com.noggin.oca",
        "appactivity": "com.noggin.oca.MainActivity",
        "newCommandTimeout": "60",
        "androidDeviceReadyTimeout": "60"
    }

    desired_capabilities_for_iOS_10_iPhone6 = {
        # iPhone 6 with iOS 10.2 - new iOS needs XCuit
        "platformName": "iOS",
        "platformVersion": "10.2",
        "deviceName": "iPhone 6",
        "app": PATH("/Users/lukasl/Build_xcode/Products/Debug-iphoneos/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        # "autoAcceptAlerts": "true",
        "xcodeOrgId": "5MJR4HSABR",
        "xcodeSigningId": "iPhone Developer",
        "useNewWDA": "true",  # If true, forces uninstall of any existing WebDriverAgent app on device
        "showXcodeLog": "true",  # show more logs in console
        "automationName": "XCUITest",
        "udid": "4b15c4284897fa6f9b4c5205325a9cece997ad35"
    }

    desired_capabilities_for_iOS_iPad = {
        # iPad mini with iOS 9.3.5
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPad mini",
        "app": PATH("/Users/lukasl/Build_xcode/Products/Debug-iphoneos/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        # "newCommandTimeout": "45",
        "autoAcceptAlerts": "true",
        "udid": "db55c238e873230ee454c54a63724397a2981acd"
    }

    desired_capabilities_for_iOS_iPhone4 = {
        # iPhone 4s simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 4s",
        "app": PATH("/Users/lukasl/Build_xcode/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "45",
        "autoAcceptAlerts": "true"
    }

    desired_capabilities_for_iOS_iPhone5 = {
        # iPhone 5 simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 5",
        "app": PATH("/Users/lukasl/Build_xcode/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "45",
        "autoAcceptAlerts": "true"
    }

    desired_capabilities_for_iOS_iPhone6s = {
        # iPhone 6s simulator with iOS 9.3
        "platformName": "iOS",
        "platformVersion": "9.3",
        "deviceName": "iPhone 6s",
        "app": PATH("/Users/lukasl/Build_xcode/Products/Debug-iphonesimulator/OCA.app"),
        "bundleId": "com.noggin.ocalukasl",
        "newCommandTimeout": "45",
        "autoAcceptAlerts": "true"
    }
