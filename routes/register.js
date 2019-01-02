const express = require('express');
const router = express.Router();

const mongoose = require('mongoose');
const Person = mongoose.model('Person');

router.get('/', (req, res) => {
    Person.find({}, (err, ppl) => {
        res.render('register', {data: ppl[0]});
    })
});

module.exports = router;
