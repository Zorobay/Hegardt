const express = require("express");
const cors = require("cors");
const path = require("path");
const bodyParser = require("body-parser");

// Routes
const indexRouter = require("./endpoints/index");
const personalFileRouter = require("./endpoints/person");

// Create a new express app
const app = express();

// Use CORS to allow communication to frontend
app.use(cors());

// use bodyparser to parse url body
app.use(bodyParser.urlencoded({extended: true}));

// Whenever we get a request on the form "/whatever" it should use the routes file to redirect
app.use("/person/", personalFileRouter);
app.use("/", indexRouter);

// Setup error handling middleware
app.use(function (err, req, res, next) {
    // Do logging and user-friendly error message display
    console.error(err.message);
    res.status(404).send({
        status: 404,
        message: err.message
    });
});

// Serve static files
app.use(express.static(path.join(__dirname, "public")));
app.use(express.static(path.join(__dirname, "node_modules")));

//Export our app to use it in other files (like in index.common)
module.exports = app;
