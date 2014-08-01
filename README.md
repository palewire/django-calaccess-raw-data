# django-calaccess-parser

A simple Django app to download, extract and load the [CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/) campaign finance and lobbying activity database.

[![Build Status](https://travis-ci.org/california-civic-data-coalition/django-calaccess-parser.png?branch=master)](https://travis-ci.org/california-civic-data-coalition/django-calaccess-parser)
[![PyPI version](https://badge.fury.io/py/django-calaccess-parser.png)](http://badge.fury.io/py/django-calaccess-parser)
[![Coverage Status](https://coveralls.io/repos/california-civic-data-coalition/django-calaccess-parser/badge.png?branch=master)](https://coveralls.io/r/california-civic-data-coalition/django-calaccess-parser?branch=master)

* Documentation: [http://django-calaccess-parser.rtfd.org](http://django-calaccess-parser.rtfd.org)
* Issues: [https://github.com/california-civic-data-coalition/django-calaccess-parser/issues](https://github.com/california-civic-data-coalition/django-calaccess-parser/issues)
* Packaging: [https://pypi.python.org/pypi/django-calaccess-parser](https://pypi.python.org/pypi/django-calaccess-parser)
* Testing: [https://travis-ci.org/california-civic-data-coalition/django-calaccess-parser](https://travis-ci.org/california-civic-data-coalition/django-calaccess-parser)
* Coverage: [https://coveralls.io/r/california-civic-data-coalition/django-calaccess-parser](https://coveralls.io/r/california-civic-data-coalition/django-calaccess-parser)

## Requirements

- Django 1.6
- MySQL 5.5
- Patience

## Installation

- Install django-calaccess-parser with pip

```bash
$ pip install https://github.com/california-civic-data-coalition/django-calaccess-parser/archive/master.zip
```

- Configure the `DATABASE` dictionary in `settings.py`
```python
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'local_calaccess_db',
        'USER': 'calaccessuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'local_infile': 1,
        }
    }
}
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
This'll take a while. Go grab some coffee or do something else productive with your life.

## Explore data

Start the development server and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   to inspect the Cal-access data (you'll need the Admin app enabled).
