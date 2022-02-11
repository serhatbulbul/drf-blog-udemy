from django.urls import include, path
from yazi.api.views import YaziDetayAPIView, YaziGuncellemeAPIView, YaziListelemeAPIView, YaziOlusturAPIView

app_name = "yazi"
urlpatterns = [
    path('listele', YaziListelemeAPIView.as_view(), name='listele'),
    path('detay/<slug>', YaziDetayAPIView.as_view(), name='detay'),
    path('guncelle/<slug>', YaziGuncellemeAPIView.as_view(), name='guncelle'),
    path('olustur/', YaziOlusturAPIView.as_view(), name='olustur'),
]
