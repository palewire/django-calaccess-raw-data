.PHONY: bootstrap docs load runserver test

bootstrap:
	mysqladmin -h localhost -u root -pmysql drop calaccess
	mysqladmin -h localhost -u root -pmysql create calaccess
	python example/manage.py syncdb
	python example/manage.py downloadcalaccess
	python example/manage.py collectstatic --noinput
	python example/manage.py runserver

docs:
	cd docs && make livehtml

load:
	python example/manage.py --skip-download --skip-unzip --skip-prep --skip-clear --skip-clean

runserver:
	python example/manage.py runserver

test:
	coverage run setup.py test
	coverage report -m
