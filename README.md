## django-psdb-engine

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-psdb-engine) ![PyPI - Downloads](https://img.shields.io/pypi/dm/django-psdb-engine) ![Made for - PlanetScale](https://img.shields.io/badge/made%20for-PlanetScale-black?style=flat&logo=planetscale)

This package helps you interact with your [PlanetScale](https://planetscale.com) databases in your Django projects in an easier way.

### Usage

Install the package by running the following command.

```sh
pip install django-psdb-engine
```

And finally, update your `DATABASES` configuration and change the `ENGINE` field.

```python
DATABASES = {
    'default': {
      'ENGINE': 'django_psdb_engine',
      ...
      'OPTIONS': {'ssl': {'ca': ...}}
    }
}
```

**Note**: Since Django uses the `UTF-8` charset and it points to `utf8mb3` in MySQL and this charset is deprecated in MySQL 8, you may need to add `{"charset": "utf8mb4"}` and migrate your chanegs with no problem.

```diff
- 'OPTIONS': {'ssl': {'ca': ...}}
+ 'OPTIONS': {'ssl': {'ca': ...}, 'charset': 'utf8mb4'}
```

### Requirements
- django >= 2.2
- mysqlclient >= 2.1.0

### License
Free software: [MIT license](LICENSE)