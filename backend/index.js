const GeoSearcherBackend = require("./src/GeoSearcherBackend");

const mongoose = require("mongoose");
require("dotenv").config();
const jsonDoc = require("../python/all_ppl.json");

mongoose.connect(`mongodb://${process.env.DB_USER}:${process.env.DB_PASSWORD}@${process.env.DB}`, {useNewUrlParser: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;

db.on("error", () => {
    console.log(`Connection error! Failed to connect to ${process.env.DB}`);
});
db.on("connected", function () {
    console.log(`Mongoose connection open on mongodb://${process.env.DB}`);
    if (process.argv[2] === "--populate") {
        uploadPersonsFromJson(jsonDoc);
    }
});

require("./models/Person");
const app = require("./app");
const server = app.listen(process.env.PORT || 3000, () => {
    console.log(`Express is running on port ${server.address().port}`);
});

const getId = function (fileId) {
    if (fileId == null || fileId.length === 0)
        return null;

    const zeros = "0".repeat(24 - fileId.length);
    return mongoose.mongo.ObjectId(`${zeros}${fileId}`);
};

const getFormatLocation = function (locationObj) {
    if (locationObj) {
        let locs = [];
        for (let loc of [locationObj.city, locationObj.region, locationObj.country]) {
            if (loc)
                locs.push(loc);
        }
        return locs.join(", ");
    } else {
        return "";
    }
};

let uploadPersonsFromJson = async function (personsJson) {
    let geosearcher = new GeoSearcherBackend();

    let addLatLon = async function (locObj) {
        if (locObj) {
            let formatLoc = getFormatLocation(locObj);
            await geosearcher.getLocation(formatLoc, (err, res) => {
                if (err) {
                    locObj.latitude = null;
                    locObj.longitude = null;
                    personsJson.faulty = true;  // Track which db entries might need a look-over
                    console.error(err);
                } else {
                    locObj.latitude = res.DisplayPosition.Latitude;
                    locObj.longitude = res.DisplayPosition.Longitude;
                }
            });
        }
    };

    const Person = mongoose.model("Person");

    // clear database
    Person.deleteMany({}, function () {
    });

    for (let key in personsJson) {
        console.log("---------------------------------");
        const personJson = jsonDoc[key];

        // Convert python dates to JS dates
        if (personJson.birth_date != null)
            personJson.birth_date.date = new Date(personJson.birth_date.date.$date);

        if (personJson.death_date != null)
            personJson.death_date.date = new Date(personJson.death_date.date.$date);

        if (personJson.bury_date != null)
            personJson.bury_date.date = new Date(personJson.bury_date.date.$date);

        // Parse spouses
        personJson.spouses.forEach((sp) => {
            if (sp.marriage_date != null)
                sp.marriage_date.date.$date = new Date(sp.marriage_date.date.$date);

            sp._id = getId(sp._id); // Convert file id to ObjectID
            // Save latitude and longitude of marriage location
            addLatLon(sp.location);
        });

        // Convert fileIds to ObjectIDs
        personJson["_id"] = getId(personJson["file_id"]);
        personJson["father"] = getId(personJson["father"]);
        personJson["mother"] = getId(personJson["mother"]);

        // For some reason the children list is not recognized as a list...
        const childrenIds = [];
        personJson["children"].forEach((child) => {
            childrenIds.push(getId(child));
        });
        personJson.children = childrenIds;

        // Add coordinates to all locations
        await addLatLon(personJson.birth_location);
        await addLatLon(personJson.death_location);
        await addLatLon(personJson.bury_location);

        console.log(`Finished creating: ${personJson.full_name}`);
        let p = new Person(personJson);
        p.save()
            .then(() => {
                console.log(p);
            })
            .catch((error) => {
                console.log(error);
            });
    }
};
