const mongoose = require('mongoose');
require('dotenv').config();

mongoose.connect(process.env.DATABASE, {useNewUrlParser: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.on('connected', function() {
    console.log(`Mongoose connection open on ${process.env.DATABASE}`);
});

require('./models/Person');
const app = require('./app');
const server = app.listen(3000, () => {
    console.log(`Express is running on port ${server.address().port}`);
});