from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from yorum.api.paginations import YorumSayfalama
from yorum.api.permissions import SahibiMi
from yorum.api.serializers import YorumListelemeSerializer, YorumOlusturmaSerializer, YorumSilmeGuncellemeSerializer
from yorum.models import Yorum


class YorumOlusturmaAPIView(CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumOlusturmaSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class YorumListelemeAPIView(ListAPIView):
    serializer_class = YorumListelemeSerializer
    pagination_class = YorumSayfalama

    def get_queryset(self):
        queryset = Yorum.objects.filter(ana_yorum=None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(yazi=query)
        return queryset


class YorumSilmeAPIView(DestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSilmeGuncellemeSerializer
    lookup_field = 'pk'  # silme islemlerinde lookupfield kullanılır
    permission_classes = [SahibiMi]


class YorumGuncellemeAPIView(UpdateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSilmeGuncellemeSerializer
    lookup_field = 'pk'  # silme islemlerinde lookupfield kullanılır
    permission_classes = [SahibiMi]
