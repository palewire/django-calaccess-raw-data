How to contribute
=================

This walkthrough will show you how to install the source code of this application
to fix bugs and develop new features.

First create a new virtualenv.

.. code-block:: bash

    $ virtualenv django-calaccess-raw-data

Jump in.

.. code-block:: bash

    $ cd django-calaccess-raw-data
    $ . bin/activate

Clone the repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-raw-data>`_.

.. code-block:: bash

    $ git clone https://github.com/california-civic-data-coalition/django-calaccess-raw-data.git repo

Move into it and install the Python dependencies.

.. code-block:: bash

    $ cd repo
    $ pip install -r requirements_dev.txt

Make sure you have MySQL or PostgreSQL installed, because we don't currently support any other database backends.

If you want to use MySQL. Create a new database named ``calaccess`` like this:

.. code-block:: bash

    mysqladmin -h localhost -u root -p create calaccess

Then create a file at ``example/project/settings_local.py`` to save your custom database credentials. That
might look something like this.

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

If you'd prefer to use PostgreSQL, your local settings should be more like this:

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

This create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess

Finally create your database and get to work.

.. code-block:: bash

    $ python example/manage.py migrate

You might start by loading the data dump from the web.

.. code-block:: bash

    $ python example/manage.py downloadcalaccessrawdata
