Frequently asked questions
==========================

Questions and answers about this application and the underlying the CAL-ACCESS database


Does django-calaccess-raw-data modify the source data?
------------------------------------------------------

No. The bulk CAL-ACCESS data from the state is parsed and loaded "as is."
Any modification to the data made during the process is considered a bug in the software.

This application is intended as a base layer below more sophisticated apps,
like `django-calaccess-campaign-browser <http://django-calaccess-campaign-browser.californiacivicdata.org/>`_,
that transform the source data and load it into simplified models to serve as a
platform for investigative analysis.

.. image:: /_static/application-layers.png

Will django-calaccess-raw-data load *all* of the CAL-ACCESS data?
-----------------------------------------------------------------

No. The raw data provided by the state contains some errors in how values are escaped, quoted and delimited. The result is that a small number of records we
cannot yet automatically parse are lost during the loading process.

However, according to our own `tracking information <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/tracking.html>`_,
99.9998% of records in the downloaded source file will be loaded into the database.

For more information checkout:

* The `reportcalaccessrawdata <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/managementcommands.html#reportcalaccessrawdata>`_ command, which runs a several checks and produces a report on the current state of the CAL-ACCESS data
* The `list <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/calaccess_raw_files_report.csv>`_ of all CAL-ACCESS raw data files, including record and column counts at each stage of the process (this .CSV file is one of the outputs of ``reportcalaccessrawdata``)
* Records that could not be parsed by the ``cleancalaccessrawfile`` command are in ``<myproject>/data/log``

Why does django-calaccess-raw-data use data loading techniques not supported by Django?
---------------------------------------------------------------------------------------

Because the CAL-ACCESS database is huge. With more than 35 million records sprawled across 76 tables,
it can take a long time to load into a database using `the standard Django tools <https://docs.djangoproject.com/es/1.9/topics/db/queries/#creating-objects>`_,
which insert one record at a time. In our early testing, it ook as long as 24 hours to load all of CAL-ACCESS
into a database on a standard laptop computer.

To speed things up, our loading commands take advantage of the built-in bulk loading tools offered by PostgreSQL and MySQL,
which are not currently included in Django's system. These tools (``COPY`` in PostgreSQL and ``LOAD DATA INFILE`` in MySQL) insert CSV files from the file system
directly into the database in a small fraction of the time it would take to load them row by row.

As part of developing these tools we released `django-postgres-copy <http://django-postgres-copy.californiacivicdata.org/en/latest/>`_, a Django extension
that makes it easier for us and other developers to work with these valuable tools.

Why doesn't django-calaccess-raw-data only work with PostgreSQL and MySQL databases?
------------------------------------------------------------------------------------

Because of the answer above. To run our loading routines in a acceptable amount of time, we
need to take advantage of bulk file loading tools not currently supported by Django.

So far, we have only written custom loading routines for MySQL and PostgreSQL. We would
welcome contributions that would expand our database support to other systems, like SQLite
and Microsoft SQL Server. But we haven't got there yet.

How far back does the CAL-ACCESS database go?
---------------------------------------------

According to an `FAQ document <https://www.documentcloud.org/documents/2711615-FAQ/pages/1.html>`_ provided by the Secretary of State, electronic disclosure documents
started being filed in CAL-ACCESS on Jan. 1, 2000. Historical analysis of the database,
should start from that date, the documentation says.

Do the daily exports include *all* tables in the CAL-ACCESS database?
---------------------------------------------------------------------

No. We've compared the list of tables in the daily exports to what's described in the `official documentation <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p2>`_ provided by the Secretary of State, there as many 73 tables excluded from the daily exports.

Some of these missing tables have names or descriptions suggesting they could contain sensitive information, such as user credentials and bank account numbers. It's understandable that these tables would not be released.

