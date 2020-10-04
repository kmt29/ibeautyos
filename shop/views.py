from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import *
from .models import *
import base64


def shop(request):
    item = Item.objects.all()
    tags = Tag.objects.all()
    
    context = {'item':item,
                'tags':tags}
    return render(request, "shop/shop.html", context)

def get_by_tag(request,tag):
    search_tag = Tag.objects.get(name=tag)
    item = search_tag.item_set.all()
    tags = Tag.objects.all()
    context = {'item':item,
                'tags':tags,
                'search_tag':search_tag}
    return render(request,"shop/shop.html",context)

def post_item(request):
    form = product_posting_form()
    if request.user.is_staff:
        if request.method == 'POST':
            if form.is_valid:
                
                form = product_posting_form(request.POST,request.FILES)
                name = form.data['name']
                description = form.data['description']
                price = form.data['price']
                file_list=[]
                x = 0
                for files in request.FILES:
                    img_data = base64.b64encode(request.FILES[f'image{x}'].read())
                    file_list.append(img_data)
                    x = x + 1
                item = Item.objects.create( name=name,
                                            description=description,
                                            images=file_list,
                                            price=price)
                item.save()
                
                return redirect("/admin")
                
        return render(request, "shop/post_item.html", {'form':form})

    return redirect("/")
