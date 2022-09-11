"""
Django settings for NinjaApp project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mf#0n$io7f9gxl(wv8srccp(ckh^dkotsrbr-84+yr22fyp64u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['hitfizz.herokuapp.com','*',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo',
    'crispy_forms',
    'cloudinary',
    'hitcount',
    'ckeditor',
    'ckeditor_uploader',
    'django_social_share',
    'django_comments_xtd',
    'django_comments',
]
CKEDITOR_UPLOAD_PATH="uploads/"


LOGIN_URL = 'login'  # or actual url
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID = 1
COMMENTS_APP = 'django_comments_xtd'

COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_CONFIRM_EMAIL = False

# Either enable sending mail messages to the console:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Or set up the EMAIL_* settings so that Django can send emails:
EMAIL_HOST = "smtp.mail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''#"Helpdesk <helpdesk@yourdomain>"
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

ROOT_URLCONF = 'NinjaApp.urls'

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

WSGI_APPLICATION = 'NinjaApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
    #'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3',
   # }
#}
#postgresl
DATABASES = {

    #'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'shobie',
       # 'USER': 'postgres',
        #'PASSWORD': 'Kihonda1628',
        #'Host' : 'Localhost',
       #  }
#}

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dalcas9g2fbrq7',
        'USER': 'dgnpelaibjwitq',
        'PASSWORD': '70f8cdada79ac8cd1a853b5403c8f34acbc00a2a0a3464aa09c1de6ba6a904b7',
        'Host' : 'ec2-34-231-221-151.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

   # 'default': {
      #  'ENGINE': 'django.db.backends.postgresql_psycopg2',
       # 'NAME': 'd9sd54vogh6bj2',
       # 'USER': 'jsenlpmrihfsaw',
       # 'PASSWORD': 'f4fd113526d136943c055d39d2592fa13ff84baedbfe33d73d72134371c4c7c5',
       # 'Host' : 'ec2-3-225-110-188.compute-1.amazonaws.com',
      #  'PORT': '5432',
  #  }
#}

    #'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
       # 'NAME': 'shobie',
       # 'USER': 'postgres',
       # 'PASSWORD': 'Kihonda1628',
       # 'Host' : 'Localhost',
        # }
#}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
cloudinary.config( 
  cloud_name = "shobie", 
  api_key = "758162452528722", 
  api_secret = "Xe6Puzh9__RGAT8UUr_KR8vn1_0" 
)

COMMENTS_XTD_CONFIRM_EMAIL = False

# Either enable sending mail messages to the console:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Or set up the EMAIL_* settings so that Django can send emails:
EMAIL_HOST = "smtp.mail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Your email'
EMAIL_HOST_PASSWORD = 'Your email password'
DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@yourdomain>"

#MEDIA_URL = '/media/'  # or any prefix you choose
#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATIC_URL = 'static/'

STATIC_DIRS=[
     os.path.join(BASE_DIR,'STATIC')  
 
     
]

STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_URL = '/mediaFiles/'
MEDIA_ROOT = os.path.join(BASE_DIR,'mediaFILES')

X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
