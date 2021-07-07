const http = require('http');

const connected_users={};

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer(function(req, res) {
	if (req.url == '/events'){
		res.writeHead(200, {
			'Content-Type': 'text/event-stream',
			'Cache-Control': 'no-cache',
			'connection': 'keep-alive',
			'Access-Control-Allow-Origin': '*'
		});
		var id = (new Date()).toLocaleTimeString();

		// Sends a SSE evern 5 seconds on a single connection
		setInterval(function() {
			res.write('id: ' + id + '\n');
			res.write("data: " + (new Date()).toLocaleTimeString()+"\n\n");
		}, 5000);
	} else {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.setHeader('Content-Type', 'text/event-stream');
	res.write('Hello World\n');
	console.log('wrote Hello World');
	res.write('FinalMessage\n');
	console.log('wrote Final Message');

	var id = (new Date()).toLocaleTimeString();

	setInterval(function() {
		res.write((new Date()).toLocaleTimeString() + "\n\n");
		console.log('wrote timestamp');
		res.flush();
	}, 5000);

	res.end
	}
});

server.on('connection', function(socket) {
	socket.__fd=socket.fd;
	connected_users[socket.__fd]=socket.remoteAddress;
	console.log(connected_users);
	socket.on('close', function() {
		delete connected_users[socket.__fd];
		console.log(connected_users);
	});
});

server.listen(port, hostname, function() {
	console.log('Server running at http://${hostname}:${port}/');
});
