from django.shortcuts import render
from shop.models import *
# Create your views here.
def home(request):
    item = None
    try:
        item = Item.objects.filter(is_feature=True)
    except:
        item = []
        
    context = {'item':item}
    return render(request,"core/home.html",context)