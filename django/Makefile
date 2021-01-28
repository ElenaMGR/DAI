all:
	sudo docker-compose up
build:
	sudo docker-compose build

django-startproject:
	sudo docker-compose run web django-admin startproject sitio_web .
	sudo chown -R ${USER}:${USER} .

django-startapp:
	sudo docker-compose run web python manage.py startapp mi_aplicacion
	sudo chown -R ${USER}:${USER} .

django-makemigrations:
	docker-compose run web python manage.py makemigrations

django-migrate:
	docker-compose run web python manage.py migrate

django-createsuperuser:
	docker-compose run web python manage.py createsuperuser

django-collectstatic:
	docker-compose run web python manage.py collectstatic

django-collectstatic-clear:
	docker-compose run web python manage.py collectstatic --clear