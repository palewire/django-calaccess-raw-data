.PHONY: bootstrap docs load rs sh ship test

bootstrap:
	mysqladmin -h localhost -u root -p create calaccess_raw
	python example/manage.py makemigrations calaccess_raw
	python example/manage.py migrate
	python example/manage.py update
	python example/manage.py collectstatic --noinput
	python example/manage.py runserver

docs:
	python example/manage.py createcalaccessrawmodeldocs
	cd docs && make livehtml

load:
	python  example/manage.py updatecalaccessrawdata --skip-download --skip-clean --keep-files

testload:
	dropdb calaccess_raw
	createdb calaccess_raw
	python example/manage.py migrate
	python example/manage.py test calaccess_raw;

rs:
	python example/manage.py runserver

sh:
	python example/manage.py shell

ship:
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

test:
	flake8 calaccess_raw
	coverage run example/manage.py test calaccess_raw
	coverage report -m

testdocs:
	python example/manage.py test calaccess_raw.tests.test_docs.DocumentationTestCase

testutils:
	coverage run example/manage.py test calaccess_raw.tests.test_utilities.UtilityTestCase
	coverage report -m

testannotations:
	coverage run example/manage.py test calaccess_raw.tests.test_annotations.AnnotationTestCase
	coverage report -m

testfields:
	coverage run example/manage.py test calaccess_raw.tests.test_fields.FieldTestCase
	coverage report -m

testcommands:
	coverage run example/manage.py test calaccess_raw.tests.test_commands.CommandTestCase
	coverage report -m

testadmins:
	coverage run example/manage.py test calaccess_raw.tests.test_admins.AdminTestCase
	coverage report -m

testmodels:
	coverage run example/manage.py test calaccess_raw.tests.test_models.ModelTestCase
	coverage report -m
