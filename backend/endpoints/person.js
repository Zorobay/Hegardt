const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const Person = mongoose.model('Person');
require('dotenv').config();

// Lookup person by id
router.get('/id/:id', (req, res, next) => {
    const id = req.params.id;

    Person.findById(id)
        .then(person => {
            res.json(person);
        })
        .catch(err => {
            next(err);
        })
});

router.get("/siblings/:id", (req, res) => {
    let id = req.params.id;

});

// Lookup person by name
router.get("/query/:type/:term", (req, res) => {
    let term = req.params.term;
    let type = req.params.type;
    if (term.length > 0) {
        if (type !== "name")
            return;  // Implement more query types

        let st = term.replace(" ", "|");
        const re = new RegExp(st, "ig");

        Person.find({first_name: re}, (err, ppl) => {
            res.json(ppl);
        })
            .limit(30)
    } else {
        res.json([])
    }
});

router.get("/all", (req, res) => {
    Person.find({}, (err, ppl) => {
        if (err)
            console.log(err);
        else {
            res.json(ppl);
        }
    })
});


module.exports = router;
