const mongoose = require('mongoose');
const moment = require('moment');

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
});

/**
 * Calculates the age of this person.
 * @returns {*} Returns the age as a number if birth date is recorded, null otherwise
 */
personSchema.methods.getAge = function () {
    const bd = this.birth_date;
    if (bd && bd.year) {
        const d = moment(bd.year, 'YYYY');
        const now = moment(Date.now());
        return now.diff(d, 'years');
    }
    return null;
}

/**
 * Fins all (biological) siblings of this person.
 * @returns {Array} Returns all the siblings as a list. If no siblings were found, returns an empty list.
 */
personSchema.methods.getSiblings = function () {
    const sibs = [];
    this.model('Person').findById(this.mother).then((mom) => {
        sibs.extend(mom.children);
        console.log(sibs)
    });

    this.model('Person').findById(this.father).then((pa) => {
        sibs.concat(pa.children);
    });

    return sibs;

}

module.exports = mongoose.model('Person', personSchema, 'persons');