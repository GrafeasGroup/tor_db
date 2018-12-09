#!/usr/bin/env python
# <apology_block>
# This is a test to see if using Django as a standalone application is any easier
# than dealing with the myriad pain points of SQLAlchemy. It's ridiculous and
# probably a bad idea, but why how do you learn without trying things?

# What we're doing here is using the bare minimum settings information to use
# the Django ORM without actually using Django. This is not necessarily the
# normal way to use it, but it is not unheard of and there are specific
# recommendations from the Django team for this situation that are being followed
# here.

# Basically, just import this file at the top of any file that needs to use
# the ORM and everything should just work. We don't need to actually use anything
# from it, we just have to import it.

# SQLAlchemy can suck it.

# Usage:
#
# python manage.py makemigrations
# python manage.py migrate

# </apology_block>

import os
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tor_db',
]

SECRET_KEY = os.environ.get(
    'TOR_DB_SECURITY_KEY',
    'pink fluffy unicorns dancing on rainbows'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('TOR_DB_PATH', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE' : 'django.db.backends.mysql',
#         'NAME' : 'playground',
#         'USER' : 'admin',
#         'PASSWORD' : 'pasw',
#         'HOST' : 'localhost',
#     }
# }

if not settings.configured:
    settings.configure(
        INSTALLED_APPS = INSTALLED_APPS,
        DATABASES = DATABASES,
    )
    django.setup()
