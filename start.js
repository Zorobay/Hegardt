const app = require('./app');
const mongoose = require('mongoose');
require('dotenv').config();


mongoose.connect(process.env.DATABASE, {useNewUrlParser: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    console.log("Connection successful!");

    // Define Schema for person
    var personSchema = new mongoose.Schema({
        name: String,
        born: Date
    });

    personSchema.methods.beget = function (mate) {
        console.log("Uh yeah, begetting a child with " + mate.name);
    }

    var Person = mongoose.model('Person', personSchema); //Compile Schema into Model

    var sebastian = new Person({name: "Sebastian Hegardt", born: new Date()}); // Create a person
    var d = new Date();
    var ana_lice = new Person({name: "Ana-Lice Machado", born: d.setDate(d.getDate() - 7)});
    sebastian.beget(ana_lice);

    // save both models to database
    sebastian.save(function (err) {
        if (err) return console.error(err);
    });
    ana_lice.save(function (err) {
        if (err) return console.error(err);
    });
});


const server = app.listen(3000, () => {
    console.log(`Express is running on port ${server.address().port}`);
});