from django.urls import path

from . import views

urlpatterns = [
    path("",views.shop,name="shop"),
    path("item/<int:id>",views.item_detail,name="shop-item"),
    path("tag/<str:tag>",views.get_by_tag,name="get-by-tag"),
    path("sale/",views.get_sale_item,name="sale-page")
]