SOFT NEEDED:

- Java
- Android studio and APIs for android - android avd
- Python + pip
- Selenium  (pip install -U selenium)
- Appium client for python  (pip install Appium-Python-Client)
- Appium app from official website
- PyCharm - for running tests


for OSX:

- all above plus
- xcode 7.3 (version 8 is not supported by appium)
- node
- npm
- brew
- brew install libimobiledevice

need udid from real device - open iTunes with connected device and click on serial number
iOS version and device name for "desire_capabilities.py"
in appium yous need to provide path to app - to get app file you need to build it in xcode



Appium in CLI:

- npm install -g appium
- npm install wd
appium -p 4723 -bp 5724 --session-override --log-level debug




CONFIGURING ANDROID DEVICE:

1. enable developer mode
2. enable USB debugging
3. disable “Auto capitalize” in keyboard settings - because login starts from small letter “b”
4. prevent device from disabling - enable option stay awake while plugged in
5. unlock device and prevent automatic locking


PULLING APK FILE FROM ANDROID DEVICE:
(You can use app file from repo "com.noggin.oca.apk")

first - install app from google store
next open terminal and use:

adb devices
adb shell pm list packages
adb shell pm path com.noggin.
adb pull /data/app/com.noggin.oca.apk
aapt dump badging com.noggin.oca.apk

finding app activity through adb - appActivity:
android adb devices
adb shell
dumpsys window windows | grep -E ‘mCurrentFocus|mFocusedApp’
(app need to be open on device)



BUILDING .APP FILE ON OSX:

build app through cordova
build app through xcode
on real device, first You need to run app from xcode - it will install it on the device (You have to TRUST app in General - Device management)


STARTING APPIUM:
- provide paths for android sdk and xcode
- provide path to app file (android - .apk file, ios - .app file from xcode)
- for iOS provide BundleID from xcode, check "Force device", type device name and check "UDID" (search for it in iTunes)


file desired_capabilities.py need to be updated accordingly to used device:
- it contains names of devices
- UDDID
- OS version and name

to use device defined in desired_capabilities.py You need to open test case and change line:
"desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad" for example to:
"desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPhone6"



issues:

- Test Case 2 is not working correctly because there is bug in OCA mobile app = alerts are not visible after login
- some elements have attribute visible: false and appium is unable to interact with those elements for example map
- for some reason test sometime fail to start in first run, but after running it again it is working correctly 
- Test Case 3 - test 3 --still need some fix with "hamburger button"