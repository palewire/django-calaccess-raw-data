# Django Calaccess Parser *(in active development)*

Download, extract and load the [CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/) campaign finance and lobbying activity database.

Currently tied to MySQL just to get it in and look at it. Need to figure out how to leverage CSVKit and shoehorn it into Django.

* cal_access_testing.sql -- MySQL dump of the table schemas.

* env_settings.py.example -- set-up your local settings here and save as env_settings.py.

* clean_data.py -- quoting of fields was a problem with the data before they moved to TSV from CSV format. This fixed that as well as NULL bytes in the data. It would be great to get taking care of encoding, date conversions and the rest right here.

* load_cut.py -- uses LOAD DATA INFILE to quickly suck in the data and make some lookup tables.

* check_load.py -- make sure rows imported matches the number of lines in the csv file.

## Requirements
- Python 2.7
- MySQL 5.5

*If you want to use the campaign finance app:*
- Node 0.10.25
- npm 1.3.x
- grunt-cli
- bower

The project is structured using the Datadesk [django project template](https://github.com/datadesk/django-project-template). Check out that codebase to understand how this project is setup.

## Installation
First, setup a virtual environment for the project.

__With virtualenv__
```bash
$ cd my-virtual-envs
$ virtualenv --no-site-packages calaccess
$ cd calaccess
$ . bin/activate
```

__With [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)__
```bash
$ mkvirtualenv calaccess
```

Clone the repo, install the dependecies, and configure the project 
```bash
$ git clone git@github.com:california-civic-data-coalition/django-calaccess-parser.git
$ cd django-calaccess-parser
$ pip install -r requirements.txt
$ cp project/settings_dev.template project/settings_dev.py
```
### Database setup
If you haven't already, create a MySQL user and database to store the CAL Access data and add it to `settings_dev.py`. This should look something like:
```bash
$ mysql -uroot
```
```sql
CREATE DATABASE local_calaccess_db;
CREATE USER 'calaccessuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* To 'calaccessuser'@'localhost' IDENTIFIED BY 'password';

```

:rotating_light: __HEADS UP__: Ensure that `DEBUG` is set to `False` and `local_infile:1` is added to the database tuple in your `settings_dev.py` file __BEFORE__ you run the load commands (See [settings_dev.template](https://github.com/california-civic-data-coalition/django-calaccess-parser/blob/master/project/settings_dev.template) for an example). Otherwise, when MySQL throws a warning or error, the Django ORM will stop the data load. Be sure to return `DEBUG` to `True` later when doing active development on the application.

### Loading the data

Next, sync the database, create a Django admin user, and run the management command to the load the CAL Access data 
```bash
$ python manage.py syncdb
$ python manage.py downloadaccess
```

:warning: This'll take a while. Go grab some coffee or do something else productive with your life.

## Setting up the Campaign Finance app

The campaign finance app tracks the spending and cashflow candidates, PACs, and organizations. The app frontend build is handled by [Grunt](http://gruntjs.com/), a JavaScript tasks manager for Node.js. Make sure you have the requirements listed at the top of the README installed before loading this app up. 

Now, hop into the python shell and load up the models for the `campaign_finance` app
```bash
$ python manage.py shell
```
```python
from campaign_finance import load

load.load()
```
:warning: This'll take a while. Go grab *another* coffee or do something else productive with your life.

### Setup search
Search isn't really wired up yet but we can use [Haystack's](http://django-haystack.readthedocs.org/en/latest/toc.html) dummy search for now. Go ahead and build the index to search against.
```bash
$ python manage.py rebuild_index
```

### Setup Node, Npm, Grunt and Bower 
Everything should be good now (Go ahead and set `DEBUG` to `True` in `settings_dev.py`). Let's install the required Grunt tasks and JavaScript libraries. 

If you don't have node.js installed, go ahead and run the following fab commands:
```bash
$ fab install_node
$ fab get_node_libs
```

With that installed, let's download our frontend dependencies:
```bash
$ npm install && bower install
```

### Running the Campaign Finance app

Fire up the server and get our Grunt tasks running.
```bash 
fab rs
```

In a new terminal window, start Grunt tasks from the project root
```bash
grunt
```
Now browse to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the app in action

### License
The MIT License (MIT)

Copyright (c) 2014 California Civic Data Coalition

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
