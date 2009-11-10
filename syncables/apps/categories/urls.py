from django.conf.urls.defaults import *

urlpatterns = patterns('syncables.apps.categories.views',
    url(r'(?P<id>[0-9]+)/$', 'category_view', name='category_view'),
)
