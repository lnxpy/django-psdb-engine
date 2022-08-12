#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'django>=2.2'
]

test_requirements = [ ]

setup(
    author="Sadra Yahyapour",
    author_email='lnxpylnxpy@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Django PlanetScale database engine.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_psdb_engine',
    name='django_psdb_engine',
    packages=find_packages(include=['django_psdb_engine', 'django_psdb_engine.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lnxpy/django_psdb_engine',
    version='1.0.0',
    zip_safe=False,
)
