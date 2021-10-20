"""
Django settings for trickle_api_2 project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xt-%)$jkh&1r1q6)oyi#!_o-6sd6!(2$4rpg_z1)*)=^445mm+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'elasticapm.contrib.django',
    'api1',
    'api2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'elasticapm.contrib.django.middleware.TracingMiddleware',
]

ROOT_URLCONF = 'trickle_api_2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'trickle_api_2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


logfile_maxBytes = 10485760
logfile_backupCount = 3
log_level = "INFO"

logfile_basepath = os.path.join(BASE_DIR, "log")
if not os.path.exists(logfile_basepath):
    os.makedirs(logfile_basepath)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s.%(msecs)03d] %(levelname)5s [%(thread)d:%(module)s:%(funcName)10s():%(lineno)s] "   "%(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'DEBUG'
        },
        'commands': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logfile_basepath, "commands.log"),
            'formatter': 'verbose',
            'maxBytes': logfile_maxBytes,
            'backupCount': logfile_backupCount
        },
    },
    'loggers': {
        'django': {
            'handlers': ['commands', 'console'],
            'propagate': True,
            'level': 'ERROR',
        },
        'commands': {
            'handlers': ['commands', 'console'],
            'level': log_level,
        },
    }
}

HOST_URL = "localhost"
HOST_PORT = "8082"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PROJECT_NAME = "Demo-QA-Apps"
APP_NAME = "trace-refapp-test"
PROFILE_KEY = "+Wj6Wb+BZ+tYUFMHcC1So1+52oP0k4mAsgXYo4BV6NksQYscyB9tLwhi0sSCZ2vHBf2h+zybHZu0e6IBo5/5r1IBBqUjfR+UrU+ptYXZhRtc8d31qCbhc4llsYQruVsLsuWrS7501kaIeCFOsGsAyIhPGWODfcvYLpaDsKqlERnpbhTLgNYE4ZFPP0lZJONkbInKXAANgo3w4DciNiOLZyxxnjZCkxEHqWzG4RLwUu9prP+ahPzuZ2ltyED8JnTrBfB+nHZoA+WSBm1+8IC2n+6RNYGAy0KRUQAyWTigNQr+ChOurq7gDAx5a5YHcfK2RnvAvftJfLx5p9n8N8lw3M1/s5Yu60wR3s0+Kwka52fTvZCnG/+FhJNqj0rf9nOvQ+F5sNBPwGUSXJIWoD7QB5LqkqU35CF0xAwiCcAWPBXSB0Z+NcEbrPNZrA44KLOU4cld2Q6Na5MoGVEnHoxi2Y95LxbUUqoUp+3w3bb4q9Z+iBhKVe6oh5vXvCbGzqV4xMSmHm1ajc99ubIDBaWjqQUSXRYjI6wRts9ezdbIiuSIKCDfcGHjqcHKlLQeeAfpw8Vk/aiLesRS47ZAdEinPiGXiBHQii44a3SYhfOKCJRVKHQQZrs41k/Ifz45fiObUQ1MNdMsG1KG5dRONXdmw4hqC6wXlPO5r67gef9yap9DJzJyRyCxu2JjnaOTZtgFgvDab/K5wTdpLYpsI4rFoOkriS9LeF7TK4cSH+Lw72LEl241E0Z862nyslwuDj96mb1AKlkRnr7SSruabQxFv0d+WwUHjS0LFwK842SEW8Q1qOrfScvb4jRO6tXgYZakcNtChS+QjxWgSc461T3Ssdqg8Cse+1OeJte/ZufVpMCogjWpn/UsX9D42lQm0EvpYAp93ZPOgNsiAZsqeXYGE1IfGdIIt4laXZkb/L2fvfX1zip55thlrD/cWZiPiXo/+Bk7/5t8JXu23f8kr3f2n8Q2F23eYPOu7RpwJCHeBwhi0/u3wAoWmniOiOotWWwhlFSILQiwxB5O9UEk3OL6QA=="

try:
    from sf_apm_lib.snappyflow import Snappyflow
    project_name = PROJECT_NAME
    app_name = APP_NAME
    profile_key = PROFILE_KEY
    sf = Snappyflow()
    sf.init(profile_key, project_name, app_name)
    SFTRACE_CONFIG = sf.get_trace_config()
    ELASTIC_APM = {
        'SERVICE_NAME': "Service-2",
        'SERVER_URL': SFTRACE_CONFIG.get('SFTRACE_SERVER_URL'),
        'GLOBAL_LABELS': SFTRACE_CONFIG.get('SFTRACE_GLOBAL_LABELS'),
        'VERIFY_SERVER_CERT': SFTRACE_CONFIG.get('SFTRACE_VERIFY_SERVER_CERT'),
        'SPAN_FRAMES_MIN_DURATION': SFTRACE_CONFIG.get('SFTRACE_SPAN_FRAMES_MIN_DURATION'),
        'STACK_TRACE_LIMIT': SFTRACE_CONFIG.get('SFTRACE_STACK_TRACE_LIMIT'),
        'CAPTURE_SPAN_STACK_TRACES': SFTRACE_CONFIG.get('SFTRACE_CAPTURE_SPAN_STACK_TRACES'),
        'DJANGO_TRANSACTION_NAME_FROM_ROUTE': True,
        'CENTRAL_CONFIG': False,
        'DEBUG': True
    }
    print(ELASTIC_APM)
except Exception as ex:
    print(ex)