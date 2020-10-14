from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields.array import ArrayField
from django.shortcuts import redirect

class Tag(models.Model):
    class Meta:
        app_label = 'shop'
    name=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.name

        
# Create your models here.
class Item(models.Model):
    class Meta:
        app_label = 'shop'
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=None,blank=True)
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
            for image in self.image_set.all():
                data.append(image.image.url)
        except Exception as e:
            data.append('/static/media/ibeauty_logo.png')
        return data
    
class Image(models.Model):
    class Meta:
        app_label = 'shop'
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.item.name

class Webcontent(models.Model):
    class Meta:
        app_label = 'shop'
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

        






