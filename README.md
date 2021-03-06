# **Appium POC**

## Functional tests for OCA mobile app, using Appium and Python.


### **NEEDED SOFTWARE:**

- Java jdk
- Android studio and APIs for android - android avd
- brew install python3 (or on Windows just install from .exe file)
- node (tested on 6.10)
- npm
- "cd" to project directory and use "pip install -r requirements.txt"
~~- pip install -U selenium==3.3.1 (use version below 3.3.2 - probably there is bug in version 3.3.2)~~
- npm install -g appium@latest
~~- pip install Appium-Python-Client~~
~~- pip install html-testRunner~~
- PyCharm - for editing/viewing tests


**for OSX all above, plus:**

- Xcode 7.3  # needed for testing iOS9
(rename Xcode.app to Xcode7.app)
- xcode 8.1  # needed for testing iOS10
- brew install --HEAD libimobiledevice
- brew link --overwrite libimobiledevice
- brew install ideviceinstaller
- brew link --overwrite ideviceinstaller
- brew install ios-webkit-debug-proxy

- to switch between xcode versions, use: sudo xcode-select -switch /Applications/Xcode7.app

**TO RUN APPIUM WITH iOS 10:**
- You have to launch Appium in CLI and use version starting from 1.6.3 - currently 1.6.5 is the latest 

INSTALL APPIUM > 1.6.3 TO WORK WITH iOS10: (CLI commands)

- npm install -g webpack
- brew install ideviceinstaller
- brew install carthage
- npm install -g ios-deploy
- npm install -g deviceconsole

~~- cd /usr/local/lib/node_modules/appium/node_modules/~~
~~- npm install eslint-config-appium~~
~~- npm i eslint-plugin-import@latest --save-dev~~
~~- npm i eslint-plugin-mocha@latest --save-dev~~
~~- npm i eslint-plugin-promise@latest --save-dev~~

~~- npm install babel-runtime~~

~~- npm install appium-xcuitest-driver@latest~~

~~- npm install appium-uiautomator2-driver@latest~~

~~(for latest version of WebDriverAgent from Appium go to:
https://github.com/appium/WebDriverAgent.git and place it in /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/)~~

- cd /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent
- mkdir -p Resources/WebDriverAgent.bundle
- ./Scripts/bootstrap.sh (there maybe some errors about Inspector)
- open WebDriverAgent.xcodeproj (in Xcode change the Signing certificates to development) -- set iOS Developer in Build Settings and add unique 
BundleID and choose dev Team (if there are some warnings after build, for example, no config file, try to resolved them - set "no" dor project settings file

(- to test WebDriverAgent on real device use CLI command: 
xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=4b15c4284897fa6f9b4c5205325a9cece997ad35' test  --id is a UDID of the device
Last line output after using above command should be; "Listening on USB". Then you are all set!
THIS IS NOT MANDATORY (Appium should handle it, only signing WebDriverAgent code in Xcode maybe necessary))


- id = UDID from real device - open iTunes with connected device and click on serial number or use terminal command: "idevice_id -l"

(so if You need to run other version of iOS 10, for example iOS 10.3, You have to change build settings for WebDriverRunner in Xcode))


# **EXECUTING TESTS:**

### 1. Update file /appium-poc/Conf/desired_capabilities.py:

###### /appium-poc/Conf/desired_capabilities.py file contains information about devices
###### open desired_capabilities.py file and search for device on which You want to run tests, if that device is not present You have to create a new one. 
To do that, copy/past some existing device and edit it's details:
- UDID from real device - open iTunes with connected device and click on serial number or use terminal command: "idevice_id -l"
- iOS version and device name
- path to app - to get app file You need to build it in Xcode for specific device that You have - after build just copy/past .app file into repository
and provide name of that file in desired_capabilities.py
- also You have to edit /appium-poc/configuration.py to add new device to if condition


### 2. Start Appium server in CLI:

- appium  # this will launch Appium server on default port = 4723
- appium -p 4735  # to change port use "-p" flag
- appium --log-timestamp --log /file_path  # starting appium with logging to file


### 3. Execute test:

- open new terminal tab
- cd to repository
- type: python run.py -test <name_of_the_test_file> -platform <name_of_the_platform_to_run_test>
- example: python run.py -t test_Login -p IOS_10_emulator (You can also use: "all" as test parameter)
- example 2: python run.py --test test_ManagingLogs --platform Android_7 --port 4735 (default value for port = 4723)
  
- test files are located in /appium-poc/tests
- available platforms are defined in /appium-poc/configuration.py
- devices details are defined in /appium-poc/Conf/desired_capabilities.py


### **run on iOS9 and iOS10**

- You need to install Xcode 7 and Xcode 8 and Appium >= 1.6.3 in CLI mode, 

Appium can run both iOS versions but You need to switch between Xcode versions 
(Xcode7 must have different name because appium in CLI will search for app "Xcode" so that should be version 8)
(with Xcode 8 You can run tests for iOS10 and to run tests for iOS9 You have to switch to Xcode 7)

- 'sudo xcode-select -switch /Applications/Xcode.app' and run 'appium' - for iOS10 and 'sudo xcode-select -switch /Applications/Xcode7.app' and run 'appium' - for iOS 9)

