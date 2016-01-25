Changelog
=========

0.2.0 (January 2016)
---------------------

* Support for Python 3.5
* Support for Django 1.9
* Simplified downloadcalaccessrawdata. Now only downloads, unzips and preps
* Introduced updatecalaccessrawdata, which downloads, cleans and loads data
* Added --resume-download option in case download is interrupted
* Added --csv option to loadcalaccessrawfile so that users can load from a file other than the one specified for the given calaccess_raw model
* Added --keep-files option. Unless the option is invoked downloadcalaccessrawdata, cleancalaccessrawfile, loadcalaccessrawfile and updatecalaccessrawdata now clear out original and intermediate files  
* Support for multiple databases configured in Django DATABASE settings. Users can now load into a specified database using --database option
* Fixed verifycalaccessrawfile
* Updated management command options to most recent Django style, using argparse instead of optparse
* Hundreds of unique keys, field defs and choices patched by Code Rushers
* Automatically generated table documentation page
* Expanded documentation

0.1.2 (February 2015)
---------------------

* Substituted clint for progressbar
* Improved choices for form type fields

0.1.1 (January 2015)
--------------------

* Datetime support for MySQL fields
* Fixed bug that didn't allow null values in PostgreSQL datetime fields


0.1.0 (November 2014)
---------------------

* Support for PostgreSQL database backends
* Upgraded to Django 1.7
* Prettified management command output and logging
* Improved docs, admins and configuration for some campaign finance models
* Numerous small bug fixes and documentation corrections


0.0.7 (August 2014)
-------------------

* Complete set of models that cover 100% of source CSV files
* Management commands that prep and load the data for MySQL backends
* Administration panels for previewing the data
