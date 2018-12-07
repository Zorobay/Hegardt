const express = require('express');
const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');
const moment = require('moment');

const Person = mongoose.model('Person');

//Respond to any requests to the root url
router.get('/', (req, res) => {
    res.render('personal_file', {exists: true, name: "Sebastian Hegardt"});
});

// Respond to any request to a particular personal file
router.get('/*/', (req, res) => {
    const pageId = req.params[0];


    Person.find({_id: pageId}).then((persons) => {
        const person = persons[0];
        person.age = person.getAge();
        person.siblings = person.getSiblings();
        console.log(person.siblings)
        res.render('personal_file', person);
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
