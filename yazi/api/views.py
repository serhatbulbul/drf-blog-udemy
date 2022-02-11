from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from yazi.api.paginations import YaziSayfalama

# ozel izinler
from yazi.api.permissions import SahibiMi
from yazi.api.serializers import YaziOlusturmaGuncellemeSerializer, YaziSerializer
from yazi.models import Yazi


class YaziListelemeAPIView(ListAPIView):  # dataların goruntulendiği yer
    # queryset = Yazi.objects.all() # hepsini görteriyor
    serializer_class = YaziSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['baslik']
    pagination_class = YaziSayfalama

    def get_queryset(self):
        queryset = Yazi.objects.filter(taslak=False)
        return queryset


class YaziDetayAPIView(RetrieveAPIView):  # dataların detaylarının goruntulendiği yer
    queryset = Yazi.objects.all()
    serializer_class = YaziSerializer
    lookup_field = 'slug'


class YaziGuncellemeAPIView(
    RetrieveUpdateAPIView, DestroyModelMixin
):  # retrieveupdate ile formların içinde eski veriler görünüyor
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer
    lookup_field = 'slug'
    permission_classes = [SahibiMi]

    def perform_update(self, serializer):
        serializer.save(duzenleyen_kullanici=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class YaziOlusturAPIView(CreateAPIView):
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
