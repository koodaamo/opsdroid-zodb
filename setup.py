#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['ZODB']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Petri Savolainen",
    author_email='petri@koodaamo.fi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="ZODB support for opsdroid",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='opsdroid zodb',
    name='opsdroid-zodb',
    packages=['opsdroid_zodb'],
    setup_requires=setup_requirements,
    entry_points = {
        'opsdroid_databases': [
            'zodb = opsdroid_zodb.database'
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/koodaamo/opsdroid-zodb',
    version='0.1.0',
    zip_safe=False,
)
