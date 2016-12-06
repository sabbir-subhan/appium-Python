SOFT NEEDED:

- Java
- Android studio and APIs for android - android avd
- Python + pip
- Selenium  (pip install -U selenium)
- Appium client for python  (pip install Appium-Python-Client)
- Appium app from official website
- PyCharm - for opening and running tests (also could be run from terminal)


for OSX all above plus:

- xcode 8.1 (version 8 is not supported by appium but brew need version 8.1 to install libimobiledevice - so install xcode 8.1 froma appstore)
- node
- npm
- brew
- brew install libimobiledevice
- brew install ideviceinstaller
- rename xcode - applications - xcode -- rename to: xcode8
- download xcode 7.3 and install - open appium and add path to xcode 7.3

You probably also need to use:

- sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer/
- sudo chmod -R 777 /var/db/lockdown/


need UDID from real device - open iTunes with connected device and click on serial number
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

- first - install app from google store

next open terminal and use:

- adb devices
- adb shell pm list packages
- adb shell pm path com.noggin.
- adb pull /data/app/com.noggin.oca.apk
- aapt dump badging com.noggin.oca.apk

finding app activity through adb - appActivity:
- android adb devices
- adb shell
- dumpsys window windows | grep -E ‘mCurrentFocus|mFocusedApp’
 (app need to be open on device)



BUILDING .APP FILE ON OSX:

- edit config.xml - change "id" for example to "com.noggin.oca$YOUR_USER_NAME"
- build app through cordova
- enable developer mode on device
- open project in xcode and change Bundle Identifier accordingly to "id" above
- build app through xcode (7.3)
- on real device, first You need to run app from xcode - it will install it on the device (You have to TRUST app in General - Device management)


STARTING APPIUM:

- provide paths for android sdk and xcode
- provide path to app file (android - .apk file, ios - .app file from xcode(xcode build the app file for example in /Users/$USER/Library/Developer/Xcode/DerivedData/))
- for iOS provide BundleID from xcode, check "Force device", type device name and check "UDID" (search for it in iTunes)


file desired_capabilities.py need to be updated accordingly to used device:
- it contains names of devices
- UDDID
- OS version and name
- paths to .apk and .app files

to use device defined in desired_capabilities.py You need to open test case and change line:
"desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad" for example to:
"desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPhone6"


Known issues:

- some elements have attribute visible: false and appium is unable to interact with those elements for example map
- for some reason test sometimes fail to start on the first run, but after running it again it is working correctly 


Additional info:

Locators for elements are based mostly on visible texts, so if in OCA webpage some name, for example, for event type will be changed it will stop working.

Required configuration on OCA webpage:

- user accounts with correct settings (see credentials.py)
- 3 types of events (Incident, event_for_chooser_fields, event_for_on_load/save_test)
- option list inside "Central list templates" with values; "1", "2", "3" - that list is added as a option list to event type: event_for_on_load/save_test
- two sequences for events (on load and on save) - that sequences are added to event type: event_for_on_load/save_test



