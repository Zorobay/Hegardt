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
    console.log(pageId);
    Person.find({_id: pageId}).then((persons) => {
        const person = persons[0];
        const age = (person.birth_date && person.birth_date.year) ? moment().diff(person.birth_date.year.toString(), 'years') : null;
        person.age = age;
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
