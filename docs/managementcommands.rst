Management commands
===================

cleancalaccessrawfile
---------------------

Clean a source CAL-ACCESS file and reformat it as a CSV

.. code-block:: bash

    Usage: manage.py cleancalaccessrawfile [options] <file path>

    Clean a source CAL-ACCESS file and reformat it as a CSV

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit


downloadcalaccessrawdata
------------------------

Download, unzip, clean and load the latest snapshot of the CAL-ACCESS database

.. code-block:: bash

    Usage: manage.py downloadcalaccessrawdata [options] 

    Download, unzip, clean and load the latest snapshot of the CAL-ACCESS database

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on exception
      --skip-download       Skip downloading of the ZIP archive
      --skip-unzip          Skip unzipping of the archive
      --skip-prep           Skip prepping of the unzipped archive
      --skip-clear          Skip clearing out ZIP archive and extra files
      --skip-clean          Skip cleaning up the raw data files
      --skip-load           Skip loading up the raw data files
      --noinput             Download the ZIP archive without asking permission
      --version             show program's version number and exit
      -h, --help            show this help message and exit


loadcalaccessrawfile
--------------------

Load a cleaned CAL-ACCESS file for a model into the database

.. code-block:: bash

    Usage: manage.py loadcalaccessrawfile [options] <model name>

    Load a cleaned CAL-ACCESS file for a model into the database

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit


totalcalaccessrawdata
---------------------

Print out the total of CAL-ACCESS tables and rows in the database

.. code-block:: bash

    Usage: manage.py totalcalaccessrawdata [options] 

    Print out the total of CAL-ACCESS tables and rows in the database

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit


verifycalaccessrawfile
----------------------

Compare the number of records in a model against its source CSV

.. code-block: bash

    Usage: example/manage.py verifycalaccessrawfile [options] <model name>

    Compare the number of records in a model against its source CSV

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit

