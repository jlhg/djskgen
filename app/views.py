from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from core.helpers import generate_secret_key


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_ANALYTICS_ID'] = settings.GOOGLE_ANALYTICS_ID
        return context


class SecretKeysView(GenericViewSet, mixins.ListModelMixin):
    def get_queryset(self):
        pass  # pragma: no cover

    def list(self, request, *args, **kwargs):
        return Response([generate_secret_key() for _ in range(20)])
