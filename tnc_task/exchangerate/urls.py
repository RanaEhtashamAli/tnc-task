from django.urls import include, path
from .views import CreateListExchangeRateViewSet, CreateAPIKeyView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quotes', CreateListExchangeRateViewSet)


urlpatterns = [
    path('get_api_key/', CreateAPIKeyView.as_view())
]
urlpatterns += router.urls
