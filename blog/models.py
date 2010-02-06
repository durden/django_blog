from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class PostManager(models.Manager):
    def search(self, search_string):
        search_string = search_string.strip()
        queryset = self.get_query_set()

        return queryset.filter(
                            models.Q(title__icontains=search_string) | \
                            models.Q(body__icontains=search_string))


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    body = models.TextField()
    published = models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField(Category)

    objects = PostManager()

    @models.permalink
    def get_absolute_url(self):
        return ('single_post', [self.slug])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-published']
