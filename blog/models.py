from django.db import models
from shop.models import Item
from django.utils.datetime_safe import datetime

# Create your models here.
class Post(models.Model):
    class Meta:
        app_label = 'blog'
    title = models.CharField(max_length=200,blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField(max_length=None,blank=True)
    related_items = models.ManyToManyField(Item,blank=True)

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    class Meta:
        app_label = 'blog'
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self):
        return self.post.title
