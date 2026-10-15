"""
Django settings for feuerundbohne project.
"""

import os
from pathlib import Path
from juntagrico import defaults

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

ALLOWED_HOSTS = ['feuerundbohne.juntagrico.science', 'localhost', 'fubatja.ch']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'juntagrico.apps.JuntagricoAdminConfig',
    'feuerundbohne',
    'juntagrico_assignment_request',
    'juntagrico',
    'import_export',  # benötigt ab 1.6
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
    'crispy_bootstrap4',
    'django_select2',
    'djrichtextfield',
]

ROOT_URLCONF = 'feuerundbohne.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','feuerundbohne.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'feuerundbohne/templates'],  # location of your overriding templates
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'feuerundbohne.wsgi.application'


LANGUAGE_CODE = 'de'
DJRICHTEXTFIELD_CONFIG = defaults.richtextfield_config(LANGUAGE_CODE)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'
EMAIL_BACKEND='juntagrico.backends.email.EmailBackend'


STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     STYLE_SHEET Settings
"""

STYLES = {'static': ['feuerundbohne/css/customize.css']}

"""
     FAVICON Settings
"""

FAVICON = "/static/feuerundbohne/img/Boehnli_33x32.ico"

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Feuer&Bohne"
ORGANISATION_LONG_NAME = "Feuer&Bohne"
ORGANISATION_ADDRESS = {"name":"Genossenschaft Feuer&Bohne", 
            "street" : "Hombergstrasse",
            "number" : "53",
            "zip" : "4600",
            "city" : "Olten",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {"PC" : "46-110-7",
            "IBAN" : "CH21 0839 0038 7046 1010 7",
            "BIC" : "ABSOCH22XXX",
            "NAME" : "Alternative Bank Schweiz",
            "ESR" : ""}
SHARE_PRICE = "250"

CONTACTS = {
    "general": "info@feuerundbohne.ch"
}

ORGANISATION_WEBSITE = {
    'name': "www.feuerundbohne.ch",
    'url': "https://www.feuerundbohne.ch"
}

"""
     eingefügt von Lorenz am 20.03.2022 nach Anweisung von David Simmen (slack chat)
"""
FROM_FILTER = {
    'filter_expression': 'info@fubatja\.ch',
    'replacement_from': 'info@fubatja.ch'
}

# Use time zone Zurich for the time
USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

ASSIGNMENT_UNIT = "HOURS"
