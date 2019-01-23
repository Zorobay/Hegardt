const mongoose = require('mongoose');
const moment = require('moment');
const _ = require('lodash');

const dateSchema = new mongoose.Schema({
    date: Date,
    year: {
        type: Number,
        min: 0,
        max: new Date().getFullYear()
    },
    month: {
        type: Number,
        min: 1,
        max: 12
    },
    day: {
        type: Number,
        min: 1,
        max: 31
    }
}, {_id: false});

const locationSchema = new mongoose.Schema({
    country: {type: String, trim: true},
    region: {type: String, trim: true},
    city: {type: String, trim: true},
    notes: {type: String, trim: true}
}, {_id: false});

const spouseSchema = new mongoose.Schema({
    _id: mongoose.mongo.ObjectId,
    date: dateSchema,
    location: locationSchema
}, {_id: false});

const personSchema = new mongoose.Schema({
    first_name: {type: String, trim: true},
    middle_name: {type: [String], trim: true},
    last_name: {type: String, trim: true},
    sex: {
        type: String,
        enum: ["MAN", "WOMAN", "OTHER", ""],
        default: ""
    },
    birth_date: dateSchema,
    birth_location: locationSchema,
    death_date: dateSchema,
    death_location: locationSchema,
    bury_date: dateSchema,
    bury_location: locationSchema,
    occupation: {type: [String], trim: true},
    notes: String,
    file_id: {type: String, trim: true},
    spouses: [spouseSchema],
    father: mongoose.Schema.Types.ObjectId,
    mother: mongoose.Schema.Types.ObjectId,
    children: [mongoose.Schema.Types.ObjectId],
    references: [String]
}, {toObject: { virtuals: true },
    toJSON: { virtuals: true }
});

/**
 * Finds all biological siblings of this person.
 * @param callback(sibs) the function to call when finished. Sets the sibs parameter of the callback function to a list
 * of sibling IDs or an empty list if no siblings were found.
 */
personSchema.methods.getSiblings = function (callback) {

    const self = this;
    const mId = this.mother;
    const pId = this.father;
    var sibs = [];

    this.model('Person').find({_id: {$in: [mId, pId]}}, "children", function (err, res) {

        res.forEach(chList => {sibs = sibs.concat(chList.children); });
        sibs = _.uniqWith(sibs, _.isEqual);  // Remove duplicates
        _.remove(sibs, self._id);  // Remove own id


        if (sibs.length != 0) {
            self.model('Person').find({_id: {$in: sibs}}, function (err, res) { callback(res); });
        } else {
            callback(sibs);
        }
    });
};

personSchema.virtual('birth_date_pretty').get(function () {
    let zeroPad = function(d) {return d != null && d < 10 ? "0" + d : d};
    const date = this.birth_date;
    return date != null ? [date.year, zeroPad(date.month), zeroPad(date.day)].join('-') : "??";
});

/**
 * The full name of this person as a string.
 */
personSchema.virtual('full_name').get(function() {
    return this.first_name + " " + this.middle_name.join(' ') + " " + this.last_name;
});

/**
 * The age of this person in years. Is null if no birth date has been recorded.
 */
personSchema.virtual('age').get(function () {
    const bd = this.birth_date;
    if (bd) {
        const d = moment(bd.date);
        const now = moment(Date.now());
        return now.diff(d, 'years');
    }
    return null;
});

personSchema.virtual('is_dead').get(function() {
    return this.death_date || this.age > 123;
});

module.exports = mongoose.model('Person', personSchema, 'persons');