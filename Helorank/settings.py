"""
Django settings for Helorank project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bio@ekskh*c*(xwozih4c+w#=l+dr0pi(%i2a_y$njq-97drgf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if os.environ.get('DJANGO_DEBUG') is not None:
    DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'accounts',
    'leagues',
    # New! Look at me!
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Helorank.urls'

WSGI_APPLICATION = 'Helorank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
if DEBUG:
    # Development Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'deaensll3m9a0s',
            'USER': 'zdudfdflhhgqbj',
            'PASSWORD': 'E7HBOdFBXUA3cRVXpjdN3QlaAN',
            'HOST': 'ec2-54-225-91-60.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
else:
    #Production Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd3qvf805r639eu',
            'USER': 'znjhyvilaqetlg',
            'PASSWORD': 'CNkeLSwjt4EwRFhW3M3vvV1eJl',
            'HOST': 'ec2-54-225-84-29.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates

TEMPLATE_DIRS = (
    'templates'
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = 'media'
    STATICFILES_DIRS = (
        'static',
    )
else:
    AWS_STORAGE_BUCKET_NAME = 'helorank'
    AWS_ACCESS_KEY_ID = 'AKIAJFQSQMRXQG4I43TA'
    AWS_SECRET_ACCESS_KEY = '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'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://s3-us-west-1.amazonaws.com/helorank/'
    STATIC_URL = 'http://s3-us-west-1.amazonaws.com/helorank/'
    STATICFILES_DIRS = (
        'static',
    )


    
