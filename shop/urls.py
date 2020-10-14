from django.urls import path

from . import views

urlpatterns = [
    path("",views.shop,name="shop"),
    path("item/<int:id>",views.item_detail,name="shop-item"),
    path("tag/<str:tag>",views.get_by_tag,name="get-by-tag"),
    #path("post-item",views.post_item,name="shop-postItem"),
]