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
            // Find their siblings
            person.getSiblings((sibs) => {
                person.siblings = sibs;
                res.json(person);
            });

        })
        .catch(err => {
            next(err);
        })
});

// Lookup person by name
router.get("/search/:term", (req, res) => {
    let term = req.params.term;
    if (term.length > 0) {
        let st = term.replace(" ", "|");
        const re = new RegExp(st, "ig");
        console.log(st);

        Person.find({first_name: re}, (err, ppl) => {
            res.json(ppl);
        })
            .limit(30)
    } else {
        res.json([])
    }
});

router.get("/all/:limit", (req, res) => {
    let limit = req.params.limit;
    try {
        limit = parseInt(limit);
    } catch (e) {
        throw e;
    }

    Person.find({}).limit(limit).exec((err, ppl) => {
        if (err)
            console.log(err);
        else {
            console.log("Limit " + limit);
            console.log(ppl);
            res.json(ppl);
        }
    });
});

router.get("/all", (req, res) => {
    Person.find({}, (err, ppl) => {
        if (err)
            console.log(err);
        else {
            res.json(ppl);
            console.log(ppl);
        }
    })
});


module.exports = router;
