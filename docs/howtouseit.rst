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

Also in the Django settings, configure a database connection. Currently this application only supports MySQL backends.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'my_calaccess_db',
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

Now you're ready to sync the database tables.

.. code-block:: bash

    $ python manage.py syncdb

A final setting, ``CALACCESS_DOWNLOAD_DIR``, tels our application where to store the large files it's going to download.
You can put it anywhere you want.

.. code-block:: python

    CALACCESS_DOWNLOAD_DIR = "/path/to/wherever/"

Or you could put the files in your system's temp directory, if you felt like it

.. code-block:: python

    import tempfile
    CALACCESS_DOWNLOAD_DIR = tempfile.gettempdir()

Loading the data
----------------

Once everything is set up, this management command will download the latest bulk data release from the state
and load it in the database. This'll take a while. Go grab some coffee.

.. code-block:: bash

    $ python manage.py downloadaccess

Exploring the data
------------------

Start the development server and visit `http://localhost:8000/admin/ <http://127.0.0.1:8000/admin/>`_
to inspect the CAL-ACESS data in your Django administration panel.

.. code-block:: bash

    $ python manage.py runserver
