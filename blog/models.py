from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=60)

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    body = models.TextField()
    published = models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField(Category)
