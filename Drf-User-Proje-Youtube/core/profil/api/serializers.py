from profil.models import *
from rest_framework import serializers


class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    pfoto = serializers.ImageField(read_only=True)
    class Meta:
        model = Profil
        fiedls = "__all__"

class ProfilFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ["pfoto"]

class ProfilMesajlariSerializer(serializers.ModelSerializer):
    user_profil = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfilMesajlari
        fields = "__all__"