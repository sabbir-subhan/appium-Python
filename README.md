# **Appium POC** #

## Functional tests for OCA mobile app, using Appium and Python. ##


## **SOFT NEEDED:** ##

- Java
- Android studio and APIs for android - android avd
- Python + pip
- Selenium  (pip install -U selenium)
- Appium client for python  (pip install Appium-Python-Client)
- Appium app from official website
- PyCharm - for opening and running tests (also could be run from terminal)


**for OSX all above plus:**

- xcode 8.1 is needed for testing iOS10 (version 8 is not supported by appium 1.5.3 but brew need version 8.1 to install libimobiledevice - so install xcode 8.1 from appstore)
- node
- npm
- brew
- brew install --HEAD libimobiledevice
- brew link --overwrite libimobiledevice
- brew install ideviceinstaller
- brew link --overwrite ideviceinstaller
- rename xcode - applications - xcode --rename to: xcode8
- download xcode 7.3 and install - open appium and add path to xcode 7.3

- to switch between xcode versions, for example: sudo xcode-select -switch /Applications/Xcode8.app
(for testing iOS10 You need Xcode in version 8 - so rename old version of Xcode7 and leave 8 as a default version) 


### **TO RUN APPIUM AND iOS 10:** ###
- You have to lunch Appium in CLI and use version starting from 1.6.0 - currently 1.6.3 is the latest 
https://github.com/appium/appium-xcuitest-driver

CONFIG APPIUM 1.6.3:

- brew install ideviceinstaller
- brew install carthage
- npm install -g ios-deploy
- npm install -g deviceconsole
- n stable
- npm install -g npm@latest
- npm install -g appium@1.6.3 (or just appium or appium@beta)

- go to: /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent
- run: ./Scripts/bootstrap.sh
- run: open WebDriverAgent.xcodeproject -- and set iOS Developer in Build Settings and add unique BundleID and choose dev Team
- run: xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=4b15c4284897fa6f9b4c5205325a9cece997ad35' test  --id is a UDID of the device

Last line output after using above command should be; "Listening on USB". Then you are all set!



desired_capabilities.py and appium settings:

- UDID from real device - open iTunes with connected device and click on serial number or use terminal command: "idevice_id -l"
- iOS version and device name
- path to app - to get app file You need to build it in xcode



Appium in CLI:

- npm install -g appium
- npm install wd
- appium -p 4723
(appium -p 4723 -bp 5724 --session-override --log-level debug)
(appium --full-reset)

current GUI version - 1.5.3
current CLI beta version - 1.6.3


### **CONFIGURING ANDROID DEVICE:** ###

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
- adb shell pm list packages | grep noggin
- adb shell pm path <result from above command>
- adb pull <path to package>

finding app activity through adb - appActivity:
- adb shell dumpsys activity activities | grep com.noggin.oca
 (app need to be open on device)


### **CONFIGURING IOS DEVICE:** ###

