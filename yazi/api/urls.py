from django.urls import include, path
from yazi.api.views import YaziListelemeAPIView

urlpatterns = [
    path('/listele', YaziListelemeAPIView.as_view(), name='listele'),
]
