from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Product.Status.PUBLISHED)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('cat_slug', kwargs={'cat_slug': self.slug})
    def __str__(self):
        return self.name
class ProductDetails(models.Model):
    material = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    warranty_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.material} | {self.size} | {self.warranty_years} года"
class Product(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    objects = models.Manager()  # обычный менеджер
    published = PublishedManager()
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True, related_name='products')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    details = models.OneToOneField(ProductDetails, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.title