- remember to restart Appium server after changing Xcode version
(Appium 1.5.3 can run only iOS9)


####**to run tests on IOS9 (real device):**

- switch Xcode 7 version using: sudo xcode-select -switch /Applications/Xcode7.app
- in another console run: ios_webkit_debug_proxy -c <device udid>:27753
- **iPad:** ios_webkit_debug_proxy -c db55c238e873230ee454c54a63724397a2981acd:27753
- in new console start Appium server using CLI command: "appium"
- start test using CLI command: "python run.py -t test_Login -p IOS_9_iPad"

####**to run tests on IOS10 (real device):**

- switch Xcode 8 version using: sudo xcode-select -switch /Applications/Xcode.app
- in new console start Appium server using CLI command: "appium"
- start test using CLI command: "python run.py -t test_Login -p IOS_10_iPhone"


## **CONFIGURING ANDROID DEVICE:**

1. enable developer mode
2. enable USB debugging
3. disable “Auto capitalize” in keyboard settings - because login starts from small letter “b”
4. prevent device from disabling - enable option stay awake while plugged in
5. unlock device and prevent automatic screen locking


PULLING APK FILE FROM ANDROID DEVICE:
(You can use app file from repo "com.noggin.oca.apk")

- first - install app from google store

next open terminal and use:

- adb devices
- adb shell pm list packages | grep noggin
- adb shell pm path <result from above command>
- adb pull <path to package>

finding app activity through adb - appActivity:
- adb shell dumpsys activity activities | grep com.noggin.oca or dumpsys window windows | grep -E mCurrentFocus
 (app need to be open on device)

- if You have multiple devices connected:
 (adb -s <device id> shell ...)


## **CONFIGURING IOS DEVICE:**

