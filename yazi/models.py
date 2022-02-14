from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Yazi(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )  # default 1 olmazsa api den oluştururken hata veriyor
    baslik = models.CharField(max_length=120)
    icerik = models.TextField()
    taslak = models.BooleanField(default=False)
    olusturulma_tarihi = models.DateTimeField(editable=False)
    duzenlenme_tarihi = models.DateTimeField()
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    resim = models.ImageField(upload_to='resim/yazi', blank=True, null=True)
    duzenleyen_kullanici = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='duzenleyen_kullanici'
    )

    class Meta:
        ordering = ['-id']

    def get_slug(self):  # slug'i oluşturmak için kullanılır.
        slug = slugify(self.baslik.replace("ı", "i"))
        unique = slug
        number = 1

        while Yazi.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.olusturulma_tarihi = timezone.now()
        self.duzenlenme_tarihi = timezone.now()
        self.slug = self.get_slug()
        return super(Yazi, self).save(*args, **kwargs)

    def __str__(self):
        return self.baslik
