#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='nose-watcher',
    version='0.1.3',
    description='A nose plugin to watch for changes within the local'
                ' directory.',
    long_description=readme + '\n\n' + history,
    author='Chris Trotman',
    author_email='chris@trotman.io',
    url='https://github.com/solarnz/nose-watcher',
    packages=[
        'nose_watcher',
    ],
    include_package_data=True,
    install_requires=[
        'python-inotify==0.6-test'
    ],
    license="BSD",
    zip_safe=False,
    keywords='nose-watcher',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing'
    ],
    test_suite='tests',
    entry_points={
        'nose.plugins.0.10': [
            'watcher = nose_watcher.nose_watcher:WatcherPlugin'
        ]
    },
)