1. for iOS 9.3.5 and older - enable UI Automation
2. prevent device from disabling - enable option stay awake while plugged in
3. unlock device and prevent automatic screen locking
4. for iOS 10 and newer - allow all permissions for the app (because Appium can't auto accept alerts on iOS higher than 9.3.5) 


BUILDING .APP FILE ON OSX:

- edit config.xml - change "id" for example to "com.noggin.oca$YOUR_USER_NAME"
- build app through Cordova
- enable developer mode on device
- open project in xcode and change Bundle Identifier accordingly to "id" above
- build app through Xcode
- on real device, first You need to run app from xcode - it will install it on the device (You have to TRUST app in General - Device management)
- path to built file is located in Conf/desired_capabilities 


### **CONFIGURE APPIUM GUI:**  (optional)

- provide paths for android sdk and xcode
- provide path to app file (android - .apk file, ios - .app file from xcode(xcode build the app file for example in /Users/$USER/Library/Developer/Xcode/DerivedData/) or in other location(ProjectSettings))
- for iOS provide BundleID from xcode, check "Force device", device name and check "UDID" (search for it in iTunes or use terminal command: "idevice_id -l")
- uncheck "No reset" checkbox 
- if inspector in Appium does not work, try to uncheck "Bundle Identifier"

file /Conf/desired_capabilities.py need to be updated accordingly to used device:
- name of device
- UDID
- OS version and name
- paths to .apk and .app files


# Some required configuration on OCA web page:

- disable Mobile Dashboard - go to OCA -> Settings -> Security -> User account types -> select account type -> choose "None" in Mobile dashboard selector

- disable mobile encryption (PIN) in OCA Settings - Settings - Security tap

- locators for elements are partially based on visible texts, so if in OCA web page, for example event type name, will be changed, tests will stop working

- create users accounts with correct settings (see credentials.py) and check if You can login (accept Terms and Conditions for new user)

- disable Auto-Correction on iOS devices and on iOS10 simulator

- provide image and video sample file for real devices and android emulators (sample files should be copied while tests are running but for some devices or emulators that functionality may not work)


### for TC: Managing Events
- 3 types of events (Incident, event_for_chooser_fields, event_for_on_load/save_test)
- option list inside "Central list templates" with values; "1", "2", "3" - that list is added as a option list to event type: event_for_on_load/save_test
- two sequences for events (on load and on save) - that sequences are added to event type: event_for_on_load/save_test
- EVENT TYPE: event_for_on_load/save_test, should have two single line fields with properties "Sequential prefix" pinpointing to correct sequences ("sequence_onload" with vaule: "test on load",
 and second; "sequence_onsave" with value: "test on save") and two fields with visibility rules ("field to restore" with value: "value for field 1" and visibility rule pointing to "New option list"
 with value "1",and second field; "New email address" with value: "test@noggin.com" and visibility rule pointing to "new option list" with value "2")
- EVENT TYPE: event_for_chooser_fields, should have "event chooser" field (name: "New events chooser") with property "Minimum selected options" set to "1", and second event chooser field inside sub form
 with name: "New events chooser inside sub form"

### for TC: Send Photo and Send Video 
- test steps have different order than those in Jira task, because in this way, before running test it is no longer necessary 
  to prepare sample photo and video files on real device, but unfortunately for emulators before running test "test_SendingVideo" tester must copy some video file into the emulator
- go to OCA web page - Settings - Settings - Security tab and in section Mobile, uncheck "Encrypt saved data in the app" and "Block jailbroken/rooted devices from using the app"

### for TC: QuickAccessButtons
- create quick access buttons - see task OCAMOB-48 prepare Lodging Agency named: "contact_group_for_tests" - - create Lodging agency named: "contact_group_for_tests" -- create new contact group and add "Agency" option to it,
 and configure Quick Access buttons for mobile app, 
 Login to OCA server>Click on Settings>Mobile Quick access Buttons>Add Quick Access buttons (see task in Jira), remember to firstly open some link on device/emulator - Android will ask witch browser You want to use

### for TC: SentCommunication
- create contact with name: "CONTACT_FOR_APPIUM_TESTS" with email address

### for Test Case: Assets
- assets types named: "asset_with_visibility_rules", "asset_with_max_number_of_fields". Asset type with visibility rules must have 5 fields: 
 "Name", "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore", "New website address" with value: "http://bitnoi.se/" and "New email address" 
-- visibility rules like in TC: Events
- Lodging agency named: "contact_group_for_tests" is needed

### for TC: Managing Reports
- create Lodging agency named: "contact_group_for_tests" -- create new contact group and add "Agency" option to it
- report type with all fields, named: "report_for_tests", 
- report type with chooser fields, named: "report_with_chooser_fields",
- report type with chooser fields, must contain asset chooser field as a last field in form, 
- report type with on load and on save sequence (with default value = "test on load") and on save sequence, named: "report_with_on_load_sequence" (like in TC: Managing Events),
- report type with visibility rules, named: "report_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
 "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
 (option 1 restores field to restore, option 2 restores New email address field, option 3 restores New website address),
- report type with on create approval workflow, named: "report_with_on_create_approval"
- report type, named: "report_with_assigned_question" and workflow assigned to that - triggered on edit report , that workflow must contain "Assign a question node" with title: "Report approval task" and
  two possible answers: "Yes/No", (field Assign to: Contact that activated workflow: Workflow info)
- prepare Role for contact - choose contact that will be used to run test (default = Bitnoise QA)
    (Go to a resource assignment and allocate yourself into a role - Contacts>Resource Assignment - Select any resource Assignment 
    choose tab: Resources and click Structure button, in new window click Add - Contact role, type same new name and choose Role type as Role contacts and click OK and Save
    choose the contact you are logged in as example Bitnoise QA - Open contact and click on Roles - You can see role allocation - Make sure that the status in IN)

### for TC: Managing Logs
- log type with all fields, named: "log_with_all_fields",
- log type with chooser fields, named: "log_with_chooser_fields", with log chooser filed as a last field in form
- log type with on load (with default value = "test on load") and on save sequence, named: "log_with_on_load_sequence" (like in TC: Managing Events), 
- log type with visibility rules, named: "log_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
 "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
 (option 1 restores field to restore, option 2 restores New email address field, option 3 restores New website address)

### for TC: Maps
- Login to the OCA server > Click on OCA designer > Symbology and Colour Coding > Add more symbology - new point symbol name: "point2"
- Login to oca server > Click on mapping > Layers > Add > Drawing > Ok > Draw geometry (draw some shape using line tool) > Save map as "FOR MOBILE"

### for TC: Create Objects From Mapping Layer
- Login to the OCA server > Click on OCA designer > Symbology and Colour Coding > Add more symbology - new point symbol name: "point2"
- Login to oca server > Click on mapping > Layers > Add > Drawing > Ok > Draw geometry (draw some shape using line tool) > Save map as "FOR MOBILE" (the same map as in TC: Maps)
- other Saved maps that are needed for TC: All active events, All assets, All contacts, All tasks - for proper TC execution in OCA app should be present one event, asset, task and contact with mapping data or address data

### for TC: OfflineObjects
- airplane mode on iOS emulators is unavailable

### for TC: Read Only Properties
- Go to setting > OCA designer > Create object types: Asset, Reports, Event, Risk
- for each new type add the following: - option list: name = Is Read only ?, Options = Yes A, Yes B, No, Maximum selected options = Height of field = 3, Default value = (None) - *Options may come from a central list or a user-defined list
- Add the 2 sets of the following fields: option list, single-line text, multi-line text, rich text, phone number, fax number, cell number, email address, website address, location, date, date & time, date & optional time, number, sub form, single-line text inside the sub form
- Make the 1st set of fields Read only if Is Read only ? = Yes A.
- Make the 2nd set of fields visible only if Is Read only ? = Yes B.
- Set up default values for all fields in both sets.

### for TC: Sending Communications
- make sure that the "A_CONTACT_FOR_APPIUM_TESTS" is present in OCA or change name of the contact in test case script
- go to OCA web page -> Documents -> edit "Comms documents" -> change read access level to all users
- highlight OCA Generic Escalation Fax.pdf and click Properties -> change read access level to all users
- prepare some sample image and video for real devices

### for TC: Low Users Communications
- If not already present in OCA, create three low level users: "A_CONTACT_FOR_APPIUM_TESTS", "test_general" and "test_expire_in_1_day" or change names of the contacts in this script, (those users must have email addresses) 
- Create high user: "test_admin" or change name of the contact in this script
- Login to OCA server -> Click on Settings > Settings>Security > Under Access levels set the write access level to administrators only(high access)

### for TC: Html Formatting 
- new event type, with rich text containing image, table and link, name for new event type: "event_with_rich_text",
 (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
inside OCA designer add image, table and link into rich text field, image name = "cats.jpg"
- create new event named: "event_with_image" - use event type created above
- new report type, with rich text containing image, table and link, name for new report type: "report_with_rich_text",
 (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
inside OCA designer add image, table and link into rich text field, image name = "everest.jpg"
- create new report named: "report_with_image" - use report type created above
- new log type, with rich text containing image, table and link
 (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
 name for new log type: "log_with_rich_text",
inside OCA designer add image, table and link into rich text field, image name = "panda.jpg"
- create new log named: "log_with_image" - use log type created above

### for TC: Rich Text Fields
- (EDIT OBJECTS TYPE FROM TC: Html Formatting) create a new Asset type that has a rich text field and a subform with a rich text field
- new object type, with rich text containing image, table and link, name for new object type: "asset_with_rich_text",
 (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
inside OCA designer add image, table and link into rich text field, image name = "cats.jpg" and add the same
elements into rich text field inside sub form - image name: "everest.jpg"
- create new asset named: "asset_with_image" - use asset type created above
- create new object type for Event just like Asset, first image use: "cats.jpg" and for sub form: "everest.jpg"
- create new object type for Report just like Asset, but for the first image use: "everest.jpg" and for sub form: "panda.jpg"
- create new object type for Log just like Asset, but for the first image use: "panda.jpg" (Log can't have sub form)
- create new object type for Contact Group just like Asset, but for the first image use: "cats.jpg" (Contact Group can't have sub form)
- create new object type for Contact just like Asset, but for the first image use: "panda.jpg" (Contact can't have sub form)
(remember to create each one of new objects types on OCA web page)


#**BEFORE EACH NEW RUN OF TESTS:**

- make sure to launch appium server
- make sure that real devices are connected and unlocked 
- make sure that users accounts in OCA web page have correct properties (for example expiration dates) and other tests have proper configurations in OCA web page
- disable PIN authentication in OCA web page 

##**RUNNING TESTS ON EMULATORS:**

- change desired_capabilities
- for Android, open Appium settings, check "Launch AVD" and choose created simulator from the list (first You need to create simulator) and add udid of the simulator (from adb devices), start emulator and then run Appium
- for iOS, You have to build app for exact simulator
- for iOS - open Appium settings and uncheck UDID checkbox and change device name - choose from dropdown in Appium settings


OCA APP VERSIONS:

- android: 10.0.13
- iOS: 10.0.13


#**Known issues:**

- real devices can overheat, which is causing test to fail
- if You are running tests on real iOS device, sometimes Appium server and ios_webkit_debug_proxy need to be restarted to work properly 
- "in switch_context_to_webview self.driver.switch_to.context(contexts[1]) IndexError: list index out of range"  --> You have to launch ios_webkit_debug_proxy for real device
- some elements have attribute "visible: false" and appium is unable to interact with those elements for example map --this is bug in Appium
- for some reason test sometimes fail to start on the first run, but after running it again it is working correctly (it may depends on that how fast device/simulator is starting)
- if Appium, after running test, will throws: "An unknown server-side error occurred while processing the command. Original error: Installing", use: sudo chmod -R 777 /var/db/lockdown/
- if Appium, after running test, throws error: "is device plugged in?" -- just disconnect device and reconnect it again (it may happen after booting OSX with connected device)
- Appium and OCA app sometime have problems to collaborate - if test fails, try to run it again or shutdown Appium and reconnect device
- if tests are running fine but Appium inspector is not launching on iOS - You need to rebuild app by cordova and xcode and reinstall it on device 
- if after starting test, Appium throws errors like: "lockdown_receive_message error!" -- also try to use sudo chmod -R 777 /var/db/lockdown/
- Appium can't switch between apps so only tapping on specific coordinates will work in another app, for example when OCA will open Safari
- Appium 1.6.3 - "Could not proxy command to remote server. Original error: Error: socket hang up" - launch Xcode and rebuild WebDriverAgentRunner
- Appium > 1.6 - can't handle double tap method
- Error about Xcode version, to switch xcode version use: sudo xcode-select -switch /Applications/Xcode.app
- Appium 1.6 -- "socket hang up" - rebuild WebDriver Runner
- error containing "adbExec" - uninstall android apps from device: "Unlock", "Appium Settings" -- Appium will install them automatically 
- for some reason on iOS -- "No reset" checkbox in Appium setting is not working, so tests for iOS are written to compensate it, but remember to run Android tests with checkbox "No reset" checked
- Appium server hangs on: "Waiting for WebDriverAgent server to finish loading..." -- problem with WebDriver build
- info XCUITest xcodebuild exited with code '65' and signal 'null' -- This usually means that the necessary code signing is not set up correctly
- if You open WebDriverAgent project in Xcode and there is lack of Routing Http Server - open WebDriverAgent directory and run ./Scripts/bootstrap.sh
- "Instruments exited with code 255" = "Instruments exited with code 251" = We exceeded the number of retries allowed for instruments to successfully start; failing launch"  -- kill Appium server, 
    switch to proper Xcode version, restart host and device, ? 
- Instruments exited with error 253 - rebuild OCA app through Xcode
- "Error while executing atom: operation timed out" -- reconnect device and restart appium server
- sometimes there are problems with real iOS 10 device - tests are failing because of appium server errors --try to reconnect device and restart appium server
- double clicking action is not working properly with appium above 1.5.3
- double clicking action may not work properly on iOS emulators
- "selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing 
the command. Original error: Could not install app: 'Command 'ios-deploy --id 4b15c4284897fa6f9b4c5205325a9cece997ad35 --uninstall --bundle
 /Users/lukasl/repos/appium-poc/iPhone6_10.3_OCA.app' exited with code 253'"   ---> start from killing Appium server and restarting it, if this won't worked - rebuild WebDriverAgent and/or rebuild OCA app through Xcode 
 (usually, it occurs after switching iOS versions)
- An unknown server-side error occurred while processing the command. Original error: Command failed: ideviceinstaller -u  ????? - observed on iPad with iOS9 ?????  (try "brew install --HEAD ideviceinstaller")   ??
- Error: connect ECONNREFUSED 127.0.0.1:8100   -- reinstall appium - npm uninstall -g appium + npm install -g appium
- (The application does not have a valid signature.)  -- rebuild and install OCA app through Xcode
- When running on Android, Appium sometimes can freeze on "Getting connected devices..." ---> restart Appium server
- error: "WebDriverException: Message: target.frontMostApp().keyboard() failed to tap 'h'" = "failed to tap 'h'"  -- observed on iOS 9 emulator - choose Simulator -> Hardware -> Keyboard -> Toggle Software Keyboard
- error: "A valid provisioning profile for this executable was not found."  --> rebuild OCA app through Xcode
- error: "Original error: ChromeDriver crashed during startup"  --> You started two parallel tests on Android devices and chromedriver just crashed
- Android 7 real device and airplane mode -- sometimes there are some problems with switching to airplane mode, to fix it switch manually airplane mode on and off (or try to restart device and/or switch display off) and then start the test
- error: "WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: Error while executing atom: Element is not currently visible and may not be manipulated (status: 11)"
 --> probably some problem with crashing iOS instruments? 
- airplane mode on iOS emulators is unavailable
- WebDriverException when sending text --> error occurred after downgrading from Appium 1.6.6 beta 4 to 1.6.5
- error: "An unknown server-side error occurred while processing the command. Original error: Unable to launch WebDriverAgent because of xcodebuild failure: "iproxy exited with code '208'""  --> kill iproxy process - ps -ax|grep -i "iproxy"
