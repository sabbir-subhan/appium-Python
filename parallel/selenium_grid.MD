# For running tests in parallel mode You need to start selenium grid in first console and as many appium nodes as connected real devices in new consoles. 


console number one:
#needed: selenium-server-standalone-3.0.1.jar
	java -jar selenium-server-standalone-3.0.1.jar -role hub -hubConfig C:\selenium\hubconfig.json

console number two:
	appium --nodeconfig C:\selenium\nodeconfig1.json -p 4732 -bp 5724

console number three:
	appium --nodeconfig C:\selenium\nodeconfig2.json -p 4736 -bp 5734

console number four:
	appium --nodeconfig C:\selenium\nodeconfig3.json -p 4734 -bp 5744




# After settings all up - You can run three scripts by launching second one just after starting the first. You can use for example PyCharm to run them or nose runner to launch them in separate consoles.



