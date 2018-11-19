const express = require('express');
const path = require('path');
const routes = require('./routes/index');

// Create a new express app
const app = express();

//Specify our paths and the view engine we use
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// Whenever we get a request on the form '/whatever' it should use the routes file to redirect
app.use('/', routes);

//Export our app to use it in other files (like in start.js)
module.exports == app;