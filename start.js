const mongoose = require('mongoose');
require('dotenv').config();
const jsonDoc = require('./python/all_ppl.json');

mongoose.connect(process.env.DATABASE, {useNewUrlParser: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.on('connected', function () {
    console.log(`Mongoose connection open on ${process.env.DATABASE}`);
    uploadPersonsFromJson(jsonDoc);
});

require('./models/Person');
const app = require('./app');
const server = app.listen(3000, () => {
    console.log(`Express is running on port ${server.address().port}`);
});

let getId = function (fileId) {
    if (fileId.length == 0 || fileId == null)
        return null;

    const zeros = "0".repeat(24 - fileId.length);
    return mongoose.mongo.ObjectId(`${zeros}${fileId}`);
}

let uploadPersonsFromJson = function (personsJson) {
    const Person = mongoose.model('Person');

    var i = 0;
    for (key in personsJson) {
        console.log("---------------------------------");
        const personJson = jsonDoc[key];

        // Convert python dates to JS dates
        if (personJson.birth_date != null)
            personJson.birth_date.date = new Date(personJson.birth_date.date.$date);

        if (personJson.death_date != null)
            personJson.death_date.date = new Date(personJson.death_date.date.$date);

        if (personJson.bury_date != null)
            personJson.bury_date.date = new Date(personJson.bury_date.date.$date);

        personJson.spouses.forEach((sp) => {
            if (sp.marriage_date != null)
                sp.marriage_date.date.$date = new Date(sp.marriage_date.date.$date);

            sp._id = getId(sp._id); // Convert file id to ObjectID
        })

        // Convert fileIds to ObjectIDs
        personJson["_id"] = getId(personJson["file_id"]);
        personJson["father"] = getId(personJson["father"]);
        personJson["mother"] = getId(personJson["mother"]);

        // For some reason the children list is not recognized as a list...
        const childrenIds = [];
        personJson["children"].forEach((child) => { childrenIds.push(getId(child)); });
        personJson.children = childrenIds;

        console.log(personJson);
        p = new Person(personJson);
        p.save()
            .then(() => {
                console.log(p);
            })
            .catch((error) => {
                console.log(error);
            });
    }
}