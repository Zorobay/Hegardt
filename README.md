# Hegardt Frontend

## TODO
- [x] Update gender of all people by parsing HTML (father, mother or grandfather, grandmother)...
- [x] Store people and recipes as a HashMap in the store to allow for fast retrieval with ID
- [ ] Implement **webpack**
- [ ] Implement login functionality
- [ ] Implement admin mode to edit people and upload new people
- [ ] Implement function to choose **language**!
  - [x] Implement language button
  - [ ] Implement the language in most elements on the site.
  - [ ] Save language file to local storage (validate age of it too)
  - [ ] Set active class to dropdown item when clicked
- [ ] Features in `PersonalFilePage`
  - [x] Add birth date to the right of all names (links)
  - [x] Fix children
  - [x] Fix siblings
- [ ] Features in `search-form`
  - [x] Get search function to work again
  - [ ] Show birth date in small print under the name in results
  - [ ] Searching for `Johan Hegardt` now matches ALL Johan...not what we want.
  - [x] Disable chrome form fill
  - [ ] Enable arrow keys to be used in the result list (go over to a modified dropdown list?)
- [ ] Features in `People map`
  - [ ] Implement linking to PersonalFile when clicking on a marker in map
  - Filtering (in a `Form` inside a `Collapse`)
    - [ ] Gender
    - [ ] Name
    - [x] Dead or alive
    - [ ] Location by born/dead/buried
- [ ] `SignupPage`
    - [ ] Check that the personal ID exists, and print the name that it links to.
    - [ ] Check that email is not already registered!
- [ ] **CV**
- [ ] **Recipes**
    - [x] Upload recipes to collection
    - [x] Create recipe Model
    - [x] List all recipes
    - [x] Recipe page
    - [ ] Creat a table of contents sidebar
## Running the web app

Run the frontend using: 

```bash
npm run serve --fix
```

## Development

### Install npm dependencies
First, install all the dependencies:
```npm
npm install
```

### Define environment variables

Create a `.env` file in the root directory and define the following variables

```.env
# Requires the prefix VUE_APP and url requires http/https:// protocol
VUE_APP_API_BASE_URL=<http://url:port>  
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
