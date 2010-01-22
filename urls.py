# Urls
from django.conf.urls.defaults import *

# Views
from blog_template.views import *

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/(.*)', admin.site.root),

    (r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': 'static/'}),

    # Homepage is base template with nothing else (i.e. index page)
    (r'^', include('blog_template.blog.urls')),

    # Grab any word, and pass it as 'template' to static_page view
    # Not using b/c it appends .html for templates
    url(r'^(?P<template>\w+)/$', static_page, name='static_page'),
)
