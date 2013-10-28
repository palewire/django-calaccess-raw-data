Download, extract and load the [CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/) campaign finance and lobbying activity database.

Currently tied to MySQL just to get it in and look at it. Need to figure out how to leverage CSVKit and shoehorn it into Django.

* cal_access_testing.sql -- MySQL dump of the table schemas.

* env_settings.py.example -- set-up your local settings here and save as env_settings.py.

* clean_data.py -- quoting of fields was a problem with the data before they moved to TSV from CSV format. This fixed that as well as NULL bytes in the data. It would be great to get taking care of encoding, date conversions and the rest right here.

* load_cut.py -- uses LOAD DATA INFILE to quickly suck in the data and make some lookup tables.

* check_load.py -- make sure rows imported matches the number of lines in the csv file.

