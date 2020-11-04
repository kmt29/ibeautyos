from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from .forms import *
from .models import *
import base64


def shop(request):
    return get_by_tag(request,'all')

def get_by_tag(request,tag):
    page_num = request.GET.get('page',1)
    search_tag = None
    if tag == 'all' or tag == None:
        item = Paginator(Item.objects.all(),16)
        item = item.page(page_num)
    else:
        search_tag = Tag.objects.get(name=tag)
        item = Paginator(search_tag.item_set.all(),16)
        item = item.page(page_num)

    page_num = request.GET.get('page',1)
    

    tags = Tag.objects.all()
    context = {'item':item,
                'tags':tags,
                'search_tag':search_tag}
    return render(request,"shop/shop.html",context)

def item_detail(request,id):
    item = Item.objects.get(id=id)
    context = {'item':item}
    return render(request,"shop/item.html",context)

def get_sale_item(request):
    discounted_items = Item.objects.filter(is_discount=True)

    context={'item':discounted_items}
    return render(request,"shop/sale.html",context)
