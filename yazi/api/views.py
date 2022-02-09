from cgitb import lookup

from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
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


class YaziGuncellemeAPIView(UpdateAPIView):
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer
    lookup_field = 'slug'


class YaziOlusturAPIView(CreateAPIView):
    queryset = Yazi.objects.all()
    serializer_class = YaziOlusturmaGuncellemeSerializer
