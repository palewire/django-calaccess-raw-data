#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='django-calaccess-raw-data',
    version='2.0.0',
    packages=(
        'calaccess_raw',
        'calaccess_raw.admin',
        'calaccess_raw.management',
        'calaccess_raw.migrations',
        'calaccess_raw.management.commands',
        'calaccess_raw.models',
        'calaccess_raw.annotations',
    ),
    include_package_data=True,
    license='MIT',
    description="A Django app to download, extract and load campaign "
                "finance and lobbying activity data from the California "
                "Secretary of State\'s CAL-ACCESS database",
    url='http://django-calaccess.californiacivicdata.org/',
    author='California Civic Data Coalition',
    author_email='cacivicdata@gmail.com',
    install_requires=(
        'django>=1.9',
        'django-postgres-copy>=2.3.5',
        'csvkit>=1.0',
        'requests',
        'clint',
        'hurry.filesize',
        'pytz',
    ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: MIT License',
    ),
)
