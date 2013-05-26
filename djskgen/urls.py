from django.conf.urls import patterns, url
from djskgen.views import keygen

urlpatterns = patterns('',
                       url(r'^$', keygen.index, name='index'),
                       )
