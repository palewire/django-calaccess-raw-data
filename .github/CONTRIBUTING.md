# How to contribute

We welcome issues and pull requests for all parties. If you're looking for a place to plug in,
work through our [getting started guide of new contributors](http://django-calaccess.californiacivicdata.org/en/latest/howtocontribute.html)
and then check out [our open issues list](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues) to see if anything interests you. If this repository isn't your cup of tea, check out our other projects [on GitHub](https://github.com/california-civic-data-coalition/).

## How do the tests work?

Our code is tested using [Django's built-in unittesting](https://docs.djangoproject.com/en/1.9/topics/testing/) system via the [TravisCI](https://travis-ci.org/california-civic-data-coalition/django-calaccess-raw-data)
continuous integration service.

In addition, prior to the Django unittests code is evaluated using Python's
[pep8](https://pypi.python.org/pypi/pep8) and [pyflakes](https://pypi.python.org/pypi/pyflakes) style
guide enforcement tools.

When a commit or pull request is made with our repository, those tests are rerun with the latest code.
We try not to be too uptight, but we generally expect the tests to be pass before we will merge a request.

## How can I contribute documentation?

The [documentation](http://django-calaccess.californiacivicdata.org/) for this
project is published online by ReadTheDocs using the files found in [a dedicated repository](https://github.com/california-civic-data-coalition/django-calaccess-technical-documentation).

Those files are compiled using Python's [Sphinx](http://www.sphinx-doc.org/en/stable/) documentation framework, which is written in [reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) format.

To make edits to the documentation, change the ``.rst`` files found in that directory, commit
your changes and submit them as a pull request.

## Who is in charge of the repository?

Maintaining the code and handling outside pull requests is managed by the leadership
team at the California Civic Data Coalition.

## What is the California Civic Data Coalition?

The California Civic Data Coalition is a loosely coupled team of journalists from the Los Angeles Times Data Desk, the Washington Post, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

The coalition was formed in 2014 by Ben Welsh and Agustin Armendariz to lead the development of open-source software that makes California's public data easier to access and analyze. The effort has drawn hundreds of contributions from developers and journalists at dozens of competing news outlets.

Its primary focus is refining CAL-ACCESS, the jumbled, dirty and difficult government database that tracks campaign finance and lobbying activity in California politics.

In 2015 the coalition was named a winner of the Knight News Challenge and awarded $250,000 in philanthropic funding from the Knight Foundation, the Democracy Fund, the William and Flora Hewlett Foundation and the Rita Allen Foundation.

Read more at [californiacivicdata.org](http://www.californiacivicdata.org)
