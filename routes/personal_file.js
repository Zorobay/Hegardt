const express = require('express');
const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');

const Person = mongoose.model('Person');

require('dotenv').config();
const googleMapsClient = require('@google/maps').createClient({
    key: process.env.GOOGLE_MAPS_API_KEY
});

//Respond to any requests to the root url
router.get('/', (req, res) => {
    res.render('personal_file', {exists: true, name: "Sebastian Hegardt"});
});

// Respond to any request to a particular personal file
router.get('/*/', (req, res) => {
    const pageId = req.params[0];

    Person.findById(pageId).then(person => {
        person.getSiblings(function (sibs) {

                person.title = `Ansedel - ${person.full_name}`;
                person.siblings = sibs;
                person.geo = googleMapsClient.geocode({
                    address: 'Lund, Sweden'
                }, function (err, response) {
                    if (!err) {
                        console.log(response.json.results);
                        res.render('personal_file', person);
                    } else {
                        console.log(err);
                    }
                })

            }
        );
    }).catch((error) => {
        console.log(error);
        res.render('missing_personal_file');
    })
});

// Handle rout and validate properties of req.
router.post('/',
    (req, res) => {

    });


module.exports = router;
