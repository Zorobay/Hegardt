const express = require("express");
const router = express.Router();

const mongoose = require("mongoose");
const Person = mongoose.model("Person");

router.get("/", (req, res) => {
    Person.find({}, (err, ppl) => {
        res.render("register", {title: "Personregister", ppl: JSON.stringify(ppl)});
    })
});

module.exports = router;
