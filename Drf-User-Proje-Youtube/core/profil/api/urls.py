from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiller", ProfilViewSet)
router.register(r"profil_mesajlari", ProfilMesajlariViewSet, basename="durum")

urlpatterns = [
    path("", include(router.urls)),
    path("profil_foto/", ProfilFotoUpdateView.as_view(),name="profil-foto"),
]