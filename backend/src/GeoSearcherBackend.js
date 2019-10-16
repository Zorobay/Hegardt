const request = require('request');
const axios = require('axios');
const fetch = require('node-fetch');


module.exports = class GeoSearcherBackend {
    constructor() {

    }

    get_url(searchTerm) {
        return `https://geocoder.api.here.com/6.2/geocode.json?app_id=${process.env.HERE_API_ID}&app_code=${process.env.HERE_API_KEY}&searchtext=${encodeURIComponent(searchTerm)}`;
    }

    async getLocation(phrase, callback) {
        let url = this.get_url(phrase);
        await fetch(url)
            .then(res => {
                if (res.ok) {
                    return res.json();
                } else {
                    return new Error("Response with status " + res.status);
                }
            })
            .then(body => {
                let view = body.Response.View;
                if (view.length > 0) {
                    callback(undefined, view[0].Result[0].Location);
                } else {
                    callback(new Error(`Location [${phrase}] not found!`))
                }
            })
            .catch(err => callback(err, undefined));
    }
};
