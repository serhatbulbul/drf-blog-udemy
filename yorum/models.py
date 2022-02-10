from xml.etree.ElementTree import Comment

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from yazi.models import Yazi


class Yorum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yazi = models.ForeignKey(Yazi, on_delete=models.CASCADE, related_name='yazi')
    content = models.TextField()
    ana_yorum = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='cevaplar')
    olusturulma_tarihi = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-olusturulma_tarihi']

    def __str__(self):
        return self.yazi.baslik + " " + self.user.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.olusturulma_tarihi = timezone.now()
        self.duzenlenme_tarihi = timezone.now()
        return super(Yorum, self).save(*args, **kwargs)

    def alt_yorum(self):
        return Yorum.objects.filter(ana_yorum=self)

    @property
    def any_alt_yorum(self):
        return Yorum.objects.filter(ana_yorum=self).exists()
