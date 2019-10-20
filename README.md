# Hegardt

## TODO
- [ ] Store people as a HashMap in the store to allow for fast retrieval with ID
- [ ] Implement login functionality
- [ ] Implement admin mode to edit people and upload new people
- [ ] Implement function to choose **language**!
  - [x] Implement language button
  - [ ] Save language file to local storage (validate age of it too)
  - [ ] Set active class to dropdown item when clicked
- [ ] Features in `PersonalFilePage`
  - [ ] Fix siblings
- [ ] Features in `search-form`
  - [x] Get search function to work again
  - [ ] Searching for `Johan Hegardt` now matches ALL Johan...not what we want.
  - [ ] Disable chrome form fill
  - [ ] Enable arrow keys to be used in the result list (go over to a modified dropdown list?)
- [ ] Features in `People map`
  - Filtering (in a `Form` inside a `Collapse`)
    - [ ] Gender
    - [ ] Name
    - [ ] Dead or alive
    - [ ] Location by born/dead/buried
  - Other features
    - [ ] Implement linking to PersonalFile when clicking on a marker in map

## Running the web app

First, install nodemon: `npm -g install nodemon`. 

### Backend
Run the backend using: `nodemon backend/index.js`
You can repopulate the database from the JSON database file by running the backend with the option `--populate`

### Frontend
Run the frontend using: 

```bash
cd client
npm run serve --fix
```

## Development

### Install npm dependencies
First, install all the dependencies:
```npm
npm install
```
### Create environment variables file
Then, create a `backend/.env` file. Define the following variabes:
```
DB=<database URL>
DB_USER=<database username>
DB_PASSWORD=<database password>
HERE_API_ID=<HERE api ID>
HERE_API_KEY=<HERE api key>
```

### Setup heroku
Install the [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if not already installed: 

Open console and login to heroku using `heroku login`. Find the heroku project name using `heroku list`.

Finally, add the gir remote to be able to push new changes to heroku:

```
heroku git:remote -a <project name> -r heroku
```

### Push changes to heroku and git

Changes can be pushed to git ONLY using `git push origin master` and to heroku ONLY using `git push heroku master`.
