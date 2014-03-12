# Django Cal-Access parser

**django-calacces-parser** is a simple Django app to download, extract and load the [CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/) campaign finance and lobbying activity database into MySQL.

Detailed documentation is in the "docs" directory. *(coming soon)*

## Requirements
- Django 1.6
- MySQL 5.5
- Patience

## Installation
- Install django-calaccess-parser with pip
```bash
$ pip install https://github.com/california-civic-data-coalition/django-calaccess-parser/archive/0.1-alpha.tar.gz
```

- Add `calaccess` to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = (
    ...
    'calaccess',
)
```

## Loading the data
- Set `settings.CALACCESS_DOWNLOAD_DIR` environment variable to your preferred path to store the data
- Next, sync the database, create a Django admin user, and run the management command to the load the CAL Access data 
```bash
$ python manage.py syncdb
$ python manage.py downloadaccess
```
:warning: This'll take a while. Go grab some coffee or do something else productive with your life.

## Available flags for `downloadcalaccess`
```
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

```
## Explore data

Start the development server and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   to inspect the Cal-access data (you'll need the Admin app enabled).
   
## Authors
- [Agustin Armendariz](https://github.com/armendariz)
- [Ben Welsh](https://github.com/palewire)
- [Aaron Williams](https://github.com/aboutaaron)
