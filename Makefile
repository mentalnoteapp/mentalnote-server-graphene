DOCKER := $(shell which docker-compose)
NPM := $(shell which npm)
PYTHON := env/bin/python
PIP := env/bin/pip

all: venv docker

venv:
	virtualenv -p python3 env
	$(PIP) install -r requirements.txt

docker:
	docker-compose build
	#docker-compose run django python ./source/manage.py migrate
	#docker-compose run django python ./source/manage.py collectstatic --noinput
