===============================
Nose-Watcher
===============================

.. image:: https://badge.fury.io/py/nose-watcher.png
    :target: http://badge.fury.io/py/nose-watcher

.. image:: https://travis-ci.org/solarnz/nose-watcher.png?branch=develop
        :target: https://travis-ci.org/solarnz/nose-watcher

.. image:: https://pypip.in/d/nose-watcher/badge.png
        :target: https://pypi.python.org/pypi/nose-watcher

.. image:: https://coveralls.io/repos/solarnz/nose-watcher/badge.png?branch=develop
        :target: https://coveralls.io/r/solarnz/nose-watcher?branch=develop


A nose plugin to watch for changes within the local directory.

* Free software: BSD license
* Documentation: http://nose-watcher.readthedocs.org.

Inspired by the `nose-watch <https://github.com/lukaszb/nose-watch>`_ nose
plugin.

Note: nose-watcher will only run on linux, due to the depenency on
`python-inotify` and `inotify`.

Features
--------

* Watches for changes in the local directory, then runs nosetests with the
  specified command line options.

* Doesn't run the tests multiple times if you're using vim, Unlike the similar
  plugin `nose-watch`.


Installation_
------------

.. code-block:: shell

    pip install nose-watcher

Usage
-----

.. code-block:: shell

    nosetests --with-watcher

Documentation
-------------

More documentation can be found at
`ReadTheDocs <http://nose-watcher.rtfd.org>`_
