from dataclasses import field

from rest_framework import serializers
from yazi.models import Yazi


class YaziSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yazi
        fields = (
            'user',
            'baslik',
            'icerik',
            'olusturulma_tarihi',
            'slug',
            'resim',
            'duzenleyen_kullanici',
        )


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
