const express = require('express');
const {body, validationResult} = require('express-validator/check');
const router = express.Router();
const mongoose = require('mongoose');

const Person = mongoose.model('Person');
//Respond to any requests to the root url
router.get('/', (req, res) => {
    //console.log("WOW")
    res.render('db_browser', {title: "Sök i databasen"});
});

// Handle rout and validate properties of req.
router.post('/',
    [
        body('first_name')
            .isLength({min: 2})
            .withMessage('Please enter a name')
    ],
    (req, res) => {
        const errors = validationResult(req);

        if (errors.isEmpty()) {
            //res.send('Thank you for your registration!');

            // Send shit to mongo db
            const j = {
                occupation: ["Engineering", "Mascot"],
                first_name: "Mc Doo",
                last_name: "Memphis",
                death_location: {
                    country: "Sweden",
                    region: "Skåne",
                    city: "Lund"
                }
            };
            console.log(j);
            const registration = new Person(j);
            registration.save()
                .then(() => {
                    res.send('Wow coolt!');
                })
                .catch(() => {
                    res.send('That did not work!');
                })
        } else {
            res.render('db_browser', {
                title: 'Sök i databasen',
                errors: errors.array(),
                data: req.body,
            });
        }
    });


module.exports = router;
