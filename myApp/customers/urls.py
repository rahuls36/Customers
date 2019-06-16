from rest_framework import routers
from .api import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'api/customers',CustomerViewSet,'customers')


urlpatterns = router.urls