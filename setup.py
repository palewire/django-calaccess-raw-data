#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(file_name):
    """Read the provided file."""
    this_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_dir, file_name)
    with open(file_path) as f:
        return f.read()


def version_scheme(version):
    """
    Version scheme hack for setuptools_scm.
    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342
    If that issue is resolved, this method can be removed.
    """
    import time

    from setuptools_scm.version import guess_next_version

    if version.exact:
        return version.format_with("{tag}")
    else:
        _super_value = version.format_next_version(guess_next_version)
        now = int(time.time())
        return _super_value + str(now)


def local_version(version):
    """
    Local version scheme hack for setuptools_scm.
    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342
    If that issue is resolved, this method can be removed.
    """
    return ""


setup(
    name='django-calaccess-raw-data',
    author='California Civic Data Coalition',
    author_email='b@palewi.re',
    url='http://django-calaccess.californiacivicdata.org/',
    description=("A Django app to download, extract and load campaign "
                "finance and lobbying activity data from the California "
                "Secretary of State's CAL-ACCESS database"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=(
        'calaccess_raw',
        'calaccess_raw.admin',
        'calaccess_raw.management',
        'calaccess_raw.migrations',
        'calaccess_raw.management.commands',
        'calaccess_raw.models',
        'calaccess_raw.annotations'
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=(
        'django>=3.2.*',
        'django-postgres-copy>=2.6.*',
        'requests',
        'clint',
        'hurry.filesize',
        'pytz',
        'pandas',
        'django-internetarchive-storage',
        'csvkit',
    ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'License :: OSI Approved :: MIT License'
    ),
    project_urls={
        'Project': 'https://www.californiacivicdata.org/',
        'Documentation': 'https://django-calaccess.californiacivicdata.org/',
        'Funding': 'https://www.californiacivicdata.org/about/',
        'Source': 'https://github.com/palewire/django-calaccess-raw-data',
        'Testing': 'https://github.com/palewire/django-calaccess-raw-data/actions/workflows/tests.yaml',
        'Tracker': 'https://github.com/palewire/django-calaccess-raw-data/issues'
    },
    setup_requires=["pytest-runner", "setuptools_scm"],
    use_scm_version={"version_scheme": version_scheme, "local_scheme": local_version},
)
