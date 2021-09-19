from rest_framework import serializers

from .models import MhDSdPw, MhDSdCi, MhDSdCd

class HmisPwSerializer(serializers.ModelSerializer):
    class Meta:
        model = MhDSdPw
        fields = '__all__'


class HmisCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MhDSdCd
        fields = '__all__'


class HmisCiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MhDSdCi
        fields = '__all__'