# Hegardt

## Development

### Install npm dependencies
First, install all the dependencies:
```npm
npm install
```
### Create environment variables file
Then, create a .env file in the project root. Define the following variabes:
```
DB=
DB_USER=
DB_PASSWORD=
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