"""
Django settings for LoveRoom project.

Generated by 'django-admin startproject' using Django 1.11.22.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fx1l#+sf)*#*vz%xr7z7(4yc#v!e$d4rocfq4f_z)7qyg&^uj_'

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
    'apps.blog',
    'apps.house',
    'apps.owner',
    'apps.Uc',
    'apps.help',
    'apps.apis',
    'apps.show',
    'apps.alipay',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LoveRoom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.Uc.context_processors.regform',
                'apps.Uc.context_processors.phform',
                'apps.Uc.context_processors.pwform',

            ],
        },
    },
]

WSGI_APPLICATION = 'LoveRoom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 配置日志
LOG_ROOT = os.path.join(BASE_DIR,'logs')
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)

FontPath = os.path.join(BASE_DIR,'/static/fonts/')

LOGGING =  {
    'version' : 1,
    'disable_existing_loggers' : True,
    'formatters' : {
        'standard' : {
            'format' : '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        }
    },
    'filter' : {

    },
    'handlers' : {
        'mail_admins' : {
            'level' : 'ERROR',
            'class' : 'django.utils.log.AdminEmailHandler',
            'include_html' : True,
        },
        'default' : {
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(LOG_ROOT,'all.log'),
            'maxBytes' : 1024*1024*5,
            'backupCount' : 5,
            'formatter' : 'standard',
            'encoding' : 'utf-8',
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'error.log'),
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            'encoding' : 'utf-8',
            },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'request.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            'encoding' : 'utf-8',
            },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            'encoding' : 'utf-8',
            },
        'account_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'Uc.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding' : 'utf-8',
        },
        'apis_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'apis.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding' : 'utf-8',
        },
        'house_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'house.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding' : 'utf-8',

        }
    },
    'loggers': {
        # 'django': {
        #     'handlers1': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
        'account':{
            'handlers': ['account_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'apis': {
            'handlers': ['apis_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'house': {
            'handlers': ['house_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# 配置媒体文件路径
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'Uc.User'

CACHES = {
    'default': {
        # BACKEND配置缓存后端为RedisCache
        'BACKEND': 'django_redis.cache.RedisCache',
        # LOCATION配置redis服务器地址
        'LOCATION': 'redis://192.168.0.20:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "",
        },
    },
}

ALIPAY = {
    'app_id': '2016101400680725',
    'key': '760bdzec6y9goq7ctyx96ezkz78287de',
    'seller_email': 'overseas_kgtest@163.com',
    'gateway': 'https://openapi.alipaydev.com/gateway.do?',
    'server_url': "http://127.0.0.1:8000",
    # app的私钥
    'app_private_key': "keys/app_private_key.txt",
    # alipay的公钥
    'alipay_public_key': "keys/alipay_public_key.txt",
}