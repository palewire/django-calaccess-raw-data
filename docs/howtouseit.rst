How to use it
=============

This guide will walk users through the process of installing the latest official release `from the Python Package Index <https://pypi.python.org/pypi/django-calaccess-raw-data/>`_. If you want to install the raw source code or contribute as a developer refer to the `"How to contribute" <howtocontribute.html>`__ page.

.. warning::

    This library is intended to be plugged into a project created with the Django web
    framework. Before you can begin, you'll need to have one up and running.
    If you don't know how, `check out the official Django documentation <https://docs.djangoproject.com/en/dev/intro/tutorial01/>`_.

Installing the Django app
-------------------------

The latest official release of the application can be installed from the Python Package Index using ``pip``.

.. code-block:: bash

    $ pip install django-calaccess-raw-data

The app needs to be added to the ``INSTALLED_APPS`` in your Django project's ``settings.py`` configuration file.

.. code-block:: python

    INSTALLED_APPS = (
        # ... other apps up here ...
        'calaccess_raw',
    )

Connecting to a local database
------------------------------

Also in the ``settings.py`` file, you will need to configure Django so it can connect to a database.

Unlike a typical Django project, this application only supports the MySQL and PostgreSQL database backends. This is because we enlist specialized tools to load the immense amount of source data more quickly than Django typically allows. We haven't wdeveloped those routines for SQLite and the other Django backends yet, but we're working on it.

Pick one of the two and continue below.

If you choose MySQL
~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you have a MySQL server installed. If you don't, now is the time to hit Google and figure out how. If you're using Apple's OSX operating system, you can `install via Homebrew <http://thisdotlife.com/2013/05/30/how-to-install-mysql-on-mac-os-x-using-homebrew-tutorial/>`_. `Here <http://dev.mysql.com/doc/refman/5.5/en/installing.html>`_ is the official MySQL documentation for how to get it done.

Once that's handled, add a database connection string like this to your ``settings.py``.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'calaccess',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '3306',
            # You'll need this to use our data loading tricks
            'OPTIONS': {
                'local_infile': 1,
            }
        }
    }

Return the command line. This will create a MySQL database to store the data.

.. code-block:: bash

    $ mysqladmin -h localhost -u your-username-here -p create calaccess

And, if you don't have it already, you'll need to install a Python library that can access MySQL via Django. That can be done with `pip <https://pip.pypa.io/en/latest/installing.html>`_, a Python package management tool.

.. code-block:: bash

    $ pip install mysqlclient

If you choose PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you have a PostgreSQL server installed. If you don't, now is the time to hit Google and figure out how. `Here <https://wiki.postgresql.org/wiki/Detailed_installation_guides>`_ is the official PostgreSQL documentation for how to get it done.

Once that's handled, add a database connection string like this to your ``settings.py``.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

Return to the command line. This will create a PostgreSQL database to store the data.

.. code-block:: bash

    $ createdb calaccess

If you don't have it already, you'll need to install a Python library that can access PostgreSQL via Django. That can be done with `pip <https://pip.pypa.io/en/latest/installing.html>`_, a Python package management tool.

.. code-block:: bash

    $ pip install psycopg2

Loading the data
----------------

Now you're ready to create the database tables with Django using its ``manage.py`` utility belt.

.. code-block:: bash

    $ python manage.py migrate

Once everything is set up, this management command will download the latest bulk data release from the state and load it in the database. It'll take a while. Go grab some coffee.

.. code-block:: bash

    $ python manage.py downloadcalaccessrawdata

Exploring the data
------------------

Finally, start the development server and visit `localhost:8000/admin/ <http://localhost:8000/admin/>`_ in your browser to inspect the CAL-ACESS data in your Django administration panel.

.. code-block:: bash

    $ python manage.py runserver

If you don't have a super user that can log into the admin you might need to return to the command line and make one.

.. code-block:: bash

    $ python manage.py createsuperuser