const express = require('express');
//const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');

const Person = mongoose.model('Person');

require('dotenv').config();
// const googleMapsClient = require('@google/maps').createClient({
//     key: process.env.GOOGLE_MAPS_API_KEY
// });

router.get('/id/:id', (req, res, next) => {
    const id = req.params.id;

    Person.findById(id)
        .catch(err => {
            next(err);
        })
        .then(person => {
            res.json(person);
        })
});

router.get("/all", (req, res) => {
    Person.find({}, (err, ppl) => {
        if (err)
            console.log(err);
        else
            res.json(ppl);
    })
});
// Respond to any request to a particular personal file
/*router.get('/!*!/', (req, res) => {
    console.log("hejs2")
    const pageId = req.params[0];

    Person.findById(pageId).then(person => {
        person.getSiblings(function (sibs) {
                console.log(person);
                person.siblings = sibs;
                res.render('personal_file', person);

                // person.geo = googleMapsClient.geocode({
                //     address: 'Lund, Sweden'
                // }, function (err, response) {
                //     if (!err) {
                //         console.log(response.json.results);
                //     } else {
                //         console.log(err);
                //     }
                // })
            }
        );
    }).catch((error) => {
        console.log(error);
        res.render('missing_personal_file');
    })
});*/


module.exports = router;
