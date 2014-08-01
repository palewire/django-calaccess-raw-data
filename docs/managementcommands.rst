Management commands
===================

downloadcalaccess
------------------

.. code-block:: bash

    Usage: manage.py downloadcalaccess [options] 

    Download the latest snapshot of the CalAccess database

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
