const sqlite = require('sqlite3');

let db = new sqlite.Database('../../mydatabase.db', (err) => {
	if (err) {
		console.error(err.message);
	}
	console.log('Connected to mydatabase.db.');
});

db.serialize(() => {
	db.each('SELECT * FROM temps', (err, row) => {
		if (err) {
			console.err(err.message);
		}
		console.log(row);
	});
});

db.close((err) => {
	if (err) {
		console.error(err.message);
	}
	console.log('Close the database connection.');
});
