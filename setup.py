#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'click_repl',
                'pathlib',
                'jsonschema',
                ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="SAP Ariba Foundation Services",
    author_email='david.liu07@sap.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python package to build metadata driven command line tools (CLI) with out-of-the-box REST Swagger/OpenAPI support",
    install_requires=requirements,
    entry_points='''
    [console_scripts]
    metacli=metacli.metacli:metacli
    ''',
    license="Apache Software License 2.0",
    long_description=history,
    include_package_data=True,
    keywords='metacli',
    name='metacli',
    packages=find_packages(include=['metacli']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tw4dl/metacli',
    version='0.0.0',
    zip_safe=False,
)