However, many of these tables contain information that should be publicly available. For instance, there's a series of tables that describe elections, races and candidates that are not included in the daily exports, even though the list of candidates for the current election is `published <http://cal-access.ss.ca.gov/Campaign/Candidates/#assembly>`_ on the CAL-ACCESS website.

When we `reached out <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/62#issuecomment-58655390>`_ to the Secretary of State, asking that they include any elections-related tables in the daily exports, we were told that "[g]iven our current resource constraints, staff cannot modify the database export to include that other data."

Here's a sampling of missing tables we think should be made public:

* CASH_RECON_REPORT_WRK - Table description contains this mysterious comment: "J M needs to describe this table. Cox - 4/28/2000"
* CODE_LIST - This table contains a list of CAL file codes. Examples include entity codes, office codes and expense codes
* CORRESPONDENCE - Table description contains this mysterious comment: "J M needs to describe this table. Cox - 4/28/2000"
* DISCLOSURE_PROCEDURES - Table description contains this mysterious comment: "J M needs to describe this table."
* ELECTION_CANDIDATES - This table indicates if a candidate for a given race is an incumbent.
* ELECTION_LINKS - No description
* ELECTION_RACES - No description
* ELECTION_TYPES - This table links election types and their descriptions. 
* ELECTIONS - No description
* ERRORS_AND_OMISSIONS - This table contains results of audit checks and the validation process.
* FEDERAL_FORMS - Table used to log reciept of federal filings. 
* FEES - Fees, descriptions and their value
* FILER_CORRESPONDENCE_BUILD2 - Table description contains this mysterious comment: "J M needs to describe this table."
* FILER_ELECTIONS - Table description contains this mysterious comment: "J M needs to describe this table. He indicates it is for future use."
* FILER_NOTICE_GENERATION_DEF - "J M needs to describe this table. He indicates it is for future use."
* FILER_OBLIGATIONS - Table description contains this mysterious comment: "J M needs to describe this table. He indicates it is for future use."
* FILER_TYPES_TO_FORMS - Table description contains this mysterious comment: "J M needs to describe this table. It is in his list of tables designed for future releases."
* FILING_ERROR_TYPES - This lookup table provides a cross reference for errors and their and messages.
* FILING_ERRORS - This table contains the errors assocated with a given filing and each of it's amendments.
* FILING_ID_TEMP - No description
* FORM_CODES - This lookup table assocates record types to forms. 
* FORMS - This table describes the form set.
* LATE_CONT_IND_EXP_REPORT - Table description contains this mysterious comment: "J M needs to describe this table."
* LOCAL_FORMS This table is used to log reciept of local paper filings.
* PRD_DATA_AUDIT - No description
* PRD_FINE_DETAIL - Detail information on how a fine was calculated.
* PRD_FINES - Fine summary data table.
* PRD_LIMITS - Table description contains this mysterious comment: "J M needs to describe this table."
* PRD_WAIVERS - Table description contains this mysterious comment: "J Mo needs to describe this table."
* TVIEW_CONTRIBUTIONS3 - Campaign Disclosure reporting tables. "Need to get DH's Documentation to describe."

What is the California Civic Data Coalition?
--------------------------------------------

The California Civic Data Coalition is a loosely coupled team of journalists from the Los Angeles Times Data Desk,
the Washington Post, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

The coalition was formed in 2014 by Ben Welsh and Agustin Armendariz to lead the development of open-source software
that makes California's public data easier to access and analyze. The effort has drawn hundreds of contributions
from developers and journalists at dozens of competing news outlets.

Its primary focus is refining CAL-ACCESS, the jumbled, dirty and difficult government database that tracks campaign finance and lobbying activity in California politics.

In 2015 the coalition was named a winner of the Knight News Challenge and awarded $250,000 in philanthropic funding
from the Knight Foundation, the Democracy Fund, the William and Flora Hewlett Foundation and the Rita Allen Foundation.

Read more at `californiacivicdata.org <http://www.californiacivicdata.org>`_.
