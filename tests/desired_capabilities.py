import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "4.4",
    "deviceName": "QUANTUM_2_400",
    "app": PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk"),
    "appPackage": "com.noggin.oca",
    "appActivity": "com.noggin.oca.OCApp"
}


