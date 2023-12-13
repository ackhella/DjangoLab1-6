from rest_framework import routers
from .viewsets import ItemViewSet

router = routers.DefaultRouter()

router.register('item', ItemViewSet)

urlpatterns = router.urls
