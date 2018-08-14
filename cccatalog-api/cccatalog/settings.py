"""
Django settings for cccatalog project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import psycopg2
from socket import gethostname, gethostbyname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where to collect static files in production/development deployments
STATIC_ROOT = "/var/api_static_content/static"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The default key is only valid for local configurations and is not suitable for production use.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'ny#b__$f6ry4wy8oxre97&-68u_0lk3gw(z=d40_dxey3zw0v1')

# SECURITY WARNING: don't run with debug turned on in production!
true_strings = ['true', 'True', 't']
DEBUG = os.environ.get('DJANGO_DEBUG_ENABLED', default=False) in true_strings

ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ.get('LOAD_BALANCER_URL'),
                 'api-dev.creativecommons.engineering',
                 "api.creativecommons.engineering",
                 gethostname(), gethostbyname(gethostname())]

# Domains that shortened links may point to
SHORT_URL_WHITELIST = {
    'api-dev.creativecommons.engineering',
    'api.creativecommons.engineering',
    'ccccatalog.herokuapp.com'
}
SHORT_URL_PATH_WHITELIST = ['/list', '/image/']

# Intermittently run tasks
CRON_CLASSES = [
    'cccatalog.api.utils.scheduled_tasks.SaveCachedTrafficStats'
]

# Application definition

INSTALLED_APPS = [
    'cccatalog',
    'cccatalog.api',
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cron',
    'oauth2_provider',
    'social_django',
    'rest_framework',
    'rest_framework_social_oauth2',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

CACHES = {
    # Site cache writes to 'default'
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://' +
                    os.environ.get('REDIS_HOST','cache') + ':6379/' + '0',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get('REDIS_PASSWORD')
        },
    },
    # For rapidly changing stats that we don't want to hammer the database with
    "traffic_stats": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://' +
                    os.environ.get('REDIS_HOST', 'cache') + ':6379/' + '1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get('REDIS_PASSWORD')
        },
    },
    # For ensuring consistency among multiple Django workers and servers.
    # Used by Redlock.
    "locks": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://' +
                    os.environ.get('REDIS_HOST', 'cache') + ':6379/' + '2',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get('REDIS_PASSWORD')
        },
    }
}

AUTHENTICATION_BACKENDS = (
    # GitHub social login
    'social_core.backends.github.GithubOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'cccatalog.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'cccatalog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME'),
        'USER': os.environ.get('DJANGO_DATABASE_USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST'),
        'PORT': os.environ.get('DJANGO_DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Allow anybody to access the API from any domain
CORS_ORIGIN_ALLOW_ALL = True

# API specific configuration

# The version of the API. We follow the semantic versioning specification.
API_VERSION = os.environ.get(
    'SEMANTIC_VERSION',
    "Version not specified."
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('GITHUB_SOCIAL_CLIENT_ID')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('GITHUB_SOCIAL_CLIENT_SECRET')

ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', 'localhost')
ELASTICSEARCH_PORT = int(os.environ.get('ELASTICSEARCH_PORT', 9200))

# Additional settings for dev/prod environments
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
ELASTICSEARCH_AWS_REGION = \
    os.environ.get('ELASTICSEARCH_AWS_REGION', 'us-east-1')

ROOT_SHORTENING_URL = os.environ.get('ROOT_SHORTENING_URL', 'dev.shares.cc')
