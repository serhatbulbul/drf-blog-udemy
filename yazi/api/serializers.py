from dataclasses import field

from rest_framework import serializers
from yazi.models import Yazi


class YaziSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yazi
        fields = (
            'baslik',
            'icerik',
            'olusturulma_tarihi',
            'slug',
            'resim',
        )


class YaziOlusturmaGuncellemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yazi
        fields = (
            'baslik',
            'icerik',
            'resim',
        )
