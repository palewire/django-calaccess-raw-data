.PHONY: db docs example runserver test

db:
	mysqladmin -h localhost -u root -pmysql drop calaccess
	mysqladmin -h localhost -u root -pmysql create calaccess

docs:
	cd docs && make livehtml

example:
	python example/manage.py syncdb
	python example/manage.py downloadcalaccess

runserver:
	python example/manage.py runserver

test:
	coverage run setup.py test
	coverage report -m
