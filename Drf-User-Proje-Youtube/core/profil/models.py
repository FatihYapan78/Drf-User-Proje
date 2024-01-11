from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    user = models.OneToOneField(User, related_name="profil", on_delete=models.CASCADE) # user.profil
    bio = models.CharField(max_length=150, null=True, blank=True)
    sehir = models.CharField(max_length=50, null=True, blank=True)
    pfoto = models.ImageField(upload_to="profil_foto/%Y/%m/", null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Profiller"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.pfoto:
            img = Image.open(self.pfoto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.pfoto.path)


class ProfilMesajlari(models.Model):
    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mesajlar = models.CharField(max_length=250)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profil)
    
    class Meta:
        verbose_name_plural = "Profil Mesajları"