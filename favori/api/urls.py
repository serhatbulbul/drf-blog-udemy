from django.urls import path
from favori.api.views import FavoriAPIView, FavoriListelemeOlusturmaAPIView

app_name = 'favori'


urlpatterns = [
    path('listele-olustur', FavoriListelemeOlusturmaAPIView.as_view(), name='listele-olustur'),
    path('guncelle-sil/<pk>', FavoriAPIView.as_view(), name='guncelle-sil'),
]
