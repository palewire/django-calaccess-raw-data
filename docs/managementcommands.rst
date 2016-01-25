Management commands
===================

Updating the database
---------------------

updatecalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~~

This master command. It brings together all of the other update commands to
download, unzip, clean and load the latest snapshot of the CAL-ACCESS database.

Examples
````````

Running the entire routine is as simple as this.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata

If your download crashes, there's a way to restart it.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --resume-download

You can skip the download's confirmation prompt using Django's standard ``--noinput`` option.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --noinput

Individual components of the routine can be skipped with corresponding options.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --skip-download
    # Or...
    $ python manage.py updatecalaccessrawdata --skip-clean
    # Or...
    $ python manage.py updatecalaccessrawdata --skip-load
    # And feel free to mix and match...
    $ python manage.py updatecalaccessrawdata --skip-download --skip-clean

The source files downloaded as part of the process will be deleted unless the ``--keep-files``
option is provided.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --keep-files

The other options are below.

Options
```````

.. code-block:: bash

    usage: manage.py updatecalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [--resume-download] [--skip-download]
                                            [--skip-clean] [--skip-load]
                                            [--keep-files] [--noinput] [--test]
                                            [-d DATABASE] [-a APP_NAME]

    Download, unzip, clean and load the latest CAL-ACCESS database ZIP

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
      --resume-download     Resume downloading of ZIP archive from a previous
                            attempt
      --skip-download       Skip downloading of the ZIP archive
      --skip-clean          Skip cleaning up the raw data files
      --skip-load           Skip loading up the raw data files
      --keep-files          Keep zip, unzipped, TSV and CSV files
      --noinput             Download the ZIP archive without asking permission
      --test, --use-test-data
                            Use sampled test data (skips download, clean a load)
      -d DATABASE, --database DATABASE
                            Alias of database where data will be inserted.
                            Defaults to the 'default' in DATABASE settings.
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app where model will be imported from


cleancalaccessrawfile
~~~~~~~~~~~~~~~~~~~~~

Clean a source CAL-ACCESS TSV file and reformat it as a CSV. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

Provide the name of the TSV file you would like to process. The command will
attempt to find it in the application's download directory.

.. code-block:: bash

    $ python manage.py cleancalaccessrawfile RcptCd.TSV

The original file will be deleted in favor of the new CSV unless the ``--keep-files``
option is provided.

.. code-block:: bash

    $ python manage.py cleancalaccessrawfile RcptCd.TSV --keep-files

Options
```````

.. code-block:: bash

    usage: manage.py cleancalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color] [--keep-files]
                                           file_name

    Clean a source CAL-ACCESS TSV file and reformat it as a CSV

    positional arguments:
      file_name             Name of the TSV file to be cleaned and discarded for a
                            CSV

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
      --keep-files          Keep original TSV file

downloadcalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~~~~

Download, unzip and prep the latest CAL-ACCESS database ZIP. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

Here is how to run the command.

.. code-block:: bash

    $ python manage.py downloadcalaccessrawdata

If your download crashes, there's a way to restart it.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --resume-download

You can skip the download's confirmation prompt using Django's standard ``--noinput`` option.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata --noinput

Options
```````

.. code-block:: bash

    usage: manage.py downloadcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color]
                                              [--resume] [--keep-files]
                                              [--noinput]

    Download, unzip and prep the latest CAL-ACCESS database ZIP

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
~~~~~~~~~~~~~~~~~~~~

Load clean CAL-ACCESS CSV file into a database model. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

The command expects the name of the Django database model where the file
will be loaded.

.. code-block:: bash

    $ python manage.py loadcalaccessrawfile RcptCd

The model will attempt to load its default CSV file unless one is provided with the ``--csv`` argument.

.. code-block:: bash

    $ python manage.py loadcalaccessrawfile RcptCd --csv=/home/jerry/Data/MyFile.csv

Options
```````

.. code-block:: bash

    usage: manage.py loadcalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                          [--settings SETTINGS]
                                          [--pythonpath PYTHONPATH] [--traceback]
                                          [--no-color] [--c CSV] [--keep-files]
                                          [--d DATABASE] [-a APP_NAME]
                                          model_name

    Load clean CAL-ACCESS CSV file into a database model

    positional arguments:
      model_name            Name of the model into which data will be loaded

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
      --keep-files          Keep CSV file after loading
      --d DATABASE, --database DATABASE
                            Alias of database where data will be inserted.
                            Defaults to the 'default' in DATABASE settings.
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app where model will be imported from


Inspecting the data
-------------------

totalcalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~

Print table and record counts from the CAL-ACCESS raw database

Examples
````````

.. code-block:: bash

    $ python manage.py totalcalaccessrawdata

Options
```````

    usage: manage.py totalcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color]

    Print table and record counts from the CAL-ACCESS raw database

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


verifycalaccessrawfile
~~~~~~~~~~~~~~~~~~~~~~

Compare the number of records in a model against its source CSV

Examples
````````

The command expects to be provided with the name of a Django model to analyze.

.. code-block:: bash

    $ python manage.py verifycalaccessrawfile RcptCd

Options
```````

.. code-block:: bash'

    usage: manage.py verifycalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [-a APP_NAME]
                                            model_name

    Compare the number of records in a model against its source CSV

    positional arguments:
      model_name            Name of model to verify

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
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app where model will be imported from
