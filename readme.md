## Build app :
pip install -r requirements.txt

## Create database
python3 manage.py migrate

## Generate fixtures:
python manage.py loaddata fixture.json

## Unit tests
python manage.py test

## Functional tests (end to end tests)
e2e.py is an example functional test that can be launched in gitlab-ci with the functional_tests stage in .gitlab-ci.yml

## Run app:
python manage.py runserver 0.0.0.0:8000


