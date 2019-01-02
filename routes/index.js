const express = require('express');
const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');

const Person = mongoose.model('Person');
//Respond to any requests to the root url
router.get('/', (req, res) => {
    //console.log("WOW")
    var ct = 0;
    Person.countDocuments({}, function (err, count) {
        ct = count;
        console.log(`Documents: ${count}`);
        //res.render('db_browser', {title: "Sök i databasen", numDocs: ct});
        res.render('homepage', {title: "Hegardt.se - Släktdatabas"});
    })
});

module.exports = router;
