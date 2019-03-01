// server.js

const express = require('express');
const app = express();
const bodyParser = require('body-parser');

const PORT = 3000;

const indexRouter = require('./routes/index');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/index', indexRouter);

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(PORT, function() {
	console.log('Server is running on Port', PORT);
});
