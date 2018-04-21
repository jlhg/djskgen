from django.conf.urls import patterns, url

from app.views import index

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       )
