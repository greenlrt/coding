const sqlite = require('sqlite3');

let db = new sqlite.Database('../../mydatabase.db', (err) => {
	if (err) {
		console.error(err.message);
	}
	console.log('Connected to mydatabase.db.');
});

db.serialize(() => {
	db.each('SELECT * FROM temps ORDER BY zone', (err, row) => {
		if (err) {
			console.err(err.message);
		}
		console.log(row);
	});
	db.all('SELECT * FROM temps ORDER BY zone', (err, rows) => {
		if (err) {
			console.err(err.message);
		}
		console.log(rows);
	});
		
});

db.close((err) => {
	if (err) {
		console.error(err.message);
	}
	console.log('Close the database connection.');
});
