#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'python-inotify==0.6-test'
]

setup(
    name='nose-watcher',
    version='0.1.1',
    description='A nose plugin to watch for changes within the local directory.',
    long_description=readme + '\n\n' + history,
    author='Chris Trotman',
    author_email='chris@trotman.io',
    url='https://github.com/solarnz/nose-watcher',
    packages=[
        'nose_watcher',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='nose-watcher',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    entry_points={
        'nose.plugins.0.10': [
            'watcher = nose_watcher.nose_watcher:WatcherPlugin'
        ]
    },
)
