"""
Django settings for djangoD2 project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7zfcz4za_@yf4*=6z=goxv5i7y&%(hf6-7#pt0i*a@@iq&rl!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'internet_shop',
    'news_portal.apps.NewPortalConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'fpages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'debug_toolbar',
    'django_apscheduler',
]

SITE_ID = 2


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

ROOT_URLCONF = 'djangoD2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


WSGI_APPLICATION = 'djangoD2.wsgi.application'

ACCOUNT_FORMS = {'signup': 'account.forms.CommonSignupForm'}


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'OPTIONS': {'timeout': 5, }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
#
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.yandex.ru'  # ?????????? ?????????????? ????????????-?????????? ?????? ???????? ???????? ?? ?????? ????
EMAIL_PORT = 465  # ???????? smtp ?????????????? ???????? ????????????????????
EMAIL_HOST_USER = os.getenv('HOST_USER')  # ???????? ?????? ????????????????????????, ????????????????, ???????? ???????? ?????????? user@yandex.ru, ???? ???????? ???????? ???????????? user, ?????????? ??????????????, ?????? ?????? ???? ?????? ???????? ???? ????????????
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')  # ???????????? ???? ??????????
EMAIL_USE_SSL = True  # ???????????? ???????????????????? ssl, ?????????????????? ?? ??????, ?????? ??????, ?????????????????? ?? ???????????????????????????? ????????????????????, ???? ???????????????? ?????? ?????????? ??????????????????????
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_ADDR')


ADMINS = [
    ('yana', os.getenv('EMAIL ADMIN')),
    # ???????????? ???????? ?????????????? ?? ?????????????? ('??????', '???? ??????????')
]
SERVER_EMAIL = 'Django07.22@yandex.ru'  # ?????? ?????????? ?? ?????? ???????????? ?????????????????? FROM ?? ???????????????? ????????????????

# ???????????? ????????, ?????????????? ?????????? ???????????????????????? ?????? ???????????????? (???????????????????? ???????????? ???? ????????????????)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# ???????? ???????????? ???? ?????????????????????? ???? 25 ????????????, ???? ?????? ?????????????????????????? ??????????????????, ???????????? ?????????????????? ?????????? ????????????????, ???? ?????? ??????????????, ?????? ???????????? ???????? ???? ???????????????????????????????????? ??????????????
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#
# REDIS_HOST = '0.0.0.0'
# REDIS_PORT = '6379'
#
# CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
#
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'