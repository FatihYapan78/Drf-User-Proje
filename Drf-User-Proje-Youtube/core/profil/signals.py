from django.contrib.auth.models import User
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    # print(instance.username,"-------",created)
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=Profil)
def create_ilk_mesaj(sender, instance, created, **kwargs):
    # print(instance.username,"-------",created)
    if created:
        ProfilMesajlari.objects.create(
            user_profil = instance,
            mesajlar = f"{instance.user.username} aramıza Hoşgeldin."
        )