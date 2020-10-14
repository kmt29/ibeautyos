from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Webcontent)

class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
       model = Item

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass