.PHONY: db example runserver test

db:
	mysqladmin -h localhost -u root -pmysql drop calaccess
	mysqladmin -h localhost -u root -pmysql create calaccess

example:
	python example/manage.py syncdb

runserver:
	python example/manage.py runserver

test:
	coverage run setup.py test
	coverage report -m
