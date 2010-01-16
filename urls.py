from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from blog_template.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),

    # Homepage is base template with nothing else (i.e. index page)
    (r'^$', static_page, {'template': 'base'}),

    # Grab any word, and pass it as 'template' to static_page view
    # Not using b/c it appends .html for templates
    #(r'^(?P<template>\w+)/$', static_page),

    (r'^(?P<template>\w+)/$', direct_to_template),
)
