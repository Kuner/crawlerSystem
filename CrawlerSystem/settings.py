"""
Django settings for crawlerSystem project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import socket
HOSTNAME = socket.gethostname()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = '*'

TITLE = 'crawler system'

_op = os.path.dirname
PROJECT_ROOT = _op(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

APP_LABEL = os.path.basename(PROJECT_ROOT)
PREFIX = 'CN'

def get_app_label():
    return APP_LABEL

account_prefix = 'crawler'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xmn@w2u)%f0*%@u2ib8^*z=@tbd=@8q6xp97t5h1#gu*x3%g#v'



STATIC_URL = '/static/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CrawlerSystem'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.CustomRequestMiddleware',
    'middleware.AuthMiddleware',
]

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/usr/lib/python2.6/site-packages/debug_toolbar/templates',
    os.path.join(os.path.dirname(PROJECT_ROOT), 'templates').replace('\\','/'),
)

TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(PROJECT_ROOT), 'templates').replace('\\','/'),],
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

WSGI_APPLICATION = 'CrawlerSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qiu',
        'USER': 'qiu',
        'PASSWORD': '123456',
        'HOST': '47.52.140.4',
        'PORT': '3306',
    },
    'read': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qiu',
        'USER': 'qiu',
        'PASSWORD': '123456',
        'HOST': '47.52.140.4',
        'PORT': '3306',
    },
    'write': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qiu',
        'USER': 'qiu',
        'PASSWORD': '123456',
        'HOST': '47.52.140.4',
        'PORT': '3306',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_SAVE_EVERY_REQUEST =  True

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


ROOT_URLCONF = 'urls'

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

DEFAULT_CHARSET='utf-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\','/')

# print "static:",STATIC_ROOT

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static').replace('\\','/'),
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\','/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


print '=' * 40,os.getpid()
print 'The system coding is %s !' % sys.getfilesystemencoding()
print 'The environment is %s !' % HOSTNAME


