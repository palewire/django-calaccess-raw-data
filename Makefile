.PHONY: bootstrap docs load rs sh ship test

bootstrap:
	pipenv run python example/manage.py makemigrations calaccess_raw
	pipenv run python example/manage.py migrate
	pipenv run python example/manage.py update
	pipenv run python example/manage.py collectstatic --noinput
	pipenv run python example/manage.py runserver

docs:
	pipenv run python example/manage.py createcalaccessrawmodeldocs
	cd docs && make livehtml

load:
	pipenv run python  example/manage.py updatecalaccessrawdata --skip-download --skip-clean --keep-files

testload:
	dropdb calaccess_raw
	createdb calaccess_raw
	pipenv run python example/manage.py migrate
	pipenv run python example/manage.py test calaccess_raw;

rs:
	pipenv run python example/manage.py runserver

sh:
	pipenv run python example/manage.py shell

ship:
	rm -rf build/
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/* --skip-existing

test:
	pipenv run flake8 calaccess_raw
	pipenv run coverage run example/manage.py test calaccess_raw
	pipenv run coverage report -m

testdocs:
	pipenv run python example/manage.py test calaccess_raw.tests.test_docs.DocumentationTestCase

testutils:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_utilities.UtilityTestCase
	pipenv run coverage report -m

testannotations:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_annotations.AnnotationTestCase
	pipenv run coverage report -m

testfields:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_fields.FieldTestCase
	pipenv run coverage report -m

testcommands:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_commands.CommandTestCase
	pipenv run coverage report -m

testadmins:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_admins.AdminTestCase
	pipenv run coverage report -m

testmodels:
	pipenv run coverage run example/manage.py test calaccess_raw.tests.test_models.ModelTestCase
	pipenv run coverage report -m
