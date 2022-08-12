==================
django-psdb-engine
==================

.. image:: https://img.shields.io/pypi/v/django_psdb_engine.svg
        :target: https://pypi.python.org/pypi/django_psdb_engine

.. image:: https://img.shields.io/travis/lnxpy/django_psdb_engine.svg
        :target: https://travis-ci.com/lnxpy/django_psdb_engine

.. image:: https://readthedocs.org/projects/django-psdb-engine/badge/?version=latest
        :target: https://django-psdb-engine.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

Django `PlanetScale <https://planetscale.com>`_ database engine. This package is a better solution for `planetscale/django_psdb_engine <https://github.com/planetscale/django_psdb_engine>`_.

* Free software: MIT license

Usage
-----
Make this database engine ready in two simple steps. First thing first, install the package.

.. code:: sh

   $ pip install django-psdb-engine


And finally, update your databases configuration by changing the ``ENGINE`` field.

.. code:: python

   DATABASES = {
     'default': {
       'ENGINE': 'django_psdb_engine',
       ...
       'OPTIONS': {'ssl': {'ca': ...}}
     }
   }

Requirements
------------
- django >= 2.2