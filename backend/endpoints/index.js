const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");

const Person = mongoose.model("Person");
//Respond to any requests to the root url
router.get("/", (req, res) => {
    //console.log("WOW")
    Person.countDocuments({}, function (err, count) {
        console.log(`Documents: ${count}`);
        //res.render("db_browser", {title: "Sök i databasen", numDocs: ct});
        res.render("homepage", {title: "Hegardt.se - Släktdatabas"});
    });
});

module.exports = router;
