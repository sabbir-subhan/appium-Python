import os
from configuration import platform, PROJECT_ROOT
import logging
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )


class DesiredCapabilities(object):

    logging.info("Setting up the desired_capabilities")

    capabilities = {

        "Android_4": {
            "platformName": "ANDROID",
            "platformVersion": "4.4.2",
            "deviceName": "QUANTUM_2_400",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8.apk"),  # path to .apk file
            # "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),  # path to .apk file
            # "appPackage": "com.noggin.oca",
            # "appActivity": "com.noggin.oca.MainActivity",
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 15,
            # "newCommandTimeout": "60",  # How long (in seconds) Appium will wait for a new command from the client before assuming the client quit and ending the session
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            # "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "recreateChromeDriverSessions": True,
            "udid": "0123456789ABCDEF"
        },

        "Android_4_emulator": {
            # Google Nexus 4 - 4.4.2 - API 19 - 768x1280
            "platformName": "ANDROID",
            "platformVersion": "4.4.2",
            "deviceName": "192.168.56.101:5556",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8-x86.apk"),  # path to .apk file
            # "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8-x86.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "recreateChromeDriverSessions": True,
            "androidDeviceReadyTimeout": 60  # Android only
        },

        "Android_5": {
            "platformName": "ANDROID",
            "platformVersion": "5.1.1",
            "deviceName": "POP 3",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "automationName": "Appium",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "recreateChromeDriverSessions": True,
            "udid": "7d7d9a62"
        },

        "Android_5_emulator": {
            "platformName": "ANDROID",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8-x86.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "recreateChromeDriverSessions": True,
            "androidDeviceReadyTimeout": 60  # Android only
        },

        "Android_6_emulator": {
            # Google Nexus 5X
            "platformName": "ANDROID",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8-x86.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "fullReset": True,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "androidDeviceReadyTimeout": 60  # Android only
        },

        "Android_6": {
            "platformName": "ANDROID",
            "platformVersion": "6.0.1",
            # "automationName": "Appium",  # probably necessary to enable this and disable platformVersion when switching to webview context, but currently there is only NATIVE_APP context
            "deviceName": "SM-G930F",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "udid": "ad0816033848eb0443"
        },

        "Android_7": {
            "platformName": "ANDROID",
            "platformVersion": "7.0",
            "deviceName": "SM-G930F",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8.apk"),  # path to .apk file
            # "appPackage": "com.noggin.oca",
            # "appActivity": "com.noggin.oca.MainActivity",
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            # "automationName": "Appium",  # (by default appium passes to appium-android-driver on the absence of automationName)
            "automationName": "uiautomator2",
            # "autoAcceptAlerts": True,  # not working with Android
            # "browserName": "Chromium",
            "clearSystemFiles": True,
            # "fullReset": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "recreateChromeDriverSessions": True,
            "udid": "ad0816033848eb0443"
        },

        "Android_7_emulator": {
            # Google Nexus 5X - 7.0.0 - API 24 - 1080x1920 or emulator-5556
            "platformName": "ANDROID",
            "platformVersion": "7.0",
            # "deviceName": "192.168.56.101:5555",
            "deviceName": "emulator-5556",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8-x86.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "recreateChromeDriverSessions": True,
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "androidDeviceReadyTimeout": 60  # Android only
        },

        "Android_7.1_emulator": {
            # Google Nexus 5X - API 25
            "platformName": "ANDROID",
            "platformVersion": "7.1",
            "deviceName": "emulator-5554",
            "app": os.path.join(PROJECT_ROOT, "oca-v10.0.8-x86.apk"),  # path to .apk file
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "appWaitActivity": "com.noggin.ocalukasl.MainActivity",
            "automationName": "uiautomator2",
            # "appWaitDuration": 20000,
            "deviceReadyTimeout": 5,
            # "fullReset": True,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "chromedriverExecutable": os.path.join(PROJECT_ROOT, "chromedriver"),
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "androidDeviceReadyTimeout": 60  # Android only
        },

        "IOS_9_iPad": {
            # iPad mini with iOS 9.3.5
            "platformName": "iOS",
            "platformVersion": "9.3",
            "deviceName": "iPad mini 1024x768",
            "app": os.path.join(PROJECT_ROOT, "iPad_9.3.5_OCA.app"),  # path to .apk file
            # "app": PATH("/Users/lukasl/Build_xcode/Products/iPad9.3.5/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            # "newCommandTimeout": "60",
            "autoAcceptAlerts": True,
            "automationName": "Appium",
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            # "noReset": False,
            "fullReset": True,  # iOS9 is not logging out automatically so fullReset is necessary
            "udid": "db55c238e873230ee454c54a63724397a2981acd"
        },

        "IOS_9_emulator": {
            # iPhone 5s simulator with iOS 9.3.5
            "platformName": "iOS",
            "platformVersion": "9.3",
            "deviceName": "iPhone 5s",
            "app": os.path.join(PROJECT_ROOT, "iPhone_9.3_OCA.app"),  # path to .apk file
            # "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone9.3/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            "newCommandTimeout": 60,
            "launchTimeout": 200000,  # iOS only
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            "fullReset": False,  # if True - Uninstall app after real device test, destroy Simulator after sim test
            "noReset": True,  # if True - Do not destroy or shut down sim after test. Start tests running on whichever sim is running, or device is plugged in
            "autoAcceptAlerts": True
        },

        "IOS_10": {
            # iPhone 6 with iOS 10.2 - new iOS need Xcuit Test
            "platformName": "iOS",
            "platformVersion": "10.3",
            "deviceName": "iPhone 6",
            "app": os.path.join(PROJECT_ROOT, "iPhone6_10.3_OCA.app"),  # path to .apk file (real device has different apk file than emulator)
            # "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone10.2/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            # "autoAcceptAlerts": True,  # not working on iOS10
            "xcodeOrgId": "5MJR4HSABR",  # 10 characters string generated by Apple - search for it in Xcode
            "xcodeSigningId": "iPhone Developer",
            # "useNewWDA": True,  # If True, forces uninstall of any existing WebDriverAgent app on device
            "usePrebuiltWDA": True,  # Skips the build phase of running the WDA app
            "preventWDAAttachments": True,  # capability to help with XCUITest speed and disk usage
            # "showXcodeLog": True,
            # "showIOSLog": True,
            "automationName": "XCUITest",
            # "autoWebview": True,
            # "newCommandTimeout": "60",
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            "noReset": False,
            "fullReset": False,
            "udid": "4b15c4284897fa6f9b4c5205325a9cece997ad35"
        },

        "IOS_10_iPad": {
            # iPad with iOS 10.3
            "platformName": "iOS",
            "platformVersion": "10.3",
            "deviceName": "iPad 2048x1536",
            "app": os.path.join(PROJECT_ROOT, "iPad_10.3_OCA.app"),  # path to .apk file
            "bundleId": "com.noggin.ocalukasl",
            "xcodeOrgId": "5MJR4HSABR",  # 10 characters string generated by Apple - search for it in Xcode
            "xcodeSigningId": "iPhone Developer",
            "usePrebuiltWDA": True,  # Skips the build phase of running the WDA app
            "preventWDAAttachments": True,  # capability to help with XCUITest speed and disk usage
            "automationName": "XCUITest",
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            "noReset": False,
            "fullReset": False,
            "udid": "16edd6bdad3ea6ba8a00a034adfe70ecaa03c639"
        },

        "IOS_10_emulator": {
            # iPhone 7 simulator with iOS 10.3
            "platformName": "iOS",
            "platformVersion": "10.3",
            "deviceName": "iPhone 7",
            "app": os.path.join(PROJECT_ROOT, "iPhone_10.3_OCA.app"),  # path to .apk file
            # "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone7/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            # "newCommandTimeout": "60",
            "launchTimeout": 200000,  # iOS only
            "automationName": "XCUITest",
            "xcodeOrgId": "5MJR4HSABR",
            "xcodeSigningId": "iPhone Developer",
            # "showXcodeLog": True,
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            "preventWDAAttachments": True,  # capability to help with XCUITest speed and disk usage
            # "useNewWDA": True,
            "usePrebuiltWDA": True,
            "noReset": False,
            "fullReset": False
        },

    }

    @staticmethod
    def get_desired_capabilities():

        # return DesiredCapabilities.capabilities[ENVIRONMENT_TEST + PLATFORM_VERSION]
        return DesiredCapabilities.capabilities[platform]
