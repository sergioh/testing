from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'', include('syncables.conf.common.urls.admin')),
    (r'', include('syncables.conf.common.urls.jsi18n')),
    # local app urls here
    (r'^categories/', include('syncables.apps.categories.urls')),
    # cms
    (r'^', include('cms.urls')),
)
