# Urls
from django.conf.urls.defaults import *

# Views
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from blog_template.views import *

# Models
from blog_template.blog.models import Post

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/(.*)', admin.site.root),

    # Homepage is base template with nothing else (i.e. index page)
    (r'^$', include('blog_template.blog.urls')),

    # Blogs
    (r'^blog/$', include('blog_template.blog.urls')),

    # Grab any word, and pass it as 'template' to static_page view
    # Not using b/c it appends .html for templates
    url(r'^(?P<template>\w+)/$', static_page, name='static_page'),

    (r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': 'static/'}),
)
