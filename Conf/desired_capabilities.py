import os
from configuration import platform


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class DesiredCapabilities(object):

    capabilities = {

        "Android 4": {
            "platformName": "ANDROID",
            "platformVersion": "4.4.2",
            "deviceName": "QUANTUM_2_400",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),  # path to .apk file
            # "appPackage": "com.noggin.oca",
            # "appActivity": "com.noggin.oca.MainActivity",
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "newCommandTimeout": 60,  # How long (in seconds) Appium will wait for a new command from the client before assuming the client quit and ending the session
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "udid": "0123456789ABCDEF"
        },

        "Android 5": {
            "platformName": "ANDROID",
            "platformVersion": "5.1.1",
            "deviceName": "POP 3",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "udid": "7d7d9a62"
        },

        "Android 5 emulator": {
            "platformName": "ANDROID",
            "platformVersion": "5.1.0",
            "deviceName": "192.168.56.101:5555",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "DeviceReadyTimeout": 300  # Android only
        },

        "Android 6 emulator": {
            "platformName": "ANDROID",
            "platformVersion": "6.0",
            "deviceName": "192.168.56.101:5555",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            # "fullReset": True,
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "DeviceReadyTimeout": 300  # Android only
        },

        "Android 6": {  # UPDATED TO ANDROID 7.0
            "platformName": "ANDROID",
            "platformVersion": "6.0.1",
            # "automationName": "Appium",  # probably necessary to enable this and disable platformVersion when switching to webview context, but currently there is only NATIVE_APP context
            "deviceName": "SM-G930F",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "udid": "ad0816033848eb0443"
        },

        "Android 7": {
            "platformName": "ANDROID",
            "platformVersion": "7.0",
            "deviceName": "SM-G930F",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            # "appPackage": "com.noggin.oca",
            # "appActivity": "com.noggin.oca.MainActivity",
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            # "autoAcceptAlerts": True,  # not working with Android
            "newCommandTimeout": 60,
            "automationName": "Appium",
            # "browserName": "Chromium",
            "clearSystemFiles": True,
            # "fullReset": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "udid": "ad0816033848eb0443"
        },

        "Android 7 emulator": {
            "platformName": "ANDROID",
            "platformVersion": "7.0",
            "deviceName": "192.168.56.101:5555",
            "app": PATH("/Users/lukasl/repos/appium-poc/oca-v10.0.8.apk"),
            "appPackage": "com.noggin.ocalukasl",
            "appActivity": "com.noggin.ocalukasl.MainActivity",
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "chromedriverExecutable": "/Users/lukasl/repos/appium-poc/chromedriver",
            "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote",
            "chromeOptions": {
                "androidDeviceSocket": "com.noggin.ocalukasl_devtools_remote"
            },
            "DeviceReadyTimeout": 300  # Android only
        },

        "IOS 9": {
            # iPad mini with iOS 9.3.5
            "platformName": "iOS",
            "platformVersion": "9.3",
            "deviceName": "iPad mini",
            "app": PATH("/Users/lukasl/Build_xcode/Products/iPad9.3.5/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            "newCommandTimeout": 90,
            "autoAcceptAlerts": True,
            "automationName": "Appium",
            "clearSystemFiles": True,
            "startIWDP": True,
            # "noReset": False,
            "fullReset": True,
            "udid": "db55c238e873230ee454c54a63724397a2981acd"
        },

        "IOS 9 emulator": {
            # iPhone 5 simulator with iOS 9.3.5
            "platformName": "iOS",
            "platformVersion": "9.3",
            "deviceName": "iPhone 5",
            "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone9.3/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            "newCommandTimeout": 120,
            "launchTimeout": 400000,  # iOS only
            "clearSystemFiles": True,
            "startIWDP": True,
            "autoAcceptAlerts": True
        },

        "IOS 10": {
            # iPhone 6 with iOS 10.2 - new iOS need Xcuit Test
            "platformName": "iOS",
            "platformVersion": "10.2",
            "deviceName": "iPhone 6",
            "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone10.2/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            # "autoAcceptAlerts": True,  # not working on iOS10
            "xcodeOrgId": "5MJR4HSABR",  # 10 characters string generated by Apple - search for it in Xcode
            "xcodeSigningId": "iPhone Developer",
            # "useNewWDA": True,  # If True, forces uninstall of any existing WebDriverAgent app on device
            "usePrebuiltWDA": True,  # Skips the build phase of running the WDA app
            "preventWDAAttachments": True,  # capability to help with XCUITest speed and disk usage
            "showXcodeLog": True,
            # "showIOSLog": True,
            "automationName": "XCUITest",
            # "autoWebview": True,
            "newCommandTimeout": 60,
            "clearSystemFiles": True,
            "startIWDP": True,  # start ios-webkit-debug-proxy
            "noReset": False,
            "fullReset": False,
            "udid": "4b15c4284897fa6f9b4c5205325a9cece997ad35"
        },

        "IOS 10 emulator": {
            # iPhone 7 simulator with iOS 10.2
            "platformName": "iOS",
            "platformVersion": "10.2",
            "deviceName": "iPhone 7",
            "app": PATH("/Users/lukasl/Build_xcode/Products/iPhone7/OCA.app"),
            "bundleId": "com.noggin.ocalukasl",
            "newCommandTimeout": 120,
            "launchTimeout": 400000,  # iOS only
            "automationName": "XCUITest",
            "xcodeOrgId": "5MJR4HSABR",
            "xcodeSigningId": "iPhone Developer",
            "showXcodeLog": True,
            "clearSystemFiles": True,
            "startIWDP": True,
            "preventWDAAttachments": True,  # capability to help with XCUITest speed and disk usage
            "usePrebuiltWDA": True
        },

    }

    @staticmethod
    def get_desired_capabilities():

        # return DesiredCapabilities.capabilities[ENVIRONMENT_TEST + PLATFORM_VERSION]
        return DesiredCapabilities.capabilities[platform]
