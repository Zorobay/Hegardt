const express = require('express');
const { body, validationResult } = require('express-validator/check');
const router = express.Router();

//Respond to any requests to the root url
router.get('/', (req, res) => {
    res.render('db_browser', {title: "Sök i databasen"});
});

// Handle rout and validate properties of req.
router.post('/',
    [
        body('name')
            .isLength({min: 2})
            .withMessage('Please enter a name'),
        body('email')
            .isAscii()
            .withMessage('Jävla svensk email!')
    ],
    (req, res) => {
        const errors = validationResult(req);

        if (errors.isEmpty()) {
            res.send('Thank you for your registration!');
        } else {
            res.render('form', {
                title: 'Registration form',
                errors: errors.array(),
                data: req.body,
            });
        }
    });

module.exports = router;
