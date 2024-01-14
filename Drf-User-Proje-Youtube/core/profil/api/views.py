from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profil.models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .permission import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProfilViewSet(ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated, KendiProfiliOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'sehir']
    # filter_backends = [SearchFilter]
    # search_fields = ["sehir"]

class ProfilMesajlariViewSet(ModelViewSet):
    serializer_class = ProfilMesajlariSerializer
    permission_classes = [IsAuthenticated, MesajSahibiOrReadOnly]

    def perform_create(self, serializer):
        user_profil = self.request.user.profil
        serializer.save(user_profil=user_profil)

    def get_queryset(self):
        queryset = ProfilMesajlari.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profil__user__username=username)
        return queryset

class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil = self.request.user.profil
        return profil

