from rest_framework.routers import DefaultRouter

from app.views import SecretKeyView

router = DefaultRouter()
router.register('secret_key', SecretKeyView, base_name='secret_key')
