//var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
if (!!window.EventSource) {
	var source = new EventSource('http://192.168.1.26:3000/events');
	source.onmessage = function(e) {
		console.log(e.data);
	};
} else {
var xmlhttp = new XMLHttpRequest(),
	method = 'GET',
	url = 'http://192.168.1.26:3000/';

xmlhttp.onreadystatechange = function () {
	//do something
	console.log(xmlhttp);
};
xmlhttp.open(method, url, true);
xmlhttp.send();
}

