from django.db import models
from django.urls import reverse


class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name="Header")
    content = models.TextField(blank=True, verbose_name="Information")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    price = models.CharField(max_length=255, verbose_name="Price")
    country = models.TextField(blank=True, verbose_name="Country")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated time")
    is_published = models.BooleanField(default=True,)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Region")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tour', kwargs={'tour_slug': self.slug})

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ['-time_create','name']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        ordering = ['id']

