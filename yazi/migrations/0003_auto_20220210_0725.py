# Generated by Django 3.2.10 on 2022-02-10 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yazi', '0002_auto_20220209_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazi',
            name='duzenleyen_kullanici',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='duzenleyen_kullanici', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='yazi',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]