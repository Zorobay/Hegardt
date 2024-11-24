import express from 'express';
import handlebars from 'express-handlebars';
import path, {dirname} from 'path';
import PersonService from "./src/services/PersonService.js";
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import LanguageService from "./src/services/LanguageService.js";

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// ==== Load env variables ====
const port = process.env.PORT || 3000;

// ==== Setup services ====
const personService = new PersonService();
const languageService = new LanguageService();

const app = express();
const hbs = handlebars.create({
    helpers: {
        testHelper() {
            return 'test!';
        },
        l(key) {
            console.log("gdsgf")
            return (Math.random() * 100).toString();
        }
    },
    layoutsDir: path.join(__dirname, '/views/layouts'),
    partialsDir: path.join(__dirname, 'views/partials'),
    extname: 'hbs',
    defaultLayout: 'main',
});

//Serves static files
app.use('/assets', express.static(path.join(__dirname, 'assets')))

//Sets our app to use the handlebars engine
app.set('view engine', 'hbs');
app.set("views", "./views");
//Sets handlebars configurations (we will go through them later on)
app.engine('hbs', hbs.engine);

// Register endpoints
app.get('/', (req, res) => {
    res.render('home');
});

app.get('/table/view', (req, res) => {
    res.render('table', personService.getAllPersons());
})

app.get('/person/:id', (req, res) => {
    const id = req.params.id;
    res.render('person', personService.getPersonById(id));
})

//Makes the app listen to port 3000
app.listen(port, () => console.log(`App listening to port http://localhost:${port}`));
