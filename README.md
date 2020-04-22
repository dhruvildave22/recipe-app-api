# recipe-api


## Getting started

To start project, run:

```
$ git clone git@github.com:dhruvildave22/recipe-app-api.git
$ cd recipe-api
$ docker build .
$ docker-compose build
$ docker-compose run app sh -c "python manage.py makemigrations"
$ docker-compose run app sh -c "python manage.py migrate"
$ docker-compose run app sh -c "python manage.py createsuperuser"
```

at last run this command to run server
```
$ docker-compose up
```

It will be starting development server at http://127.0.0.1:8000/
