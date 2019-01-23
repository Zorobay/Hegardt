const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

// Routes
const indexRouter = require("./routes/index");
const personalFileRouter = require("./routes/personal_file");
const registerRouter = require("./routes/register");
const searchRouter = require("./routes/search");

// Create a new express app
const app = express();

//Specify our paths and the view engine we use
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

// use bodyparser to parse url body
app.use(bodyParser.urlencoded({ extended: true }));

// Whenever we get a request on the form "/whatever" it should use the routes file to redirect
app.use("/register", registerRouter);
app.use("/ansedel/", personalFileRouter);
app.use("/search", searchRouter);
app.use("/", indexRouter);

// Serve static files
app.use(express.static(path.join(__dirname,"public")));
app.use(express.static(path.join(__dirname, "node_modules")));

//Set the app to use moment
app.locals.moment = require("moment");
//Export our app to use it in other files (like in start.js)
module.exports = app;