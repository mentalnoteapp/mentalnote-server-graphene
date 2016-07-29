# Mental Note DRF
Django restframework version of the mental note project.

# Usage

## build
1. `docker-componse build`

## initializer database
1. `docker-compose run django python ./src/manage.py migrate`

## run
1. `docker-compose run -p 8000:8000 django python ./src/manage.py runserver 0.0.0.0:8000`
