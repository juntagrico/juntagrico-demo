"""
Django settings for demo project.
"""
import os
from pathlib import Path

from juntagrico import defaults

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

if not DEBUG:
    ALLOWED_HOSTS = ['demo.juntagrico.science',]

ADMINS = (
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
)
MANAGERS = ADMINS

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

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'demo',
    'juntagrico_billing',
    'juntagrico',
    'fontawesomefree',
    'impersonate',
    'crispy_forms',
    'crispy_bootstrap4',
    'adminsortable2',
    'polymorphic',
    'import_export',
    'django_select2',
    'djrichtextfield',
]

ROOT_URLCONF = 'demo.urls'

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

# HTTP

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

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

# Email
# Disabled in Demo
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'de'
DATE_INPUT_FORMATS = ['%d.%m.%Y',]

TIME_ZONE = 'Europe/Zurich'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# django.contrib.staticfiles
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# django.contrib.sites Settings

SITE_ID = 1

# django.contrib.auth Settings

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

LOGIN_REDIRECT_URL = "/"


# impersonate settings

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}


# crispy forms settings

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# import export settings

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'


# Rich text editor settings

DJRICHTEXTFIELD_CONFIG = defaults.richtextfield_config(LANGUAGE_CODE)


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

STYLES = {'static': ['demo/css/customize.css']}

# Demo Settings
DEMO_USER='(Benutzername ist "admin")'
DEMO_PWD='(Passwort ist "admin")'


# juntagrico billing setting

BILLS_USERMENU = True


# Test mode
TEST_MODE = os.environ.get("JUNTAGRICO_TEST_MODE", 'False')=='True'

if TEST_MODE:
    INSTALLED_APPS.append('testmode')
