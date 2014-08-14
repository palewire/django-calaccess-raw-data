.PHONY: bootstrap clean cleanfile docs load loadtable runserver shell test

bootstrap:
	mysqladmin -h localhost -u root -pmysql drop calaccess
	mysqladmin -h localhost -u root -pmysql create calaccess
	python example/manage.py syncdb
	python example/manage.py downloadcalaccess
	python example/manage.py collectstatic --noinput
	python example/manage.py runserver

clean:
	python -m cProfile example/manage.py downloadcalaccess --skip-download --skip-unzip --skip-prep --skip-clear --skip-load > speed.txt

cleanfile:
	python -m cProfile example/manage.py cleancalaccessfile CVR_SO_CD.TSV > speed.txt

docs:
	cd docs && make livehtml

load:
	python example/manage.py downloadcalaccess --skip-download --skip-unzip --skip-prep --skip-clear --skip-clean

loadtable:
	python example/manage.py loadcalaccessfile FilerAcronymsCd

runserver:
	python example/manage.py runserver

shell:
	python example/manage.py shell

test:
	pep8 calaccess
	pyflakes calaccess
	coverage run setup.py test
	coverage report -m
