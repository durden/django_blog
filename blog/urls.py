# Urls
from django.conf.urls.defaults import *

# Views
from django.views.generic import list_detail

# Models
from blog_template.blog.models import Post

urlpatterns = patterns('',
    # Homepage is base template with nothing else (i.e. index page)
    url(r'^$', list_detail.object_list,
        {'queryset': Post.objects.order_by('-published'),
                        'template_object_name': 'post',}, name="blog_home"),
)
