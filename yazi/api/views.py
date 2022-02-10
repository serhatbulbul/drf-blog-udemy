from cgitb import lookup

from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# ozel izinler
from yazi.api.permissions import SahibiMi
from yazi.api.serializers import YaziOlusturmaGuncellemeSerializer, YaziSerializer
from yazi.models import Yazi


class YaziListelemeAPIView(ListAPIView):  # dataların goruntulendiği yer
    queryset = Yazi.objects.all()
    serializer_class = YaziSerializer


class YaziDetayAPIView(RetrieveAPIView):  # dataların detaylarının goruntulendiği yer
    queryset = Yazi.objects.all()
    serializer_class = YaziSerializer
    lookup_field = 'slug'


class YaziSilmeAPIView(DestroyAPIView):
    queryset = Yazi.objects.all()
    serializer_class = YaziSerializer
    lookup_field = 'slug'
    permission_classes = [SahibiMi]


class YaziGuncellemeAPIView(RetrieveUpdateAPIView):  # retrieveupdate ile formların içinde eski veriler görünüyor
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer
    lookup_field = 'slug'
    permission_classes = [SahibiMi]

    def perform_update(self, serializer):
        serializer.save(duzenleyen_kullanici=self.request.user)


class YaziOlusturAPIView(CreateAPIView):
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
