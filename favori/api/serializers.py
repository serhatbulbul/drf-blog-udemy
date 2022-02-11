from favori.models import Favori
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class FavoriListelemeOlusturmaSerializer(ModelSerializer):
    class Meta:
        model = Favori
        fields = '__all__'

    def validate(self, attrs):
        fav_kontrol = Favori.objects.filter(yazi=attrs['yazi'], user=attrs['user'])
        if fav_kontrol.exists():
            raise serializers.ValidationError('Bu yazıya zaten favori eklediniz.')
        return attrs


class FavoriAPISerializer(ModelSerializer):
    class Meta:
        model = Favori
        fields = ['icerik']
