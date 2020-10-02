from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields.array import ArrayField

class Tag(models.Model):
    name=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.name

        
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=None,blank=True)
    images = ArrayField(models.BinaryField(),null=True,blank=True, editable=False)
    is_stock = models.BooleanField(default=True)
    is_feature = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag,blank=True)
    price = models.IntegerField(null=False,blank=False, default=0)

    def __str__(self):
        return self.name
    
    @property
    def get_images(self):
        data = []
        try:
            for images in self.images:
                data.append(bytes(images).decode('utf-8'))
        except:
            data = ''
        return data


        






