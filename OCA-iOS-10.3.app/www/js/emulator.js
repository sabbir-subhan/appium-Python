//This file is run before everything else
var start = new Date().getTime();
var laps = {
	records:{},
	active: {}
};
function time(message){
	console.log("[TIME] " + (new Date().getTime()-start)/1000 + ": " + message);
}
function lap(command, name){
	var now = new Date().getTime();
	if (!laps.records[name]) laps.records[name] = [];
	
	if (command == 'start') {
		laps.active[name] = now;
	} else {
		var start = laps.active[name];
		laps.records[name].push(now-start);
		delete laps.active[name];
	}
}
function lapReport(){
	var report = {};
	for (var name in laps.records){
		var records = laps.records[name];
		report[name] = {};
		console.log("[TIME]: " + name);
		report[name].max = Math.max.apply(Math, records);
		console.log("[TIME] max: " + report[name].max);
		report[name].min = Math.min.apply(Math, records);
		console.log("[TIME] min: " + report[name].min);
		report[name].avg = records.reduce(function(a,b){return a+b}) / records.length;
		console.log("[TIME] avg: " + report[name].avg);
	}
	return report;
}
if (typeof FileReader != 'undefined') webkitFileReader = FileReader;