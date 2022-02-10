from django.urls import path
from yorum.api.views import YorumGuncellemeAPIView, YorumListelemeAPIView, YorumOlusturmaAPIView, YorumSilmeAPIView

app_name = 'yorum'

urlpatterns = [
    path('olustur/', YorumOlusturmaAPIView.as_view(), name='olustur'),
    path('listele/', YorumListelemeAPIView.as_view(), name='listele'),
    path('sil/<pk>/', YorumSilmeAPIView.as_view(), name='sil'),
    path('guncelle/<pk>/', YorumGuncellemeAPIView.as_view(), name='guncelle'),
]
