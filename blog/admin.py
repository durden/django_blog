from django.contrib import admin
from blog_template.blog.models import *

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
