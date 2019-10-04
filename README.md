# russianhackteam
Tutorial on GitHub Pages + Travis CI + Heroku + Zeit with simple Flask app.

[![Build Status](https://travis-ci.org/morejust/russianhackteam.svg?branch=master)](https://travis-ci.org/morejust/russianhackteam)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Deploy to now](https://deploy.now.sh/static/button.svg)](https://deploy.now.sh/?repo=https://github.com/morejust/russianhackteam)

### Flask project files

* **index.html** - just redirect to `templates/index.html` - for GH Pages demo
* **templates/** folder with html files
* **requirements.txt** - python packages to be installed 


## Need for services

### [GitHub Pages](https://morejust.github.io/russianhackteam)

* index.html (in `master`, `docs` or `gh-pages` branch)
* proper routing for static files (please google)

### [Travis](https://travis-ci.org/morejust/russianhackteam)

* .travis.yml

### [Heroku](https://russianhackteam.herokuapp.com/)

* Procfile
* app.json (optional: only to make "deploy with heroku" button work)

### [Zeit](https://russianhackteam.okhlopkov.now.sh)

* now.json
* non-organization repos only
* non-mutable disk of deployed server




-----------
Автор: [@ohld](https://okhlopkov.com) вдохновлялся:
* Документациями
* https://github.com/realpython/discover-flask
* https://zeit.co/blog/python-wsgi
