from rest_framework.routers import DefaultRouter

from app.views import SecretKeysView

router = DefaultRouter()
router.register('secret_keys', SecretKeysView, base_name='secret_keys')
