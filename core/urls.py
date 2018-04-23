from django.conf.urls import url, include

from app.routers import router
from app.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(router.urls)),
]
