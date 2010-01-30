# Urls
from django.conf.urls.defaults import *

# Views
from django.views.generic import list_detail
from blog_template.blog.views import *

# Models
from blog_template.blog.models import Post

urlpatterns = patterns('',
    url(r'post/(?P<slug>[a-z-]+)/$', blog_generic_view,
            {'redirect_to': list_detail.object_detail, 'slug_field' : 'slug',},
        name='single_post'),

    # Homepage is base template with nothing else (i.e. index page)
    url(r'^$', blog_generic_view, {'redirect_to': list_detail.object_list},
        name="blog_home"),
)
