.PHONY: bootstrap docs load rs sh test

bootstrap:
	mysqladmin -h localhost -u root -pmysql drop calaccess
	mysqladmin -h localhost -u root -pmysql create calaccess
	python example/manage.py syncdb
	python example/manage.py downloadcalaccessrawdata
	python example/manage.py collectstatic --noinput
	python example/manage.py runserver

docs:
	python example/manage.py createcalaccessrawmodeldocs
	cd docs && make livehtml

load:
	python  example/manage.py downloadcalaccessrawdata --skip-download --skip-unzip --skip-prep --skip-clear --skip-clean

testload:
	dropdb calaccess_raw
	createdb calaccess_raw
	python example/manage.py migrate
	python example/manage.py test calaccess_raw;

rs:
	python example/manage.py runserver

sh:
	python example/manage.py shell

test:
	pep8 calaccess_raw
	pyflakes calaccess_raw
	coverage run example/manage.py test calaccess_raw
	coverage report -m
