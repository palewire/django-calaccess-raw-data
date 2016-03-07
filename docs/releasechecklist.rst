Release checklist
=================

The steps to follow each time release a new version of this package.

* Update docs/changelog.rst
* Update setup.py with new version and any new dependencies
    * Consider including RC (release candidate) in release name until we're sure we're uploading a package with all tiny details accounted for
* Update requirements_dev.txt with any new dependencies
* Run `python setup.py sdist`, make sure their aren't any errors
* Spotcheck new release package in dist/, (e.g., make sure templates appear in calaccess_raw/templates/calaccess_raw/
* Run `python setup.py sdist upload`
* Confirm that description text is fixed (i.e., close #1187)
* Release on GitHub
    *`git commit` final change and run `git tag "v#.#.#" with whatever the release number is
    * Run `git push origin master --tags`
    * Add list of changes to the current release which should appear [here](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/releases) and publish.
