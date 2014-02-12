# Django Calaccess Parser

Download, extract and load the [CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/) campaign finance and lobbying activity database.

Currently tied to MySQL just to get it in and look at it. Need to figure out how to leverage CSVKit and shoehorn it into Django.

* cal_access_testing.sql -- MySQL dump of the table schemas.

* env_settings.py.example -- set-up your local settings here and save as env_settings.py.

* clean_data.py -- quoting of fields was a problem with the data before they moved to TSV from CSV format. This fixed that as well as NULL bytes in the data. It would be great to get taking care of encoding, date conversions and the rest right here.

* load_cut.py -- uses LOAD DATA INFILE to quickly suck in the data and make some lookup tables.

* check_load.py -- make sure rows imported matches the number of lines in the csv file.

### Requirements
- Python 2.7
- MySQL 5.5

*If you want to use the campaign finance app:*
- Node 0.10.25
- npm 1.3.x
- grunt-cli
- bower

### Installation
```bash
$ git clone git@github.com:california-civic-data-coalition/django-calaccess-parser.git
$ cd django-calaccess-parser
$ cp project/settings_dev.template project/settings_dev.py
```
Clone the repo, `cd` inside of it and then create a local `settings_dev.py` file. If you haven't already, create a MySQL database to store the CAL Access data and add it to `settings_dev.py`.

:rotating_light: *HEADS UP*: Ensure that `DEBUG` is set to `False` and `local_infile=1` is add to the database tuple in your `settings_dev.py` file __BEFORE__ you run the load commands (See [settings_dev.template](https://github.com/california-civic-data-coalition/django-calaccess-parser/blob/master/project/settings_dev.template) for an example). Otherwise, when MySQL throws a warning or error, the Django ORM will stop the data load. Be sure to return `DEBUG` to `True` later when doing active development on the application.

Next, sync the database, create a Django admin user, and run the management command to the load the CAL Access data 
```bash
$ python manage.py syncdb
$ python manage.py downloadaccess
```

:warning: This'll take a while. Go grab some coffee or do something else productive with your life.

### Setting up the Campaign Finance app

Now, hop into the python shell and load up the models for the `campaign_finance` app
```bash
$ python manage.py shell
```
```python
from campaign_finance import load

load.load()
```
:warning: This'll take a while. Go grab *another* coffee or do something else productive with your life.

Everything should be good now (Go ahead and set `DEBUG` to `True` in `settings_dev.py`). Let's fire up the server and get our Grunt tasks running.

Start the server
```bash 
fab rs
```

In a new terminal window, start Grunt tasks from the project root
```bash
grunt
```
Now browse to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the app in action

### License
Django Calaccess Parser - Explore and analyze California campaign finance data without the headache
Copyright (C) 2014 California Civic Data Coalition

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program (See the copy [here](https://github.com/california-civic-data-coalition/django-calaccess-parser/blob/master/LICENSE.txt)).  If not, see <http://www.gnu.org/licenses/>.