#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='django-calaccess-raw-data',
    version='1.2.0',
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
    description='A Django app to download, extract and load campaign \
finance and lobbying activity data from the California \
Secretary of State\'s CAL-ACCESS database',
    url='http://django-calaccess-raw-data.californiacivicdata.org/',
    author='California Civic Data Coalition',
    author_email='cacivicdata@gmail.com',
    install_requires=(
        'django>=1.8',
        'csvkit',
        'requests',
        'clint',
        'hurry.filesize',
        'django-postgres-copy',
        'pytz',
    ),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'License :: OSI Approved :: MIT License',
    ),
)
