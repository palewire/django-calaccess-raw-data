How to contribute
=================

This walkthrough will show you how to install the source code of this application
to fix bugs and develop new features.

First create a new virtualenv.

.. code-block:: bash

    $ virtualenv django-calaccess-parser

Jump in.

.. code-block:: bash

    $ cd django-calaccess-parser
    $ . bin/activate

Clone the repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-parser>`_.

.. code-block:: bash

    $ git clone https://github.com/california-civic-data-coalition/django-calaccess-parser.git repo

Move into it and install the Python dependencies.

.. code-block:: bash

    $ cd repo
    $ pip install -r requirements_dev.txt

Make sure you have a MySQL database installed. If you don't, now is the time to hit Google and figure out how.
Then create a new database named ``calaccess``.

.. code-block:: bash

    mysqladmin -h localhost -u root -pmysql create calaccess

If you have a different username or password substitute it above. And then create a file at ``example/project/settings_local.py``
where you where you save your custom database credentials. That might look something like this.

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

Finally create your database and get to work.

.. code-block:: bash

    $ python example/manage.py syncdb

You might start by loading the data dump from the web.

.. code-block:: bash

    $ python example/manage.py downloadaccess
