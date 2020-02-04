"""
Django settings for localcosmos_private project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-l4*f++k5$u!cr(o#-hio-d9hl)9b&nb37%_6v3l^w#20(rr!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
host_list = os.environ.get('ALLOWED_HOSTS', [])
if host_list:
    ALLOWED_HOSTS = host_list.split('|')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # localcosmos
    'django.contrib.sites',

    'localcosmos_server',
    'localcosmos_server.app_admin',
    'localcosmos_server.server_control_panel',
    'localcosmos_server.datasets',
    'localcosmos_server.online_content',

    'django_road',    
    'anycluster',
    'content_licencing',

    'rules',
    'el_pagination',
    'django_countries',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',

    'octicons',
    'imagekit',

    'django.forms',
]

MIDDLEWARE = [
    'localcosmos_server.middleware.LocalCosmosServerSetupMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'localcosmos_server.app_admin.middleware.AppAdminMiddleware',
    'localcosmos_server.server_control_panel.middleware.ServerControlPanelMiddleware',
]

ROOT_URLCONF = 'localcosmos_private.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'localcosmos_server.context_processors.localcosmos_server',
            ],
            'loaders' : [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        }
    },
]

WSGI_APPLICATION = 'localcosmos_private.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['DATABASE_NAME'],
        'USER' : os.environ['DB_USER'],
        'PASSWORD' : os.environ['DB_PASSWORD'],
        'HOST' : 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/localcosmos/static/'

MEDIA_ROOT = '/var/www/localcosmos/media/'
MEDIA_URL = '/media/'

from localcosmos_server.settings import *

# location where apps are installed
# your apps index.html will be in LOCALCOSMOS_APPS_ROOT/{APP_UID}/www/index.html
LOCALCOSMOS_APPS_ROOT = '/var/www/localcosmos/apps/' 

SERVER_EMAIL = 'server@localcosmos-private'

admin_list = os.environ.get('LOCALCOSMOS_PRIVATE_ADMINS', [])
ADMINS = []
if admin_list:
    # 'name,email|name,email'
    ADMINS = [tuple(admin.split(',')) for admin in admin_list.split('|')]


EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', False)
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
    
