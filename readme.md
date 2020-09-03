## build app :
pip install -r requirements.txt

## Create database
python3 manage.py migrate

## generate fixtures:
python manage.py loaddata fixture.json

## unit tests
python manage.py test

## run app:
python manage.py runserver 0.0.0.0:8000


