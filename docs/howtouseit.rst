How to use it
=============

Installing the Django app
-------------------------

The latest official release of the application can be installed from the Python Package Index using ``pip``.

.. code-block:: bash

    $ pip install django-calaccess-raw-data

The app needs to be added to the ``INSTALLED_APPS`` in your Django project's settings.

.. code-block:: python

    INSTALLED_APPS = (
        # ... other apps up here ...
        'calaccess_raw',
    )

Also in the Django settings, create a database configure Django so it can connect to it. You have a choice of two different databases when using this application, MySQL and PostgreSQL.

The settings below refer to using MySQL as your database.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'calaccess',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '3306',
            # You'll need this to use our data loading tricks
            'OPTIONS': {
                'local_infile': 1,
            }
        }
    }

This will create the MySQL database.

.. code-block:: bash

    $ mysqladmin -h localhost -u root -p create calaccess

The settings below refer to using PostgreSQL as your database.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

This will create the PostgreSQL database.

.. code-block:: bash

    $ createdb calaccess

Now you're ready to sync the database tables.

.. code-block:: bash

    $ python manage.py migrate

Loading the data
----------------

Once everything is set up, this management command will download the latest bulk data release from the state
and load it in the database. This'll take a while. Go grab some coffee.

.. code-block:: bash

    $ python manage.py downloadcalaccessrawdata

Exploring the data
------------------

Start the development server and visit `http://localhost:8000/admin/ <http://127.0.0.1:8000/admin/>`_
to inspect the CAL-ACESS data in your Django administration panel.

.. code-block:: bash

    $ python manage.py runserver
