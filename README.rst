California Campaign Finance
=====

django-calacces-browser is a simple Django app to build campaign finance data from the cal access database. It is reliant upon the django-calaccess-parser app.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "calaccess-browser" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'calaccess-browser',
      )
2. Include the campaign finance URLconf in your project urls.py like this::

	url(r'^finance/', include('campaign_finance.urls')),

3. Run `python manage.py syncdb` to create the campaign finance models.

4. Run `python manage.py build_campaign_finance` to load campaign finance models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to inspect candidates and committee info (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/browser/ to browse the data.
