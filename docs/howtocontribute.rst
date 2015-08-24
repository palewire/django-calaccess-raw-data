How to contribute
=================

This walkthrough will show you how to install the source code of this application
to fix bugs and develop new features.

Preparing a development environment
-----------------------------------

It is not required, but it is recommended that development of the library
be done from within a contained virtual environment.

One way to accomplish is with Python's ``virtualenv`` tool and its helpful companion ``virtualenvwrapper``. If you have that installed a new project can be started with
the following:

.. code-block:: bash

    $ mkproject django-calaccess-raw-data

That will jump into a new folder in your code directory, where you can clone our code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-raw-data>`_.

.. code-block:: bash

    $ git clone https://github.com/california-civic-data-coalition/django-calaccess-raw-data.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements_dev.txt

Connecting to a local database
------------------------------

Unlike a typical Django project, this application only supports the MySQL and PostgreSQL database backends. This is because we enlist specialized tools to load the immense amount of source data more quickly than Django typically allows.

We haven't developer similar routines for SQLite and the other Django backends yet, but we're working on it. This might be something you could work on!

If you choose MySQL
~~~~~~~~~~~~~~~~~~~

Create a new database named ``calaccess`` like this:

.. code-block:: bash

    mysqladmin -h localhost -u root -p create calaccess

Create a file at ``example/project/settings_local.py`` to save your custom database credentials. That might look something like this.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'calaccess',
            'USER': 'yourusername', # <-- This
            'PASSWORD': 'yourpassword', # <-- And this
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'local_infile': 1,
            }
        }
    }

If you choose PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~

Create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess -U postgres

Create a file at ``example/project/settings_local.py`` to save your custom database credentials. That might look something like this.

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

Once the database is configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create the tables and get to work.

.. code-block:: bash

    $ python example/manage.py migrate

You might start by loading the data dump from the web.

.. code-block:: bash

    $ python example/manage.py downloadcalaccessrawdata
