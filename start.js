const mongoose = require('mongoose');
require('dotenv').config();
const jsonDoc = require('./python/all_ppl.json');

mongoose.connect(process.env.DATABASE, {useNewUrlParser: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.on('connected', function() {
    console.log(`Mongoose connection open on ${process.env.DATABASE}`);
    const Person = mongoose.model('Person');

    var size = 0;
    for (key in jsonDoc) {
        if (key == 20) {
            console.log(jsonDoc[key]);
            const p = new Person(jsonDoc[key]);
            p.save()
                .then(() => { console.log("WTF SAVED!"); })
                .catch(() => { console.log("SHIT! error"); })
        }
    }
});

require('./models/Person');
const app = require('./app');
const server = app.listen(3000, () => {
    console.log(`Express is running on port ${server.address().port}`);
});