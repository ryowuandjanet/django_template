from .base import *

# 將base.py DEBUG 和 ALLOWED_HOSTS 移到這裡(不做修改)
DEBUG = True
ALLOWED_HOSTS = ['*']

# 將base.py INSTALLED_APPS裡的 'debug_toolbar' 移到這裡
INSTALLED_APPS += [
	'debug_toolbar',
]

# 將base.py MIDDLEWARE裡的 'debug_toolbar.middleware.DebugToolbarMiddleware' 移到這裡
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# 將 DEBUG_TOOLBAR_PANELS 及 DEBUG_TOOLBAR_CONFIG 移到這裡(不做修改)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": {
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel'
    },
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# 將 DATABASES 移到這裡(不做修改)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 新增 STRIPE_PUBLIC_KEY 及 STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
