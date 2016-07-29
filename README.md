# Mental Note DRF
Django restframework version of the mental note project.

# Usage

## build
`docker-componse build`

## initializer database
`docker-compose run django python ./src/manage.py migrate`

## run
`docker-compose run -p 8000:8000 django python ./src/manage.py runserver 0.0.0.0:8000`

## test
`docker-compose run django py.test ./src/`
