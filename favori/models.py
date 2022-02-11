from django.contrib.auth.models import User
from django.db import models
from yazi.models import Yazi


class Favori(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yazi = models.ForeignKey(Yazi, on_delete=models.CASCADE)
    icerik = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username
