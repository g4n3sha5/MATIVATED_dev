"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
try:
    envType = os.environ['ENV_TYPE']
    if envType == 'LOCAL':
        from dotenv import load_dotenv
        load_dotenv()

except:
    pass
try:
    envType = os.environ['ENV_TYPE']
    if envType == 'PROD':
        pwd = str(os.environ['SQL_PASSWORD'])
        SESSION_COOKIE_DOMAIN = 'mativated.com'
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'm4tivated$main',
                'USER': 'm4tivated',
                'PASSWORD': pwd,
                'HOST': 'm4tivated.mysql.eu.pythonanywhere-services.com',
        }
    }


except:
    pass

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    try:
        CLOUDINARY_STORAGE = {
             'CLOUD_NAME': os.environ['CLOUD_NAME'],
             'API_KEY': os.environ['CLOUD_API_KEY'],
             'API_SECRET': os.environ['CLOUD_API_SECRET']
         }

        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    except:
        pass

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# LOCALE_PATHS = (
#   os.path.join(BASE_DIR, 'locale'),
# )

SITE_ID = 1
LANGUAGE_CODE = 'pl-PL'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'h26.seohost.pl'
EMAIL_PORT = '587'
SERVER_EMAIL = 'no-reply@mativated.com'
EMAIL_HOST_USER = 'no-reply@mativated.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

try:
    env = os.environ['EMAIL_PASSWORD']
    if env:
        EMAIL_HOST_PASSWORD = str(env)
except:
    EMAIL_HOST_PASSWORD = ''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

try:
    env = os.environ['SECRET_KEY']
    if env:
        SECRET_KEY = os.environ['SECRET_KEY']
except:
    SECRET_KEY = 'django-insecure-q$h-7xe*!yo(u8wr-het-!8ybcp%wmyw-(mc+j^3(r7%&obof$'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['*']
INTERNAL_IPS = [
    "127.0.0.1",
    "mativated.com"
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'main',
    'Notifications',
    'Journal',
    'WorkoutJournal',
    'Clubs',
    'Presentation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'account_register.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'Notifications.views.notifications',
                'Notifications.views.reportSuggestion'
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

WSGI_APPLICATION = 'main.wsgi.application'
ASGI_APPLICATION = 'main.asgi.application'
SESSIONS_ENGINE = 'django.contrib.sessions.backends.cache'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
        },
    },
    "root": {
        "handlers": ["console"],

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = "/profile/"
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None

# do zmiany True
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 7
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 500
