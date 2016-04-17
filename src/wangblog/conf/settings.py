"""
Django settings for WangBlog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!w^&&xb4%+f%sw&5dkv*#73*9e76kch%!n+w2p*xjn@fco$cse'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'wangblog.User'

RECAPTCHA_PUBLIC_KEY = ''
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'wangblog',
    'oauth2_provider',
    'corsheaders',
    'rest_framework',
)

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.AllowAny',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    # ),
    'PAGE_SIZE': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wangblog.urls'

WSGI_APPLICATION = 'wangblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

from django.core.urlresolvers import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('home')

CLIENT_ID = ''
CLIENT_SECRET = ''
if DEBUG:
    OAUTH_SERVER = 'localhost:8000'
else:
    OAUTH_SERVER = 'auth.loginsight.cn'
LOGAGENT_CLIENT_ID = '1S_wRvye9?Xq4mU91e!MPixJ9Qjl3yQIaW?7G=2j'
LOGAGENT_CLIENT_SECRET = 'hLXU?HCktQu::1xz9EsjWMUq:yiLp2A=SgQpH4HKTgM4zFS@WMQjFtVGSYV.gu6wC!6UCgfxSqyzKUZWymuyQq_lUGQH;Udmhy3gvAQ73GNF3HXgzT94YkNP0RvIx:m1'
DEFALUT_SENTRY_CLIENT_ID = 'ZvwRr6t?WkzuHO5htOkCjti-FHL=Ri5DsA!;6qWX'
DEFAULT_SENTRY_CLIENT_SECRET = 'ASzRYogeWgVasXPXsbpBAPTBYEXHiNjITAQBngM;TMmtH=xj1m7Lx33WNW99E9ozCEi88flhazxupg4Cr?:x=bbfZ=ih9;Fo7J6jjNc6jRZ9Q:CLOqB2dN!zv@lQz!=T'

