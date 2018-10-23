from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


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

    slug = models.SlugField(
        null=True,
        unique=True,
        editable=False
    )

    # Template dosyasında image url adresini almak için
    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return None

    def get_unique_slug(self):
        slug = slugify(unidecode(self.title[0:30]))
        last_id = blogModel.objects.last().id
        now_id = last_id + 1
        slug = "%s-%s" % (slug, now_id)
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super(blogModel, self).save(*args, **kwargs)
