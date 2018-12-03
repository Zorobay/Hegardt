const express = require('express');
const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');

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
        person.exists = true;

        res.render('personal_file', person);
    }).catch(() => {
        res.render('personal_file', {esists:false});
    })
});

// Handle rout and validate properties of req.
router.post('/',
    (req, res) => {

    });


module.exports = router;
