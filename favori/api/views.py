from cgitb import lookup

from favori.api.paginations import FavoriSayfalama
from favori.api.permissions import SahibiMi
from favori.api.serializers import FavoriAPISerializer, FavoriListelemeOlusturmaSerializer
from favori.models import Favori
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class FavoriListelemeOlusturmaAPIView(ListCreateAPIView):

    serializer_class = FavoriListelemeOlusturmaSerializer
    pagination_class = FavoriSayfalama
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favori.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favori.objects.all()
    serializer_class = FavoriAPISerializer
    lookup_field = 'pk'
    permission_classes = [SahibiMi]
