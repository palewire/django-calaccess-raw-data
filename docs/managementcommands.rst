Management commands
===================

cleancalaccessrawfile
---------------------

Clean a source CAL-ACCESS file and reformat it as a CSV

.. code-block:: bash

    Usage: manage.py cleancalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color] [--keep-files]
                                           file_name

    Clean a source CAL-ACCESS file and reformat it as a CSV

    positional arguments:
      file_name

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      --keep-files          Keep original .tsv files


downloadcalaccessrawdata
------------------------

Download, unzip and prepare the latest snapshot of the CAL-ACCESS database

.. code-block:: bash

    Usage: manage.py downloadcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color]
                                              [--resume] [--keep-files]
                                              [--noinput]

    Download, unzip and prepare the latest snapshot of the CAL-ACCESS database

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      --resume              Resume downloading of the ZIP archive from a previous
                            attempt
      --keep-files          Keep downloaded zip and unzipped files
      --noinput             Download the ZIP archive without asking permission


loadcalaccessrawfile
--------------------

Load a cleaned CAL-ACCESS file for a model into the database

.. code-block:: bash

    Usage: manage.py loadcalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                          [--settings SETTINGS]
                                          [--pythonpath PYTHONPATH] [--traceback]
                                          [--no-color] [--c CSV] [--keep-files]
                                          [--d DATABASE] [-a APP_NAME]
                                          model_name

    Load clean CAL-ACCESS file into its corresponding database model

    positional arguments:
      model_name

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      --c CSV, --csv CSV    Path to comma-delimited file to be loaded. Defaults to
                            one associated with model.
      --keep-files          Keep original .tsv files
      --d DATABASE, --database DATABASE
                            Alias of database where data will be inserted.
                            Defaults to the 'default' in DATABASE settings.
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app where model will be imported from


totalcalaccessrawdata
---------------------

Print out the total of CAL-ACCESS tables and rows in the database

.. code-block:: bash

    Usage: manage.py totalcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color]

    Print out the total count tables and rows in the CAL-ACCESS raw database

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.


updatecalaccessrawdata
------------------------

Download, unzip, clean and load the latest snapshot of the CAL-ACCESS database

.. code-block:: bash

    Usage: manage.py updatecalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [--resume-download] [--skip-download]
                                            [--skip-clean] [--skip-load]
                                            [--keep-files] [--noinput]
                                            [--use-test-data] [-d DATABASE]
                                            [-a APP_NAME]

    Download, unzip, clean and load the latest snapshot of the CAL-ACCESS database

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      --resume-download     Resume downloading of the ZIP archive from a previous
                            attempt
      --skip-download       Skip downloading of the ZIP archive
      --skip-clean          Skip cleaning up the raw data files
      --skip-load           Skip loading up the raw data files
      --keep-files          Keep zip, unzipped, .tsv and .csv files
      --noinput             Download the ZIP archive without asking permission
      --use-test-data       Use sampled test data (skips download, unzip, prep,
                            clear)
      -d DATABASE, --database DATABASE
                            Alias of database where data will be inserted.
                            Defaults to the 'default' in DATABASE settings.
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app where model will be imported from

verifycalaccessrawfile
----------------------

Compare the number of records in a model against its source CSV

.. code-block:: bash

    Usage: manage.py verifycalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            model_name

    Compare the number of records in a model against its source CSV

    positional arguments:
      model_name

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.

