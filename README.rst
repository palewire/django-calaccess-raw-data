California Campaign Finance
=====

django-calacces-browser is a simple Django app to build campaign finance data from the cal access database. It is reliant upon the django-calaccess-parser app.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. pip install https://github.com/california-civic-data-coalition/django-calaccess-parser/archive/0.1-alpha.tar.gz

2. Add "calaccess-browser" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'calaccess-browser',
      )

3. Set `settings.CALACCESS_DOWNLOAD_DIR` to where you want the data loaded

4. Run `python manage.py syncdb` to create the campaign finance models.

5. Include the campaign finance URLconf in your project urls.py like this::

    url(r'^finance/', include('campaign_finance.urls')),

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to inspect candidates and committee info (you'll need the Admin app enabled).