#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
   README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except (IOError, ImportError):
   description = open('README.md').read()

import os

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-calaccess-parser',
    version='0.2',
    packages=[
        'calaccess',
        'calaccess.management',
        'calaccess.management.commands',
        'calaccess.toolbox',
        'calaccess.toolbox.management',
        'calaccess.toolbox.management.commands',
    ],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app download and parse California campaign finance data from Cal-Access.',
    long_description=description,
    url='https://github.com/california-civic-data-coalition',
    author='Agustin Armendariz, Aaron Williams, Ben Welsh',
    author_email='ben.welsh@latimes.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    # dependencies
    install_requires=[
        'csvkit==0.6.1',
        'python-dateutil==2.1',
        'MySQL-python==1.2.4',
        'argparse==1.2.1',
        'requests==2.2.1',
        'progressbar==2.3',
        'hurry.filesize==0.9',
        'pypandoc==0.8.0',
    ],
)
