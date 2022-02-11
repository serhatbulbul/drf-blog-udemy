from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from yazi.models import Yazi
from yorum.models import Yorum


class YorumOlusturmaSerializer(ModelSerializer):
    class Meta:
        model = Yorum
        exclude = [
            'olusturulma_tarihi',
        ]

    def validate(self, attrs):
        if attrs["ana_yorum"]:
            if attrs["ana_yorum"].yazi != attrs["yazi"]:
                raise serializers.ValidationError("Yorumlar birbirine bağlı olmalıdır.")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'id',
            'email',
        ]


class YaziYorumSerializer(ModelSerializer):
    class Meta:
        model = Yazi
        fields = ['baslik', 'slug', 'id']


class YorumListelemeSerializer(ModelSerializer):

    cevaplar = SerializerMethodField()
    user = UserSerializer()
    yazi = YaziYorumSerializer()

    class Meta:
        model = Yorum
        fields = "__all__"
        # depth = 1   #foreign key olan herşeyin özelliğini gosterir

    def get_cevaplar(self, obj):
        if obj.any_alt_yorum:
            return YorumListelemeSerializer(obj.alt_yorum(), many=True).data


class YorumSilmeGuncellemeSerializer(ModelSerializer):
    class Meta:
        model = Yorum
        fields = ["content"]
