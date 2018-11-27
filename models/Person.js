const mongoose = require('mongoose');

const personSchema = new mongoose.Schema({
    first_name: {type: String, trim: true},
    middle_name: {type: [String], trim: true},
    last_name: {type: String, trim: true},
    birth_date: {
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
    },
    birth_location: {
        country: {type: String, trim: true},
        region: {type: String, trim: true},
        city: {type: String, trim: true},
        specify: {type: String, trim: true}
    },
    death_date: {
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
    },
    death_location: {
        country: {type: String, trim: true},
        region: {type: String, trim: true},
        city: {type: String, trim: true},
        specify: {type: String, trim: true}
    },
    bury_date: {
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
    },
    bury_location: {
        country: {type: String, trim: true},
        region: {type: String, trim: true},
        city: {type: String, trim: true},
        specify: {type: String, trim: true}
    },
    occupation: {type: [String], trim: true},
    notes: String,
    file_id: {type: String, trim: true},
    spouses: [mongoose.Schema.Types.ObjectId],
    father: [mongoose.Schema.Types.ObjectId],
    mother: [mongoose.Schema.Types.ObjectId],
    children: [mongoose.Schema.Types.ObjectId],
    references: [String]
});

module.exports = mongoose.model('Person', personSchema);