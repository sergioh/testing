from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^jsi18n/(?P<packages>\S+?)/$', 
        'django.views.i18n.javascript_catalog'),
)
