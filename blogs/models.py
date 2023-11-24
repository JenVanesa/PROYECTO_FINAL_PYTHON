from django.db import models
from django.conf import settings


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categories = models.ManyToManyField('Categorias')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Categorias(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "categorias"