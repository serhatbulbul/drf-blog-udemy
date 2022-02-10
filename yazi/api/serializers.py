from cgitb import lookup
from dataclasses import field

from rest_framework import serializers
from yazi.models import Yazi


class YaziSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='yazi:detay', lookup_field='slug')

    username = serializers.SerializerMethodField(method_name='yeni_kullaniciadi')

    class Meta:
        model = Yazi
        fields = (
            'username',
            'baslik',
            'icerik',
            'olusturulma_tarihi',
            'url',
            'resim',
            'duzenleyen_kullanici',
        )

    def yeni_kullaniciadi(self, obj):
        return obj.user.username


class YaziOlusturmaGuncellemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yazi
        fields = (
            'user',
            'baslik',
            'icerik',
            'resim',
            'duzenleyen_kullanici',
        )
