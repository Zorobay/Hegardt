const express = require("express");
const router = express.Router();

const mongoose = require("mongoose");
const Person = mongoose.model("Person");

// Handle global search bar searches
router.get("/:searchTerm", (req, res) => {
    var st = req.params.searchTerm.replace(" ", "|");
    const re = new RegExp(st, "ig");
    console.log(st);

    Person
        .find({first_name: re}, (err, ppl) => {
            res.json(ppl);
        })
        .project({fullName: {$concat: ["$first_name", " ", "$last_name"]}})  //TODO .project is not a function ERROR!
        .limit(30)
});

module.exports = router;