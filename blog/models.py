from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode
from ckeditor.fields import RichTextField

# Create your models here.


class blogModel(models.Model):
    title = models.CharField(
        null=True,
        blank=False,
        max_length=100
    )

    content = RichTextField(
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

    # Yeni slug üret
    def get_unique_slug(self):
        slug = slugify(unidecode(self.title[0:30]))
        try:
            last_id = blogModel.objects.last().id
        except AttributeError:
            # Obje yoksa
            last_id = 0
        now_id = last_id + 1
        slug = "%s-%s" % (slug, now_id)
        return slug

    # Title değişince güncelle
    def get_update_slug(self):
        slug = slugify(unidecode(self.title[0:30]))
        slug = "%s-%s" % (slug, self.id)
        return slug


    def save(self, *args, **kwargs):
        if self.id is not None:
            self.slug = self.get_update_slug()
        else:
            self.slug = self.get_unique_slug()
        super(blogModel, self).save(*args, **kwargs)
