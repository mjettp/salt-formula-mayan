{% from "mayan/map.jinja" import server with context %}

# Django settings for mayan project.
import os
import sys

from django.core.urlresolvers import reverse_lazy

ugettext = lambda s: s

BASE_DIR = os.path.dirname(__file__)
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOG_ROOT = os.path.abspath("/srv/mayan/logs")

sys.path.append(os.path.join(BASE_DIR, 'apps'))

PROJECT_TITLE = 'Mayan EDMS'
PROJECT_NAME = 'mayan'

DEBUG = True
DEVELOPMENT = True
TEMPLATE_DEBUG = True

ADMINS = ()
MANAGERS = ADMINS

#postgresql_psycopg2
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ server.database.name }}',
        'USER': '{{ server.database.user }}',
        'PASSWORD': '{{ server.database.password }}',
        'HOST': '{{ server.database.host }}',
        'PORT': '{{ server.database.port }}',
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('ar', ugettext('Arabic')),
    ('bg', ugettext('Bulgarian')),
    ('bs', ugettext('Bosnian (Bosnia and Herzegovina)')),
    ('da', ugettext('Danish')),
    ('de', ugettext('German (Germany)')),
    ('en', ugettext('English')),
    ('es', ugettext('Spanish')),
    ('fa', ugettext('Persian')),
    ('fr', ugettext('French')),
    ('hu', ugettext('Hungarian')),
    ('hr', ugettext('Croatian')),
    ('id', ugettext('Indonesian')),
    ('it', ugettext('Italian')),
    ('nl', ugettext('Dutch (Nethherlands)')),
    ('pl', ugettext('Polish')),
    ('pt', ugettext('Portuguese')),
    ('pt-br', ugettext('Portuguese (Brazil)')),
    ('ro', ugettext('Romanian (Romania)')),
    ('ru', ugettext('Russian')),
    ('sl', ugettext('Slovenian')),
    ('tr', ugettext('Turkish')),
    ('vi', ugettext('Vietnamese (Viet Nam)')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
STATIC_URL = '/%s-static/' % PROJECT_NAME

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'om^a(i8^6&h+umbd2%pt91cj!qu_@oztw117rgxmn(n2lp^*c!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'common.middleware.strip_spaces_widdleware.SpacelessMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'common.middleware.login_required_middleware.LoginRequiredMiddleware',
    'permissions.middleware.permission_denied_middleware.PermissionDeniedMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'mayan.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
#Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.staticfiles',
# 3rd party
# South
    'south',
# Others
    'filetransfers',
    'taggit',
    'mptt',
    'compressor',
    'rest_framework',
# Base generic
    'permissions',
    'project_setup',
    'project_tools',
    'smart_settings',
    'navigation',
    'lock_manager',
    'web_theme',
# pagination needs to go after web_theme so that the pagination template
# if found
    'pagination',
    'common',
    'django_gpg',
    'dynamic_search',
    'acls',
    'converter',
    'user_management',
    'mimetype',
    'scheduler',
    'job_processor',
    'installation',
# Mayan EDMS
    'storage',
    'app_registry',
    'folders',
    'tags',
    'document_comments',
    'metadata',
    'documents',
    'linking',
    'document_indexing',
    'document_acls',
    'ocr',
    'sources',
    'history',
    'main',
    'rest_api',
    'document_signatures',
    'checkouts',
    'bootstrap',
    'registration',
# Has to be last so the other apps can register it's signals
    'signaler',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']

COMPRESS_ENABLED=False
SENDFILE_BACKEND = 'sendfile.backends.simple'
#--------- Web theme ---------------
WEB_THEME_ENABLE_SCROLL_JS = False
#--------- Django -------------------
LOGIN_URL = reverse_lazy('login_view')
LOGIN_REDIRECT_URL = reverse_lazy('home')
#-------- LoginRequiredMiddleware ----------
LOGIN_EXEMPT_URLS = (
    r'^favicon\.ico$',
    r'^about\.html$',
    r'^legal/',  # allow the entire /legal/* subsection
    r'^%s-static/' % PROJECT_NAME,

    r'^accounts/register/$',
    r'^accounts/register/complete/$',
    r'^accounts/register/closed/$',

    r'^accounts/activate/complete/',
    r'^accounts/activate/(?P<activation_key>\w+)/$',

    r'^password/reset/$',
    r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    r'^password/reset/complete/$',
    r'^password/reset/done/$',
)
#--------- Pagination ----------------
PAGINATION_INVALID_PAGE_RAISES_404 = True
#---------- Search ------------------
SEARCH_SHOW_OBJECT_TYPE = False

SERIALIZATION_MODULES = {
    'better_yaml': 'common.serializers.better_yaml',
}

try:
    from settings_local import *
except ImportError:
    pass


if DEVELOPMENT:
    INTERNAL_IPS = ('127.0.0.1',)

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
    try:
        import rosetta
        INSTALLED_APPS += ('rosetta',)
    except ImportError:
        pass

    try:
        import django_extensions
        INSTALLED_APPS += ('django_extensions',)
    except ImportError:
        pass

    try:
        import debug_toolbar
        #INSTALLED_APPS +=('debug_toolbar',)
    except ImportError:
        pass

    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

    WSGI_AUTO_RELOAD = True
    if 'debug_toolbar' in INSTALLED_APPS:
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
        }