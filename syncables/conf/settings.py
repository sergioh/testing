"""
Extensible django settiongs.
DO NOT ADD LOCAL SETTINGS HERE.
 -> Use conf/local/settings.py
"""
# Import global settings to make it easier to extend settings. 
from django.conf.global_settings import *
# Import the project module to calculate directories relative to the module
# location.
import os
import syncables

PROJECT_ROOT, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(syncables.__file__))
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CACHE_BACKEND = 'locmem:///'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'static')

ROOT_URLCONF = 'syncables.conf.urls'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
)

INSTALLED_APPS = (
    ## django contrib
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',

    ## local apps
    'syncables.apps.common',
    'syncables.apps.categories',

    ## cms
    'cms',
    'publisher',

    ## cms plugins
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    #'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'cms.plugins.video',
    #'cms.plugins.twitter',

    ## cms's requirements
    'mptt',
    'reversion',
    'south',

    ## 3rd party apps
    'tagging',
    'django_extensions',
)

# Test database settings
TEST_DATABASE_CHARSET = 'utf-8'
TEST_DATABASE_COLLATION = 'utf8_general_ci'
DATABASE_SUPPORTS_TRANSACTIONS = True

gettext = lambda s: s

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', gettext('English')),
)

# CMS settings
CMS_LANGUAGE_CONF = {
    #'de':['en'],
}

CMS_TEMPLATES = (
    ('cms/default.html', gettext('default')),
    ('cms/cool.html', gettext('cool one')),
)

CMS_APPLICATIONS_URLS = (
)

CMS_PLACEHOLDER_CONF = {
    'right-column': {
        "plugins": ('FilePlugin', 'FlashPlugin', 'LinkPlugin', 'PicturePlugin', 'TextPlugin', 'SnippetPlugin'),
        "extra_context": {"theme":"16_16"},
        "name":gettext("right column")
    },
    
    'body': {
        "plugins": ("VideoPlugin", "TextPlugin", ),
        "extra_context": {"theme":"16_5"},
        "name":gettext("body"),
    },
    'fancy-content': {
        "plugins": ('TextPlugin', 'LinkPlugin'),
        "extra_context": {"theme":"16_11"},
        "name":gettext("fancy content"),
    },
}

CMS_NAVIGATION_EXTENDERS = (
    ('syncables.apps.categories.navigation.get_nodes',
        gettext('Categories')),
)

CMS_SOFTROOT = True
CMS_MODERATOR = True
CMS_PERMISSION = True
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNSTRANSLATED = False
