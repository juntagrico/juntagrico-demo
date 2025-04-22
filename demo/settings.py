"""
Django settings for demo project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# core settings

DEBUG = os.environ.get('JUNTAGRICO_DEBUG', False)

ALLOWED_HOSTS = ['demo.juntagrico.science',]

SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '[%(asctime)s] %(levelname)s %(message)s'}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'demo',
    'juntagrico',
    'fontawesomefree',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
    'import_export',
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','demo.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'),
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'),
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

ROOT_URLCONF = 'demo.urls'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
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
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Language etc.

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'de'
DATE_INPUT_FORMATS = ['%d.%m.%Y',]

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'


# auth settings

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

LOGIN_REDIRECT_URL = "/"


# site settings

SITE_ID = 1


# Static Files Settings

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'


# session settings

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# impersonate settings

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}


# import export settings

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'


# crispy forms settings

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# juntagrico settings

ORGANISATION_NAME = "Demo Solawi (nicht echt Anmeldung nicht verbindlich)"
ORGANISATION_LONG_NAME = "Demo Solawi (nicht echt Anmeldung nicht verbindlich)"
ORGANISATION_ADDRESS = {
    "name":"Demo Solawi (nicht echt Anmeldung nicht verbindlich)",
    "street" : "FakeStreet",
    "number" : "123",
    "zip" : "1234",
    "city" : "Niemansland",
    "extra" : ""
}
ORGANISATION_BANK_CONNECTION = {
    "PC" : "1",
    "IBAN" : "IBAN",
    "BIC" : "BIC",
    "NAME" : "Geldspeicher",
    "ESR" : ""
}
ORGANISATION_WEBSITE = {
    'name': "www.demo.org",
    'url': "https://www.demo.org"
}

CONTACTS = {
    "general": "info@juntagrico.org"
}

SHARE_PRICE = "0"

STYLES = {'static': ['/static/demo/css/customize.css']}

DEMO_USER='(Benutzername ist "admin")'
DEMO_PWD='(Passwort ist "admin")'
