# Generated by Django 5.0.1 on 2024-01-12 11:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profil", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profil",
            options={"verbose_name_plural": "Profiller"},
        ),
        migrations.AlterModelOptions(
            name="profilmesajlari",
            options={"verbose_name_plural": "Profil Mesajları"},
        ),
    ]
