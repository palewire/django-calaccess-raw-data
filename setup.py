#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='django-calaccess-raw-data',
    version='1.5.0',
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
        'django>=1.8',
        'django-postgres-copy>=0.1.0',
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
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'License :: OSI Approved :: MIT License',
    ),
)
