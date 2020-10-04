from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields.array import ArrayField
from django.shortcuts import redirect

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

class Webcontent(models.Model):
    lead_1 = models.TextField(max_length=None,blank=True)
    lead_2 = models.TextField(max_length=None,blank=True)
    topic_1 = models.TextField(max_length=None,blank=True)
    topic_2 = models.TextField(max_length=None,blank=True)
    topic_3 = models.TextField(max_length=None,blank=True)
    content_1 = models.TextField(max_length=None,blank=True)
    content_2 = models.TextField(max_length=None,blank=True)
    content_3 = models.TextField(max_length=None,blank=True)

    lead_1_mm = models.TextField(max_length=None,blank=True)
    lead_2_mm = models.TextField(max_length=None,blank=True)
    topic_1_mm = models.TextField(max_length=None,blank=True)
    topic_2_mm = models.TextField(max_length=None,blank=True)
    topic_3_mm = models.TextField(max_length=None,blank=True)
    content_1_mm = models.TextField(max_length=None,blank=True)
    content_2_mm = models.TextField(max_length=None,blank=True)
    content_3_mm = models.TextField(max_length=None,blank=True)

    def save(self, *args, **kwargs):
        if Webcontent.objects.count() == 1:
            tobedeleted = Webcontent.objects.all()
            tobedeleted[0].delete()
            
        super(Webcontent, self).save(*args, **kwargs)

        






