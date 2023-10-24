run:
	python manage.py runserver

mig:
	python manage.py makemigrations
	python manage.py migrate

admin:
	python manage.py createsuperuser

proj:
	django-admin startproject config .

app:
	django-admin startapp default