1. for iOS 9.3.5 and older - enable UI Automation
2. prevent device from disabling - enable option stay awake while plugged in
3. unlock device and prevent automatic locking
4. for iOS 10 and newer - allow all permissions for the app (because Appium can't auto accept alerts on iOS higher than 9.3.5) 


BUILDING .APP FILE ON OSX:

- edit config.xml - change "id" for example to "com.noggin.oca$YOUR_USER_NAME"
- build app through cordova
- enable developer mode on device
- open project in xcode and change Bundle Identifier accordingly to "id" above
- build app through xcode (7.3)
- on real device, first You need to run app from xcode - it will install it on the device (You have to TRUST app in General - Device management)


### **CONFIGURE APPIUM GUI:** ###

- provide paths for android sdk and xcode
- provide path to app file (android - .apk file, ios - .app file from xcode(xcode build the app file for example in /Users/$USER/Library/Developer/Xcode/DerivedData/) or in other location(ProjectSettings))
- for iOS provide BundleID from xcode, check "Force device", device name and check "UDID" (search for it in iTunes or use terminal command: "idevice_id -l")
- uncheck "No reset" checkbox 
- if inspector in Appium doesn't work, try to uncheck "Bundle Identifier"


file desired_capabilities.py need to be updated accordingly to used device:
- it contains names of devices
- UDDID
- OS version and name
- paths to .apk and .app files

to use device defined in desired_capabilities.py You need to open test case and change line;
- "desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad" for example to:
- "desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPhone6"


Additional info:

Locators for elements are based mostly on visible texts, so if in OCA webpage some name, for example, for event type will be changed it will stop working.

Required configuration on OCA webpage:

- users accounts with correct settings (see credentials.py)
- 3 types of events (Incident, event_for_chooser_fields, event_for_on_load/save_test)
- option list inside "Central list templates" with values; "1", "2", "3" - that list is added as a option list to event type: event_for_on_load/save_test
- two sequences for events (on load and on save) - that sequences are added to event type: event_for_on_load/save_test
- EVENT TYPE: event_for_on_load/save_test, should have two single line fields with properties "Sequential prefix" pinpointing to correct sequences ("sequence_onload" with vaule: "test on load",
 and second; "sequence_onsave" with value: "test on save") and two fields with visibility rules ("field to restore" with value: "value for field 1" and visibility rule pointing to "New option list"
 with value "1",and second field; "New email address" with value: "test@noggin.com" and visibility rule pointing to "new option list" with value "2")
- EVENT TYPE: event_for_chooser_fields, should have "event chooser" field (name: "New events chooser") with property "Minimum selected options" set to "1", and second event chooser field inside sub form
with name: "New events chooser inside sub form"



### **BEFORE EACH NEW RUN OF TESTS:** ###

- for some reason on iOS -- "No reset" checkbox in Appium setting is not working, so tests for iOS are written to compensate it, but remember to run Android tests with checkbox "No reset" checked
- make sure to lunch appium server
- make sure that real devices are connected and unlocked 
- make sure line in test case: "desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad" is pinpointing to correct desired_capabilities for Your real device (see desired_capabilities.py)
- make sure that users accounts in OCA webpage have correct properties (for example expiration dates) and other tests have proper configurations in OCA webpage


### **RUNNING TESTS ON SIMULATORS:** ###

- change desired_capabilities
- for Android, open Appium settings, check "Launch AVD" and choose created simulator from the list (first You need to create simulator) and add udid of the simulator (from adb devices), start emulator and then run Appium
- for iOS, You have to build app for exact simulator
- for iOS - open Appium settings and uncheck UDID checkbox and change device name - choose from dropdown in Appium settings



APP VERSIONS:

- android: 9.1.3
- iOS: 9.1.4


### **Known issues:** ###

- some elements have attribute "visible: false" and appium is unable to interact with those elements for example map --that is bug in Appium https://github.com/appium/appium/issues/4131
- for some reason test sometimes fail to start on the first run, but after running it again it is working correctly (it may depends on that how fast device/simulator is starting)
- if Appium, after running test, will throws: "An unknown server-side error occurred while processing the command. Original error: Installing", use: sudo chmod -R 777 /var/db/lockdown/
- if Appium, after running test, throws error: "is device plugged in?" -- just disconnect device and reconnect it again (it may happen after booting OSX with connected device)
- for some reason on iOS -- "No reset" checkbox in Appium setting is not working, so tests for iOS are written to compensate it, but remember to run Android tests with checkbox "No reset" checked -- https://github.com/appium/appium/issues/4956
- Appium and OCA app sometime have problems to collaborate - if test fails, try to run it again or shutdown Appium and reconnect device
- if tests are running fine but Appium inspector is not lunching on iOS - You need to rebuild app by cordova and xcode and reinstall it on device 
- if after starting test, Appium throws errors like: "lockdown_receive_message error!" -- use sudo chmod -R 777 /var/db/lockdown/
- Appium can't switch between apps so only tapping on specific coordinates will work in another app, for example when OCA will open Safari
- Appium 1.6.3 - "Could not proxy command to remote server. Original error: Error: socket hang up" - lunch Xcode and rebuild WebDriverAgentRunner
