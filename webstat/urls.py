from django.conf.urls.defaults import *

urlpatterns = patterns('webstat.views',
    (r'^$', 'index'),
)
