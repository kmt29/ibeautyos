from django.contrib import admin
from blog.models import *

# Register your models here.
#################################################
class BlogImageAdmin(admin.StackedInline):
    model = BlogImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [BlogImageAdmin]
    class Meta:
        model = Post
#################################################