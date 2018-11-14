all: install test migrate start link

install:
	pip3 install -r requirements.txt

test:
	python3 manage.py test

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

start:
	python3 manage.py runserver
