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

However, according to our own `tracking information <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/tracking.html>`_, 99.9998 percent of records in the downloaded source file will be loaded into the database.

For information checkout:

* The ```reportcalaccessrawdata`` <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/managementcommands.html#reportcalaccessrawdata>`_ command, which runs a several checks and produces a report on the current state of the CAL-ACCESS data
* The `list <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/calaccess_raw_files_report.csv>`_ of all CAL-ACCESS raw data files, including record and column counts at each stage of the process (this .CSV file is one of the outputs of ``reportcalaccessrawdata``)
* Records that could not be parsed by the ``cleancalaccessrawfile`` command are in <myproject>/data/log

How far back does the CAL-ACCESS database go?
---------------------------------------------

According to `the official state documentation <http://www.documentcloud.org/documents/1308002-cal-access-about.html#document/p235>`_, electronic disclosure documents
started being filed in CAL-ACCESS on Jan. 1, 2000. Historical analysis of the database,
should start from that date, the documentation says.

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
