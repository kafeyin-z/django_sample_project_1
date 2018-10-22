from django.db import models


# Create your models here.


class blogModel(models.Model):
    title = models.CharField(
        null=True,
        blank=False,
        max_length=100
    )

    content = models.TextField(
        null=True,
        blank=False,
        max_length=1000
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='blog'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    update_date = models.DateTimeField(
        auto_now=True
    )

    # Template dosyasında image url adresini almak için
    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return None
