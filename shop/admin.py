from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Webcontent)

################################################
class ItemImageAdmin(admin.StackedInline):
    model = ItemImage

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin]
    class Meta:
       model = Item
