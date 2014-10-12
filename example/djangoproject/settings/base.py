"""
Django settings for djangoproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEPLOY_DIR = os.path.join(BASE_DIR, '..', 'deploy')
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SET THIS IN djangoproject.settings.production'

# SECURITY WARNING: don't run with debug turned on in production!
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
    'bearbones',
    'django_medusa',
    'pipeline',
    'rest_framework',
    'bbcms',
    'example',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangoproject.urls'

WSGI_APPLICATION = 'djangoproject.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


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


# Static files

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATIC_ROOT = os.path.join(DEPLOY_DIR, 'static')
STATICFILES_FINDERS = (
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DEPLOY_DIR, 'media')

BOWER_BASE_DIR = os.path.join(BASE_DIR, 'static/bower')
NPM_BASE_DIR = os.path.join(BASE_DIR, '../node_modules')
PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_CSSMIN_BINARY = os.path.join(NPM_BASE_DIR, 'cssmin/bin/cssmin')
PIPELINE_CSSMIN_ARGUMENTS = ''

# npm install -g uglify-js
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_BINARY = os.path.join(NPM_BASE_DIR, 'uglify-js/bin/uglifyjs')
PIPELINE_UGLIFYJS_ARGUMENTS = ''
PIPELINE_LESS_BINARY = os.path.join(BASE_DIR, '../node_modules/less/bin/lessc')
#PIPELINE_DISABLE_WRAPPER = True
PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'bower/bootstrap/dist/css/bootstrap.min.css',
            'bower/bootstrap/dist/css/bootstrap-theme.min.css',
            'css/example.less',
        ),
        'output_filename': 'css/main.css'
    },
    'cms': {
        'source_filenames': (
            'bower/bootstrap/dist/css/bootstrap.css',
            'bower/pnotify/pnotify.core.css',
            'bower/pnotify/pnotify.buttons.css',
            'bower/pnotify/pnotify.history.css',
            'css/bbcms.css',
        ),
        'output_filename': 'css/cms.css'
    }
}

PIPELINE_JS = {
    'main': {
        'source_filenames': (
            'bower/jquery/jquery.js',
            'bower/bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/main.js'
    },
    'cms': {
        'source_filenames': (
            'bower/jquery/jquery.js',
            'bower/angular/angular.js',
            'bower/bootstrap/dist/js/bootstrap.js',
            'bower/angular-resource/angular-resource.js',
            'bower/angular-cookies/angular-cookies.js',
            'bower/angular-sanitize/angular-sanitize.js',
            'bower/angular-route/angular-route.js',
            'bower/lodash/dist/lodash.compat.js',
            'bower/restangular/dist/restangular.js',
            'bower/pnotify/pnotify.core.js',
            'bower/pnotify/pnotify.buttons.js',
            'bower/pnotify/pnotify.callbacks.js',
            'bower/pnotify/pnotify.confirm.js',
            'bower/pnotify/pnotify.desktop.js',
            'bower/pnotify/pnotify.history.js',
            'bower/pnotify/pnotify.nonblock.js',
            'bower/angular-pnotify/src/angular-pnotify.js',
            'js/cms/app/scripts/*.js',
            'js/cms/app/scripts/*/*.js',
        ),
        'output_filename': 'js/cms.js'
    }
}

MEDUSA_RENDERER_CLASS = 'django_medusa.renderers.DiskStaticSiteRenderer'
MEDUSA_MULTITHREAD = False  # This doesn't work for some reason
MEDUSA_DEPLOY_DIR = DEPLOY_DIR

MEDUSA_RENDER_PATHS = [
    '/',
]
